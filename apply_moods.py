"""Apply mood tags to quotes_data.dart.

JSON format (moods.json):
{
  "exact textEn key": ["mood1", "mood2"],
  ...
}
"""
import json
import re

DART_PATH = 'c:/Users/lalli/Flutter/coach_phrase_app/lib/data/services/quotes_data.dart'
MOODS_JSON = 'c:/Users/lalli/Flutter/coach_phrase_app/moods.json'

with open(MOODS_JSON, 'r', encoding='utf-8') as f:
    all_moods = json.load(f)


def unescape_dart(s):
    result = []
    i = 0
    while i < len(s):
        if s[i] == '\\' and i + 1 < len(s):
            nxt = s[i + 1]
            if nxt == 'u' and i + 5 < len(s):
                try:
                    result.append(chr(int(s[i+2:i+6], 16)))
                    i += 6
                    continue
                except ValueError:
                    pass
            elif nxt == "'":
                result.append("'"); i += 2; continue
            elif nxt == '\\':
                result.append('\\'); i += 2; continue
            elif nxt == 'n':
                result.append('\n'); i += 2; continue
        result.append(s[i]); i += 1
    return ''.join(result)


def main():
    with open(DART_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    applied = 0
    out_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        out_lines.append(line)

        m = re.match(r"(\s+textEn: ')(.*)(',)\s*$", line)
        if m:
            en_text = unescape_dart(m.group(2))
            moods = all_moods.get(en_text, [])
            if moods:
                # Find the next 'category:' line and inject moods before it
                # Then look forward for the category line
                j = i + 1
                while j < len(lines):
                    out_lines.append(lines[j])
                    if 'category:' in lines[j]:
                        # Inject moods AFTER the category line
                        moods_str = ', '.join(f"'{m}'" for m in moods)
                        out_lines.append(f"      moods: [{moods_str}],\n")
                        applied += 1
                        i = j + 1
                        break
                    j += 1
                continue
        i += 1

    with open(DART_PATH, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)

    print(f"Applied moods to {applied} quotes")


if __name__ == '__main__':
    main()
