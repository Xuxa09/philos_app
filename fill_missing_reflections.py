"""Fill missing reflections for pragmatism, existentialism, and eastern quotes.

Parses quotes_data.dart, finds QuoteModels with empty reflections,
generates reflections via keyword-matched templates, and writes them
back directly into quotes_data.dart.
"""
import re
import os

DART_PATH = 'c:/Users/lalli/Flutter/coach_phrase_app/lib/data/services/quotes_data.dart'


# ===========================================================================
# === Pragmatism templates (Emerson, James, Dewey, Peirce, Rorty) ===========
# ===========================================================================
PRAGMATISM_T = {
    "action": {
        "en": "Truth shows itself in action, not in argument. Test your beliefs by living them.",
        "pt": "A verdade se mostra na ação, não no argumento. Teste suas crenças vivendo-as.",
        "es": "La verdad se muestra en la acción, no en el argumento. Prueba tus creencias viviéndolas."
    },
    "self_reliance": {
        "en": "Trust yourself. The voice that speaks to you alone is worth more than all borrowed wisdom.",
        "pt": "Confie em si mesmo. A voz que fala só a você vale mais que toda sabedoria emprestada.",
        "es": "Confía en ti mismo. La voz que te habla a ti solo vale más que toda sabiduría prestada."
    },
    "experience": {
        "en": "Experience is the only true teacher. Let life write its lessons on you.",
        "pt": "A experiência é a única mestra verdadeira. Deixe a vida escrever suas lições em você.",
        "es": "La experiencia es la única maestra verdadera. Deja que la vida escriba sus lecciones en ti."
    },
    "growth": {
        "en": "Growth requires risking what you currently know. Step beyond your present self.",
        "pt": "O crescimento exige arriscar o que você atualmente sabe. Vá além do seu eu presente.",
        "es": "El crecimiento requiere arriesgar lo que ahora sabes. Ve más allá de tu yo presente."
    },
    "courage": {
        "en": "Courage is not the absence of fear but action in spite of it. Take the next bold step today.",
        "pt": "Coragem não é ausência de medo, mas ação apesar dele. Dê o próximo passo ousado hoje.",
        "es": "El coraje no es ausencia de miedo sino acción a pesar de él. Da el próximo paso audaz hoy."
    },
    "books": {
        "en": "Books are how minds across time meet. Read what shapes you, not what entertains you.",
        "pt": "Os livros são como mentes através do tempo se encontram. Leia o que o molda, não o que o entretém.",
        "es": "Los libros son cómo las mentes a través del tiempo se encuentran. Lee lo que te moldea, no lo que te entretiene."
    },
    "friendship": {
        "en": "Friendship is the rarest treasure life offers. Tend it with the care it deserves.",
        "pt": "A amizade é o tesouro mais raro que a vida oferece. Cultive-a com o cuidado que merece.",
        "es": "La amistad es el tesoro más raro que la vida ofrece. Cultívala con el cuidado que merece."
    },
    "thought_action": {
        "en": "Thinking matters only when it changes how you live. Test ideas by their fruits.",
        "pt": "O pensamento só importa quando muda como você vive. Teste ideias pelos seus frutos.",
        "es": "El pensamiento solo importa cuando cambia cómo vives. Prueba las ideas por sus frutos."
    },
    "freedom": {
        "en": "Freedom is the inner space where you choose without fear. Defend it daily.",
        "pt": "A liberdade é o espaço interior onde você escolhe sem medo. Defenda-o diariamente.",
        "es": "La libertad es el espacio interior donde eliges sin miedo. Defiéndelo diariamente."
    },
    "happiness": {
        "en": "Happiness is built by good action, not chased as a feeling. Do well and feeling follows.",
        "pt": "A felicidade é construída pela boa ação, não perseguida como sentimento. Faça o bem e o sentimento segue.",
        "es": "La felicidad se construye con buena acción, no se persigue como sentimiento. Haz el bien y el sentimiento sigue."
    },
    "education": {
        "en": "Real education awakens the desire to learn forever. Choose teachers who light fires.",
        "pt": "A verdadeira educação desperta o desejo de aprender para sempre. Escolha professores que acendem chamas.",
        "es": "La verdadera educación despierta el deseo de aprender para siempre. Elige maestros que enciendan llamas."
    },
    "nature": {
        "en": "Nature is the slowest and best teacher. Spend time outside today.",
        "pt": "A natureza é a mestra mais lenta e melhor. Passe tempo lá fora hoje.",
        "es": "La naturaleza es la maestra más lenta y mejor. Pasa tiempo afuera hoy."
    },
    "art": {
        "en": "Art shapes us in ways arguments cannot. Surround yourself with beauty.",
        "pt": "A arte nos molda de maneiras que argumentos não podem. Cerque-se de beleza.",
        "es": "El arte nos moldea de maneras que los argumentos no pueden. Rodéate de belleza."
    },
    "writing": {
        "en": "Writing clarifies thinking. Put your ideas on paper to discover what you really believe.",
        "pt": "Escrever clarifica o pensamento. Coloque suas ideias no papel para descobrir no que realmente acredita.",
        "es": "Escribir clarifica el pensamiento. Pon tus ideas en papel para descubrir en qué crees realmente."
    },
    "fear": {
        "en": "Do the thing you fear and the death of fear is certain. Action dissolves dread.",
        "pt": "Faça a coisa que você teme e a morte do medo é certa. A ação dissolve o pavor.",
        "es": "Haz la cosa que temes y la muerte del miedo es segura. La acción disuelve el pavor."
    },
    "religion": {
        "en": "Religion is what you do when no one is watching. Your daily acts are your real creed.",
        "pt": "Religião é o que você faz quando ninguém está olhando. Seus atos diários são seu credo real.",
        "es": "La religión es lo que haces cuando nadie te mira. Tus actos diarios son tu credo real."
    },
    "today": {
        "en": "Today is the only day you have. Make it worthy of remembering.",
        "pt": "Hoje é o único dia que você tem. Torne-o digno de ser lembrado.",
        "es": "Hoy es el único día que tienes. Hazlo digno de ser recordado."
    },
    "thought": {
        "en": "Your life is shaped by your habitual thoughts. Tend the inner garden.",
        "pt": "Sua vida é moldada por seus pensamentos habituais. Cuide do jardim interior.",
        "es": "Tu vida está moldeada por tus pensamientos habituales. Cuida el jardín interior."
    },
    "society": {
        "en": "Society pulls toward conformity; resist gently and remain yourself.",
        "pt": "A sociedade puxa para a conformidade; resista gentilmente e permaneça você mesmo.",
        "es": "La sociedad empuja hacia la conformidad; resiste con suavidad y mantente tu mismo."
    },
    "power": {
        "en": "Power lives in the moment of choice. Recognize it and act with intention.",
        "pt": "O poder vive no momento da escolha. Reconheça-o e aja com intenção.",
        "es": "El poder vive en el momento de la elección. Reconócelo y actúa con intención."
    },
    "soul": {
        "en": "Tend your inner life as carefully as your outer one. The soul shapes everything else.",
        "pt": "Cuide da sua vida interior tão cuidadosamente quanto da exterior. A alma molda tudo o mais.",
        "es": "Cuida tu vida interior tan cuidadosamente como la exterior. El alma moldea todo lo demás."
    },
    "love": {
        "en": "Love is not a feeling alone but a way of acting. Practice it concretely today.",
        "pt": "O amor não é apenas um sentimento, mas um modo de agir. Pratique-o concretamente hoje.",
        "es": "El amor no es solo un sentimiento sino una forma de actuar. Practícalo concretamente hoy."
    },
    "self_know": {
        "en": "Stop asking who others think you are. Discover who you truly are by acting on your deepest values.",
        "pt": "Pare de perguntar quem os outros pensam que você é. Descubra quem você realmente é agindo sobre seus valores mais profundos.",
        "es": "Deja de preguntar quién creen los demás que eres. Descubre quién eres realmente actuando sobre tus valores más profundos."
    },
    "individual": {
        "en": "Each soul is unique and unrepeatable. Stop comparing yourself to others.",
        "pt": "Cada alma é única e irrepetível. Pare de se comparar com os outros.",
        "es": "Cada alma es única e irrepetible. Deja de compararte con los demás."
    },
    "imagination": {
        "en": "Imagination is the gateway to the future. Spend time daily picturing what could be.",
        "pt": "A imaginação é a porta para o futuro. Reserve tempo diário para imaginar o que pode ser.",
        "es": "La imaginación es la puerta al futuro. Pasa tiempo diario imaginando lo que podría ser."
    },
    "humility": {
        "en": "Humility opens doors that pride keeps closed. Practice not knowing.",
        "pt": "A humildade abre portas que o orgulho mantém fechadas. Pratique o não saber.",
        "es": "La humildad abre puertas que el orgullo mantiene cerradas. Practica el no saber."
    },
    "work": {
        "en": "Real work is its own reward. Find what you love and pour yourself into it.",
        "pt": "O verdadeiro trabalho é sua própria recompensa. Encontre o que você ama e se entregue a ele.",
        "es": "El verdadero trabajo es su propia recompensa. Encuentra lo que amas y entrégate a ello."
    },
    "habit": {
        "en": "Habits shape destiny more than dramatic decisions. Tend the small daily choices.",
        "pt": "Os hábitos moldam o destino mais que decisões dramáticas. Cuide das pequenas escolhas diárias.",
        "es": "Los hábitos moldean el destino más que las decisiones dramáticas. Cuida las pequeñas elecciones diarias."
    },
    "doubt": {
        "en": "Doubt is the engine of inquiry. Welcome it as the starting point of real thinking.",
        "pt": "A dúvida é o motor da investigação. Acolha-a como ponto de partida do pensamento real.",
        "es": "La duda es el motor de la indagación. Acógela como punto de partida del pensamiento real."
    },
    "community": {
        "en": "We grow through belonging, not isolation. Invest in the community that shapes you.",
        "pt": "Crescemos pelo pertencer, não pelo isolamento. Invista na comunidade que o molda.",
        "es": "Crecemos por pertenecer, no por aislarnos. Invierte en la comunidad que te moldea."
    },
    "democracy": {
        "en": "Democracy is a way of life, not just a form of government. Practice it in daily encounters.",
        "pt": "A democracia é um modo de vida, não apenas uma forma de governo. Pratique-a em encontros diários.",
        "es": "La democracia es una forma de vida, no solo una forma de gobierno. Practícala en encuentros diarios."
    },
    "consequence": {
        "en": "Judge ideas by their consequences in life, not their elegance in theory.",
        "pt": "Julgue as ideias por suas consequências na vida, não por sua elegância na teoria.",
        "es": "Juzga las ideas por sus consecuencias en la vida, no por su elegancia en teoría."
    },
    "hope": {
        "en": "Hope is a discipline, not a feeling. Choose it again each morning.",
        "pt": "A esperança é uma disciplina, não um sentimento. Escolha-a novamente a cada manhã.",
        "es": "La esperanza es una disciplina, no un sentimiento. Elígela de nuevo cada mañana."
    },
    "fallback": {
        "en": "What is true is what works in life. Test ideas by their consequences in the real world.",
        "pt": "O que é verdadeiro é o que funciona na vida. Teste ideias pelas suas consequências no mundo real.",
        "es": "Lo que es verdadero es lo que funciona en la vida. Prueba las ideas por sus consecuencias en el mundo real."
    },
}

