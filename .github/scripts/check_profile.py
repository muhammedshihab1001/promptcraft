import sys

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

sys.exit(1 if failed else 0)