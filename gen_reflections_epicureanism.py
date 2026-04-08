"""Generate reflections for 143 epicureanism quotes."""
import json

with open('c:/Users/lalli/Flutter/coach_phrase_app/epicureanism_keys.json', 'r', encoding='utf-8') as f:
    keys = json.load(f)

# Reusable reflection templates - same theme = same reflection text
DEATH = {"en": "Death cannot harm us because it never coexists with us. Free yourself from this fear and live more boldly.",
         "pt": "A morte n\u00e3o pode nos ferir porque nunca coexiste conosco. Liberte-se desse medo e viva com mais ousadia.",
         "es": "La muerte no puede da\u00f1arnos porque nunca coexiste con nosotros. Lib\u00e9rate de este miedo y vive con m\u00e1s audacia."}

CONTENTMENT = {"en": "True wealth is wanting little, not having much. Practice gratitude for what you already possess.",
               "pt": "A verdadeira riqueza \u00e9 desejar pouco, n\u00e3o ter muito. Pratique a gratid\u00e3o pelo que voc\u00ea j\u00e1 possui.",
               "es": "La verdadera riqueza es desear poco, no tener mucho. Practica la gratitud por lo que ya posees."}

PHILOSOPHY = {"en": "Philosophy is not for one age or season; it is for the whole of life. Begin today, regardless of where you stand.",
              "pt": "A filosofia n\u00e3o \u00e9 para uma idade ou esta\u00e7\u00e3o; \u00e9 para toda a vida. Comece hoje, n\u00e3o importa onde voc\u00ea est\u00e1.",
              "es": "La filosof\u00eda no es para una edad o estaci\u00f3n; es para toda la vida. Comienza hoy, sin importar d\u00f3nde est\u00e9s."}

ANGER = {"en": "Anger is a fleeting madness; what you do under its influence often outlives the feeling. Pause before you act.",
         "pt": "A raiva \u00e9 uma loucura passageira; o que voc\u00ea faz sob sua influ\u00eancia frequentemente sobrevive ao sentimento. Pause antes de agir.",
         "es": "La ira es una locura pasajera; lo que haces bajo su influencia a menudo sobrevive al sentimiento. Haz una pausa antes de actuar."}

FRIENDSHIP = {"en": "Friendship is not just help in need but the trust that help would come if needed. Cultivate that trust.",
              "pt": "Amizade n\u00e3o \u00e9 s\u00f3 ajuda na necessidade, mas a confian\u00e7a de que a ajuda viria se necess\u00e1rio. Cultive essa confian\u00e7a.",
              "es": "La amistad no es solo ayuda en la necesidad, sino la confianza de que la ayuda vendr\u00eda si fuera necesaria. Cultiva esa confianza."}

PRESENT = {"en": "The future is uncertain, the past is gone. Only this present hour is yours to inhabit fully.",
           "pt": "O futuro \u00e9 incerto, o passado se foi. Apenas esta hora presente \u00e9 sua para habitar plenamente.",
           "es": "El futuro es incierto, el pasado se fue. Solo esta hora presente es tuya para habitar plenamente."}

ADVERSITY = {"en": "Hardship reveals what comfort hides. Trust that what you must endure today is shaping who you will become.",
             "pt": "A dificuldade revela o que o conforto esconde. Confie que o que voc\u00ea precisa suportar hoje est\u00e1 moldando quem voc\u00ea ser\u00e1.",
             "es": "La dificultad revela lo que la comodidad oculta. Conf\u00eda en que lo que debes soportar hoy est\u00e1 moldeando qui\u00e9n ser\u00e1s."}

BEGINNING = {"en": "Starting is half of finishing. Whatever you have been postponing, take the first small step today.",
             "pt": "Come\u00e7ar \u00e9 metade de terminar. O que quer que voc\u00ea esteja adiando, d\u00ea o primeiro pequeno passo hoje.",
             "es": "Empezar es la mitad de terminar. Sea lo que sea que hayas estado postergando, da el primer peque\u00f1o paso hoy."}

GREED = {"en": "Greed never finds its bottom; the more you chase, the more empty you become. Stop and notice what you already have.",
         "pt": "A gan\u00e2ncia nunca encontra seu fundo; quanto mais voc\u00ea persegue, mais vazio se torna. Pare e perceba o que j\u00e1 tem.",
         "es": "La codicia nunca encuentra su fondo; cuanto m\u00e1s persigues, m\u00e1s vac\u00edo te vuelves. Detente y observa lo que ya tienes."}

