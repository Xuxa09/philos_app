"""Generate reflections for classical (Plato/Aristotle/Socrates) quotes via auto-matching."""
import json

with open('c:/Users/lalli/Flutter/coach_phrase_app/classical_keys.json', 'r', encoding='utf-8') as f:
    keys = json.load(f)

T = {
    "wisdom": {
        "en": "Wisdom is recognizing how much you do not know. Begin every inquiry with humility.",
        "pt": "A sabedoria \u00e9 reconhecer o quanto voc\u00ea n\u00e3o sabe. Comece toda investiga\u00e7\u00e3o com humildade.",
        "es": "La sabidur\u00eda es reconocer cu\u00e1nto no sabes. Comienza toda investigaci\u00f3n con humildad."
    },
    "virtue": {
        "en": "Virtue is a habit, not a single act. Practice excellence daily and it becomes who you are.",
        "pt": "A virtude \u00e9 um h\u00e1bito, n\u00e3o um \u00fanico ato. Pratique a excel\u00eancia diariamente e ela se torna quem voc\u00ea \u00e9.",
        "es": "La virtud es un h\u00e1bito, no un solo acto. Practica la excelencia diariamente y se vuelve qui\u00e9n eres."
    },
    "knowledge": {
        "en": "True knowledge comes from active inquiry, not passive memorizing. Question what you have been taught.",
        "pt": "O verdadeiro conhecimento vem da investiga\u00e7\u00e3o ativa, n\u00e3o da memoriza\u00e7\u00e3o passiva. Questione o que lhe foi ensinado.",
        "es": "El verdadero conocimiento viene de la investigaci\u00f3n activa, no de la memorizaci\u00f3n pasiva. Cuestiona lo que te han ense\u00f1ado."
    },
    "self_know": {
        "en": "Knowing yourself is the foundation of all other knowing. Examine your own beliefs first.",
        "pt": "Conhecer a si mesmo \u00e9 a base de todo outro conhecimento. Examine suas pr\u00f3prias cren\u00e7as primeiro.",
        "es": "Conocerse a s\u00ed mismo es el fundamento de todo otro conocimiento. Examina tus propias creencias primero."
    },
    "happiness": {
        "en": "Happiness is the activity of a soul aligned with virtue. Build it through daily good action.",
        "pt": "A felicidade \u00e9 a atividade de uma alma alinhada com a virtude. Construa-a atrav\u00e9s da boa a\u00e7\u00e3o di\u00e1ria.",
        "es": "La felicidad es la actividad de un alma alineada con la virtud. Constr\u00fayela mediante la buena acci\u00f3n diaria."
    },
    "soul": {
        "en": "Care for your soul more than your body or possessions. The inner life shapes everything else.",
        "pt": "Cuide da sua alma mais que do corpo ou das posses. A vida interior molda todo o resto.",
        "es": "Cuida tu alma m\u00e1s que tu cuerpo o posesiones. La vida interior moldea todo lo dem\u00e1s."
    },
    "education": {
        "en": "Education shapes the whole life that follows. Choose carefully what you let into your mind.",
        "pt": "A educa\u00e7\u00e3o molda toda a vida que se segue. Escolha cuidadosamente o que voc\u00ea deixa entrar na sua mente.",
        "es": "La educaci\u00f3n moldea toda la vida que sigue. Elige cuidadosamente lo que dejas entrar en tu mente."
    },
    "courage": {
        "en": "Courage makes other virtues possible. Without it, even good intentions wither.",
        "pt": "A coragem torna outras virtudes poss\u00edveis. Sem ela, at\u00e9 boas inten\u00e7\u00f5es murcham.",
        "es": "El coraje hace posibles otras virtudes. Sin \u00e9l, incluso las buenas intenciones se marchitan."
    },
    "friendship": {
        "en": "True friendship is rare and worth more than wealth. Tend it carefully.",
        "pt": "A verdadeira amizade \u00e9 rara e vale mais que riqueza. Cultive-a com cuidado.",
        "es": "La verdadera amistad es rara y vale m\u00e1s que la riqueza. Cult\u00edvala con cuidado."
    },
    "love": {
        "en": "Love is what makes us reach beyond ourselves. Honor it as a force greater than reason.",
        "pt": "O amor \u00e9 o que nos faz ir al\u00e9m de n\u00f3s mesmos. Honre-o como uma for\u00e7a maior que a raz\u00e3o.",
        "es": "El amor es lo que nos hace ir m\u00e1s all\u00e1 de nosotros mismos. Hon\u00f3ralo como una fuerza mayor que la raz\u00f3n."
    },
    "death": {
        "en": "Fear of death is fear of the unknown. The wise neither chase nor flee it.",
        "pt": "O medo da morte \u00e9 medo do desconhecido. O s\u00e1bio nem a persegue nem foge dela.",
        "es": "El miedo a la muerte es miedo a lo desconocido. El sabio ni la persigue ni huye de ella."
    },
    "justice": {
        "en": "Justice is each person doing what they are best suited for. Find your role and play it well.",
        "pt": "A justi\u00e7a \u00e9 cada pessoa fazendo aquilo para o que \u00e9 mais adequada. Encontre seu papel e fa\u00e7a-o bem.",
        "es": "La justicia es cada persona haciendo aquello para lo que es m\u00e1s apta. Encuentra tu papel y hazlo bien."
    },
    "moderation": {
        "en": "Excess in anything destroys; balance preserves. Cultivate the middle path.",
        "pt": "O excesso em qualquer coisa destr\u00f3i; o equil\u00edbrio preserva. Cultive o caminho do meio.",
        "es": "El exceso en cualquier cosa destruye; el equilibrio preserva. Cultiva el camino del medio."
    },
    "politics": {
        "en": "Politics is too important to ignore. Refusing to engage means being ruled by lesser people.",
        "pt": "A pol\u00edtica \u00e9 importante demais para ignorar. Recusar-se a engajar significa ser governado por pessoas menores.",
        "es": "La pol\u00edtica es demasiado importante para ignorar. Negarse a participar significa ser gobernado por personas menores."
    },
    "change": {
        "en": "Everything flows; nothing stays the same. Resist nothing and find your peace.",
        "pt": "Tudo flui; nada permanece igual. N\u00e3o resista a nada e encontre sua paz.",
        "es": "Todo fluye; nada permanece igual. No resistas nada y encuentra tu paz."
    },
    "art": {
        "en": "Art reveals the universal hidden in the particular. Look beyond surfaces to what really matters.",
        "pt": "A arte revela o universal escondido no particular. Olhe al\u00e9m das superf\u00edcies para o que realmente importa.",
        "es": "El arte revela lo universal oculto en lo particular. Mira m\u00e1s all\u00e1 de las superficies a lo que realmente importa."
    },
    "fear": {
        "en": "Fear shrinks when you face it; it grows when you flee. Look directly at what frightens you.",
        "pt": "O medo encolhe quando voc\u00ea o enfrenta; cresce quando voc\u00ea foge. Olhe diretamente para o que o assusta.",
        "es": "El miedo se encoge cuando lo enfrentas; crece cuando huyes. Mira directamente lo que te asusta."
    },
    "anger": {
        "en": "Anger is easy; well-directed anger is rare. Pause before reacting.",
        "pt": "A raiva \u00e9 f\u00e1cil; a raiva bem direcionada \u00e9 rara. Pause antes de reagir.",
        "es": "La ira es f\u00e1cil; la ira bien dirigida es rara. Detente antes de reaccionar."
    },
    "music": {
        "en": "Music shapes the soul like nothing else can. Listen to what nourishes you.",
        "pt": "A m\u00fasica molda a alma como nada mais. Escute o que o nutre.",
        "es": "La m\u00fasica moldea el alma como nada m\u00e1s. Escucha lo que te nutre."
    },
    "writing": {
        "en": "To write is to think more deeply. Put your confused feelings into words.",
        "pt": "Escrever \u00e9 pensar mais profundamente. Coloque seus sentimentos confusos em palavras.",
        "es": "Escribir es pensar m\u00e1s profundamente. Pon tus sentimientos confusos en palabras."
    },
    "youth_age": {
        "en": "Each age has its gifts and limits. Honor where you are without rushing or regretting.",
        "pt": "Cada idade tem seus dons e limites. Honre onde voc\u00ea est\u00e1 sem se apressar ou se arrepender.",
        "es": "Cada edad tiene sus dones y l\u00edmites. Honra donde est\u00e1s sin apurarte o arrepentirte."
    },
    "wealth": {
        "en": "True wealth is contentment with little. Reduce desires before increasing possessions.",
        "pt": "A verdadeira riqueza \u00e9 contentamento com pouco. Reduza desejos antes de aumentar posses.",
        "es": "La verdadera riqueza es contentamiento con poco. Reduce los deseos antes de aumentar las posesiones."
    },
    "nature": {
        "en": "Nature has wisdom we forget when distracted. Listen to its rhythms today.",
        "pt": "A natureza tem sabedoria que esquecemos quando distra\u00eddos. Escute seus ritmos hoje.",
        "es": "La naturaleza tiene sabidur\u00eda que olvidamos cuando estamos distra\u00eddos. Escucha sus ritmos hoy."
    },
    "law": {
        "en": "Good people do not need laws; bad people will evade them. Cultivate inner virtue first.",
        "pt": "Pessoas boas n\u00e3o precisam de leis; as m\u00e1s as evitar\u00e3o. Cultive a virtude interior primeiro.",
        "es": "Las personas buenas no necesitan leyes; las malas las evadir\u00e1n. Cultiva la virtud interior primero."
    },
    "speech": {
        "en": "Words shape what is possible. Listen twice as much as you speak.",
        "pt": "As palavras moldam o que \u00e9 poss\u00edvel. Ou\u00e7a o dobro do que voc\u00ea fala.",
        "es": "Las palabras moldean lo posible. Escucha el doble de lo que hablas."
    },
    "habit": {
        "en": "We are what we repeatedly do. Change your habits and you change your life.",
        "pt": "Somos o que fazemos repetidamente. Mude seus h\u00e1bitos e voc\u00ea muda sua vida.",
        "es": "Somos lo que hacemos repetidamente. Cambia tus h\u00e1bitos y cambias tu vida."
    },
    "patience": {
        "en": "Great things take time. Be patient with what you are growing.",
        "pt": "Coisas grandes levam tempo. Seja paciente com o que voc\u00ea est\u00e1 cultivando.",
        "es": "Las grandes cosas toman tiempo. S\u00e9 paciente con lo que est\u00e1s cultivando."
    },
    "humanity": {
        "en": "We are made for one another, not for isolation. Reach toward others today.",
        "pt": "Fomos feitos uns para os outros, n\u00e3o para o isolamento. Estenda-se aos outros hoje.",
        "es": "Estamos hechos los unos para los otros, no para el aislamiento. Acerc\u00e1te a otros hoy."
    },
    "fallback": {
        "en": "The unexamined life is not worth living. Question your assumptions and act on the answers.",
        "pt": "A vida n\u00e3o examinada n\u00e3o vale a pena ser vivida. Questione suas suposi\u00e7\u00f5es e aja sobre as respostas.",
        "es": "La vida no examinada no vale la pena ser vivida. Cuestiona tus suposiciones y act\u00faa sobre las respuestas."
    },
}

