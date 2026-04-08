"""Generate reflections for pragmatism (Emerson, James, Dewey, Peirce, Rorty) quotes."""
import json

with open('c:/Users/lalli/Flutter/coach_phrase_app/pragmatism_keys.json', 'r', encoding='utf-8') as f:
    keys = json.load(f)

T = {
    "action": {
        "en": "Truth shows itself in action, not in argument. Test your beliefs by living them.",
        "pt": "A verdade se mostra na a\u00e7\u00e3o, n\u00e3o no argumento. Teste suas cren\u00e7as vivendo-as.",
        "es": "La verdad se muestra en la acci\u00f3n, no en el argumento. Prueba tus creencias vivi\u00e9ndolas."
    },
    "self_reliance": {
        "en": "Trust yourself. The voice that speaks to you alone is worth more than all borrowed wisdom.",
        "pt": "Confie em si mesmo. A voz que fala s\u00f3 a voc\u00ea vale mais que toda sabedoria emprestada.",
        "es": "Conf\u00eda en ti mismo. La voz que te habla a ti solo vale m\u00e1s que toda sabidur\u00eda prestada."
    },
    "experience": {
        "en": "Experience is the only true teacher. Let life write its lessons on you.",
        "pt": "A experi\u00eancia \u00e9 a \u00fanica mestra verdadeira. Deixe a vida escrever suas li\u00e7\u00f5es em voc\u00ea.",
        "es": "La experiencia es la \u00fanica maestra verdadera. Deja que la vida escriba sus lecciones en ti."
    },
    "growth": {
        "en": "Growth requires risking what you currently know. Step beyond your present self.",
        "pt": "O crescimento exige arriscar o que voc\u00ea atualmente sabe. V\u00e1 al\u00e9m do seu eu presente.",
        "es": "El crecimiento requiere arriesgar lo que ahora sabes. Ve m\u00e1s all\u00e1 de tu yo presente."
    },
    "courage": {
        "en": "Courage is not the absence of fear but action in spite of it. Take the next bold step today.",
        "pt": "Coragem n\u00e3o \u00e9 aus\u00eancia de medo, mas a\u00e7\u00e3o apesar dele. D\u00ea o pr\u00f3ximo passo ousado hoje.",
        "es": "El coraje no es ausencia de miedo sino acci\u00f3n a pesar de \u00e9l. Da el pr\u00f3ximo paso audaz hoy."
    },
    "books": {
        "en": "Books are how minds across time meet. Read what shapes you, not what entertains you.",
        "pt": "Os livros s\u00e3o como mentes atrav\u00e9s do tempo se encontram. Leia o que o molda, n\u00e3o o que o entret\u00e9m.",
        "es": "Los libros son c\u00f3mo las mentes a trav\u00e9s del tiempo se encuentran. Lee lo que te moldea, no lo que te entretiene."
    },
    "friendship": {
        "en": "Friendship is the rarest treasure life offers. Tend it with the care it deserves.",
        "pt": "A amizade \u00e9 o tesouro mais raro que a vida oferece. Cultive-a com o cuidado que merece.",
        "es": "La amistad es el tesoro m\u00e1s raro que la vida ofrece. Cult\u00edvala con el cuidado que merece."
    },
    "thought_action": {
        "en": "Thinking matters only when it changes how you live. Test ideas by their fruits.",
        "pt": "O pensamento s\u00f3 importa quando muda como voc\u00ea vive. Teste ideias pelos seus frutos.",
        "es": "El pensamiento solo importa cuando cambia c\u00f3mo vives. Prueba las ideas por sus frutos."
    },
    "freedom": {
        "en": "Freedom is the inner space where you choose without fear. Defend it daily.",
        "pt": "A liberdade \u00e9 o espa\u00e7o interior onde voc\u00ea escolhe sem medo. Defenda-o diariamente.",
        "es": "La libertad es el espacio interior donde eliges sin miedo. Defi\u00e9ndelo diariamente."
    },
    "happiness": {
        "en": "Happiness is built by good action, not chased as a feeling. Do well and feeling follows.",
        "pt": "A felicidade \u00e9 constru\u00edda pela boa a\u00e7\u00e3o, n\u00e3o perseguida como sentimento. Fa\u00e7a o bem e o sentimento segue.",
        "es": "La felicidad se construye con buena acci\u00f3n, no se persigue como sentimiento. Haz el bien y el sentimiento sigue."
    },
    "education": {
        "en": "Real education awakens the desire to learn forever. Choose teachers who light fires.",
        "pt": "A verdadeira educa\u00e7\u00e3o desperta o desejo de aprender para sempre. Escolha professores que acendem chamas.",
        "es": "La verdadera educaci\u00f3n despierta el deseo de aprender para siempre. Elige maestros que enciendan llamas."
    },
    "nature": {
        "en": "Nature is the slowest and best teacher. Spend time outside today.",
        "pt": "A natureza \u00e9 a mestra mais lenta e melhor. Passe tempo l\u00e1 fora hoje.",
        "es": "La naturaleza es la maestra m\u00e1s lenta y mejor. Pasa tiempo afuera hoy."
    },
    "art": {
        "en": "Art shapes us in ways arguments cannot. Surround yourself with beauty.",
        "pt": "A arte nos molda de maneiras que argumentos n\u00e3o podem. Cerque-se de beleza.",
        "es": "El arte nos moldea de maneras que los argumentos no pueden. Rod\u00e9ate de belleza."
    },
    "writing": {
        "en": "Writing clarifies thinking. Put your ideas on paper to discover what you really believe.",
        "pt": "Escrever clarifica o pensamento. Coloque suas ideias no papel para descobrir no que realmente acredita.",
        "es": "Escribir clarifica el pensamiento. Pon tus ideas en papel para descubrir en qu\u00e9 crees realmente."
    },
    "fear": {
        "en": "Do the thing you fear and the death of fear is certain. Action dissolves dread.",
        "pt": "Fa\u00e7a a coisa que voc\u00ea teme e a morte do medo \u00e9 certa. A a\u00e7\u00e3o dissolve o pavor.",
        "es": "Haz la cosa que temes y la muerte del miedo es segura. La acci\u00f3n disuelve el pavor."
    },
    "religion": {
        "en": "Religion is what you do when no one is watching. Your daily acts are your real creed.",
        "pt": "Religi\u00e3o \u00e9 o que voc\u00ea faz quando ningu\u00e9m est\u00e1 olhando. Seus atos di\u00e1rios s\u00e3o seu credo real.",
        "es": "La religi\u00f3n es lo que haces cuando nadie te mira. Tus actos diarios son tu credo real."
    },
    "today": {
        "en": "Today is the only day you have. Make it worthy of remembering.",
        "pt": "Hoje \u00e9 o \u00fanico dia que voc\u00ea tem. Torne-o digno de ser lembrado.",
        "es": "Hoy es el \u00fanico d\u00eda que tienes. H\u00e1zlo digno de ser recordado."
    },
    "thought": {
        "en": "Your life is shaped by your habitual thoughts. Tend the inner garden.",
        "pt": "Sua vida \u00e9 moldada por seus pensamentos habituais. Cuide do jardim interior.",
        "es": "Tu vida est\u00e1 moldeada por tus pensamientos habituales. Cuida el jard\u00edn interior."
    },
    "society": {
        "en": "Society pulls toward conformity; resist gently and remain yourself.",
        "pt": "A sociedade puxa para a conformidade; resista gentilmente e permane\u00e7a voc\u00ea mesmo.",
        "es": "La sociedad empuja hacia la conformidad; resiste con suavidad y mant\u00e9nte tu mismo."
    },
    "power": {
        "en": "Power lives in the moment of choice. Recognize it and act with intention.",
        "pt": "O poder vive no momento da escolha. Reconhe\u00e7a-o e aja com inten\u00e7\u00e3o.",
        "es": "El poder vive en el momento de la elecci\u00f3n. Recon\u00f3celo y act\u00faa con intenci\u00f3n."
    },
    "soul": {
        "en": "Tend your inner life as carefully as your outer one. The soul shapes everything else.",
        "pt": "Cuide da sua vida interior t\u00e3o cuidadosamente quanto da exterior. A alma molda tudo o mais.",
        "es": "Cuida tu vida interior tan cuidadosamente como la exterior. El alma moldea todo lo dem\u00e1s."
    },
    "love": {
        "en": "Love is not a feeling alone but a way of acting. Practice it concretely today.",
        "pt": "O amor n\u00e3o \u00e9 apenas um sentimento, mas um modo de agir. Pratique-o concretamente hoje.",
        "es": "El amor no es solo un sentimiento sino una forma de actuar. Pract\u00edcalo concretamente hoy."
    },
    "self_know": {
        "en": "Stop asking who others think you are. Discover who you truly are by acting on your deepest values.",
        "pt": "Pare de perguntar quem os outros pensam que voc\u00ea \u00e9. Descubra quem voc\u00ea realmente \u00e9 agindo sobre seus valores mais profundos.",
        "es": "Deja de preguntar qui\u00e9n creen los dem\u00e1s que eres. Descubre qui\u00e9n eres realmente actuando sobre tus valores m\u00e1s profundos."
    },
    "individual": {
        "en": "Each soul is unique and unrepeatable. Stop comparing yourself to others.",
        "pt": "Cada alma \u00e9 \u00fanica e irrepet\u00edvel. Pare de se comparar com os outros.",
        "es": "Cada alma es \u00fanica e irrepetible. Deja de compararte con los dem\u00e1s."
    },
    "trust_self": {
        "en": "Listen to the whisper that is meant only for you. Trust your own quiet knowing.",
        "pt": "Escute o sussurro destinado apenas a voc\u00ea. Confie no seu pr\u00f3prio conhecimento silencioso.",
        "es": "Escucha el susurro destinado solo a ti. Conf\u00eda en tu propio conocimiento silencioso."
    },
    "imagination": {
        "en": "Imagination is the gateway to the future. Spend time daily picturing what could be.",
        "pt": "A imagina\u00e7\u00e3o \u00e9 a porta para o futuro. Reserve tempo di\u00e1rio para imaginar o que pode ser.",
        "es": "La imaginaci\u00f3n es la puerta al futuro. Pasa tiempo diario imaginando lo que podr\u00eda ser."
    },
    "humility": {
        "en": "Humility opens doors that pride keeps closed. Practice not knowing.",
        "pt": "A humildade abre portas que o orgulho mant\u00e9m fechadas. Pratique o n\u00e3o saber.",
        "es": "La humildad abre puertas que el orgullo mantiene cerradas. Practica el no saber."
    },
    "work": {
        "en": "Real work is its own reward. Find what you love and pour yourself into it.",
        "pt": "O verdadeiro trabalho \u00e9 sua pr\u00f3pria recompensa. Encontre o que voc\u00ea ama e se entregue a ele.",
        "es": "El verdadero trabajo es su propia recompensa. Encuentra lo que amas y entr\u00e9gate a ello."
    },
    "fallback": {
        "en": "What is true is what works in life. Test ideas by their consequences in the real world.",
        "pt": "O que \u00e9 verdadeiro \u00e9 o que funciona na vida. Teste ideias pelas suas consequ\u00eancias no mundo real.",
        "es": "Lo que es verdadero es lo que funciona en la vida. Prueba las ideas por sus consecuencias en el mundo real."
    },
}