WISDOM = {"en": "Wisdom is not the same as knowledge; it lives in how you act, not what you know. Practice it daily.",
          "pt": "A sabedoria n\u00e3o \u00e9 o mesmo que conhecimento; vive em como voc\u00ea age, n\u00e3o no que sabe. Pratique-a diariamente.",
          "es": "La sabidur\u00eda no es lo mismo que el conocimiento; vive en c\u00f3mo act\u00faas, no en lo que sabes. Pract\u00edcala diariamente."}

reflections = [
    DEATH,  # 1
    GREED,  # 2
    {"en": "Nothing in life is owned, only borrowed. Hold all your possessions and relationships with open hands.",
     "pt": "Nada na vida \u00e9 possu\u00eddo, apenas emprestado. Segure todas as suas posses e rela\u00e7\u00f5es com m\u00e3os abertas.",
     "es": "Nada en la vida es propio, solo prestado. Sost\u00e9n todas tus posesiones y relaciones con manos abiertas."},  # 3
    {"en": "Promises kept build a life of integrity. Watch what you commit to, then honor it.",
     "pt": "Promessas cumpridas constroem uma vida de integridade. Cuide do que voc\u00ea se compromete, ent\u00e3o honre.",
     "es": "Las promesas cumplidas construyen una vida de integridad. Cuida lo que prometes, luego honra."},  # 4
    CONTENTMENT,  # 5
    PHILOSOPHY,  # 6
    {"en": "Philosophy without practical relief is empty noise. Test ideas by whether they make life more bearable.",
     "pt": "Filosofia sem al\u00edvio pr\u00e1tico \u00e9 ru\u00eddo vazio. Teste ideias pelo qu\u00e3o mais suport\u00e1vel tornam a vida.",
     "es": "La filosof\u00eda sin alivio pr\u00e1ctico es ruido vac\u00edo. Prueba las ideas por cu\u00e1nto hacen la vida m\u00e1s soportable."},  # 7
    PHILOSOPHY,  # 8
    {"en": "The classic problem of evil has no easy answer. Sit with the question instead of accepting comfortable lies.",
     "pt": "O problema cl\u00e1ssico do mal n\u00e3o tem resposta f\u00e1cil. Sente-se com a pergunta em vez de aceitar mentiras confort\u00e1veis.",
     "es": "El problema cl\u00e1sico del mal no tiene respuesta f\u00e1cil. Si\u00e9ntate con la pregunta en vez de aceptar mentiras c\u00f3modas."},  # 9
    BEGINNING,  # 10
    FRIENDSHIP,  # 11
    GREED,  # 12
    DEATH,  # 13
    DEATH,  # 14
    {"en": "Govern yourself or your impulses will govern you. The choice is daily and lifelong.",
     "pt": "Governe a si mesmo ou seus impulsos governar\u00e3o voc\u00ea. A escolha \u00e9 di\u00e1ria e vital\u00edcia.",
     "es": "Gob\u00edrnate a ti mismo o tus impulsos te gobernar\u00e1n. La elecci\u00f3n es diaria y de por vida."},  # 15
    FRIENDSHIP,  # 16
    {"en": "Love brings both peace and conflict; expect both. The wise prepare for both faces of love.",
     "pt": "O amor traz tanto paz quanto conflito; espere ambos. O s\u00e1bio se prepara para ambas as faces do amor.",
     "es": "El amor trae tanto paz como conflicto; espera ambos. El sabio se prepara para ambas caras del amor."},  # 17
    {"en": "Money pursued without principles corrupts the pursuer. Earn rightly or risk losing yourself.",
     "pt": "Dinheiro perseguido sem princ\u00edpios corrompe o perseguidor. Ganhe corretamente ou arrisque perder-se.",
     "es": "El dinero perseguido sin principios corrompe al perseguidor. Gana correctamente o arriesgas perderte."},  # 18
    BEGINNING,  # 19
    {"en": "Words have the power to heal what wounds the soul. Speak gently when someone is suffering.",
     "pt": "As palavras t\u00eam o poder de curar o que fere a alma. Fale gentilmente quando algu\u00e9m est\u00e1 sofrendo.",
     "es": "Las palabras tienen el poder de sanar lo que hiere al alma. Habla suavemente cuando alguien sufre."},  # 20
    {"en": "Even those we conquer can shape us in return. Be alert to who or what is influencing you.",
     "pt": "At\u00e9 aqueles que conquistamos podem nos moldar em troca. Esteja alerta para quem ou o que est\u00e1 influenciando voc\u00ea.",
     "es": "Incluso aquellos a quienes conquistamos pueden moldearnos a cambio. Mant\u00e9nte alerta de qui\u00e9n o qu\u00e9 te est\u00e1 influenciando."},  # 21
    ANGER,  # 22
    DEATH,  # 23
    BEGINNING,  # 24
    {"en": "The less you depend on tomorrow, the freer today becomes. Practice not relying on what may never come.",
     "pt": "Quanto menos voc\u00ea depende do amanh\u00e3, mais livre o hoje se torna. Pratique n\u00e3o depender do que pode nunca chegar.",
     "es": "Cuanto menos dependes del ma\u00f1ana, m\u00e1s libre se vuelve el hoy. Practica no depender de lo que quiz\u00e1s nunca llegue."},  # 25
    {"en": "When the world overwhelms you, retreat into your own depths. There you will find your center again.",
     "pt": "Quando o mundo o sobrecarrega, recolha-se em suas pr\u00f3prias profundezas. L\u00e1 voc\u00ea encontrar\u00e1 seu centro novamente.",
     "es": "Cuando el mundo te abruma, retr\u00e1ete a tus propias profundidades. All\u00ed encontrar\u00e1s tu centro de nuevo."},  # 26
    BEGINNING,  # 27
    GREED,  # 28
    {"en": "Faults are easier to copy than virtues. Choose carefully whom you spend your time with.",
     "pt": "Defeitos s\u00e3o mais f\u00e1ceis de copiar do que virtudes. Escolha cuidadosamente com quem voc\u00ea passa seu tempo.",
     "es": "Los defectos son m\u00e1s f\u00e1ciles de copiar que las virtudes. Elige cuidadosamente con quien pasas tu tiempo."},  # 29
    {"en": "Most prayers ask for things that would harm us if granted. Better to align desire with what is good.",
     "pt": "A maioria das ora\u00e7\u00f5es pede coisas que nos machucariam se concedidas. Melhor alinhar o desejo com o que \u00e9 bom.",
     "es": "La mayor\u00eda de las oraciones piden cosas que nos da\u00f1ar\u00edan si fueran concedidas. Mejor alinear el deseo con lo que es bueno."},  # 30
    GREED,  # 31
    DEATH,  # 32
    PRESENT,  # 33
    BEGINNING,  # 34
    {"en": "Acceptance lightens what cannot be changed. Stop fighting reality and find your power within it.",
     "pt": "A aceita\u00e7\u00e3o alivia o que n\u00e3o pode ser mudado. Pare de lutar contra a realidade e encontre seu poder dentro dela.",
     "es": "La aceptaci\u00f3n aligera lo que no se puede cambiar. Deja de luchar contra la realidad y encuentra tu poder dentro de ella."},  # 35
    {"en": "Resistance to what is brings only more suffering. Practice the quiet strength of acceptance.",
     "pt": "A resist\u00eancia ao que \u00e9 traz apenas mais sofrimento. Pratique a for\u00e7a silenciosa da aceita\u00e7\u00e3o.",
     "es": "La resistencia a lo que es solo trae m\u00e1s sufrimiento. Practica la fuerza silenciosa de la aceptaci\u00f3n."},  # 36
    ADVERSITY,  # 37
    ADVERSITY,  # 38
    {"en": "Advice is most powerful when it is brief. Speak less, mean more.",
     "pt": "Conselho \u00e9 mais poderoso quando \u00e9 breve. Fale menos, signifique mais.",
     "es": "El consejo es m\u00e1s poderoso cuando es breve. Habla menos, significa m\u00e1s."},  # 39
    ANGER,  # 40
    {"en": "Art speaks where words fail. Let images and music feed your soul too.",
     "pt": "A arte fala onde as palavras falham. Deixe que imagens e m\u00fasica alimentem sua alma tamb\u00e9m.",
     "es": "El arte habla donde las palabras fallan. Deja que las im\u00e1genes y la m\u00fasica alimenten tu alma tambi\u00e9n."},  # 41
    BEGINNING,  # 42
    {"en": "Boldness is the answer to crisis. Practice courage in small moments so it is ready for big ones.",
     "pt": "A ousadia \u00e9 a resposta \u00e0 crise. Pratique coragem em pequenos momentos para que ela esteja pronta para os grandes.",
     "es": "La audacia es la respuesta a la crisis. Practica el coraje en peque\u00f1os momentos para que est\u00e9 listo para los grandes."},  # 43
    {"en": "Hidden wounds fester. Let trusted others see your pain so it can begin to heal.",
     "pt": "Feridas escondidas apodrecem. Deixe que pessoas confi\u00e1veis vejam sua dor para que ela possa come\u00e7ar a curar.",
     "es": "Las heridas ocultas se enconan. Deja que otros de confianza vean tu dolor para que pueda empezar a sanar."},  # 44
    ADVERSITY,  # 45
    BEGINNING,  # 46
    {"en": "When the world overwhelms you, retreat into your own depths. There you will find your center again.",
     "pt": "Quando o mundo o sobrecarrega, recolha-se em suas pr\u00f3prias profundezas. L\u00e1 voc\u00ea encontrar\u00e1 seu centro novamente.",
     "es": "Cuando el mundo te abruma, retr\u00e1ete a tus propias profundidades. All\u00ed encontrar\u00e1s tu centro de nuevo."},  # 47
    {"en": "Living well and dying well are one art. Practice today the calm you hope to have at the end.",
     "pt": "Viver bem e morrer bem s\u00e3o uma s\u00f3 arte. Pratique hoje a calma que espera ter no fim.",
     "es": "Vivir bien y morir bien son un solo arte. Practica hoy la calma que esperas tener al final."},  # 48
    BEGINNING,  # 49
    {"en": "Bad times do not last forever. Hold steady; conditions always change.",
     "pt": "Os tempos ruins n\u00e3o duram para sempre. Mantenha-se firme; as condi\u00e7\u00f5es sempre mudam.",
     "es": "Los malos tiempos no duran para siempre. Mant\u00e9nte firme; las condiciones siempre cambian."},  # 50
    ADVERSITY,  # 51
    FRIENDSHIP,  # 52
    {"en": "Your neighbor's misfortune may quickly become your own. Care for others as a form of self-care.",
     "pt": "O infort\u00fanio do seu vizinho pode rapidamente se tornar o seu. Cuide dos outros como uma forma de cuidar de si.",
     "es": "El infortunio de tu vecino puede r\u00e1pidamente convertirse en el tuyo. Cuida a otros como una forma de cuidarte a ti mismo."},  # 53
    ANGER,  # 54
    {"en": "Hunger seasons every meal; rarity gives value. Notice what abundance has dulled in you.",
     "pt": "A fome tempera cada refei\u00e7\u00e3o; a raridade d\u00e1 valor. Note o que a abund\u00e2ncia embotou em voc\u00ea.",
     "es": "El hambre sazona cada comida; la rareza da valor. Nota lo que la abundancia ha embotado en ti."},  # 55
    {"en": "Pleasure at its peak is simply the absence of pain. Aim for tranquility, not excess.",
     "pt": "O prazer no auge \u00e9 simplesmente a aus\u00eancia da dor. Mire na tranquilidade, n\u00e3o no excesso.",
     "es": "El placer en su m\u00e1ximo es simplemente la ausencia del dolor. Apunta a la tranquilidad, no al exceso."},  # 56
    CONTENTMENT,  # 57
    CONTENTMENT,  # 58
    GREED,  # 59
    CONTENTMENT,  # 60
    CONTENTMENT,  # 61
    FRIENDSHIP,  # 62
    FRIENDSHIP,  # 63
    BEGINNING,  # 64
    GREED,  # 65
    CONTENTMENT,  # 66
    {"en": "Hope is what carries us through dark times. Hold onto it even when reasons seem absent.",
     "pt": "A esperan\u00e7a \u00e9 o que nos carrega em tempos sombrios. Segure-a mesmo quando as raz\u00f5es parecem ausentes.",
     "es": "La esperanza es lo que nos lleva a trav\u00e9s de tiempos oscuros. Af\u00e9rrate a ella incluso cuando las razones parezcan ausentes."},  # 67
    {"en": "Universal madness suggests universal humility. Be gentle with yourself and with others who err.",
     "pt": "Loucura universal sugere humildade universal. Seja gentil consigo mesmo e com os outros que erram.",
     "es": "La locura universal sugiere humildad universal. S\u00e9 gentil contigo mismo y con otros que se equivocan."},  # 68
    {"en": "Justice undone by those who judge poisons society. Demand integrity from those given authority.",
     "pt": "A justi\u00e7a desfeita por aqueles que julgam envenena a sociedade. Exija integridade daqueles a quem foi dada autoridade.",
     "es": "La justicia deshecha por quienes juzgan envenena a la sociedad. Exige integridad a quienes se les ha dado autoridad."},  # 69
    {"en": "Humility before knowledge keeps you teachable. Your ignorance is greater than your understanding.",
     "pt": "Humildade diante do conhecimento o mant\u00e9m ensin\u00e1vel. Sua ignor\u00e2ncia \u00e9 maior que seu entendimento.",
     "es": "La humildad ante el conocimiento te mantiene ense\u00f1able. Tu ignorancia es mayor que tu entendimiento."},  # 70
    {"en": "Variety brings depth to character and life. Cultivate range, not repetition.",
     "pt": "A variedade traz profundidade ao car\u00e1ter e \u00e0 vida. Cultive amplitude, n\u00e3o repeti\u00e7\u00e3o.",
     "es": "La variedad trae profundidad al car\u00e1cter y a la vida. Cultiva amplitud, no repetici\u00f3n."},  # 71
    {"en": "Your neighbor's misfortune may quickly become your own. Care for others as a form of self-care.",
     "pt": "O infort\u00fanio do seu vizinho pode rapidamente se tornar o seu. Cuide dos outros como uma forma de cuidar de si.",
     "es": "El infortunio de tu vecino puede r\u00e1pidamente convertirse en el tuyo. Cuida a otros como una forma de cuidarte a ti mismo."},  # 72
    {"en": "Persistence wears down even stone. Whatever you want to change, do it daily.",
     "pt": "A persist\u00eancia desgasta at\u00e9 a pedra. Seja o que for que voc\u00ea queira mudar, fa\u00e7a-o diariamente.",
     "es": "La persistencia desgasta incluso la piedra. Sea lo que sea que quieras cambiar, hazlo diariamente."},  # 73
    {"en": "Brevity of life is the greatest motivator. Stop wasting hours on what does not matter.",
     "pt": "A brevidade da vida \u00e9 o maior motivador. Pare de desperdi\u00e7ar horas com o que n\u00e3o importa.",
     "es": "La brevedad de la vida es el mayor motivador. Deja de desperdiciar horas en lo que no importa."},  # 74
    PRESENT,  # 75
    CONTENTMENT,  # 76
    {"en": "We always crave what we are not. Notice the grass-is-greener trap and step out of it.",
     "pt": "Sempre ansiamos pelo que n\u00e3o somos. Note a armadilha da grama mais verde do outro lado e saia dela.",
     "es": "Siempre anhelamos lo que no somos. Nota la trampa del c\u00e9sped m\u00e1s verde y sal de ella."},  # 77
    DEATH,  # 78
    {"en": "Anything that frees you from fear is genuinely good. Pursue what gives you peace.",
     "pt": "Qualquer coisa que o libera do medo \u00e9 genuinamente boa. Busque o que lhe d\u00e1 paz.",
     "es": "Cualquier cosa que te libere del miedo es genuinamente buena. Busca lo que te da paz."},  # 79
    {"en": "Art speaks where words fail. Let images and music feed your soul too.",
     "pt": "A arte fala onde as palavras falham. Deixe que imagens e m\u00fasica alimentem sua alma tamb\u00e9m.",
     "es": "El arte habla donde las palabras fallan. Deja que las im\u00e1genes y la m\u00fasica alimenten tu alma tambi\u00e9n."},  # 80
    {"en": "Some passion is required for any creative life. Embrace your obsessions; they are clues to your purpose.",
     "pt": "Alguma paix\u00e3o \u00e9 necess\u00e1ria para qualquer vida criativa. Abrace suas obsess\u00f5es; s\u00e3o pistas do seu prop\u00f3sito.",
     "es": "Alguna pasi\u00f3n es necesaria para cualquier vida creativa. Abraza tus obsesiones; son pistas de tu prop\u00f3sito."},  # 81
    {"en": "Let your work mature before showing it to the world. Patience refines what haste ruins.",
     "pt": "Deixe seu trabalho amadurecer antes de mostr\u00e1-lo ao mundo. A paci\u00eancia refina o que a pressa arru\u00edna.",
     "es": "Deja que tu trabajo madure antes de mostrarlo al mundo. La paciencia refina lo que la prisa arruina."},  # 82
    {"en": "Self-reliance is the highest dignity. Stop praying for what your own effort can bring.",
     "pt": "A autoconfian\u00e7a \u00e9 a maior dignidade. Pare de orar pelo que seu pr\u00f3prio esfor\u00e7o pode trazer.",
     "es": "La autoconfianza es la mayor dignidad. Deja de orar por lo que tu propio esfuerzo puede traer."},  # 83
    {"en": "Difficulty is the seed of glory. The harder the path, the more meaningful the arrival.",
     "pt": "A dificuldade \u00e9 a semente da gl\u00f3ria. Quanto mais dif\u00edcil o caminho, mais significativa a chegada.",
     "es": "La dificultad es la semilla de la gloria. Cuanto m\u00e1s dif\u00edcil el camino, m\u00e1s significativa la llegada."},  # 84
    {"en": "We are all imperfect. The best person is simply the one with fewest flaws and most awareness of them.",
     "pt": "Todos somos imperfeitos. A melhor pessoa \u00e9 simplesmente aquela com menos defeitos e mais consci\u00eancia deles.",
     "es": "Todos somos imperfectos. La mejor persona es simplemente aquella con menos defectos y m\u00e1s conciencia de ellos."},  # 85
    {"en": "Know your limits and act before you are forced. Graceful exits matter more than long stays.",
     "pt": "Conhe\u00e7a seus limites e aja antes de ser for\u00e7ado. Sa\u00eddas graciosas importam mais que longas perman\u00eancias.",
     "es": "Conoce tus l\u00edmites y act\u00faa antes de ser forzado. Las salidas elegantes importan m\u00e1s que las largas estad\u00edas."},  # 86
    {"en": "Choose tasks that match your real capacity. Trying to carry too much wastes both energy and time.",
     "pt": "Escolha tarefas que combinem com sua capacidade real. Tentar carregar demais desperdi\u00e7a energia e tempo.",
     "es": "Elige tareas que coincidan con tu capacidad real. Intentar cargar demasiado desperdicia energ\u00eda y tiempo."},  # 87
    {"en": "Difficulty is the seed of glory. The harder the path, the more meaningful the arrival.",
     "pt": "A dificuldade \u00e9 a semente da gl\u00f3ria. Quanto mais dif\u00edcil o caminho, mais significativa a chegada.",
     "es": "La dificultad es la semilla de la gloria. Cuanto m\u00e1s dif\u00edcil el camino, m\u00e1s significativa la llegada."},  # 88
    {"en": "We are all imperfect. The best person is simply the one with fewest flaws and most awareness of them.",
     "pt": "Todos somos imperfeitos. A melhor pessoa \u00e9 simplesmente aquela com menos defeitos e mais consci\u00eancia deles.",
     "es": "Todos somos imperfectos. La mejor persona es simplemente aquella con menos defectos y m\u00e1s conciencia de ellos."},  # 89
    {"en": "Self-reliance is the highest dignity. Stop praying for what your own effort can bring.",
     "pt": "A autoconfian\u00e7a \u00e9 a maior dignidade. Pare de orar pelo que seu pr\u00f3prio esfor\u00e7o pode trazer.",
     "es": "La autoconfianza es la mayor dignidad. Deja de orar por lo que tu propio esfuerzo puede traer."},  # 90
    {"en": "Conflict and competition often bring out the worst, not the best. Compete with yesterday's self instead.",
     "pt": "O conflito e a competi\u00e7\u00e3o frequentemente trazem o pior, n\u00e3o o melhor. Compita com o seu eu de ontem em vez disso.",
     "es": "El conflicto y la competencia a menudo sacan lo peor, no lo mejor. Compite con tu yo de ayer en su lugar."},  # 91
    PRESENT,  # 92
    PRESENT,  # 93
    PRESENT,  # 94
    PRESENT,  # 95
    PRESENT,  # 96
    PRESENT,  # 97
    {"en": "Each year reminds us that we are temporary. Use the year well; it will not return.",
     "pt": "Cada ano nos lembra que somos tempor\u00e1rios. Use bem o ano; ele n\u00e3o voltar\u00e1.",
     "es": "Cada a\u00f1o nos recuerda que somos temporales. Usa bien el a\u00f1o; no regresar\u00e1."},  # 98
    PRESENT,  # 99
    {"en": "Riches are tools, not masters. Decide whether you own them or they own you.",
     "pt": "Riquezas s\u00e3o ferramentas, n\u00e3o mestres. Decida se voc\u00ea as possui ou se elas o possuem.",
     "es": "Las riquezas son herramientas, no amos. Decide si las posees o ellas te poseen."},  # 100
    BEGINNING,  # 101
    {"en": "Wealth changes problems but does not eliminate them. Be honest about what you are really chasing.",
     "pt": "A riqueza muda os problemas, mas n\u00e3o os elimina. Seja honesto sobre o que voc\u00ea est\u00e1 realmente perseguindo.",
     "es": "La riqueza cambia los problemas, pero no los elimina. S\u00e9 honesto sobre lo que realmente persigues."},  # 102
    {"en": "Difficulty is the seed of glory. The harder the path, the more meaningful the arrival.",
     "pt": "A dificuldade \u00e9 a semente da gl\u00f3ria. Quanto mais dif\u00edcil o caminho, mais significativa a chegada.",
     "es": "La dificultad es la semilla de la gloria. Cuanto m\u00e1s dif\u00edcil el camino, m\u00e1s significativa la llegada."},  # 103
    ADVERSITY,  # 104
    CONTENTMENT,  # 105
    {"en": "Writing clarifies thinking; speech only conveys it. Use the pen to discover your own mind.",
     "pt": "A escrita clarifica o pensamento; a fala apenas o transmite. Use a caneta para descobrir sua pr\u00f3pria mente.",
     "es": "La escritura clarifica el pensamiento; el habla solo lo transmite. Usa la pluma para descubrir tu propia mente."},  # 106
    {"en": "Envy drains the envious, not the envied. Choose to celebrate others' wins instead.",
     "pt": "A inveja drena o invejoso, n\u00e3o o invejado. Escolha celebrar as vit\u00f3rias dos outros em vez disso.",
     "es": "La envidia drena al envidioso, no al envidiado. Elige celebrar las victorias ajenas en su lugar."},  # 107
    {"en": "Nothing of value comes without effort. Honor the work as much as the result.",
     "pt": "Nada de valor vem sem esfor\u00e7o. Honre o trabalho tanto quanto o resultado.",
     "es": "Nada de valor viene sin esfuerzo. Honra el trabajo tanto como el resultado."},  # 108
    {"en": "Hidden wounds fester. Let trusted others see your pain so it can begin to heal.",
     "pt": "Feridas escondidas apodrecem. Deixe que pessoas confi\u00e1veis vejam sua dor para que ela possa come\u00e7ar a curar.",
     "es": "Las heridas ocultas se enconan. Deja que otros de confianza vean tu dolor para que pueda empezar a sanar."},  # 109
    DEATH,  # 110
    DEATH,  # 111
    PHILOSOPHY,  # 112
    {"en": "Practice the things that bring happiness, not the things that promise it. Test through living.",
     "pt": "Pratique as coisas que trazem felicidade, n\u00e3o as que a prometem. Teste atrav\u00e9s do viver.",
     "es": "Practica las cosas que traen felicidad, no las que la prometen. Pru\u00e9balo a trav\u00e9s del vivir."},  # 113
    CONTENTMENT,  # 114
    {"en": "What heals one harms another; there are no universal answers. Test each thing for yourself.",
     "pt": "O que cura um fere o outro; n\u00e3o h\u00e1 respostas universais. Teste cada coisa por si mesmo.",
     "es": "Lo que cura a uno da\u00f1a a otro; no hay respuestas universales. Prueba cada cosa por ti mismo."},  # 115
    {"en": "Beware ideologies that justify harm. Question any belief that demands suffering from others.",
     "pt": "Cuidado com ideologias que justificam o dano. Questione qualquer cren\u00e7a que exija sofrimento dos outros.",
     "es": "Cuidado con las ideolog\u00edas que justifican el da\u00f1o. Cuestiona cualquier creencia que exija sufrimiento de otros."},  # 116
    {"en": "Beware ideologies that justify harm. Question any belief that demands suffering from others.",
     "pt": "Cuidado com ideologias que justificam o dano. Questione qualquer cren\u00e7a que exija sofrimento dos outros.",
     "es": "Cuidado con las ideolog\u00edas que justifican el da\u00f1o. Cuestiona cualquier creencia que exija sufrimiento de otros."},  # 117
    ADVERSITY,  # 118
    {"en": "Self-reliance is the highest dignity. Stop praying for what your own effort can bring.",
     "pt": "A autoconfian\u00e7a \u00e9 a maior dignidade. Pare de orar pelo que seu pr\u00f3prio esfor\u00e7o pode trazer.",
     "es": "La autoconfianza es la mayor dignidad. Deja de orar por lo que tu propio esfuerzo puede traer."},  # 119
    {"en": "Most prayers ask for things that would harm us if granted. Better to align desire with what is good.",
     "pt": "A maioria das ora\u00e7\u00f5es pede coisas que nos machucariam se concedidas. Melhor alinhar o desejo com o que \u00e9 bom.",
     "es": "La mayor\u00eda de las oraciones piden cosas que nos da\u00f1ar\u00edan si fueran concedidas. Mejor alinear el deseo con lo que es bueno."},  # 120
    {"en": "Knowledge without character can be dangerous. Pair what you know with how you live.",
     "pt": "Conhecimento sem car\u00e1ter pode ser perigoso. Combine o que voc\u00ea sabe com como voc\u00ea vive.",
     "es": "El conocimiento sin car\u00e1cter puede ser peligroso. Combina lo que sabes con c\u00f3mo vives."},  # 121
    ADVERSITY,  # 122
    {"en": "Inner peace beats external luxury. Choose simplicity that brings calm over wealth that brings worry.",
     "pt": "A paz interior supera o luxo externo. Escolha a simplicidade que traz calma em vez da riqueza que traz preocupa\u00e7\u00e3o.",
     "es": "La paz interior vence al lujo externo. Elige la simplicidad que trae calma sobre la riqueza que trae preocupaci\u00f3n."},  # 123
    {"en": "Boldness is the answer to crisis. Practice courage in small moments so it is ready for big ones.",
     "pt": "A ousadia \u00e9 a resposta \u00e0 crise. Pratique coragem em pequenos momentos para que ela esteja pronta para os grandes.",
     "es": "La audacia es la respuesta a la crisis. Practica el coraje en peque\u00f1os momentos para que est\u00e9 listo para los grandes."},  # 124
    CONTENTMENT,  # 125
    PRESENT,  # 126
    {"en": "Art speaks where words fail. Let images and music feed your soul too.",
     "pt": "A arte fala onde as palavras falham. Deixe que imagens e m\u00fasica alimentem sua alma tamb\u00e9m.",
     "es": "El arte habla donde las palabras fallan. Deja que las im\u00e1genes y la m\u00fasica alimenten tu alma tambi\u00e9n."},  # 127
    {"en": "Living well and dying well are one art. Practice today the calm you hope to have at the end.",
     "pt": "Viver bem e morrer bem s\u00e3o uma s\u00f3 arte. Pratique hoje a calma que espera ter no fim.",
     "es": "Vivir bien y morir bien son un solo arte. Practica hoy la calma que esperas tener al final."},  # 128
    FRIENDSHIP,  # 129
    FRIENDSHIP,  # 130
    {"en": "Different temperaments clash naturally. Understand this to reduce friction with others.",
     "pt": "Temperamentos diferentes naturalmente se chocam. Entenda isso para reduzir a fric\u00e7\u00e3o com os outros.",
     "es": "Los temperamentos diferentes chocan naturalmente. Entiende esto para reducir la fricci\u00f3n con otros."},  # 131
    {"en": "Sometimes thinking too much is the obstacle. Just begin and trust the action to teach you.",
     "pt": "\u00c0s vezes pensar demais \u00e9 o obst\u00e1culo. Apenas comece e confie que a a\u00e7\u00e3o lhe ensinar\u00e1.",
     "es": "A veces pensar demasiado es el obst\u00e1culo. Solo comienza y conf\u00eda en que la acci\u00f3n te ense\u00f1ar\u00e1."},  # 132
    {"en": "Persistence wears down even stone. Whatever you want to change, do it daily.",
     "pt": "A persist\u00eancia desgasta at\u00e9 a pedra. Seja o que for que voc\u00ea queira mudar, fa\u00e7a-o diariamente.",
     "es": "La persistencia desgasta incluso la piedra. Sea lo que sea que quieras cambiar, hazlo diariamente."},  # 133
    WISDOM,  # 134
    {"en": "Life lived in expectation misses the now. Set hopes loosely and inhabit the present fully.",
     "pt": "A vida vivida em expectativa perde o agora. Estabele\u00e7a esperan\u00e7as levemente e habite o presente plenamente.",
     "es": "La vida vivida en expectativa pierde el ahora. Establece esperanzas livianamente y habita el presente plenamente."},  # 135
    {"en": "Steady mind is the only constant in changing circumstances. Cultivate equanimity.",
     "pt": "Mente firme \u00e9 a \u00fanica constante em circunst\u00e2ncias mut\u00e1veis. Cultive equanimidade.",
     "es": "Mente firme es la \u00fanica constante en circunstancias cambiantes. Cultiva ecuanimidad."},  # 136
    {"en": "Authentic art comes from real experience. Live fully so you have something to say.",
     "pt": "A arte aut\u00eantica vem da experi\u00eancia real. Viva plenamente para ter algo a dizer.",
     "es": "El arte aut\u00e9ntico viene de la experiencia real. Vive plenamente para tener algo que decir."},  # 137
    {"en": "Justice is something we agree to, not something we discover. Build it carefully through dialogue.",
     "pt": "A justi\u00e7a \u00e9 algo que acordamos, n\u00e3o algo que descobrimos. Construa-a cuidadosamente atrav\u00e9s do di\u00e1logo.",
     "es": "La justicia es algo que acordamos, no algo que descubrimos. Constr\u00fayela cuidadosamente a trav\u00e9s del di\u00e1logo."},  # 138
    ANGER,  # 139
    ANGER,  # 140
    {"en": "Some sell their words and rage as commodities. Be careful which voices you let into your head.",
     "pt": "Alguns vendem suas palavras e raiva como mercadorias. Tenha cuidado com quais vozes voc\u00ea deixa entrar na sua cabe\u00e7a.",
     "es": "Algunos venden sus palabras e ira como mercanc\u00edas. Ten cuidado con qu\u00e9 voces dejas entrar en tu cabeza."},  # 141
    {"en": "Inheritance includes both gifts and burdens. Acknowledge the patterns you carry from those before you.",
     "pt": "A heran\u00e7a inclui tanto presentes quanto fardos. Reconhe\u00e7a os padr\u00f5es que voc\u00ea carrega daqueles antes de voc\u00ea.",
     "es": "La herencia incluye tanto regalos como cargas. Reconoce los patrones que llevas de quienes vinieron antes de ti."},  # 142
    PRESENT,  # 143
]

result = {}
for i, key in enumerate(keys):
    if i < len(reflections):
        result[key] = reflections[i]

with open('c:/Users/lalli/Flutter/coach_phrase_app/reflections_epicureanism.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f'Generated {len(result)} epicureanism reflections')
