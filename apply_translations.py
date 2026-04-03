"""Apply translations from JSON files to quotes_data.dart."""
import json
import re

DART_PATH = 'c:/Users/lalli/Flutter/coach_phrase_app/lib/data/services/quotes_data.dart'

# Load all translation sources
all_translations = {}

for path in [
    'c:/Users/lalli/Flutter/coach_phrase_app/translations_extra.json',
    'c:/Users/lalli/Flutter/coach_phrase_app/translations_stoicism.json',
]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            all_translations.update(data)
    except FileNotFoundError:
        print(f"Warning: {path} not found, skipping")


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
    """Unescape Dart string back to Python string for matching."""
    result = []
    i = 0
    while i < len(s):
        if s[i] == '\\' and i + 1 < len(s):
            nxt = s[i + 1]
            if nxt == 'u' and i + 5 < len(s):
                hex_str = s[i+2:i+6]
                try:
                    result.append(chr(int(hex_str, 16)))
                    i += 6
                    continue
                except ValueError:
                    pass
            elif nxt == "'":
                result.append("'")
                i += 2
                continue
            elif nxt == '\\':
                result.append('\\')
                i += 2
                continue
            elif nxt == 'n':
                result.append('\n')
                i += 2
                continue
        result.append(s[i])
        i += 1
    return ''.join(result)


def main():
    with open(DART_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    translated = 0
    i = 0
    while i < len(lines):
        line = lines[i]

        # Match textEn line
        m = re.match(r"(\s+textEn: ')(.*)(',)\s*$", line)
        if m:
            indent = m.group(1)
            en_escaped = m.group(2)
            suffix = m.group(3)

            # Unescape to get the original text for lookup
            en_text = unescape_dart(en_escaped)

            tr = all_translations.get(en_text)
            if tr and i + 2 < len(lines):
                pt_line = lines[i + 1]
                es_line = lines[i + 2]

                # Check these are actually textPt and textEs
                if 'textPt:' in pt_line and 'textEs:' in es_line:
                    pt_text = tr.get('pt', en_text)
                    es_text = tr.get('es', en_text)

                    # Only replace if translation is different from EN
                    if pt_text != en_text:
                        lines[i + 1] = f"      textPt: '{escape_dart(pt_text)}',\n"
                        lines[i + 2] = f"      textEs: '{escape_dart(es_text)}',\n"
                        translated += 1

        i += 1

    with open(DART_PATH, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print(f"Applied {translated} translations to quotes_data.dart")


if __name__ == '__main__':
    main()
