"""Find existentialism quotes not yet translated."""
import re, json

DART_PATH = 'c:/Users/lalli/Flutter/coach_phrase_app/lib/data/services/quotes_data.dart'

with open(DART_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

cats = re.findall(r"category: '([^']+)'", content)
ens = re.findall(r"textEn: '(.*?)',", content)
pts = re.findall(r"textPt: '(.*?)',", content)

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

missing = []
for i, cat in enumerate(cats):
    if cat == 'existentialism' and i < len(ens) and i < len(pts):
        en = unescape_dart(ens[i])
        pt = unescape_dart(pts[i])
        if en == pt:
            missing.append(en)

with open('c:/Users/lalli/Flutter/coach_phrase_app/missing_exist.json', 'w', encoding='utf-8') as f:
    json.dump(missing, f, ensure_ascii=False, indent=2)

print(f'Missing existentialism translations: {len(missing)}')
