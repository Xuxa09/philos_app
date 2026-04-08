"""Generate reflections for existentialism quotes using thematic auto-matching.

Strategy: 30 thematic templates + keyword-based matching to each quote.
Fallback: a generic 'existentialist' reflection.
"""
import json
import re

with open('c:/Users/lalli/Flutter/coach_phrase_app/existentialism_keys.json', 'r', encoding='utf-8') as f:
    keys = json.load(f)

# === Thematic templates ===
T = {
    "courage": {
        "en": "Courage is what makes the rest of life possible. Practice it in small daily acts.",
        "pt": "A coragem \u00e9 o que torna o resto da vida poss\u00edvel. Pratique-a em pequenos atos di\u00e1rios.",
        "es": "El coraje es lo que hace posible el resto de la vida. Pract\u00edcalo en peque\u00f1os actos diarios."
    },
    "freedom": {
        "en": "Freedom is heavy because it comes with responsibility. Carry it boldly rather than fleeing into comfortable lies.",
        "pt": "A liberdade \u00e9 pesada porque vem com responsabilidade. Carregue-a com ousadia em vez de fugir para mentiras confort\u00e1veis.",
        "es": "La libertad es pesada porque viene con responsabilidad. Cargat\u00e9la con audacia en lugar de huir hacia mentiras c\u00f3modas."
    },
    "absurd": {
        "en": "Life has no preset meaning; you must create your own. Stop waiting for the universe to explain itself.",
        "pt": "A vida n\u00e3o tem sentido pr\u00e9-definido; voc\u00ea precisa criar o seu. Pare de esperar que o universo se explique.",
        "es": "La vida no tiene sentido predefinido; debes crear el tuyo. Deja de esperar que el universo se explique."
    },
    "self_create": {
        "en": "You are not a fixed thing; you become through your choices. Choose what you want to become today.",
        "pt": "Voc\u00ea n\u00e3o \u00e9 algo fixo; voc\u00ea se torna atrav\u00e9s das escolhas. Escolha o que quer se tornar hoje.",
        "es": "No eres algo fijo; te vuelves a trav\u00e9s de tus elecciones. Elige en qu\u00e9 quieres convertirte hoy."
    },
    "death": {
        "en": "Awareness of death sharpens life. Use mortality as a daily teacher, not a future enemy.",
        "pt": "A consci\u00eancia da morte aguça a vida. Use a mortalidade como mestra di\u00e1ria, n\u00e3o como inimiga futura.",
        "es": "La conciencia de la muerte afila la vida. Usa la mortalidad como maestra diaria, no como enemiga futura."
    },
    "love": {
        "en": "Love demands risk; refusing love costs more than its wounds. Open yourself anyway.",
        "pt": "O amor exige risco; recusar o amor custa mais que suas feridas. Abra-se mesmo assim.",
        "es": "El amor exige riesgo; rechazar el amor cuesta m\u00e1s que sus heridas. \u00c1brete de todas formas."
    },
    "solitude": {
        "en": "Solitude is not loneliness; it is intimacy with yourself. Learn to enjoy your own company.",
        "pt": "A solid\u00e3o n\u00e3o \u00e9 isolamento; \u00e9 intimidade consigo mesmo. Aprenda a desfrutar da sua pr\u00f3pria companhia.",
        "es": "La soledad no es aislamiento; es intimidad contigo mismo. Aprende a disfrutar de tu propia compa\u00f1\u00eda."
    },
    "truth": {
        "en": "Truth is more elusive than we admit; most certainties are inherited. Question what you have never questioned.",
        "pt": "A verdade \u00e9 mais elusiva do que admitimos; a maioria das certezas \u00e9 herdada. Questione o que voc\u00ea nunca questionou.",
        "es": "La verdad es m\u00e1s elusiva de lo que admitimos; la mayor\u00eda de las certezas son heredadas. Cuestiona lo que nunca has cuestionado."
    },
    "self_knowledge": {
        "en": "Knowing yourself is harder than any external pursuit. Begin every day with one honest question about who you are.",
        "pt": "Conhecer a si mesmo \u00e9 mais dif\u00edcil do que qualquer busca externa. Comece cada dia com uma pergunta honesta sobre quem voc\u00ea \u00e9.",
        "es": "Conocerse a uno mismo es m\u00e1s dif\u00edcil que cualquier b\u00fasqueda externa. Comienza cada d\u00eda con una pregunta honesta sobre qui\u00e9n eres."
    },
    "happiness": {
        "en": "Happiness is not chased but built. Each meaningful choice is a brick in its wall.",
        "pt": "A felicidade n\u00e3o \u00e9 perseguida mas constru\u00edda. Cada escolha significativa \u00e9 um tijolo em sua parede.",
        "es": "La felicidad no se persigue sino se construye. Cada elecci\u00f3n significativa es un ladrillo en su muro."
    },
    "despair": {
        "en": "Despair often hides as quiet resignation. Notice it and refuse to call it normal life.",
        "pt": "O desespero frequentemente se esconde como resigna\u00e7\u00e3o silenciosa. Note-o e se recuse a cham\u00e1-lo de vida normal.",
        "es": "La desesperaci\u00f3n a menudo se esconde como resignaci\u00f3n silenciosa. N\u00f3talo y rech\u00e1zalo como vida normal."
    },
    "create": {
        "en": "Creating is how we answer the silence of the universe. Make something today, however small.",
        "pt": "Criar \u00e9 como respondemos ao sil\u00eancio do universo. Crie algo hoje, por menor que seja.",
        "es": "Crear es c\u00f3mo respondemos al silencio del universo. Crea algo hoy, por peque\u00f1o que sea."
    },
    "morality": {
        "en": "Inherited morals deserve scrutiny. Decide what you actually believe rather than what you were told.",
        "pt": "Morais herdadas merecem escrutínio. Decida no que voc\u00ea realmente acredita, n\u00e3o no que lhe foi dito.",
        "es": "Las morales heredadas merecen escrutinio. Decide en qu\u00e9 crees realmente, no en lo que te dijeron."
    },
    "society": {
        "en": "Society wants you to be predictable; freedom requires being undefined. Resist the pressure to conform.",
        "pt": "A sociedade quer que voc\u00ea seja previs\u00edvel; a liberdade exige ser indefinido. Resista \u00e0 press\u00e3o para se conformar.",
        "es": "La sociedad quiere que seas predecible; la libertad requiere ser indefinido. Resiste la presi\u00f3n para conformarte."
    },
    "religion": {
        "en": "Faith is a personal struggle, not a borrowed answer. Find what you actually believe.",
        "pt": "A f\u00e9 \u00e9 uma luta pessoal, n\u00e3o uma resposta emprestada. Encontre no que voc\u00ea realmente acredita.",
        "es": "La fe es una lucha personal, no una respuesta prestada. Encuentra en qu\u00e9 crees realmente."
    },
    "art": {
        "en": "Art is how we make sense of being alive. Create or appreciate something beautiful today.",
        "pt": "A arte \u00e9 como damos sentido a estar vivo. Crie ou aprecie algo belo hoje.",
        "es": "El arte es c\u00f3mo damos sentido al estar vivo. Crea o aprecia algo bello hoy."
    },
    "writing": {
        "en": "Writing is a way of discovering what you think. Put words to your most confused feelings.",
        "pt": "Escrever \u00e9 um modo de descobrir o que voc\u00ea pensa. D\u00ea palavras aos seus sentimentos mais confusos.",
        "es": "Escribir es una forma de descubrir lo que piensas. Dale palabras a tus sentimientos m\u00e1s confusos."
    },
    "fear": {
        "en": "What you fear shrinks when examined directly. Look at your fears and watch them lose power.",
        "pt": "O que voc\u00ea teme encolhe quando examinado diretamente. Olhe para seus medos e veja-os perder poder.",
        "es": "Lo que temes se encoge cuando lo examinas directamente. Mira tus miedos y obs\u00e9rvalos perder poder."
    },
    "time": {
        "en": "The present is the only time that exists. Stop living in regret or anticipation.",
        "pt": "O presente \u00e9 o \u00fanico tempo que existe. Pare de viver no arrependimento ou na antecipa\u00e7\u00e3o.",
        "es": "El presente es el \u00fanico tiempo que existe. Deja de vivir en el arrepentimiento o la anticipaci\u00f3n."
    },
    "passion": {
        "en": "Passion gives life its texture. Honor your strongest feelings rather than suppressing them.",
        "pt": "A paix\u00e3o d\u00e1 \u00e0 vida sua textura. Honre seus sentimentos mais fortes em vez de suprim\u00ed-los.",
        "es": "La pasi\u00f3n da textura a la vida. Honra tus sentimientos m\u00e1s fuertes en lugar de suprimirlos."
    },
    "suffering": {
        "en": "Suffering does not give meaning, but meaning makes suffering bearable. Find your why.",
        "pt": "O sofrimento n\u00e3o d\u00e1 sentido, mas o sentido torna o sofrimento suport\u00e1vel. Encontre seu porqu\u00ea.",
        "es": "El sufrimiento no da sentido, pero el sentido hace el sufrimiento soportable. Encuentra tu porqu\u00e9."
    },
    "humanity": {
        "en": "We are flawed but capable of greatness. Honor both sides of being human.",
        "pt": "Somos imperfeitos mas capazes de grandeza. Honre ambos os lados de ser humano.",
        "es": "Somos imperfectos pero capaces de grandeza. Honra ambos lados de ser humano."
    },
    "rebellion": {
        "en": "Some refusals are essential to being you. Know what you will never accept.",
        "pt": "Algumas recusas s\u00e3o essenciais para ser voc\u00ea. Saiba o que voc\u00ea nunca aceitar\u00e1.",
        "es": "Algunas negativas son esenciales para ser t\u00fa. Sabe lo que nunca aceptar\u00e1s."
    },
    "doubt": {
        "en": "Doubt is the beginning of authentic thought. Trust questions more than easy answers.",
        "pt": "A d\u00favida \u00e9 o come\u00e7o do pensamento aut\u00eantico. Confie mais nas perguntas do que em respostas f\u00e1ceis.",
        "es": "La duda es el inicio del pensamiento aut\u00e9ntico. Conf\u00eda m\u00e1s en las preguntas que en las respuestas f\u00e1ciles."
    },
    "individual": {
        "en": "You are unrepeatable. Stop comparing your path to anyone else's.",
        "pt": "Voc\u00ea \u00e9 irrepet\u00edvel. Pare de comparar seu caminho com o de qualquer outro.",
        "es": "Eres irrepetible. Deja de comparar tu camino con el de cualquier otro."
    },
    "absurdism": {
        "en": "The absurd is what we feel when reason meets a silent universe. Live in spite of it.",
        "pt": "O absurdo \u00e9 o que sentimos quando a raz\u00e3o encontra um universo silencioso. Viva apesar dele.",
        "es": "El absurdo es lo que sentimos cuando la raz\u00f3n encuentra un universo silencioso. Vive a pesar de ello."
    },
    "memory": {
        "en": "Memory shapes who we are, but we shape memory too. Choose carefully what you keep alive.",
        "pt": "A mem\u00f3ria molda quem somos, mas n\u00f3s tamb\u00e9m moldamos a mem\u00f3ria. Escolha cuidadosamente o que mant\u00e9m vivo.",
        "es": "La memoria moldea qui\u00e9nes somos, pero nosotros tambi\u00e9n moldeamos la memoria. Elige cuidadosamente lo que mantienes vivo."
    },
    "language": {
        "en": "Words shape the worlds we can see. Choose them with care; they make reality.",
        "pt": "As palavras moldam os mundos que conseguimos ver. Escolha-as com cuidado; elas fazem a realidade.",
        "es": "Las palabras moldean los mundos que podemos ver. El\u00edgelas con cuidado; hacen la realidad."
    },
    "act": {
        "en": "Action is what makes you real. Stop describing yourself and start being yourself.",
        "pt": "A a\u00e7\u00e3o \u00e9 o que o torna real. Pare de descrever a si mesmo e comece a ser voc\u00ea mesmo.",
        "es": "La acci\u00f3n es lo que te hace real. Deja de describirte y comienza a ser t\u00fa mismo."
    },
    "fallback": {
        "en": "Existence comes before essence; you are what you choose to do, not what you were born as.",
        "pt": "A exist\u00eancia precede a ess\u00eancia; voc\u00ea \u00e9 o que escolhe fazer, n\u00e3o aquilo com que nasceu.",
        "es": "La existencia precede a la esencia; eres lo que eliges hacer, no lo que naciste siendo."
    },
}