KEYWORDS = [
    (("self-trust", "trust", "self-reli", "yourself"), "self_reliance"),
    (("experience", "exp\u00e9rien"), "experience"),
    (("courage", "brave", "afraid", "coragem"), "courage"),
    (("book", "read", "library", "livro", "leitor"), "books"),
    (("friend", "amigo", "amizade"), "friendship"),
    (("happy", "happiness", "joy", "felic"), "happiness"),
    (("educat", "teach", "school", "pupil", "child", "student", "learn", "educa\u00e7", "aprend"), "education"),
    (("nature", "natural", "natureza"), "nature"),
    (("art", "beauty", "beautiful", "poet", "music", "arte", "beleza", "m\u00fasica"), "art"),
    (("writ", "write", "escrev"), "writing"),
    (("fear", "afraid", "terror", "medo", "phobia"), "fear"),
    (("god", "religion", "faith", "divine", "pray", "deus", "religi"), "religion"),
    (("day", "today", "moment", "now", "hoje", "hoje"), "today"),
    (("think", "thought", "mind", "pensamento"), "thought"),
    (("society", "people", "crowd", "popular", "sociedade"), "society"),
    (("power", "force", "strength", "poder"), "power"),
    (("soul", "inner", "interior", "alma"), "soul"),
    (("love", "amor", "lover"), "love"),
    (("know thyself", "self-know", "myself", "conhece-te"), "self_know"),
    (("individual", "unique", "person", "indiv\u00edduo", "single"), "individual"),
    (("imagin", "dream", "vision", "imagina"), "imagination"),
    (("humble", "humility", "modest", "humilde"), "humility"),
    (("work", "labor", "trabalho", "esfor\u00e7o"), "work"),
    (("freedom", "free", "liberty", "liberdade"), "freedom"),
    (("growth", "grow", "improve", "better", "melhor"), "growth"),
    (("act", "do", "action", "deed", "fazer", "a\u00e7\u00e3o"), "action"),
    (("idea", "thought", "concept", "ideia"), "thought_action"),
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

with open('c:/Users/lalli/Flutter/coach_phrase_app/reflections_pragmatism.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f'Generated {len(result)} pragmatism reflections')

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
