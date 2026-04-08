"""Auto-tag quotes with mood labels based on textEn content.

8 moods (matching existing app categories):
- unmotivated, anxious, frustrated, fearful, lost, grateful, ambitious, tired
"""
import json
import re
import os

REFLECTIONS_DIR = 'c:/Users/lalli/Flutter/coach_phrase_app'

# === Mood keyword definitions ===
# A quote can match multiple moods (we tag ALL matches).
MOOD_KEYWORDS = {
    'unmotivated': [
        # English
        'motivat', 'lazy', 'effort', 'persever', 'persist', 'begin', 'start',
        'action', 'act ', 'do not stop', 'try again', 'fail', 'try', 'dare',
        'never give up', 'inertia', 'idle', 'work',
        # Portuguese
        'motiva', 'pregui', 'esfor\u00e7o', 'persever', 'persist', 'come\u00e7', 'come\u00e7ar',
        'a\u00e7\u00e3o', 'agir', 'tente', 'tenta', 'fracass', 'falh', 'ouse', 'ousadia',
        'in\u00e9rcia', 'trabalh',
    ],
    'anxious': [
        'anxi', 'worry', 'worried', 'restless', 'calm', 'tranquil', 'peace', 'serenity',
        'troubled', 'untroubled', 'agitat', 'still', 'storm', 'breathe',
        'preocupa', 'inquiet', 'calma', 'tranquil', 'paz', 'serenidade',
        'perturba', 'agita', 'tempestade', 'respira',
    ],
    'frustrated': [
        'frustrat', 'anger', 'angry', 'rage', 'irritat', 'mad', 'fury', 'wrath',
        'patien', 'control yourself', 'bear', 'endure',
        'frustra', 'raiva', 'irritad', 'paci\u00eancia', 'controle', 'suport',
        'aguent',
    ],
    'fearful': [
        'fear', 'afraid', 'terror', 'coward', 'brave', 'courage', 'bold',
        'death is', 'dread', 'tremble', 'panic',
        'medo', 'temer', 'temor', 'covarde', 'corag', 'bravur', 'ousad',
        'pavor', 'tremer', 'p\u00e2nico',
    ],
    'lost': [
        'meaning', 'purpose', 'lost', 'found', 'path', 'direction', 'wander',
        'know thyself', 'self-know', 'identity', 'who am i', 'meaningless',
        'sentido', 'prop\u00f3sito', 'perdid', 'caminho', 'dire\u00e7\u00e3o', 'vagar',
        'identidade', 'quem sou', 'sem sentido', 'conhece-te',
    ],
    'grateful': [
        'gratitude', 'grateful', 'thank', 'gift', 'present moment', 'enough',
        'sufficient', 'content', 'blessing', 'cherish', 'appreciate', 'joy',
        'gratid\u00e3o', 'grato', 'obrigad', 'presente', 'suficiente', 'bastant',
        'contentamento', 'b\u00ean\u00e7\u00e3o', 'aprecia', 'alegria',
    ],
    'ambitious': [
        'ambit', 'great', 'excellence', 'achievement', 'success', 'excel',
        'glory', 'master', 'dream big', 'impossible', 'goal', 'aim', 'dare',
        'climb', 'mountain', 'limit',
        'ambi\u00e7', 'grande', 'excel\u00eancia', 'realiza', 'sucesso', 'gl\u00f3ria',
        'mestre', 'sonho', 'imposs\u00edvel', 'meta', 'objetivo', 'limite',
        'escalar', 'montanha',
    ],
    'tired': [
        'rest', 'tired', 'weary', 'fatigue', 'exhaust', 'sleep', 'pause',
        'simple', 'simplicity', 'less', 'enough', 'slow',
        'descanso', 'cansad', 'fadiga', 'exaust', 'sono', 'pausa',
        'simples', 'simplicidade', 'menos', 'lento',
    ],
}


def find_moods(text):
    text_lower = text.lower()
    matched = []
    for mood, keywords in MOOD_KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                matched.append(mood)
                break
    return matched


def main():
    # Load all category key files we already extracted
    categories = ['absurdism', 'rationalism', 'epicureanism', 'eastern',
                  'stoicism', 'existentialism', 'classical', 'pragmatism']

    all_keys = []
    for cat in categories:
        path = os.path.join(REFLECTIONS_DIR, f'{cat}_keys.json')
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                all_keys.extend(json.load(f))

    print(f'Total quote keys loaded: {len(all_keys)}')

    moods_map = {}
    stats = {m: 0 for m in MOOD_KEYWORDS}

    for key in all_keys:
        moods = find_moods(key)
        if moods:
            moods_map[key] = moods
            for m in moods:
                stats[m] += 1

    with open(os.path.join(REFLECTIONS_DIR, 'moods.json'), 'w', encoding='utf-8') as f:
        json.dump(moods_map, f, ensure_ascii=False, indent=2)

    print(f'\nTagged {len(moods_map)} quotes with at least one mood')
    print('\nMood distribution:')
    for mood, count in sorted(stats.items(), key=lambda x: -x[1]):
        print(f'  {mood}: {count}')


if __name__ == '__main__':
    main()