PRAGMATISM_KEYWORDS = [
    (("self-trust", "trust thyself", "self-reli", "rely on yourself"), "self_reliance"),
    (("experience", "experiência", "vivência"), "experience"),
    (("courage", "brave", "afraid", "coragem", "valent"), "courage"),
    (("book", "read", "library", "livro", "leitor"), "books"),
    (("friend", "amigo", "amizade", "companion"), "friendship"),
    (("happy", "happiness", "joy", "felic", "alegria"), "happiness"),
    (("educat", "teach", "school", "pupil", "student", "learn", "aprend"), "education"),
    (("nature", "natural", "natureza", "wild"), "nature"),
    (("beauty", "beautiful", "poet", "music", "arte", "beleza", "música"), "art"),
    (("writ", "write", "escrev", "poet"), "writing"),
    (("fear", "afraid", "terror", "medo", "phobia"), "fear"),
    (("god", "religion", "faith", "divine", "pray", "deus", "religi"), "religion"),
    (("today", "moment", "now", "hoje", "presente"), "today"),
    (("think", "thought", "mind", "pensamento"), "thought"),
    (("society", "crowd", "popular", "sociedade", "social"), "society"),
    (("power", "force", "strength", "poder"), "power"),
    (("soul", "inner", "interior", "alma"), "soul"),
    (("love", "amor", "lover"), "love"),
    (("know thyself", "self-know", "myself", "conhece-te", "conheça-se"), "self_know"),
    (("individual", "unique", "indivíduo", "single"), "individual"),
    (("imagin", "dream", "vision", "imagina"), "imagination"),
    (("humble", "humility", "modest", "humilde"), "humility"),
    (("work", "labor", "trabalho", "esforço"), "work"),
    (("freedom", "free", "liberty", "liberdade"), "freedom"),
    (("growth", "grow", "improve", "melhor"), "growth"),
    (("habit", "hábito", "routine", "rotina", "custom"), "habit"),
    (("doubt", "dúvida", "skeptic", "question", "questiona"), "doubt"),
    (("communit", "comunidade", "neighbor", "vizinho"), "community"),
    (("democrac", "democra"), "democracy"),
    (("consequence", "conseq", "result", "effect"), "consequence"),
    (("hope", "esperanç", "esperan"), "hope"),
    (("act", "action", "deed", "fazer", "ação"), "action"),
    (("idea", "concept", "ideia"), "thought_action"),
]


