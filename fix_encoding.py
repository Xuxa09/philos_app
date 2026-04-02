"""Fix non-ASCII characters in quotes_data.dart by replacing them with Dart unicode escapes."""

path = 'c:/Users/lalli/Flutter/coach_phrase_app/lib/data/services/quotes_data.dart'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

result = []
for ch in content:
    cp = ord(ch)
    if cp > 127:
        result.append(f'\\u{cp:04x}')
    else:
        result.append(ch)

output = ''.join(result)

with open(path, 'w', encoding='utf-8') as f:
    f.write(output)

print('Done - all non-ASCII replaced with \\uXXXX escapes')
