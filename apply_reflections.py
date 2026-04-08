"""Apply reflections from JSON files to quotes_data.dart.

JSON format:
{
  "exact textEn key": {"en": "...", "pt": "...", "es": "..."},
  ...
}
"""
import json
import re
import os

DART_PATH = 'c:/Users/lalli/Flutter/coach_phrase_app/lib/data/services/quotes_data.dart'
REFLECTIONS_DIR = 'c:/Users/lalli/Flutter/coach_phrase_app'

# Load all reflection sources
all_reflections = {}
for fname in os.listdir(REFLECTIONS_DIR):
    if fname.startswith('reflections_') and fname.endswith('.json'):
        path = os.path.join(REFLECTIONS_DIR, fname)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                all_reflections.update(data)
        except FileNotFoundError:
            pass


def escape_dart(s):
    """Escape for Dart single-quoted strings, non-ASCII to \\uXXXX."""
    result = []
    for ch in s:
        cp = ord(ch)
        if ch == '\\':
            result.append('\\\\')
        elif ch == "'":
            result.append("\\'")
        elif ch == '\n':
            result.append('\\n')
        elif ch == '\r':
            pass
        elif cp > 127:
            result.append(f'\\u{cp:04x}')
        else:
            result.append(ch)
    return ''.join(result)


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
    i = 0
    while i < len(lines):
        line = lines[i]

        m = re.match(r"(\s+textEn: ')(.*)(',)\s*$", line)
        if m:
            en_escaped = m.group(2)
            en_text = unescape_dart(en_escaped)

            ref = all_reflections.get(en_text)
            if ref and i + 5 < len(lines):
                # Lines: textEn, textPt, textEs, reflectionEn, reflectionPt, reflectionEs
                refl_en_line = lines[i + 3]
                refl_pt_line = lines[i + 4]
                refl_es_line = lines[i + 5]

                if 'reflectionEn:' in refl_en_line and 'reflectionPt:' in refl_pt_line and 'reflectionEs:' in refl_es_line:
                    en_r = ref.get('en', '')
                    pt_r = ref.get('pt', '')
                    es_r = ref.get('es', '')

                    if en_r:
                        lines[i + 3] = f"      reflectionEn: '{escape_dart(en_r)}',\n"
                        lines[i + 4] = f"      reflectionPt: '{escape_dart(pt_r)}',\n"
                        lines[i + 5] = f"      reflectionEs: '{escape_dart(es_r)}',\n"
                        applied += 1
        i += 1

    with open(DART_PATH, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print(f"Applied {applied} reflections to quotes_data.dart")
    print(f"Total reflections in JSONs: {len(all_reflections)}")


if __name__ == '__main__':
    main()
