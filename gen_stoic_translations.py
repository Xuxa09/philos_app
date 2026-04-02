#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

with open('quotes_stoicism.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Get unique texts preserving order
texts = []
seen = set()
for q in data:
    t = q['text']
    if t not in seen:
        seen.add(t)
        texts.append(t)

translations = {}

def tr(key, pt, es):
    translations[key] = {"pt": pt, "es": es}