# === Keyword to template mapping ===
KEYWORDS = [
    (("courage", "brave", "fear", "afraid", "coragem"), "courage"),
    (("freedom", "free", "liberty", "liberdade"), "freedom"),
    (("absurd", "meaning", "absurdo"), "absurd"),
    (("becom", "create yourself", "self", "i am", "torna"), "self_create"),
    (("death", "die", "mortal", "dying", "born", "morte", "morrer"), "death"),
    (("love", "amor", "lover"), "love"),
    (("alone", "lonely", "solitude", "solid"), "solitude"),
    (("truth", "true", "lies", "lying", "verdade"), "truth"),
    (("know thyself", "myself", "self-know", "interior", "interi"), "self_knowledge"),
    (("happy", "happiness", "joy", "felic", "alegria"), "happiness"),
    (("despair", "desespero", "melanchol", "sad"), "despair"),
    (("create", "creation", "creating", "criar", "art", "arte", "music", "poet"), "create"),
    (("moral", "ethic", "good and evil", "right and wrong", "moralidade"), "morality"),
    (("society", "crowd", "people", "state", "social", "sociedade"), "society"),
    (("god", "religion", "faith", "pray", "deus", "religi"), "religion"),
    (("write", "writer", "book", "read", "literature", "escrev", "livro", "leitor"), "writing"),
    (("fear", "afraid", "terror", "anxiet", "medo", "ansied"), "fear"),
    (("time", "moment", "today", "future", "past", "tempo", "presente"), "time"),
    (("passion", "intense", "feel", "feeling", "emot", "paix", "sentimento"), "passion"),
    (("suffer", "pain", "sorrow", "grief", "agonia", "sofr", "dor"), "suffering"),
    (("man", "human", "humanit", "person", "homem"), "humanity"),
    (("rebel", "refuse", "no", "revolt", "rebeli", "recusa"), "rebellion"),
    (("doubt", "question", "skeptic", "d\u00favida", "questiona"), "doubt"),
    (("indiv", "unique", "alone", "self", "indiv\u00edduo"), "individual"),
    (("sisyphus", "absurd", "stranger", "estran"), "absurdism"),
    (("memory", "remember", "recall", "lembr", "mem\u00f3ria"), "memory"),
    (("word", "language", "speak", "speech", "palavra", "linguagem"), "language"),
    (("act", "action", "do", "make", "deed", "fazer", "a\u00e7\u00e3o"), "act"),
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

with open('c:/Users/lalli/Flutter/coach_phrase_app/reflections_existentialism.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f'Generated {len(result)} existentialism reflections')

# Stats by template
from collections import Counter
counts = Counter()
for key in keys:
    refl = pick_template(key)
    for name, t in T.items():
        if t == refl:
            counts[name] += 1
            break

print('\nTemplate distribution:')
for name, count in counts.most_common():
    print(f'  {name}: {count}')