# ===========================================================================
# === Existentialism templates ==============================================
# ===========================================================================
EXIST_T = {
    "courage": {
        "en": "Courage is what makes the rest of life possible. Practice it in small daily acts.",
        "pt": "A coragem é o que torna o resto da vida possível. Pratique-a em pequenos atos diários.",
        "es": "El coraje es lo que hace posible el resto de la vida. Practícalo en pequeños actos diarios."
    },
    "freedom": {
        "en": "Freedom is heavy because it comes with responsibility. Carry it boldly rather than fleeing into comfortable lies.",
        "pt": "A liberdade é pesada porque vem com responsabilidade. Carregue-a com ousadia em vez de fugir para mentiras confortáveis.",
        "es": "La libertad es pesada porque viene con responsabilidad. Cargatéla con audacia en lugar de huir hacia mentiras cómodas."
    },
    "absurd": {
        "en": "Life has no preset meaning; you must create your own. Stop waiting for the universe to explain itself.",
        "pt": "A vida não tem sentido pré-definido; você precisa criar o seu. Pare de esperar que o universo se explique.",
        "es": "La vida no tiene sentido predefinido; debes crear el tuyo. Deja de esperar que el universo se explique."
    },
    "self_create": {
        "en": "You are not a fixed thing; you become through your choices. Choose what you want to become today.",
        "pt": "Você não é algo fixo; você se torna através das escolhas. Escolha o que quer se tornar hoje.",
        "es": "No eres algo fijo; te vuelves a través de tus elecciones. Elige en qué quieres convertirte hoy."
    },
    "death": {
        "en": "Awareness of death sharpens life. Use mortality as a daily teacher, not a future enemy.",
        "pt": "A consciência da morte aguça a vida. Use a mortalidade como mestra diária, não como inimiga futura.",
        "es": "La conciencia de la muerte afila la vida. Usa la mortalidad como maestra diaria, no como enemiga futura."
    },
    "love": {
        "en": "Love demands risk; refusing love costs more than its wounds. Open yourself anyway.",
        "pt": "O amor exige risco; recusar o amor custa mais que suas feridas. Abra-se mesmo assim.",
        "es": "El amor exige riesgo; rechazar el amor cuesta más que sus heridas. Ábrete de todas formas."
    },
    "solitude": {
        "en": "Solitude is not loneliness; it is intimacy with yourself. Learn to enjoy your own company.",
        "pt": "A solidão não é isolamento; é intimidade consigo mesmo. Aprenda a desfrutar da sua própria companhia.",
        "es": "La soledad no es aislamiento; es intimidad contigo mismo. Aprende a disfrutar de tu propia compañía."
    },
    "truth": {
        "en": "Truth is more elusive than we admit; most certainties are inherited. Question what you have never questioned.",
        "pt": "A verdade é mais elusiva do que admitimos; a maioria das certezas é herdada. Questione o que você nunca questionou.",
        "es": "La verdad es más elusiva de lo que admitimos; la mayoría de las certezas son heredadas. Cuestiona lo que nunca has cuestionado."
    },
    "self_knowledge": {
        "en": "Knowing yourself is harder than any external pursuit. Begin every day with one honest question about who you are.",
        "pt": "Conhecer a si mesmo é mais difícil do que qualquer busca externa. Comece cada dia com uma pergunta honesta sobre quem você é.",
        "es": "Conocerse a uno mismo es más difícil que cualquier búsqueda externa. Comienza cada día con una pregunta honesta sobre quién eres."
    },
    "happiness": {
        "en": "Happiness is not chased but built. Each meaningful choice is a brick in its wall.",
        "pt": "A felicidade não é perseguida mas construída. Cada escolha significativa é um tijolo em sua parede.",
        "es": "La felicidad no se persigue sino se construye. Cada elección significativa es un ladrillo en su muro."
    },
    "despair": {
        "en": "Despair often hides as quiet resignation. Notice it and refuse to call it normal life.",
        "pt": "O desespero frequentemente se esconde como resignação silenciosa. Note-o e se recuse a chamá-lo de vida normal.",
        "es": "La desesperación a menudo se esconde como resignación silenciosa. Nótalo y recházalo como vida normal."
    },
    "create": {
        "en": "Creating is how we answer the silence of the universe. Make something today, however small.",
        "pt": "Criar é como respondemos ao silêncio do universo. Crie algo hoje, por menor que seja.",
        "es": "Crear es cómo respondemos al silencio del universo. Crea algo hoy, por pequeño que sea."
    },
    "morality": {
        "en": "Inherited morals deserve scrutiny. Decide what you actually believe rather than what you were told.",
        "pt": "Morais herdadas merecem escrutínio. Decida no que você realmente acredita, não no que lhe foi dito.",
        "es": "Las morales heredadas merecen escrutinio. Decide en qué crees realmente, no en lo que te dijeron."
    },
    "society": {
        "en": "Society wants you to be predictable; freedom requires being undefined. Resist the pressure to conform.",
        "pt": "A sociedade quer que você seja previsível; a liberdade exige ser indefinido. Resista à pressão para se conformar.",
        "es": "La sociedad quiere que seas predecible; la libertad requiere ser indefinido. Resiste la presión para conformarte."
    },
    "religion": {
        "en": "Faith is a personal struggle, not a borrowed answer. Find what you actually believe.",
        "pt": "A fé é uma luta pessoal, não uma resposta emprestada. Encontre no que você realmente acredita.",
        "es": "La fe es una lucha personal, no una respuesta prestada. Encuentra en qué crees realmente."
    },
    "art": {
        "en": "Art is how we make sense of being alive. Create or appreciate something beautiful today.",
        "pt": "A arte é como damos sentido a estar vivo. Crie ou aprecie algo belo hoje.",
        "es": "El arte es cómo damos sentido al estar vivo. Crea o aprecia algo bello hoy."
    },
    "writing": {
        "en": "Writing is a way of discovering what you think. Put words to your most confused feelings.",
        "pt": "Escrever é um modo de descobrir o que você pensa. Dê palavras aos seus sentimentos mais confusos.",
        "es": "Escribir es una forma de descubrir lo que piensas. Dale palabras a tus sentimientos más confusos."
    },
    "fear": {
        "en": "What you fear shrinks when examined directly. Look at your fears and watch them lose power.",
        "pt": "O que você teme encolhe quando examinado diretamente. Olhe para seus medos e veja-os perder poder.",
        "es": "Lo que temes se encoge cuando lo examinas directamente. Mira tus miedos y obsérvalos perder poder."
    },
    "time": {
        "en": "The present is the only time that exists. Stop living in regret or anticipation.",
        "pt": "O presente é o único tempo que existe. Pare de viver no arrependimento ou na antecipação.",
        "es": "El presente es el único tiempo que existe. Deja de vivir en el arrepentimiento o la anticipación."
    },
    "passion": {
        "en": "Passion gives life its texture. Honor your strongest feelings rather than suppressing them.",
        "pt": "A paixão dá à vida sua textura. Honre seus sentimentos mais fortes em vez de suprimi-los.",
        "es": "La pasión da textura a la vida. Honra tus sentimientos más fuertes en lugar de suprimirlos."
    },
    "suffering": {
        "en": "Suffering does not give meaning, but meaning makes suffering bearable. Find your why.",
        "pt": "O sofrimento não dá sentido, mas o sentido torna o sofrimento suportável. Encontre seu porquê.",
        "es": "El sufrimiento no da sentido, pero el sentido hace el sufrimiento soportable. Encuentra tu porqué."
    },
    "humanity": {
        "en": "We are flawed but capable of greatness. Honor both sides of being human.",
        "pt": "Somos imperfeitos mas capazes de grandeza. Honre ambos os lados de ser humano.",
        "es": "Somos imperfectos pero capaces de grandeza. Honra ambos lados de ser humano."
    },
    "rebellion": {
        "en": "Some refusals are essential to being you. Know what you will never accept.",
        "pt": "Algumas recusas são essenciais para ser você. Saiba o que você nunca aceitará.",
        "es": "Algunas negativas son esenciales para ser tú. Sabe lo que nunca aceptarás."
    },
    "doubt": {
        "en": "Doubt is the beginning of authentic thought. Trust questions more than easy answers.",
        "pt": "A dúvida é o começo do pensamento autêntico. Confie mais nas perguntas do que em respostas fáceis.",
        "es": "La duda es el inicio del pensamiento auténtico. Confía más en las preguntas que en las respuestas fáciles."
    },
    "individual": {
        "en": "You are unrepeatable. Stop comparing your path to anyone else's.",
        "pt": "Você é irrepetível. Pare de comparar seu caminho com o de qualquer outro.",
        "es": "Eres irrepetible. Deja de comparar tu camino con el de cualquier otro."
    },
    "absurdism": {
        "en": "The absurd is what we feel when reason meets a silent universe. Live in spite of it.",
        "pt": "O absurdo é o que sentimos quando a razão encontra um universo silencioso. Viva apesar dele.",
        "es": "El absurdo es lo que sentimos cuando la razón encuentra un universo silencioso. Vive a pesar de ello."
    },
    "memory": {
        "en": "Memory shapes who we are, but we shape memory too. Choose carefully what you keep alive.",
        "pt": "A memória molda quem somos, mas nós também moldamos a memória. Escolha cuidadosamente o que mantém vivo.",
        "es": "La memoria moldea quiénes somos, pero nosotros también moldeamos la memoria. Elige cuidadosamente lo que mantienes vivo."
    },
    "language": {
        "en": "Words shape the worlds we can see. Choose them with care; they make reality.",
        "pt": "As palavras moldam os mundos que conseguimos ver. Escolha-as com cuidado; elas fazem a realidade.",
        "es": "Las palabras moldean los mundos que podemos ver. Elígelas con cuidado; hacen la realidad."
    },
    "act": {
        "en": "Action is what makes you real. Stop describing yourself and start being yourself.",
        "pt": "A ação é o que o torna real. Pare de descrever a si mesmo e comece a ser você mesmo.",
        "es": "La acción es lo que te hace real. Deja de describirte y comienza a ser tú mismo."
    },
    "anxiety": {
        "en": "Anxiety reveals the weight of freedom. Sit with it rather than fleeing into distraction.",
        "pt": "A ansiedade revela o peso da liberdade. Sente-se com ela em vez de fugir para a distração.",
        "es": "La ansiedad revela el peso de la libertad. Siéntate con ella en lugar de huir hacia la distracción."
    },
    "authenticity": {
        "en": "Being authentic costs more than being approved of, and matters infinitely more. Choose yourself.",
        "pt": "Ser autêntico custa mais do que ser aprovado, e importa infinitamente mais. Escolha a si mesmo.",
        "es": "Ser auténtico cuesta más que ser aprobado, e importa infinitamente más. Elígete a ti mismo."
    },
    "responsibility": {
        "en": "You are responsible for what you become. No upbringing or circumstance writes the final line.",
        "pt": "Você é responsável pelo que se torna. Nenhuma criação ou circunstância escreve a linha final.",
        "es": "Eres responsable de lo que te conviertes. Ninguna crianza o circunstancia escribe la línea final."
    },
    "meaning": {
        "en": "Meaning is not found, it is made. Decide what your life will mean and live accordingly.",
        "pt": "O sentido não é encontrado, é feito. Decida o que sua vida significará e viva conforme.",
        "es": "El significado no se encuentra, se hace. Decide qué significará tu vida y vive en consecuencia."
    },
    "choice": {
        "en": "Every moment offers a choice; refusing to choose is itself a choice. Choose consciously.",
        "pt": "Cada momento oferece uma escolha; recusar-se a escolher já é uma escolha. Escolha conscientemente.",
        "es": "Cada momento ofrece una elección; rehusarse a elegir es ya una elección. Elige conscientemente."
    },
    "fallback": {
        "en": "Existence comes before essence; you are what you choose to do, not what you were born as.",
        "pt": "A existência precede a essência; você é o que escolhe fazer, não aquilo com que nasceu.",
        "es": "La existencia precede a la esencia; eres lo que eliges hacer, no lo que naciste siendo."
    },
}

