"""Extract textEn keys from a category in quotes_data.dart.
Usage: python extract_category.py <category_name>
"""
import re, json, sys

DART_PATH = 'c:/Users/lalli/Flutter/coach_phrase_app/lib/data/services/quotes_data.dart'

# Map category to header marker pairs (start, next)
CATEGORY_BOUNDS = {
    'stoicism': ('// === Stoicism', '// === Classical'),
    'classical': ('// === Classical', '// === Existentialism'),
    'existentialism': ('// === Existentialism', '// === Eastern'),
    'eastern': ('// === Eastern', '// === Epicureanism'),
    'epicureanism': ('// === Epicureanism', '// === Rationalism'),
    'rationalism': ('// === Rationalism', '// === Absurdism'),
    'absurdism': ('// === Absurdism', '// === Pragmatism'),
    'pragmatism': ('// === Pragmatism', '}'),
}

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
    cat = sys.argv[1]
    start_marker, end_marker = CATEGORY_BOUNDS[cat]

    with open(DART_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    start = content.find(start_marker)
    end = content.find(end_marker, start + len(start_marker))
    block = content[start:end]

    # Get pairs of (textEn, textPt) - only translated ones (en != pt)
    pattern = re.compile(r"textEn: '(.*?)',\s*textPt: '(.*?)',", re.DOTALL)
    pairs = pattern.findall(block)

    translated = []
    for en, pt in pairs:
        en_text = unescape_dart(en)
        pt_text = unescape_dart(pt)
        if en_text != pt_text:
            translated.append(en_text)

    out = f'c:/Users/lalli/Flutter/coach_phrase_app/{cat}_keys.json'
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(translated, f, ensure_ascii=False, indent=2)

    print(f'Extracted {len(translated)} translated {cat} quotes -> {out}')


if __name__ == '__main__':
    main()
