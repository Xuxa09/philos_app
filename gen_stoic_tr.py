#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

with open('quotes_stoicism.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

texts = []
seen = set()
for q in data:
    t = q['text']
    if t not in seen:
        seen.add(t)
        texts.append(t)

t = {}

def tr(key, pt, es):
    t[key] = {"pt": pt, "es": es}

tr("Freedom is the only worthy goal in life. It is won by disregarding things that lie beyond our control.","A liberdade é o único objetivo digno na vida. Ela é conquistada ao desconsiderar as coisas que estão além do nosso controle.","La libertad es la única meta digna en la vida. Se conquista al desestimar las cosas que están más allá de nuestro control.")
tr("Life is like a play: it's not the length, but the excellence of the acting that matters.","A vida é como uma peça de teatro: não é a duração, mas a excelência da atuação que importa.","La vida es como una obra de teatro: no es la duración, sino la excelencia de la actuación lo que importa.")
tr("Luck is what happens when preparation meets opportunity.","Sorte é o que acontece quando a preparação encontra a oportunidade.","La suerte es lo que sucede cuando la preparación se encuentra con la oportunidad.")
tr("Difficulties strengthen the mind, as labor does the body.","As dificuldades fortalecem a mente, assim como o trabalho fortalece o corpo.","Las dificultades fortalecen la mente, así como el trabajo fortalece el cuerpo.")
tr("As is a tale, so is life: not how long it is, but how good it is, is what matters.","Assim como um conto, assim é a vida: não importa quão longa seja, mas quão boa ela é.","Como un cuento, así es la vida: no importa cuán larga sea, sino cuán buena es.")
tr("No man is free who is not master of himself.","Nenhum homem é livre se não é senhor de si mesmo.","Ningún hombre es libre si no es dueño de sí mismo.")