EXIST_KEYWORDS = [
    (("courage", "brave", "coragem"), "courage"),
    (("freedom", "free will", "liberty", "liberdade"), "freedom"),
    (("absurd", "absurdo"), "absurd"),
    (("becom", "self-creat", "torna-se", "torna"), "self_create"),
    (("death", "die", "mortal", "dying", "morte", "morrer"), "death"),
    (("love", "amor", "lover"), "love"),
    (("alone", "lonely", "solitude", "solidão", "isolam"), "solitude"),
    (("truth", "true", "lies", "lying", "verdade"), "truth"),
    (("self-know", "myself", "interior", "knowing yourself", "conhece-te"), "self_knowledge"),
    (("happy", "happiness", "joy", "felic", "alegria"), "happiness"),
    (("despair", "desespero", "melanchol", "sadness", "tristeza"), "despair"),
    (("create", "creation", "creating", "criar", "artist"), "create"),
    (("moral", "ethic", "good and evil", "moralidade"), "morality"),
    (("society", "crowd", "people", "state", "social", "sociedade"), "society"),
    (("god", "religion", "faith", "pray", "deus", "religi"), "religion"),
    (("write", "writer", "literature", "escrev"), "writing"),
    (("fear", "afraid", "terror", "medo"), "fear"),
    (("anxiety", "anguish", "angst", "ansied"), "anxiety"),
    (("authentic", "autêntic", "genuine"), "authenticity"),
    (("responsib", "responsável", "responsabilidade"), "responsibility"),
    (("meaning", "sentido", "purpose", "propósito"), "meaning"),
    (("choice", "choose", "escolh"), "choice"),
    (("time", "moment", "today", "future", "past", "tempo", "presente"), "time"),
    (("passion", "intense", "feeling", "emot", "paix", "sentimento"), "passion"),
    (("suffer", "pain", "sorrow", "grief", "sofr", "dor"), "suffering"),
    (("human", "humanit", "homem", "humano"), "humanity"),
    (("rebel", "refuse", "revolt", "rebeli", "recusa"), "rebellion"),
    (("doubt", "question", "skeptic", "dúvida", "questiona"), "doubt"),
    (("indiv", "unique", "indivíduo"), "individual"),
    (("sisyphus", "stranger", "estran"), "absurdism"),
    (("memory", "remember", "recall", "lembr", "memória"), "memory"),
    (("word", "language", "speak", "speech", "palavra", "linguagem"), "language"),
    (("act", "action", "deed", "fazer", "ação"), "act"),
]


