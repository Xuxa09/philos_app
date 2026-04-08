"""Generate reflections for 40 absurdism quotes."""
import json

with open('c:/Users/lalli/Flutter/coach_phrase_app/absurdism_keys.json', 'r', encoding='utf-8') as f:
    keys = json.load(f)

# Reflections in order matching keys[]
reflections = [
    # 1 - You're on Earth. There's no cure for that.
    {
        "en": "Existence is not a problem to be solved. Stop searching for an exit and learn to inhabit this strange home.",
        "pt": "A exist\u00eancia n\u00e3o \u00e9 um problema a ser resolvido. Pare de procurar uma sa\u00edda e aprenda a habitar este lar estranho.",
        "es": "La existencia no es un problema a resolver. Deja de buscar una salida y aprende a habitar este extra\u00f1o hogar."
    },
    # 2 - No, I regret nothing... dying is such a long tiresome business
    {
        "en": "We are dying every day, slowly and quietly. Recognize that your only true regret can be not having truly lived.",
        "pt": "Estamos morrendo todos os dias, lenta e silenciosamente. Reconhe\u00e7a que seu \u00fanico arrependimento real pode ser n\u00e3o ter verdadeiramente vivido.",
        "es": "Estamos muriendo cada d\u00eda, lenta y silenciosamente. Reconoce que tu \u00fanico arrepentimiento real puede ser no haber vivido verdaderamente."
    },
    # 3 - Try again. Fail again. Fail better.
    {
        "en": "Failure is not the opposite of progress; it is its raw material. Each failure refines you closer to mastery.",
        "pt": "O fracasso n\u00e3o \u00e9 o oposto do progresso; \u00e9 sua mat\u00e9ria-prima. Cada fracasso o refina mais perto da maestria.",
        "es": "El fracaso no es lo opuesto al progreso; es su materia prima. Cada fracaso te refina m\u00e1s cerca de la maestr\u00eda."
    },
    # 4 - Why do people always expect authors to answer questions
    {
        "en": "The most valuable minds are those that question, not those that conclude. Cultivate your questions before your answers.",
        "pt": "As mentes mais valiosas s\u00e3o aquelas que questionam, n\u00e3o as que concluem. Cultive suas perguntas antes das suas respostas.",
        "es": "Las mentes m\u00e1s valiosas son las que cuestionan, no las que concluyen. Cultiva tus preguntas antes que tus respuestas."
    },
    # 5 - I always thought old age would be a writer's best chance
    {
        "en": "What seems like decline can be its own kind of clarity. Trust the wisdom that comes when illusions fade.",
        "pt": "O que parece decl\u00ednio pode ser seu pr\u00f3prio tipo de clareza. Confie na sabedoria que vem quando as ilus\u00f5es desaparecem.",
        "es": "Lo que parece declive puede ser su propio tipo de claridad. Conf\u00eda en la sabidur\u00eda que viene cuando las ilusiones se desvanecen."
    },
    # 6 - Words are the clothes thoughts wear
    {
        "en": "Choose your words with care; they shape how others receive what you most deeply mean. Naked thoughts rarely travel well.",
        "pt": "Escolha suas palavras com cuidado; elas moldam como os outros recebem o que voc\u00ea mais profundamente quer dizer. Pensamentos nus raramente viajam bem.",
        "es": "Elige tus palabras con cuidado; moldean c\u00f3mo los dem\u00e1s reciben lo que m\u00e1s profundamente quieres decir. Los pensamientos desnudos rara vez viajan bien."
    },
    # 7 - Realism falls short of reality
    {
        "en": "What is most real about you cannot be photographed or measured. Honor your dreams as much as your facts.",
        "pt": "O que \u00e9 mais real em voc\u00ea n\u00e3o pode ser fotografado ou medido. Honre seus sonhos tanto quanto seus fatos.",
        "es": "Lo m\u00e1s real de ti no puede fotografiarse ni medirse. Honra tus sue\u00f1os tanto como tus hechos."
    },
    # 8 - If you do not love me I shall not be loved
    {
        "en": "Love only exists in mutual exchange. Stop waiting to be chosen and choose first.",
        "pt": "O amor s\u00f3 existe na troca m\u00fatua. Pare de esperar ser escolhido e escolha primeiro.",
        "es": "El amor solo existe en el intercambio mutuo. Deja de esperar ser elegido y elige primero."
    },
    # 9 - The only sin is the sin of being born
    {
        "en": "You did not choose to exist, yet here you are. Stop apologizing for your existence and start using it.",
        "pt": "Voc\u00ea n\u00e3o escolheu existir, mas aqui est\u00e1. Pare de pedir desculpas pela sua exist\u00eancia e comece a us\u00e1-la.",
        "es": "No elegiste existir, pero aqu\u00ed est\u00e1s. Deja de disculparte por tu existencia y comienza a usarla."
    },
    # 10 - One day we were born, one day we shall die
    {
        "en": "Birth and death are two ends of the same brief instant. Live as if both happened today.",
        "pt": "Nascimento e morte s\u00e3o duas extremidades do mesmo instante breve. Viva como se ambos acontecessem hoje.",
        "es": "Nacimiento y muerte son dos extremos del mismo instante breve. Vive como si ambos sucedieran hoy."
    },
    # 11 - drill one hole after another into [language]
    {
        "en": "True expression requires breaking through habit. Question every word until something deeper appears.",
        "pt": "A verdadeira express\u00e3o exige romper com o h\u00e1bito. Questione cada palavra at\u00e9 que algo mais profundo apare\u00e7a.",
        "es": "La verdadera expresi\u00f3n requiere romper el h\u00e1bito. Cuestiona cada palabra hasta que algo m\u00e1s profundo aparezca."
    },
    # 12 - Ever Tried. Ever Failed. No matter.
    {
        "en": "Failure is not a verdict, it is feedback. The next attempt is always richer because of the last.",
        "pt": "O fracasso n\u00e3o \u00e9 um veredicto, \u00e9 retorno. A pr\u00f3xima tentativa \u00e9 sempre mais rica por causa da \u00faltima.",
        "es": "El fracaso no es un veredicto, es retroalimentaci\u00f3n. El pr\u00f3ximo intento es siempre m\u00e1s rico por causa del \u00faltimo."
    },
    # 13 - It was long since I had longed for anything
    {
        "en": "Desire is dangerous because it makes you vulnerable, but its absence is a deeper death. Allow yourself to want.",
        "pt": "O desejo \u00e9 perigoso porque o torna vulner\u00e1vel, mas sua aus\u00eancia \u00e9 uma morte mais profunda. Permita-se querer.",
        "es": "El deseo es peligroso porque te hace vulnerable, pero su ausencia es una muerte m\u00e1s profunda. Perm\u00edtete desear."
    },
    # 14 - Vladimir, be reasonable, you haven't yet tried everything
    {
        "en": "When you feel like giving up, the question is not 'is it worth it?' but 'have I really tried everything?'",
        "pt": "Quando voc\u00ea sente vontade de desistir, a pergunta n\u00e3o \u00e9 'vale a pena?' mas 'eu realmente tentei tudo?'",
        "es": "Cuando sientes ganas de rendirte, la pregunta no es '\u00bfvale la pena?' sino '\u00bfrealmente he intentado todo?'"
    },
    # 15 - The light of memory
    {
        "en": "Memory is fragile and untrustworthy, yet it is what we are. Hold your past lightly while it shapes you deeply.",
        "pt": "A mem\u00f3ria \u00e9 fr\u00e1gil e n\u00e3o confi\u00e1vel, mas \u00e9 o que somos. Segure seu passado levemente enquanto ele o molda profundamente.",
        "es": "La memoria es fr\u00e1gil y poco confiable, pero es lo que somos. Sost\u00e9n tu pasado livianamente mientras te moldea profundamente."
    },
    # 16 - You can only predict things after they have happened
    {
        "en": "Stop pretending you can foresee the future. Act with what you know now and adjust as life unfolds.",
        "pt": "Pare de fingir que pode prever o futuro. Aja com o que sabe agora e ajuste \u00e0 medida que a vida se desdobra.",
        "es": "Deja de fingir que puedes prever el futuro. Act\u00faa con lo que sabes ahora y ajusta a medida que la vida se desarrolla."
    },
    # 17 - Estragon: You see, you feel worse when I'm with you
    {
        "en": "Sometimes we cling to what hurts us because solitude scares us more. Examine why you keep returning.",
        "pt": "\u00c0s vezes nos apegamos ao que nos machuca porque a solid\u00e3o nos assusta mais. Examine por que voc\u00ea continua voltando.",
        "es": "A veces nos aferramos a lo que nos lastima porque la soledad nos asusta m\u00e1s. Examina por qu\u00e9 sigues regresando."
    },
    # 18 - All I know is what the words know
    {
        "en": "Words are limited, but they are also the only bridge to other minds. Use them with reverence.",
        "pt": "As palavras s\u00e3o limitadas, mas s\u00e3o tamb\u00e9m a \u00fanica ponte para outras mentes. Use-as com rever\u00eancia.",
        "es": "Las palabras son limitadas, pero son tambi\u00e9n el \u00fanico puente hacia otras mentes. \u00dasalas con reverencia."
    },
    # 19 - Dying for dark - the darker the worse
    {
        "en": "We sometimes long for the very thing that consumes us. Question what you crave most fiercely.",
        "pt": "\u00c0s vezes ansiamos pela pr\u00f3pria coisa que nos consome. Questione o que voc\u00ea anseia mais intensamente.",
        "es": "A veces anhelamos la misma cosa que nos consume. Cuestiona lo que anhelas con m\u00e1s intensidad."
    },
    # 20 - Memories are killing
    {
        "en": "What hurts most is also what we cannot let go. Let your memories accompany you, but do not let them imprison you.",
        "pt": "O que mais d\u00f3i \u00e9 tamb\u00e9m o que n\u00e3o conseguimos soltar. Deixe suas mem\u00f3rias o acompanharem, mas n\u00e3o deixe que o aprisionem.",
        "es": "Lo que m\u00e1s duele es tambi\u00e9n lo que no podemos soltar. Deja que tus recuerdos te acompa\u00f1en, pero no dejes que te aprisionen."
    },
    # 21 - The earth makes a sound as of sighs
    {
        "en": "Some questions have no graceful answer; sometimes silence or rawness is honest. Honor the questions you cannot solve.",
        "pt": "Algumas perguntas n\u00e3o t\u00eam resposta graciosa; \u00e0s vezes o sil\u00eancio ou a crueza s\u00e3o honestos. Honre as perguntas que voc\u00ea n\u00e3o pode resolver.",
        "es": "Algunas preguntas no tienen respuesta agraciada; a veces el silencio o la crudeza son honestos. Honra las preguntas que no puedes resolver."
    },
    # 22 - A writer never takes a vacation
    {
        "en": "True vocations cannot be set aside. If something pulls you ceaselessly, it is who you are.",
        "pt": "Voca\u00e7\u00f5es verdadeiras n\u00e3o podem ser deixadas de lado. Se algo o atrai incessantemente, isso \u00e9 quem voc\u00ea \u00e9.",
        "es": "Las vocaciones verdaderas no pueden dejarse de lado. Si algo te atrae incesantemente, eso es lo que eres."
    },
    # 23 - The poet cannot invent new words
    {
        "en": "Originality is not about new material, but about a new way of seeing the familiar. Renew, do not invent.",
        "pt": "A originalidade n\u00e3o se trata de material novo, mas de um novo modo de ver o familiar. Renove, n\u00e3o invente.",
        "es": "La originalidad no se trata de material nuevo, sino de una nueva forma de ver lo familiar. Renueva, no inventes."
    },
    # 24 - Estragon: They're too big
    {
        "en": "When circumstances do not fit, we adapt or we wait. Often hope itself is the most necessary adaptation.",
        "pt": "Quando as circunst\u00e2ncias n\u00e3o se ajustam, n\u00f3s nos adaptamos ou esperamos. Muitas vezes a pr\u00f3pria esperan\u00e7a \u00e9 a adapta\u00e7\u00e3o mais necess\u00e1ria.",
        "es": "Cuando las circunstancias no encajan, nos adaptamos o esperamos. A menudo la esperanza misma es la adaptaci\u00f3n m\u00e1s necesaria."
    },
    # 25 - There are two moments worthwhile in writing
    {
        "en": "Beginning is exhilarating, completion is liberating. The middle is where real character is forged.",
        "pt": "Come\u00e7ar \u00e9 emocionante, completar \u00e9 libertador. \u00c9 no meio que o car\u00e1ter real \u00e9 forjado.",
        "es": "Comenzar es emocionante, completar es liberador. Es en el medio donde se forja el verdadero car\u00e1cter."
    },
    # 26 - When we are reading, a voice comes to us
    {
        "en": "Reading awakens something inside that was sleeping. Let books call you back to your imagination.",
        "pt": "A leitura desperta algo dentro que estava adormecido. Deixe os livros o chamarem de volta \u00e0 sua imagina\u00e7\u00e3o.",
        "es": "La lectura despierta algo dentro que estaba dormido. Deja que los libros te llamen de vuelta a tu imaginaci\u00f3n."
    },
    # 27 - Poets are the sense, philosophers the intelligence
    {
        "en": "We need both feeling and thinking, the heart and the head. Neither alone is the whole of being human.",
        "pt": "Precisamos tanto do sentimento quanto do pensamento, do cora\u00e7\u00e3o e da cabe\u00e7a. Nenhum sozinho \u00e9 o todo do ser humano.",
        "es": "Necesitamos tanto el sentir como el pensar, el coraz\u00f3n y la cabeza. Ninguno solo es el todo del ser humano."
    },
    # 28 - Estragon: And if he doesn't come?
    {
        "en": "Stop trying to solve every problem before it arises. Trust that you will respond when the moment comes.",
        "pt": "Pare de tentar resolver cada problema antes que ele surja. Confie que voc\u00ea responder\u00e1 quando o momento chegar.",
        "es": "Deja de intentar resolver cada problema antes de que surja. Conf\u00eda en que responder\u00e1s cuando llegue el momento."
    },
    # 29 - Habit is a great deadener
    {
        "en": "Habits are necessary, but they can numb you to life. Periodically wake up and see your routines fresh.",
        "pt": "Os h\u00e1bitos s\u00e3o necess\u00e1rios, mas podem entorpec\u00ea-lo para a vida. Periodicamente acorde e veja suas rotinas com olhos novos.",
        "es": "Los h\u00e1bitos son necesarios, pero pueden adormecerte para la vida. Peri\u00f3dicamente despierta y ve tus rutinas con ojos frescos."
    },
    # 30 - We are all born mad. Some remain so.
    {
        "en": "There is a wildness inside all of us at birth. Conformity domesticates it, but a touch of madness keeps you alive.",
        "pt": "H\u00e1 uma selvageria dentro de todos n\u00f3s ao nascer. A conformidade a domestica, mas um toque de loucura o mant\u00e9m vivo.",
        "es": "Hay una salvajada dentro de todos nosotros al nacer. La conformidad la domestica, pero un toque de locura te mantiene vivo."
    },
    # 31 - There's never an end for the sea
    {
        "en": "Some things have no completion; they only have rhythms. Learn to live with movements that never finish.",
        "pt": "Algumas coisas n\u00e3o t\u00eam conclus\u00e3o; t\u00eam apenas ritmos. Aprenda a viver com movimentos que nunca terminam.",
        "es": "Algunas cosas no tienen conclusi\u00f3n; solo tienen ritmos. Aprende a vivir con movimientos que nunca terminan."
    },
    # 32 - Cascando (long love poem)
    {
        "en": "Love is not a problem to be solved with words. Sometimes the only honest response is to keep loving anyway.",
        "pt": "O amor n\u00e3o \u00e9 um problema a ser resolvido com palavras. \u00c0s vezes a \u00fanica resposta honesta \u00e9 continuar amando mesmo assim.",
        "es": "El amor no es un problema a resolver con palabras. A veces la \u00fanica respuesta honesta es seguir amando de todos modos."
    },
    # 33 - If you do not love me I shall not be loved (variant)
    {
        "en": "Love is not received passively; it must be given to exist. Begin by offering what you want to receive.",
        "pt": "O amor n\u00e3o \u00e9 recebido passivamente; deve ser dado para existir. Comece oferecendo o que voc\u00ea deseja receber.",
        "es": "El amor no se recibe pasivamente; debe darse para existir. Empieza ofreciendo lo que deseas recibir."
    },
    # 34 - Words are all we have
    {
        "en": "Imperfect as they are, words are how we touch each other across the void. Use them with intention.",
        "pt": "Imperfeitas como s\u00e3o, as palavras s\u00e3o como nos tocamos atrav\u00e9s do vazio. Use-as com inten\u00e7\u00e3o.",
        "es": "Imperfectas como son, las palabras son c\u00f3mo nos tocamos a trav\u00e9s del vac\u00edo. \u00dasalas con intenci\u00f3n."
    },
    # 35 - I can't go on. I'll go on.
    {
        "en": "Persistence does not require certainty or strength. Sometimes it is simply the next breath, the next step.",
        "pt": "A persist\u00eancia n\u00e3o exige certeza ou for\u00e7a. \u00c0s vezes \u00e9 simplesmente a pr\u00f3xima respira\u00e7\u00e3o, o pr\u00f3ximo passo.",
        "es": "La persistencia no requiere certeza o fuerza. A veces es simplemente la pr\u00f3xima respiraci\u00f3n, el pr\u00f3ximo paso."
    },
    # 36 - Birth was the death of him
    {
        "en": "From the moment you begin, you also start to end. Let this awareness make every day more precious.",
        "pt": "A partir do momento em que voc\u00ea come\u00e7a, tamb\u00e9m come\u00e7a a terminar. Que essa consci\u00eancia torne cada dia mais precioso.",
        "es": "Desde el momento en que comienzas, tambi\u00e9n empiezas a terminar. Que esta conciencia haga cada d\u00eda m\u00e1s precioso."
    },
    # 37 - Poets are the sense, philosophers the intelligence (variant)
    {
        "en": "Both art and thought are needed to be fully human. Cultivate the one you neglect most.",
        "pt": "Tanto a arte quanto o pensamento s\u00e3o necess\u00e1rios para ser plenamente humano. Cultive aquele que voc\u00ea mais negligencia.",
        "es": "Tanto el arte como el pensamiento son necesarios para ser plenamente humano. Cultiva aquel que m\u00e1s descuidas."
    },
    # 38 - We are all born mad. Some remain so. (variant)
    {
        "en": "The originality you were born with is precious. Do not let society polish away every strange edge.",
        "pt": "A originalidade com que voc\u00ea nasceu \u00e9 preciosa. N\u00e3o deixe a sociedade polir cada borda estranha.",
        "es": "La originalidad con que naciste es preciosa. No dejes que la sociedad pula cada borde extra\u00f1o."
    },
    # 39 - What do I know of man's destiny?
    {
        "en": "Modesty about the cosmic questions opens space for delight in the small ones. Cherish the radishes.",
        "pt": "A modestia sobre as quest\u00f5es c\u00f3smicas abre espa\u00e7o para o deleite nas pequenas. Aprecie os rabanetes.",
        "es": "La modestia sobre las preguntas c\u00f3smicas abre espacio para el deleite en las peque\u00f1as. Aprecia los r\u00e1banos."
    },
    # 40 - Ever tried. Ever failed. (variant)
    {
        "en": "Mastery is not the absence of failure but the willingness to fail with greater skill each time.",
        "pt": "A maestria n\u00e3o \u00e9 a aus\u00eancia de fracasso, mas a disposi\u00e7\u00e3o para fracassar com mais habilidade a cada vez.",
        "es": "La maestr\u00eda no es la ausencia del fracaso, sino la disposici\u00f3n a fracasar con mayor habilidad cada vez."
    },
]

result = {}
for i, key in enumerate(keys):
    if i < len(reflections):
        result[key] = reflections[i]

with open('c:/Users/lalli/Flutter/coach_phrase_app/reflections_absurdism.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f'Generated {len(result)} absurdism reflections')
