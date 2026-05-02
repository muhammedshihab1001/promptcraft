import sys
import os
import re
from pathlib import Path

filepath = sys.argv[1]
formatting_only = "--formatting-only" in sys.argv

text = open(filepath, encoding="utf-8").read()
failed = False

# Em dash check - profiles must use plain hyphens only
if "\u2014" in text:
    print(f"FOUND em dash in {filepath} - remove it and use a plain hyphen")
    failed = True

# Smart quote check - profiles must use straight quotes only
smart_quotes = ["\u2018", "\u2019", "\u201c", "\u201d"]
if any(c in text for c in smart_quotes):
    print(f"FOUND smart quotes in {filepath} - replace with plain quotes")
    failed = True

# Stop here if only formatting checks were requested
if formatting_only:
    sys.exit(1 if failed else 0)

# Extract only the leading metadata header block
# Stops at the first line that does not start with "# " after the block begins
header_lines = []
for line in text.splitlines():
    if not header_lines and not line.strip():
        continue
    if line.startswith("# "):
        header_lines.append(line)
    elif header_lines:
        break

header_text = "\n".join(header_lines)

# Required header fields must exist and have non-empty values
# Scoped to the header block only - prevents false passes from section headings
required_fields = ["Name", "Works with", "Best for", "Extends", "Version"]
for field in required_fields:
    pattern = rf"^# {re.escape(field)}:\s*(.+)$"
    match = re.search(pattern, header_text, re.MULTILINE)
    if not match or not match.group(1).strip():
        print(f"EMPTY or MISSING value for '# {field}:' in {filepath}")
        failed = True

# Version field must follow semver format X.Y.Z
version_match = re.search(r"^# Version:\s*(.+)$", header_text, re.MULTILINE)
if version_match:
    version_value = version_match.group(1).strip()
    if not re.match(r'^\d+\.\d+\.\d+$', version_value):
        print(f"INVALID Version format in {filepath}: '{version_value}' - must be X.Y.Z (e.g. 0.2.0)")
        failed = True

# Extends field must reference a real file strictly inside profiles/
# Skips when value is "None". Uses pathlib to block path traversal and directory matches.
extends_match = re.search(r"^# Extends:\s*(.+)$", header_text, re.MULTILINE)
if extends_match:
    extends_value = extends_match.group(1).strip()
    if extends_value.lower() != "none":
        profiles_root = Path("profiles").resolve()
        resolved = (profiles_root / extends_value).resolve()
        if profiles_root not in resolved.parents or not resolved.is_file():
            print(f"EXTENDS file not found: '{resolved}' referenced in {filepath}")
            failed = True

sys.exit(1 if failed else 0)