# ===========================================================================
# === Eastern templates =====================================================
# ===========================================================================
EAST_T = {
    "love": {
        "en": "Love is both a source of strength and an act of courage. Practice it as both gift and discipline.",
        "pt": "O amor é ao mesmo tempo fonte de força e ato de coragem. Pratique-o como presente e disciplina.",
        "es": "El amor es a la vez fuente de fuerza y acto de coraje. Practícalo como regalo y disciplina."
    },
    "persistence": {
        "en": "Pace matters less than direction. Keep moving toward what matters and the distance closes itself.",
        "pt": "O ritmo importa menos que a direção. Continue avançando para o que importa e a distância se fecha sozinha.",
        "es": "El ritmo importa menos que la dirección. Sigue avanzando hacia lo que importa y la distancia se cierra sola."
    },
    "emptiness": {
        "en": "What is empty is what makes things useful. Honor the spaces in your life as much as the substance.",
        "pt": "O que está vazio é o que torna as coisas úteis. Honre os espaços em sua vida tanto quanto a substância.",
        "es": "Lo vacío es lo que hace útiles las cosas. Honra los espacios en tu vida tanto como la sustancia."
    },
    "let_go": {
        "en": "Holding tightly often loses what we want to keep. Release with open hands and see what remains.",
        "pt": "Segurar com força frequentemente perde o que queremos manter. Solte com mãos abertas e veja o que permanece.",
        "es": "Sostener con fuerza a menudo pierde lo que queremos guardar. Suelta con manos abiertas y mira lo que queda."
    },
    "self_mastery": {
        "en": "Conquering yourself is harder and more lasting than conquering others. Begin within.",
        "pt": "Conquistar a si mesmo é mais difícil e mais duradouro do que conquistar os outros. Comece por dentro.",
        "es": "Conquistarse a uno mismo es más difícil y duradero que conquistar a otros. Comienza por dentro."
    },
    "simplicity": {
        "en": "Life is simple when we stop adding to it. Subtract before you add today.",
        "pt": "A vida é simples quando paramos de adicionar a ela. Subtraia antes de adicionar hoje.",
        "es": "La vida es simple cuando dejamos de añadirle cosas. Resta antes de añadir hoy."
    },
    "present": {
        "en": "The present moment is all you ever truly have. Inhabit it fully before reaching for the next.",
        "pt": "O momento presente é tudo que você realmente tem. Habite-o plenamente antes de buscar o próximo.",
        "es": "El momento presente es todo lo que verdaderamente tienes. Habítalo plenamente antes de alcanzar el próximo."
    },
    "kindness": {
        "en": "Kindness costs little and creates much. Practice it especially with those who do not return it.",
        "pt": "A gentileza custa pouco e cria muito. Pratique-a especialmente com aqueles que não a retribuem.",
        "es": "La amabilidad cuesta poco y crea mucho. Practícala especialmente con quienes no la devuelven."
    },
    "wisdom_action": {
        "en": "True wisdom shows in action, not in words. Let your life teach more than your speech.",
        "pt": "A verdadeira sabedoria se mostra na ação, não em palavras. Deixe sua vida ensinar mais que sua fala.",
        "es": "La verdadera sabiduría se muestra en la acción, no en palabras. Deja que tu vida enseñe más que tu discurso."
    },
    "anger": {
        "en": "Anger held longer harms you more than its target. Drop the burning coal from your hand.",
        "pt": "A raiva mantida por mais tempo o machuca mais que seu alvo. Solte o carvão em brasa da sua mão.",
        "es": "La ira sostenida más tiempo te daña más que a su blanco. Suelta el carbón encendido de tu mano."
    },
    "fear": {
        "en": "Fear is largely an illusion built by imagination. Examine what you fear and watch it shrink.",
        "pt": "O medo é em grande parte uma ilusão construída pela imaginação. Examine o que você teme e veja-o encolher.",
        "es": "El miedo es en gran parte una ilusión construida por la imaginación. Examina lo que temes y míralo encogerse."
    },
    "wisdom": {
        "en": "Wisdom is not stored knowledge but living understanding. Practice it in the smallest decisions.",
        "pt": "A sabedoria não é conhecimento armazenado, mas entendimento vivo. Pratique-a nas menores decisões.",
        "es": "La sabiduría no es conocimiento almacenado sino comprensión viva. Practícala en las decisiones más pequeñas."
    },
    "contentment": {
        "en": "Contentment is the rare wealth that no fortune can buy. Cultivate it in what you already have.",
        "pt": "O contentamento é a rara riqueza que nenhuma fortuna pode comprar. Cultive-o no que você já tem.",
        "es": "El contentamiento es la rara riqueza que ninguna fortuna puede comprar. Cultívalo en lo que ya tienes."
    },
    "war": {
        "en": "Even victory in war should be mourned, not celebrated. Avoid every conflict that can be avoided.",
        "pt": "Até a vitória na guerra deve ser lamentada, não celebrada. Evite todo conflito que possa ser evitado.",
        "es": "Incluso la victoria en la guerra debe ser lamentada, no celebrada. Evita todo conflicto que pueda evitarse."
    },
    "soft_strong": {
        "en": "What is soft outlasts what is hard. Yield where rigid things break.",
        "pt": "O que é macio dura mais que o que é duro. Ceda onde coisas rígidas quebram.",
        "es": "Lo blando dura más que lo duro. Cede donde las cosas rígidas se rompen."
    },
    "mistake": {
        "en": "Mistakes are only mistakes when uncorrected. Notice yours and adjust without shame.",
        "pt": "Os erros só são erros quando não corrigidos. Note os seus e ajuste sem vergonha.",
        "es": "Los errores solo son errores cuando no se corrigen. Nota los tuyos y ajusta sin vergüenza."
    },
    "silence": {
        "en": "Silence is where the deepest truths emerge. Make room for it daily.",
        "pt": "O silêncio é onde as verdades mais profundas emergem. Faça espaço para ele diariamente.",
        "es": "El silencio es donde las verdades más profundas emergen. Haz espacio para él diariamente."
    },
    "learning": {
        "en": "Learn with humility, urgency, and reverence. Treat every lesson as precious and fleeting.",
        "pt": "Aprenda com humildade, urgência e reverência. Trate cada lição como preciosa e fugaz.",
        "es": "Aprende con humildad, urgencia y reverencia. Trata cada lección como preciosa y efímera."
    },
    "small_great": {
        "en": "Big things are made of small ones. Care for the small details and the great deeds will follow.",
        "pt": "Grandes coisas são feitas de pequenas. Cuide dos pequenos detalhes e os grandes feitos seguirão.",
        "es": "Las grandes cosas están hechas de pequeñas. Cuida los pequeños detalles y las grandes hazañas seguirán."
    },
    "leader": {
        "en": "The best leaders serve. Lead by walking behind, not in front.",
        "pt": "Os melhores líderes servem. Lidere caminhando atrás, não à frente.",
        "es": "Los mejores líderes sirven. Lidera caminando detrás, no delante."
    },
    "teacher": {
        "en": "True teachers connect past to present, tradition to today. Learn from those who do both.",
        "pt": "Verdadeiros mestres conectam passado e presente, tradição e hoje. Aprenda com aqueles que fazem ambos.",
        "es": "Los verdaderos maestros conectan pasado y presente, tradición y hoy. Aprende de quienes hacen ambos."
    },
    "balance": {
        "en": "Opposites belong to each other. Welcome both light and shadow as part of the same whole.",
        "pt": "Os opostos pertencem um ao outro. Acolha tanto a luz quanto a sombra como parte do mesmo todo.",
        "es": "Los opuestos se pertenecen mutuamente. Acoge tanto la luz como la sombra como parte del mismo todo."
    },
    "non_action": {
        "en": "True power does not seek itself. Practice doing without trying.",
        "pt": "O verdadeiro poder não se busca. Pratique fazer sem tentar.",
        "es": "El verdadero poder no se busca a sí mismo. Practica hacer sin intentar."
    },
    "compassion": {
        "en": "Compassion is recognition that we share the same struggle. Bring it especially to the unworthy.",
        "pt": "A compaixão é o reconhecimento de que compartilhamos a mesma luta. Traga-a especialmente aos indignos.",
        "es": "La compasión es el reconocimiento de que compartimos la misma lucha. Tráela especialmente a los indignos."
    },
    "duty": {
        "en": "Do what is yours to do, then release the result. Devotion without attachment is the way.",
        "pt": "Faça o que é seu para fazer, depois solte o resultado. Devoção sem apego é o caminho.",
        "es": "Haz lo que es tuyo hacer, luego suelta el resultado. Devoción sin apego es el camino."
    },
    "desire": {
        "en": "Desire blinds; freedom from desire reveals. Practice wanting nothing in this moment.",
        "pt": "O desejo cega; a liberdade do desejo revela. Pratique não querer nada neste momento.",
        "es": "El deseo ciega; la libertad del deseo revela. Practica no querer nada en este momento."
    },
    "way": {
        "en": "The way that can be named is not the eternal way. Walk it without trying to define it.",
        "pt": "O caminho que pode ser nomeado não é o caminho eterno. Trilhe-o sem tentar defini-lo.",
        "es": "El camino que puede ser nombrado no es el camino eterno. Camínalo sin intentar definirlo."
    },
    "virtue": {
        "en": "Virtue is its own reward; vice is its own punishment. Live so your conscience is light.",
        "pt": "A virtude é sua própria recompensa; o vício é seu próprio castigo. Viva para que sua consciência seja leve.",
        "es": "La virtud es su propia recompensa; el vicio su propio castigo. Vive para que tu conciencia sea ligera."
    },
    "mind": {
        "en": "Your inner thoughts shape outer reality. Tend the garden of your mind carefully.",
        "pt": "Seus pensamentos interiores moldam a realidade exterior. Cuide do jardim da sua mente cuidadosamente.",
        "es": "Tus pensamientos interiores moldean la realidad exterior. Cuida el jardín de tu mente cuidadosamente."
    },
    "humility": {
        "en": "Bowing low keeps you grounded. The tallest trees are the first to fall.",
        "pt": "Curvar-se baixo o mantém enraizado. As árvores mais altas são as primeiras a cair.",
        "es": "Inclinarse bajo te mantiene enraizado. Los árboles más altos son los primeros en caer."
    },
    "fallback": {
        "en": "The way is found by walking, not by knowing. Take the next step in stillness and trust.",
        "pt": "O caminho se encontra caminhando, não sabendo. Dê o próximo passo em quietude e confiança.",
        "es": "El camino se encuentra caminando, no sabiendo. Da el próximo paso en quietud y confianza."
    },
}

