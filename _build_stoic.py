#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

with open("quotes_stoicism.json", "r", encoding="utf-8") as f:
    data = json.load(f)

texts = []
seen = set()
for q in data:
    t = q["text"]
    if t not in seen:
        seen.add(t)
        texts.append(t)

with open("_stoic_keys.json", "r", encoding="utf-8") as f:
    keys_check = json.load(f)

assert texts == keys_check, "Keys mismatch!"

# Read translations data
with open("_stoic_tr_data.json", "r", encoding="utf-8") as f:
    tr_data = json.load(f)

translations = {}
for i, key in enumerate(texts):
    idx = str(i)
    if idx in tr_data:
        translations[key] = {"pt": tr_data[idx][0], "es": tr_data[idx][1]}
    else:
        print(f"WARNING: Missing translation for index {i}: {key[:60]}")

missing = [i for i in range(len(texts)) if str(i) not in tr_data]
print(f"Total unique quotes: {len(texts)}")
print(f"Translations created: {len(translations)}")
print(f"Missing: {len(missing)}")
if missing:
    print(f"Missing indices: {missing}")

with open("translations_stoicism.json", "w", encoding="utf-8") as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

print(f"File written with {len(translations)} entries!")
