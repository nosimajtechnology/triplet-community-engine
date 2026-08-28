#!/usr/bin/env python3
"""Validate and build the installable TripleT Community Engine package."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
SKILL_NAME = "triplet-community-engine"
SKILL_DIR = ROOT / "skill" / SKILL_NAME
DIST = ROOT / "dist"
ZIP_NAME = f"{SKILL_NAME}.zip"

MAX_FILES = 500
MAX_FILE_BYTES = 25 * 1024 * 1024
MAX_TOTAL_BYTES = 25 * 1024 * 1024
MAX_ZIP_BYTES = 50 * 1024 * 1024
FIXED_TIME = (2026, 1, 1, 0, 0, 0)
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"FAIL {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
    if not match:
        fail("SKILL.md has no valid YAML front matter block")
    fields: dict[str, str] = {}
    for raw_line in match.group(1).splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if ":" not in raw_line:
            fail(f"malformed front matter line: {raw_line!r}")
        key, value = raw_line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"\'')
    return fields


def validate_links(markdown: Path) -> None:
    text = markdown.read_text(encoding="utf-8")
    for raw_target in MARKDOWN_LINK.findall(text):
        target = raw_target.strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith("#"):
            continue
        path_part = unquote(parsed.path)
        if not path_part:
            continue
        resolved = (markdown.parent / path_part).resolve()
        try:
            resolved.relative_to(SKILL_DIR.resolve())
        except ValueError:
            fail(f"{markdown.relative_to(ROOT)} links outside the Skill: {raw_target!r}")
        if not resolved.exists():
            fail(f"{markdown.relative_to(ROOT)} links to missing file {raw_target!r}")


def validate() -> list[Path]:
    if not SKILL_DIR.is_dir():
        fail(f"missing {SKILL_DIR.relative_to(ROOT)}")

    files = sorted(
        (path for path in SKILL_DIR.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(SKILL_DIR).as_posix(),
    )
    if not files:
        fail("Skill folder is empty")
    if len(files) > MAX_FILES:
        fail(f"{len(files)} files exceeds guardrail {MAX_FILES}")

    manifests = [path for path in files if path.name.lower() == "skill.md"]
    if len(manifests) != 1:
        fail(f"expected exactly one SKILL.md, found {len(manifests)}")
    manifest = manifests[0]
    if manifest.parent != SKILL_DIR:
        fail("SKILL.md must be at the top of the Skill folder")

    fields = parse_frontmatter(manifest.read_text(encoding="utf-8"))
    if fields.get("name") != SKILL_NAME:
        fail(f"SKILL.md name must be {SKILL_NAME!r}")
    if not fields.get("description"):
        fail("SKILL.md front matter is missing 'description'")
    extra_fields = set(fields) - {"name", "description"}
    if extra_fields:
        fail(f"unsupported SKILL.md front matter fields: {sorted(extra_fields)}")

    total = 0
    for path in files:
        size = path.stat().st_size
        total += size
        if size > MAX_FILE_BYTES:
            fail(f"{path.relative_to(ROOT)} exceeds {MAX_FILE_BYTES} bytes")
        if path.suffix.lower() == ".md":
            validate_links(path)
    if total > MAX_TOTAL_BYTES:
        fail(f"{total} uncompressed bytes exceeds guardrail {MAX_TOTAL_BYTES}")

    print(f"OK   {len(files)} files, {total} bytes, name={SKILL_NAME}")
    return files


def build(files: list[Path]) -> tuple[Path, str]:
    DIST.mkdir(exist_ok=True)
    output = DIST / ZIP_NAME
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            relative = path.relative_to(SKILL_DIR).as_posix()
            info = zipfile.ZipInfo(f"{SKILL_NAME}/{relative}", date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

    with zipfile.ZipFile(output) as archive:
        names = archive.namelist()
        tops = {name.split("/", 1)[0] for name in names}
        if tops != {SKILL_NAME}:
            fail(f"ZIP must contain exactly one top-level folder, found {sorted(tops)}")
        skill_paths = [name for name in names if name.lower().endswith("/skill.md")]
        if skill_paths != [f"{SKILL_NAME}/SKILL.md"]:
            fail(f"ZIP must contain one top-level SKILL.md, found {skill_paths}")

    if output.stat().st_size > MAX_ZIP_BYTES:
        fail(f"{output.relative_to(ROOT)} exceeds {MAX_ZIP_BYTES} bytes")

    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    (DIST / "SHA256SUMS").write_text(f"{digest}  {ZIP_NAME}\n", encoding="utf-8", newline="\n")
    print(f"OK   {output.relative_to(ROOT)} ({output.stat().st_size} bytes)")
    print(f"OK   sha256 {digest}")
    return output, digest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="validate without writing dist output")
    args = parser.parse_args()
    files = validate()
    if not args.check:
        build(files)


if __name__ == "__main__":
    main()

