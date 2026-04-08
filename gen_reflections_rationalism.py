"""Generate reflections for 72 rationalism quotes."""
import json

with open('c:/Users/lalli/Flutter/coach_phrase_app/rationalism_keys.json', 'r', encoding='utf-8') as f:
    keys = json.load(f)

reflections = [
    # 1
    {"en": "How you present yourself shapes how others treat you. Stand tall in self-respect and others will mirror it back.",
     "pt": "Como voc\u00ea se apresenta molda como os outros o tratam. Permane\u00e7a firme em autorrespeito e os outros o refletir\u00e3o de volta.",
     "es": "C\u00f3mo te presentas moldea c\u00f3mo los dem\u00e1s te tratan. Mantente firme en autorrespeto y los dem\u00e1s lo reflejar\u00e1n."},
    # 2
    {"en": "Most people overestimate their own judgment. Practice doubting your certainties to gain real wisdom.",
     "pt": "A maioria das pessoas superestima seu pr\u00f3prio julgamento. Pratique duvidar de suas certezas para ganhar verdadeira sabedoria.",
     "es": "La mayor\u00eda de las personas sobreestima su propio juicio. Practica dudar de tus certezas para ganar verdadera sabidur\u00eda."},
    # 3
    {"en": "Understanding liberates because it removes the chains of confusion. Pursue insight, not just information.",
     "pt": "A compreens\u00e3o liberta porque remove as correntes da confus\u00e3o. Busque o entendimento, n\u00e3o apenas a informa\u00e7\u00e3o.",
     "es": "La comprensi\u00f3n libera porque elimina las cadenas de la confusi\u00f3n. Busca el entendimiento, no solo la informaci\u00f3n."},
    # 4
    {"en": "True philosophy disturbs comfortable lies. If your thinking never unsettles anyone, ask if it is thinking at all.",
     "pt": "A verdadeira filosofia perturba mentiras confort\u00e1veis. Se seu pensamento nunca incomoda ningu\u00e9m, pergunte se \u00e9 pensamento.",
     "es": "La verdadera filosof\u00eda perturba mentiras c\u00f3modas. Si tu pensamiento nunca incomoda a nadie, preg\u00fantate si es pensamiento."},
    # 5
    {"en": "Almost everything is outside your control, but your thoughts remain yours. Cultivate that inner garden carefully.",
     "pt": "Quase tudo est\u00e1 fora do seu controle, mas seus pensamentos continuam seus. Cultive esse jardim interior com cuidado.",
     "es": "Casi todo est\u00e1 fuera de tu control, pero tus pensamientos siguen siendo tuyos. Cultiva ese jard\u00edn interior con cuidado."},
    # 6
    {"en": "Understanding people is harder than judging them, but it transforms both you and them.",
     "pt": "Compreender as pessoas \u00e9 mais dif\u00edcil do que julg\u00e1-las, mas transforma tanto voc\u00ea quanto elas.",
     "es": "Comprender a las personas es m\u00e1s dif\u00edcil que juzgarlas, pero transforma tanto a ti como a ellas."},
    # 7
    {"en": "Before acting, ask: would I want everyone to act this way? Let your principles be universal, not personal.",
     "pt": "Antes de agir, pergunte: eu gostaria que todos agissem assim? Que seus princ\u00edpios sejam universais, n\u00e3o pessoais.",
     "es": "Antes de actuar, preg\u00fantate: \u00bfquerr\u00eda que todos actuaran as\u00ed? Que tus principios sean universales, no personales."},
    # 8
    {"en": "Freedom is not doing whatever you want; it is choosing through reason rather than impulse.",
     "pt": "Liberdade n\u00e3o \u00e9 fazer o que quiser; \u00e9 escolher pela raz\u00e3o em vez do impulso.",
     "es": "La libertad no es hacer lo que quieras; es elegir por la raz\u00f3n en lugar del impulso."},
    # 9
    {"en": "Many things we call good or bad are simply meaningless coincidences. Stop seeing omens where there are none.",
     "pt": "Muitas coisas que chamamos de boas ou m\u00e1s s\u00e3o apenas coincid\u00eancias sem sentido. Pare de ver pres\u00e1gios onde n\u00e3o h\u00e1.",
     "es": "Muchas cosas que llamamos buenas o malas son solo coincidencias sin sentido. Deja de ver presagios donde no los hay."},
    # 10
    {"en": "Real seekers question everything they believe. What if your most cherished assumption is wrong?",
     "pt": "Verdadeiros buscadores questionam tudo o que acreditam. E se sua suposi\u00e7\u00e3o mais querida estiver errada?",
     "es": "Los verdaderos buscadores cuestionan todo lo que creen. \u00bfY si tu suposici\u00f3n m\u00e1s querida est\u00e1 equivocada?"},
    # 11
    {"en": "Persistence outweighs talent. Keep moving even when you feel like a beginner forever.",
     "pt": "A persist\u00eancia supera o talento. Continue avan\u00e7ando mesmo quando se sentir um iniciante para sempre.",
     "es": "La persistencia supera al talento. Sigue avanzando incluso cuando te sientas un principiante para siempre."},
    # 12
    {"en": "Truth is older than any opinion or fashion. Anchor yourself in what endures, not what trends.",
     "pt": "A verdade \u00e9 mais antiga que qualquer opini\u00e3o ou moda. Ancore-se no que perdura, n\u00e3o no que est\u00e1 na moda.",
     "es": "La verdad es m\u00e1s antigua que cualquier opini\u00f3n o moda. \u00c1ncrate en lo que perdura, no en lo que est\u00e1 de moda."},
    # 13
    {"en": "An unexamined life is sleep with eyes open. Question yourself today and you will wake up tomorrow.",
     "pt": "Uma vida n\u00e3o examinada \u00e9 sono de olhos abertos. Questione-se hoje e voc\u00ea acordar\u00e1 amanh\u00e3.",
     "es": "Una vida no examinada es sue\u00f1o con los ojos abiertos. Cuesti\u00f3nate hoy y despertar\u00e1s ma\u00f1ana."},
    # 14
    {"en": "Letting go of rigid beliefs is not loss but liberation. Old certainties die so new wisdom can be born.",
     "pt": "Abandonar cren\u00e7as r\u00edgidas n\u00e3o \u00e9 perda mas liberta\u00e7\u00e3o. Velhas certezas morrem para que nova sabedoria possa nascer.",
     "es": "Soltar creencias r\u00edgidas no es p\u00e9rdida sino liberaci\u00f3n. Las viejas certezas mueren para que pueda nacer nueva sabidur\u00eda."},
    # 15
    {"en": "Death is not the worst, only the most feared. What you fear most often turns out to be smaller than you imagined.",
     "pt": "A morte n\u00e3o \u00e9 o pior, apenas o mais temido. O que voc\u00ea mais teme frequentemente se mostra menor do que imaginava.",
     "es": "La muerte no es lo peor, solo lo m\u00e1s temido. Lo que m\u00e1s temes frecuentemente resulta menor de lo que imaginabas."},
    # 16
    {"en": "Knowledge is what you collect; wisdom is how you live. Both matter, but only one transforms you.",
     "pt": "Conhecimento \u00e9 o que voc\u00ea coleta; sabedoria \u00e9 como voc\u00ea vive. Ambos importam, mas s\u00f3 um o transforma.",
     "es": "El conocimiento es lo que recoges; la sabidur\u00eda es c\u00f3mo vives. Ambos importan, pero solo uno te transforma."},
    # 17
    {"en": "When you treat others as tools, you also reduce yourself. Honor every human as an end of their own.",
     "pt": "Quando voc\u00ea trata os outros como ferramentas, voc\u00ea tamb\u00e9m se reduz. Honre cada humano como um fim em si mesmo.",
     "es": "Cuando tratas a los dem\u00e1s como herramientas, tambi\u00e9n te reduces. Honra a cada humano como un fin en s\u00ed mismo."},
    # 18
    {"en": "Reality has a hidden order, even when chaos seems to reign. Look for the patterns beneath the noise.",
     "pt": "A realidade tem uma ordem oculta, mesmo quando o caos parece reinar. Procure os padr\u00f5es debaixo do ru\u00eddo.",
     "es": "La realidad tiene un orden oculto, incluso cuando el caos parece reinar. Busca los patrones debajo del ruido."},
    # 19
    {"en": "Where you cannot measure, you may not yet truly understand. Develop precision wherever possible.",
     "pt": "Onde voc\u00ea n\u00e3o pode medir, talvez ainda n\u00e3o entenda verdadeiramente. Desenvolva precis\u00e3o sempre que poss\u00edvel.",
     "es": "Donde no puedes medir, quiz\u00e1s a\u00fan no entiendas verdaderamente. Desarrolla precisi\u00f3n siempre que sea posible."},
    # 20
    {"en": "Books are time machines into the minds of the wisest. Spend at least one hour a day in their company.",
     "pt": "Livros s\u00e3o m\u00e1quinas do tempo para as mentes dos mais s\u00e1bios. Passe pelo menos uma hora por dia em sua companhia.",
     "es": "Los libros son m\u00e1quinas del tiempo hacia las mentes de los m\u00e1s sabios. Pasa al menos una hora al d\u00eda en su compa\u00f1\u00eda."},
    # 21
    {"en": "Quality of judgment matters more than quantity of opinions. Choose your trusted voices carefully.",
     "pt": "Qualidade de julgamento importa mais que quantidade de opini\u00f5es. Escolha cuidadosamente suas vozes confi\u00e1veis.",
     "es": "La calidad del juicio importa m\u00e1s que la cantidad de opiniones. Elige cuidadosamente tus voces confiables."},
    # 22
    {"en": "Power tempts even the wisest minds. Be especially careful when you have the most to lose by being wrong.",
     "pt": "O poder tenta at\u00e9 as mentes mais s\u00e1bias. Seja especialmente cuidadoso quando voc\u00ea tem mais a perder ao estar errado.",
     "es": "El poder tienta incluso a las mentes m\u00e1s sabias. S\u00e9 especialmente cuidadoso cuando tienes m\u00e1s que perder al estar equivocado."},
    # 23
    {"en": "Humans are imperfect by design; expecting perfection invites disappointment. Build with what is, not what should be.",
     "pt": "Os humanos s\u00e3o imperfeitos por design; esperar perfei\u00e7\u00e3o convida \u00e0 decep\u00e7\u00e3o. Construa com o que \u00e9, n\u00e3o com o que deveria ser.",
     "es": "Los humanos son imperfectos por dise\u00f1o; esperar perfecci\u00f3n invita a la decepci\u00f3n. Construye con lo que es, no con lo que deber\u00eda ser."},
    # 24
    {"en": "Material needs are simpler than desires suggest. Reduce wants and you will discover abundance.",
     "pt": "As necessidades materiais s\u00e3o mais simples do que os desejos sugerem. Reduza os desejos e voc\u00ea descobrir\u00e1 a abund\u00e2ncia.",
     "es": "Las necesidades materiales son m\u00e1s simples de lo que los deseos sugieren. Reduce los deseos y descubrir\u00e1s la abundancia."},
    # 25
    {"en": "Belief is not proof, yet humans need it to live. Be aware of what you believe and why.",
     "pt": "Cren\u00e7a n\u00e3o \u00e9 prova, mas os humanos precisam dela para viver. Esteja ciente do que voc\u00ea acredita e por qu\u00ea.",
     "es": "La creencia no es prueba, pero los humanos la necesitan para vivir. S\u00e9 consciente de lo que crees y por qu\u00e9."},
    # 26
    {"en": "Imagination shapes the worlds we then inhabit. Be careful what you give yourself to dream.",
     "pt": "A imagina\u00e7\u00e3o molda os mundos que depois habitamos. Tenha cuidado com o que voc\u00ea se permite sonhar.",
     "es": "La imaginaci\u00f3n moldea los mundos que luego habitamos. Ten cuidado con lo que te permites so\u00f1ar."},
    # 27
    {"en": "True wealth is the discipline of needing little. Practice doing without and gain everything.",
     "pt": "A verdadeira riqueza \u00e9 a disciplina de precisar de pouco. Pratique dispensar e ganhe tudo.",
     "es": "La verdadera riqueza es la disciplina de necesitar poco. Practica prescindir y ganar\u00e1s todo."},
    # 28
    {"en": "Consciousness cannot be found in matter alone. Look beyond what your senses can grasp.",
     "pt": "A consci\u00eancia n\u00e3o pode ser encontrada apenas na mat\u00e9ria. Olhe al\u00e9m do que seus sentidos podem captar.",
     "es": "La conciencia no puede encontrarse solo en la materia. Mira m\u00e1s all\u00e1 de lo que tus sentidos pueden captar."},
    # 29
    {"en": "Acting from duty rather than desire is what makes a deed truly moral. Examine your motives.",
     "pt": "Agir por dever em vez de desejo \u00e9 o que torna um ato verdadeiramente moral. Examine seus motivos.",
     "es": "Actuar por deber en lugar de deseo es lo que hace un acto verdaderamente moral. Examina tus motivos."},
    # 30
    {"en": "Knowledge starts with experience, but does not end there. Reflection is what transforms data into wisdom.",
     "pt": "O conhecimento come\u00e7a com a experi\u00eancia, mas n\u00e3o termina nela. A reflex\u00e3o \u00e9 o que transforma dados em sabedoria.",
     "es": "El conocimiento empieza con la experiencia, pero no termina ah\u00ed. La reflexi\u00f3n es lo que transforma los datos en sabidur\u00eda."},
    # 31
    {"en": "Theory tested by practice, practice illuminated by theory: that is real knowing.",
     "pt": "Teoria testada pela pr\u00e1tica, pr\u00e1tica iluminada pela teoria: isso \u00e9 conhecimento real.",
     "es": "Teor\u00eda probada por la pr\u00e1ctica, pr\u00e1ctica iluminada por la teor\u00eda: eso es conocimiento real."},
    # 32
    {"en": "How you treat the helpless reveals who you really are. Watch your actions toward those who cannot retaliate.",
     "pt": "Como voc\u00ea trata os indefesos revela quem voc\u00ea realmente \u00e9. Observe suas a\u00e7\u00f5es em rela\u00e7\u00e3o a quem n\u00e3o pode retaliar.",
     "es": "C\u00f3mo tratas a los indefensos revela qui\u00e9n eres realmente. Observa tus acciones hacia quienes no pueden tomar represalias."},
    # 33
    {"en": "Mastery of self begins with mastery of emotion. Notice your reactions before they become your master.",
     "pt": "O dom\u00ednio de si come\u00e7a com o dom\u00ednio da emo\u00e7\u00e3o. Note suas rea\u00e7\u00f5es antes que se tornem seu mestre.",
     "es": "El dominio de uno mismo comienza con el dominio de la emoci\u00f3n. Nota tus reacciones antes de que se vuelvan tu amo."},
    # 34
    {"en": "Doubt is useful, but doubt that becomes paralysis is its own kind of certainty. Move forward anyway.",
     "pt": "A d\u00favida \u00e9 \u00fatil, mas d\u00favida que se torna paralisia \u00e9 seu pr\u00f3prio tipo de certeza. Avance mesmo assim.",
     "es": "La duda es \u00fatil, pero la duda que se vuelve par\u00e1lisis es su propio tipo de certeza. Avanza de todos modos."},
    # 35
    {"en": "True freedom is not absence of guidance but guidance from your own deepest reason. Listen to it.",
     "pt": "A verdadeira liberdade n\u00e3o \u00e9 a aus\u00eancia de guia, mas a guia da sua pr\u00f3pria raz\u00e3o mais profunda. Ou\u00e7a-a.",
     "es": "La verdadera libertad no es la ausencia de gu\u00eda, sino la gu\u00eda de tu propia raz\u00f3n m\u00e1s profunda. Esc\u00fachala."},
    # 36
    {"en": "Genius is independence of mind, not memorization. Trust your own conclusions, even when they seem strange.",
     "pt": "G\u00eanio \u00e9 independ\u00eancia de mente, n\u00e3o memoriza\u00e7\u00e3o. Confie nas suas pr\u00f3prias conclus\u00f5es, mesmo quando parecem estranhas.",
     "es": "El genio es independencia de mente, no memorizaci\u00f3n. Conf\u00eda en tus propias conclusiones, incluso cuando parezcan extra\u00f1as."},
    # 37
    {"en": "Enlightenment is having the courage to use your own mind. Stop waiting for others to tell you what to think.",
     "pt": "Esclarecimento \u00e9 ter coragem de usar sua pr\u00f3pria mente. Pare de esperar que os outros lhe digam o que pensar.",
     "es": "La ilustraci\u00f3n es tener el coraje de usar tu propia mente. Deja de esperar que otros te digan qu\u00e9 pensar."},
    # 38
    {"en": "Self-knowledge brings acceptance of reality as it is. The clearer you see yourself, the less you fight life.",
     "pt": "O autoconhecimento traz aceita\u00e7\u00e3o da realidade como \u00e9. Quanto mais claramente voc\u00ea se v\u00ea, menos luta contra a vida.",
     "es": "El autoconocimiento trae aceptaci\u00f3n de la realidad tal como es. Cuanto m\u00e1s claramente te ves, menos luchas contra la vida."},
    # 39
    {"en": "Reduce no person to a function or use. Each one is an entire universe deserving of respect.",
     "pt": "N\u00e3o reduza nenhuma pessoa a uma fun\u00e7\u00e3o ou utilidade. Cada uma \u00e9 um universo inteiro digno de respeito.",
     "es": "No reduzcas a ninguna persona a una funci\u00f3n o utilidad. Cada una es un universo entero digno de respeto."},
    # 40
    {"en": "True philosophy threatens lazy beliefs of every age. If yours offends no one, ask if it is alive.",
     "pt": "A verdadeira filosofia amea\u00e7a as cren\u00e7as pregui\u00e7osas de cada \u00e9poca. Se a sua n\u00e3o ofende ningu\u00e9m, pergunte se est\u00e1 viva.",
     "es": "La verdadera filosof\u00eda amenaza las creencias perezosas de cada \u00e9poca. Si la tuya no ofende a nadie, pregunta si est\u00e1 viva."},
    # 41
    {"en": "Self-preservation is necessary, but it is the foundation, not the goal. Build something more on top of it.",
     "pt": "A autopreserva\u00e7\u00e3o \u00e9 necess\u00e1ria, mas \u00e9 a funda\u00e7\u00e3o, n\u00e3o a meta. Construa algo mais por cima dela.",
     "es": "La autopreservaci\u00f3n es necesaria, pero es el fundamento, no la meta. Construye algo m\u00e1s encima de ella."},
    # 42
    {"en": "Patterns are everywhere; the trained mind sees mathematics in everything. Train yours to perceive structure.",
     "pt": "Os padr\u00f5es est\u00e3o em toda parte; a mente treinada v\u00ea matem\u00e1tica em tudo. Treine a sua para perceber estrutura.",
     "es": "Los patrones est\u00e1n en todas partes; la mente entrenada ve matem\u00e1ticas en todo. Entrena la tuya para percibir estructura."},
    # 43
    {"en": "Certainty is rare and precious. When you find it, recognize it as a gift, not a possession.",
     "pt": "A certeza \u00e9 rara e preciosa. Quando voc\u00ea a encontrar, reconhe\u00e7a-a como um presente, n\u00e3o uma posse.",
     "es": "La certeza es rara y preciosa. Cuando la encuentres, recon\u00f3cela como un regalo, no una posesi\u00f3n."},
    # 44
    {"en": "Dignity makes each person unrepeatable. Treat yourself and others as the only one of your kind.",
     "pt": "A dignidade torna cada pessoa irrepet\u00edvel. Trate a si mesmo e aos outros como o \u00fanico de seu tipo.",
     "es": "La dignidad hace que cada persona sea irrepetible. Tr\u00e1tate a ti mismo y a los dem\u00e1s como el \u00fanico de su tipo."},
    # 45
    {"en": "Tears and outrage are easy; understanding requires real effort. Choose understanding even when it costs you.",
     "pt": "L\u00e1grimas e indigna\u00e7\u00e3o s\u00e3o f\u00e1ceis; a compreens\u00e3o exige esfor\u00e7o real. Escolha a compreens\u00e3o mesmo quando ela lhe custa.",
     "es": "Las l\u00e1grimas y la indignaci\u00f3n son f\u00e1ciles; la comprensi\u00f3n requiere esfuerzo real. Elige la comprensi\u00f3n incluso cuando te cueste."},
    # 46
    {"en": "When old beliefs die, real living becomes possible. What dogma is asking you to release today?",
     "pt": "Quando velhas cren\u00e7as morrem, viver de verdade se torna poss\u00edvel. Que dogma est\u00e1 lhe pedindo para soltar hoje?",
     "es": "Cuando viejas creencias mueren, vivir de verdad se vuelve posible. \u00bfQu\u00e9 dogma te est\u00e1 pidiendo soltar hoy?"},
    # 47
    {"en": "Tears and outrage are easy; understanding requires real effort. Choose understanding even when it costs you.",
     "pt": "L\u00e1grimas e indigna\u00e7\u00e3o s\u00e3o f\u00e1ceis; a compreens\u00e3o exige esfor\u00e7o real. Escolha a compreens\u00e3o mesmo quando ela lhe custa.",
     "es": "Las l\u00e1grimas y la indignaci\u00f3n son f\u00e1ciles; la comprensi\u00f3n requiere esfuerzo real. Elige la comprensi\u00f3n incluso cuando te cueste."},
    # 48
    {"en": "Faith without action is empty. Let your devotion show in how you live, not in what you profess.",
     "pt": "F\u00e9 sem a\u00e7\u00e3o \u00e9 vazia. Que sua devo\u00e7\u00e3o se mostre em como voc\u00ea vive, n\u00e3o no que voc\u00ea professa.",
     "es": "La fe sin acci\u00f3n est\u00e1 vac\u00eda. Que tu devoci\u00f3n se muestre en c\u00f3mo vives, no en lo que profesas."},
    # 49
    {"en": "Becoming yourself is the deepest task of life. Stop comparing your journey to anyone else's.",
     "pt": "Tornar-se voc\u00ea mesmo \u00e9 a tarefa mais profunda da vida. Pare de comparar sua jornada com a de qualquer outro.",
     "es": "Convertirse en uno mismo es la tarea m\u00e1s profunda de la vida. Deja de comparar tu camino con el de cualquier otro."},
    # 50
    {"en": "Each person carries an absolute worth that no purpose can override. Honor this in your every interaction.",
     "pt": "Cada pessoa carrega um valor absoluto que nenhum prop\u00f3sito pode anular. Honre isto em cada intera\u00e7\u00e3o sua.",
     "es": "Cada persona lleva un valor absoluto que ning\u00fan prop\u00f3sito puede anular. Honra esto en cada interacci\u00f3n tuya."},
    # 51
    {"en": "Hope and fear are twins; one cannot exist without the other. Embrace both as part of being alive.",
     "pt": "Esperan\u00e7a e medo s\u00e3o g\u00eameos; um n\u00e3o existe sem o outro. Abrace ambos como parte de estar vivo.",
     "es": "Esperanza y miedo son gemelos; uno no existe sin el otro. Abraza ambos como parte de estar vivo."},
    # 52
    {"en": "Becoming what you can become is the meaning of life. Stop running from your potential.",
     "pt": "Tornar-se o que voc\u00ea pode se tornar \u00e9 o sentido da vida. Pare de fugir do seu potencial.",
     "es": "Convertirse en lo que puedes ser es el sentido de la vida. Deja de huir de tu potencial."},
    # 53
    {"en": "Nature follows law, even when chaos seems to reign. Trust the order that holds even the storms.",
     "pt": "A natureza segue a lei, mesmo quando o caos parece reinar. Confie na ordem que sustenta at\u00e9 as tempestades.",
     "es": "La naturaleza sigue la ley, incluso cuando el caos parece reinar. Conf\u00eda en el orden que sostiene incluso las tormentas."},
    # 54
    {"en": "Hope and fear are twins; one cannot exist without the other. Embrace both as part of being alive.",
     "pt": "Esperan\u00e7a e medo s\u00e3o g\u00eameos; um n\u00e3o existe sem o outro. Abrace ambos como parte de estar vivo.",
     "es": "Esperanza y miedo son gemelos; uno no existe sin el otro. Abraza ambos como parte de estar vivo."},
    # 55
    {"en": "Tears and outrage are easy; understanding requires real effort. Choose understanding even when it costs you.",
     "pt": "L\u00e1grimas e indigna\u00e7\u00e3o s\u00e3o f\u00e1ceis; a compreens\u00e3o exige esfor\u00e7o real. Escolha a compreens\u00e3o mesmo quando ela lhe custa.",
     "es": "Las l\u00e1grimas y la indignaci\u00f3n son f\u00e1ciles; la comprensi\u00f3n requiere esfuerzo real. Elige la comprensi\u00f3n incluso cuando te cueste."},
    # 56
    {"en": "Reason and love of truth lead further than guilt ever can. Let understanding replace remorse.",
     "pt": "Raz\u00e3o e amor \u00e0 verdade levam mais longe do que a culpa jamais pode. Deixe a compreens\u00e3o substituir o remorso.",
     "es": "Raz\u00f3n y amor a la verdad llevan m\u00e1s lejos de lo que la culpa nunca puede. Deja que la comprensi\u00f3n reemplace al remordimiento."},
    # 57
    {"en": "Hope and fear are twins; one cannot exist without the other. Embrace both as part of being alive.",
     "pt": "Esperan\u00e7a e medo s\u00e3o g\u00eameos; um n\u00e3o existe sem o outro. Abrace ambos como parte de estar vivo.",
     "es": "Esperanza y miedo son gemelos; uno no existe sin el otro. Abraza ambos como parte de estar vivo."},
    # 58
    {"en": "These three questions frame every life: what to know, what to do, what to hope. Sit with each.",
     "pt": "Estas tr\u00eas perguntas enquadram cada vida: o que saber, o que fazer, o que esperar. Sente-se com cada uma.",
     "es": "Estas tres preguntas enmarcan cada vida: qu\u00e9 saber, qu\u00e9 hacer, qu\u00e9 esperar. Si\u00e9ntate con cada una."},
    # 59
    {"en": "Reason itself converges on these three questions. Let your daily life be an answer to them.",
     "pt": "A pr\u00f3pria raz\u00e3o converge para essas tr\u00eas perguntas. Que sua vida di\u00e1ria seja uma resposta a elas.",
     "es": "La raz\u00f3n misma converge en estas tres preguntas. Que tu vida diaria sea una respuesta a ellas."},
    # 60
    {"en": "Fear and hope feed each other. Acknowledge both without letting either rule you.",
     "pt": "Medo e esperan\u00e7a alimentam um ao outro. Reconhe\u00e7a ambos sem deixar que nenhum o domine.",
     "es": "Miedo y esperanza se alimentan mutuamente. Reconoce ambos sin dejar que ninguno te domine."},
    # 61
    {"en": "War destroys far more than it solves. Be skeptical of any cause that requires it as proof of nobility.",
     "pt": "A guerra destr\u00f3i muito mais do que resolve. Seja c\u00e9tico em rela\u00e7\u00e3o a qualquer causa que a exija como prova de nobreza.",
     "es": "La guerra destruye mucho m\u00e1s de lo que resuelve. S\u00e9 esc\u00e9ptico ante cualquier causa que la exija como prueba de nobleza."},
    # 62
    {"en": "Peace is not silence between conflicts; it is an active virtue. Cultivate it inside yourself first.",
     "pt": "A paz n\u00e3o \u00e9 sil\u00eancio entre conflitos; \u00e9 uma virtude ativa. Cultive-a primeiro dentro de si.",
     "es": "La paz no es silencio entre conflictos; es una virtud activa. Cult\u00edvala primero dentro de ti."},
    # 63
    {"en": "True peace requires character, not just calm. Build the inner strength that makes peace possible.",
     "pt": "A verdadeira paz exige car\u00e1ter, n\u00e3o apenas calma. Construa a for\u00e7a interior que torna a paz poss\u00edvel.",
     "es": "La verdadera paz requiere car\u00e1cter, no solo calma. Construye la fuerza interior que hace posible la paz."},
    # 64
    {"en": "Being and doing are inseparable. What you do is what you become.",
     "pt": "Ser e fazer s\u00e3o insepar\u00e1veis. O que voc\u00ea faz \u00e9 o que voc\u00ea se torna.",
     "es": "Ser y hacer son inseparables. Lo que haces es en lo que te conviertes."},
    # 65
    {"en": "Beauty and order are not in nature itself but in how we look at it. Choose to see them everywhere.",
     "pt": "Beleza e ordem n\u00e3o est\u00e3o na pr\u00f3pria natureza, mas em como olhamos para ela. Escolha v\u00ea-las em toda parte.",
     "es": "Belleza y orden no est\u00e1n en la naturaleza misma, sino en c\u00f3mo la miramos. Elige verlos en todas partes."},
    # 66
    {"en": "True freedom is acting from one's own nature, not from external compulsion. What is your nature asking?",
     "pt": "A verdadeira liberdade \u00e9 agir a partir da pr\u00f3pria natureza, n\u00e3o por compuls\u00e3o externa. O que sua natureza est\u00e1 pedindo?",
     "es": "La verdadera libertad es actuar desde la propia naturaleza, no por compulsi\u00f3n externa. \u00bfQu\u00e9 te pide tu naturaleza?"},
    # 67
    {"en": "Knowledge cannot grow in chains. Defend liberty as the soil in which all wisdom must be planted.",
     "pt": "O conhecimento n\u00e3o pode crescer em correntes. Defenda a liberdade como o solo no qual toda sabedoria deve ser plantada.",
     "es": "El conocimiento no puede crecer encadenado. Defiende la libertad como el suelo en el que toda sabidur\u00eda debe plantarse."},
    # 68
    {"en": "Peace built only on absence of conflict is fragile. Strengthen your character so peace can rest on it.",
     "pt": "A paz constru\u00edda apenas na aus\u00eancia de conflito \u00e9 fr\u00e1gil. Fortale\u00e7a seu car\u00e1ter para que a paz possa repousar nele.",
     "es": "La paz construida solo en la ausencia de conflicto es fr\u00e1gil. Fortalece tu car\u00e1cter para que la paz pueda descansar en \u00e9l."},
    # 69
    {"en": "The same thing can be good for one and bad for another. Drop absolute judgments about people and things.",
     "pt": "A mesma coisa pode ser boa para um e ruim para outro. Abandone julgamentos absolutos sobre pessoas e coisas.",
     "es": "La misma cosa puede ser buena para uno y mala para otro. Abandona los juicios absolutos sobre personas y cosas."},
    # 70
    {"en": "Becoming worthy of happiness is a different art than seeking it. Tend to your worthiness, and joy will follow.",
     "pt": "Tornar-se digno da felicidade \u00e9 uma arte diferente de busc\u00e1-la. Cuide de sua dignidade, e a alegria seguir\u00e1.",
     "es": "Volverse digno de la felicidad es un arte diferente al de buscarla. Cuida tu dignidad, y la alegr\u00eda seguir\u00e1."},
    # 71
    {"en": "Happiness is not a logical conclusion but an imaginative creation. Imagine boldly what could make you happy.",
     "pt": "A felicidade n\u00e3o \u00e9 uma conclus\u00e3o l\u00f3gica, mas uma cria\u00e7\u00e3o imaginativa. Imagine ousadamente o que poderia faz\u00ea-lo feliz.",
     "es": "La felicidad no es una conclusi\u00f3n l\u00f3gica, sino una creaci\u00f3n imaginativa. Imagina audazmente qu\u00e9 podr\u00eda hacerte feliz."},
    # 72 - placeholder if needed
    {"en": "Wisdom comes not from accumulating knowledge but from understanding what to do with it.",
     "pt": "A sabedoria n\u00e3o vem de acumular conhecimento, mas de entender o que fazer com ele.",
     "es": "La sabidur\u00eda no viene de acumular conocimiento, sino de entender qu\u00e9 hacer con \u00e9l."},
]

result = {}
for i, key in enumerate(keys):
    if i < len(reflections):
        result[key] = reflections[i]

with open('c:/Users/lalli/Flutter/coach_phrase_app/reflections_rationalism.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f'Generated {len(result)} rationalism reflections')