EAST_KEYWORDS = [
    (("love", "amor", "compaixão"), "love"),
    (("compassion", "compaix", "mercy", "piedade"), "compassion"),
    (("persist", "perseveran", "continue", "constante"), "persistence"),
    (("empty", "void", "vazio"), "emptiness"),
    (("let go", "release", "solte", "soltar", "deix"), "let_go"),
    (("master yourself", "conquer yourself", "self-master", "self-conquer"), "self_mastery"),
    (("simpl", "simple", "few", "less"), "simplicity"),
    (("present", "now", "today", "presente", "hoje"), "present"),
    (("kind", "gentle", "gentile", "amabil", "bondade"), "kindness"),
    (("anger", "ira", "raiva", "wrath"), "anger"),
    (("fear", "afraid", "medo"), "fear"),
    (("wisdom", "wise", "sabedoria", "sábio"), "wisdom"),
    (("content", "satisfied", "contentment", "contentamento"), "contentment"),
    (("war", "battle", "fight", "guerra", "luta"), "war"),
    (("soft", "yield", "flexible", "macio", "ceder"), "soft_strong"),
    (("mistake", "error", "erro", "fault"), "mistake"),
    (("silen", "still", "quiet", "silêncio", "quietude"), "silence"),
    (("learn", "study", "aprend", "estudo"), "learning"),
    (("small", "tiny", "great journey", "thousand miles", "pequeno", "passo"), "small_great"),
    (("leader", "lead", "rule", "govern", "líder", "lidera"), "leader"),
    (("teach", "master", "mestre", "professor"), "teacher"),
    (("balance", "harmony", "yin", "yang", "harmonia", "opost"), "balance"),
    (("non-act", "wu wei", "action without", "doing without"), "non_action"),
    (("duty", "dever", "dharma", "karma"), "duty"),
    (("desire", "want", "crav", "desejo"), "desire"),
    (("way", "tao", "dao", "caminho"), "way"),
    (("virtue", "virtu", "virt", "good", "bom"), "virtue"),
    (("mind", "thought", "think", "mente", "pensamento"), "mind"),
    (("humble", "humility", "modest", "humilde"), "humility"),
    (("action", "act", "do", "ação", "fazer"), "wisdom_action"),
]