KEYWORDS = [
    (("wisdom", "wise", "sabedoria", "s\u00e1bio"), "wisdom"),
    (("know thyself", "self-know", "myself", "conhece-te"), "self_know"),
    (("knowledge", "learn", "ignoran", "conheciment", "aprend"), "knowledge"),
    (("virtue", "excell", "virtuoso", "excel\u00eancia"), "virtue"),
    (("happy", "happiness", "felic", "alegr"), "happiness"),
    (("soul", "alma"), "soul"),
    (("educat", "teach", "pupil", "child", "school", "educa\u00e7"), "education"),
    (("courage", "brave", "coragem"), "courage"),
    (("friend", "amigo", "amizade"), "friendship"),
    (("love", "amor", "lover"), "love"),
    (("death", "die", "dying", "mortal", "morte", "morrer"), "death"),
    (("justice", "just", "fair", "justi\u00e7a"), "justice"),
    (("moderat", "balance", "middle", "moderacao", "equil\u00edbrio"), "moderation"),
    (("politic", "state", "govern", "ruler", "tyrant", "democracy", "pol\u00edtica"), "politics"),
    (("flux", "change", "mudan\u00e7a", "rio", "river", "flow"), "change"),
    (("art", "beauty", "beautiful", "poet", "arte", "beleza"), "art"),
    (("fear", "afraid", "terror", "medo"), "fear"),
    (("anger", "angry", "wrath", "raiva"), "anger"),
    (("music", "harmony", "m\u00fasica", "harmonia"), "music"),
    (("writ", "book", "read", "litera", "escrev", "livro"), "writing"),
    (("youth", "age", "old", "young", "juventude", "velhice"), "youth_age"),
    (("wealth", "rich", "poor", "money", "riqueza", "pobre", "dinheiro"), "wealth"),
    (("nature", "natural", "natureza"), "nature"),
    (("law", "rule", "obey", "lei"), "law"),
    (("word", "speak", "speech", "say", "tongue", "palavra", "fala"), "speech"),
    (("habit", "h\u00e1bito", "practice", "pr\u00e1tica"), "habit"),
    (("time", "hour", "patient", "patience", "tempo", "paci\u00eancia"), "patience"),
    (("man", "human", "people", "person", "humano", "homem", "pessoa"), "humanity"),
]


def pick_template(text):
    text_lower = text.lower()
    for kws, template_key in KEYWORDS:
        for kw in kws:
            if kw in text_lower:
                return T[template_key]
    return T["fallback"]


result = {}
for key in keys:
    result[key] = pick_template(key)

with open('c:/Users/lalli/Flutter/coach_phrase_app/reflections_classical.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f'Generated {len(result)} classical reflections')

from collections import Counter
counts = Counter()
for key in keys:
    refl = pick_template(key)
    for name, t in T.items():
        if t == refl:
            counts[name] += 1
            break
print('\nDistribution:')
for name, count in counts.most_common():
    print(f'  {name}: {count}')
