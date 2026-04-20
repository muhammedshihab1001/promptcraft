import sys
import os
import re

filepath = sys.argv[1]
text = open(filepath, encoding="utf-8").read()
failed = False

# Em dash check — profiles must use plain hyphens only
if "\u2014" in text:
    print(f"FOUND em dash in {filepath} - remove it and use a plain hyphen")
    failed = True

# Smart quote check — profiles must use straight quotes only
smart_quotes = ["\u2018", "\u2019", "\u201c", "\u201d"]
if any(c in text for c in smart_quotes):
    print(f"FOUND smart quotes in {filepath} - replace with plain quotes")
    failed = True

# Required header fields must exist and have non-empty values
required_fields = ["Name", "Works with", "Best for", "Extends", "Version"]
for field in required_fields:
    pattern = rf"^# {re.escape(field)}:\s*(.+)$"
    match = re.search(pattern, text, re.MULTILINE)
    if not match or not match.group(1).strip():
        print(f"EMPTY or MISSING value for '# {field}:' in {filepath}")
        failed = True

# Extends field must reference a real file (unless value is "None")
extends_match = re.search(r"^# Extends:\s*(.+)$", text, re.MULTILINE)
if extends_match:
    extends_value = extends_match.group(1).strip()
    if extends_value.lower() != "none":
        resolved = os.path.join("profiles", extends_value)
        if not os.path.exists(resolved):
            print(f"EXTENDS file not found: '{resolved}' referenced in {filepath}")
            failed = True

sys.exit(1 if failed else 0)