# ===========================================================================
# === Matching logic ========================================================
# ===========================================================================

CATEGORY_CONFIG = {
    'pragmatism': (PRAGMATISM_T, PRAGMATISM_KEYWORDS),
    'existentialism': (EXIST_T, EXIST_KEYWORDS),
    'eastern': (EAST_T, EAST_KEYWORDS),
}


def pick_template(text, category):
    templates, keywords = CATEGORY_CONFIG[category]
    text_lower = text.lower()
    for kws, template_key in keywords:
        for kw in kws:
            if kw in text_lower:
                return templates[template_key]
    return templates["fallback"]


# ===========================================================================
# === Dart string escaping ==================================================
# ===========================================================================

def escape_dart(s):
    """Escape for Dart single-quoted strings, non-ASCII to \\uXXXX."""
    result = []
    for ch in s:
        cp = ord(ch)
        if ch == '\\':
            result.append('\\\\')
        elif ch == "'":
            result.append("\\'")
        elif ch == '\n':
            result.append('\\n')
        elif ch == '\r':
            pass
        elif cp > 127:
            result.append(f'\\u{cp:04x}')
        else:
            result.append(ch)
    return ''.join(result)


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


# ===========================================================================
# === Main: parse and rewrite ===============================================
# ===========================================================================

def main():
    with open(DART_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    target_cats = set(CATEGORY_CONFIG.keys())
    applied = {cat: 0 for cat in target_cats}
    template_usage = {cat: {} for cat in target_cats}

    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"(\s+textEn: ')(.*)(',)\s*$", line)
        if not m:
            i += 1
            continue

        en_escaped = m.group(2)
        en_text = unescape_dart(en_escaped)

        # Look ahead to find reflection lines + category in the same QuoteModel block
        # Structure: textEn, textPt, textEs, reflectionEn, reflectionPt, reflectionEs, category
        end = min(i + 30, len(lines))

        refl_en_idx = refl_pt_idx = refl_es_idx = -1
        category = None
        current_refl_en = None

        for j in range(i + 1, end):
            ln = lines[j]
            if 'QuoteModel(' in ln or '];' in ln:
                break
            if refl_en_idx == -1:
                rm = re.match(r"(\s+reflectionEn: ')(.*)(',)\s*$", ln)
                if rm:
                    refl_en_idx = j
                    current_refl_en = rm.group(2)
                    continue
            if refl_pt_idx == -1:
                rm = re.match(r"(\s+reflectionPt: ')(.*)(',)\s*$", ln)
                if rm:
                    refl_pt_idx = j
                    continue
            if refl_es_idx == -1:
                rm = re.match(r"(\s+reflectionEs: ')(.*)(',)\s*$", ln)
                if rm:
                    refl_es_idx = j
                    continue
            cm = re.match(r"\s+category: '([^']+)',\s*$", ln)
            if cm:
                category = cm.group(1)
                break

        if (category in target_cats
                and refl_en_idx > 0 and refl_pt_idx > 0 and refl_es_idx > 0
                and (current_refl_en is None or current_refl_en.strip() == '')):
            ref = pick_template(en_text, category)
            en_r, pt_r, es_r = ref['en'], ref['pt'], ref['es']

            indent_en = re.match(r"^(\s+)reflectionEn:", lines[refl_en_idx]).group(1)
            indent_pt = re.match(r"^(\s+)reflectionPt:", lines[refl_pt_idx]).group(1)
            indent_es = re.match(r"^(\s+)reflectionEs:", lines[refl_es_idx]).group(1)

            lines[refl_en_idx] = f"{indent_en}reflectionEn: '{escape_dart(en_r)}',\n"
            lines[refl_pt_idx] = f"{indent_pt}reflectionPt: '{escape_dart(pt_r)}',\n"
            lines[refl_es_idx] = f"{indent_es}reflectionEs: '{escape_dart(es_r)}',\n"

            applied[category] += 1

            templates, _ = CATEGORY_CONFIG[category]
            for tname, t in templates.items():
                if t is ref:
                    template_usage[category][tname] = template_usage[category].get(tname, 0) + 1
                    break

        i += 1

    with open(DART_PATH, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print("Reflections applied:")
    total = 0
    for cat in sorted(applied.keys()):
        print(f"  {cat}: {applied[cat]}")
        total += applied[cat]
    print(f"  TOTAL: {total}")

    print()
    for cat in sorted(template_usage.keys()):
        print(f"\n[{cat}] template distribution:")
        for tname, count in sorted(template_usage[cat].items(), key=lambda x: -x[1]):
            print(f"  {tname}: {count}")


if __name__ == '__main__':
    main()
