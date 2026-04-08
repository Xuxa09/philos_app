"""Extract absurdism textEn keys from quotes_data.dart."""
import re, json

DART_PATH = 'c:/Users/lalli/Flutter/coach_phrase_app/lib/data/services/quotes_data.dart'

with open(DART_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Find absurdism block
start = content.find("// === Absurdism")
end = content.find("// === Pragmatism")
block = content[start:end]

ens = re.findall(r"textEn: '(.*?)',", block)

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

texts = [unescape_dart(e) for e in ens]

with open('c:/Users/lalli/Flutter/coach_phrase_app/absurdism_keys.json', 'w', encoding='utf-8') as f:
    json.dump(texts, f, ensure_ascii=False, indent=2)

print(f'Extracted {len(texts)} absurdism quotes')
