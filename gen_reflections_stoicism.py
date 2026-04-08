"""Generate reflections for 314 stoicism quotes using thematic templates."""
import json

with open('c:/Users/lalli/Flutter/coach_phrase_app/stoicism_keys.json', 'r', encoding='utf-8') as f:
    keys = json.load(f)

# === Thematic templates ===
CONTROL = {"en": "Focus your effort only on what is yours to control. Everything else is wasted attention.",
           "pt": "Concentre seu esfor\u00e7o apenas no que est\u00e1 sob seu controle. Todo o resto \u00e9 aten\u00e7\u00e3o desperdi\u00e7ada.",
           "es": "Concentra tu esfuerzo solo en lo que est\u00e1 bajo tu control. Todo lo dem\u00e1s es atenci\u00f3n desperdiciada."}

QUALITY_TIME = {"en": "It is not how long you live but how well. Make today worthy of being remembered.",
                "pt": "N\u00e3o \u00e9 quanto voc\u00ea vive, mas qu\u00e3o bem. Fa\u00e7a o dia de hoje digno de ser lembrado.",
                "es": "No es cu\u00e1nto vives, sino cu\u00e1n bien. Haz que el d\u00eda de hoy sea digno de ser recordado."}

PREPARATION = {"en": "Fortune favors those who prepare. Cultivate readiness so opportunity finds you ready.",
               "pt": "A sorte favorece os preparados. Cultive a prontid\u00e3o para que a oportunidade o encontre pronto.",
               "es": "La fortuna favorece a quienes se preparan. Cultiva la preparaci\u00f3n para que la oportunidad te encuentre listo."}

ADVERSITY = {"en": "Hardship strengthens what comfort softens. Welcome difficulty as your trainer.",
             "pt": "A dificuldade fortalece o que o conforto amolece. Acolha a adversidade como seu treinador.",
             "es": "La adversidad fortalece lo que la comodidad ablanda. Acoge la dificultad como tu entrenador."}

SELF_MASTERY = {"en": "True freedom begins with self-mastery. Govern yourself before trying to govern circumstances.",
                "pt": "A verdadeira liberdade come\u00e7a com o dom\u00ednio de si mesmo. Governe-se antes de tentar governar as circunst\u00e2ncias.",
                "es": "La verdadera libertad comienza con el dominio de uno mismo. Gob\u00edrnate antes de intentar gobernar las circunstancias."}

JUDGMENT = {"en": "Events themselves are neutral; your judgment makes them painful or peaceful. Examine your interpretations.",
            "pt": "Os eventos em si s\u00e3o neutros; seu julgamento os torna dolorosos ou pac\u00edficos. Examine suas interpreta\u00e7\u00f5es.",
            "es": "Los eventos en s\u00ed son neutrales; tu juicio los hace dolorosos o pac\u00edficos. Examina tus interpretaciones."}

PHILOSOPHY = {"en": "Live your philosophy, do not just speak it. Your actions teach more than your arguments ever could.",
              "pt": "Viva sua filosofia, n\u00e3o apenas a fale. Suas a\u00e7\u00f5es ensinam mais do que seus argumentos jamais poderiam.",
              "es": "Vive tu filosof\u00eda, no solo la hables. Tus acciones ense\u00f1an m\u00e1s de lo que tus argumentos podr\u00edan."}

DEATH = {"en": "Remember death often; it sharpens life. The shadow of mortality is what gives each day its value.",
         "pt": "Lembre-se da morte com frequ\u00eancia; ela aguça a vida. A sombra da mortalidade \u00e9 o que d\u00e1 valor a cada dia.",
         "es": "Recuerda la muerte a menudo; afila la vida. La sombra de la mortalidad es lo que da valor a cada d\u00eda."}

CONTENTMENT = {"en": "True wealth is wanting little, not having much. Reduce desires and you will discover abundance.",
               "pt": "A verdadeira riqueza \u00e9 desejar pouco, n\u00e3o ter muito. Reduza desejos e voc\u00ea descobrir\u00e1 a abund\u00e2ncia.",
               "es": "La verdadera riqueza es desear poco, no tener mucho. Reduce los deseos y descubrir\u00e1s la abundancia."}

PRESENT = {"en": "Only the present moment is yours. Stop reaching for past or future and inhabit now.",
           "pt": "Apenas o momento presente \u00e9 seu. Pare de buscar o passado ou o futuro e habite o agora.",
           "es": "Solo el momento presente es tuyo. Deja de alcanzar el pasado o el futuro y habita el ahora."}

NATURE = {"en": "Live in harmony with nature, not against it. Acceptance is not surrender but alignment.",
          "pt": "Viva em harmonia com a natureza, n\u00e3o contra ela. A aceita\u00e7\u00e3o n\u00e3o \u00e9 rendi\u00e7\u00e3o, mas alinhamento.",
          "es": "Vive en armon\u00eda con la naturaleza, no contra ella. La aceptaci\u00f3n no es rendici\u00f3n sino alineaci\u00f3n."}

TIME = {"en": "Time is the only resource that cannot be reclaimed. Stop wasting it on the trivial.",
        "pt": "O tempo \u00e9 o \u00fanico recurso que n\u00e3o pode ser recuperado. Pare de desperdi\u00e7\u00e1-lo com o trivial.",
        "es": "El tiempo es el \u00fanico recurso que no puede recuperarse. Deja de desperdiciarlo en lo trivial."}

CHANGE = {"en": "Everything flows; resist nothing and you suffer less. Change is the only constant.",
          "pt": "Tudo flui; n\u00e3o resista a nada e voc\u00ea sofrer\u00e1 menos. A mudan\u00e7a \u00e9 a \u00fanica constante.",
          "es": "Todo fluye; no resistas a nada y sufrir\u00e1s menos. El cambio es la \u00fanica constante."}

ACTION = {"en": "Stop discussing what a good person does and simply be one. Action speaks where words fail.",
          "pt": "Pare de discutir o que uma pessoa boa faz e simplesmente seja uma. A a\u00e7\u00e3o fala onde as palavras falham.",
          "es": "Deja de discutir lo que una buena persona hace y simplemente s\u00e9 una. La acci\u00f3n habla donde las palabras fallan."}

ANGER = {"en": "Anger costs you more than what provoked it. Pause before reacting and watch the cost shrink.",
         "pt": "A raiva lhe custa mais do que aquilo que a provocou. Pause antes de reagir e veja o custo encolher.",
         "es": "La ira te cuesta m\u00e1s que lo que la provoc\u00f3. Detente antes de reaccionar y observa cu\u00e1nto se reduce el costo."}

VIRTUE = {"en": "Virtue is its own reward; nothing else can be relied upon. Build a character no fortune can take away.",
          "pt": "A virtude \u00e9 sua pr\u00f3pria recompensa; nada mais pode ser confi\u00e1vel. Construa um car\u00e1ter que nenhuma fortuna pode tirar.",
          "es": "La virtud es su propia recompensa; en nada m\u00e1s se puede confiar. Construye un car\u00e1cter que ninguna fortuna pueda quitarte."}

SELF_INSIDE = {"en": "Look within for what you keep seeking outside. The fountain you need is already in you.",
               "pt": "Olhe para dentro pelo que voc\u00ea continua buscando fora. A fonte que voc\u00ea precisa j\u00e1 est\u00e1 em voc\u00ea.",
               "es": "Mira dentro lo que sigues buscando fuera. La fuente que necesitas ya est\u00e1 en ti."}

WORDS = {"en": "Speak only after thinking; let your speech serve, not impress. Listen twice as much as you talk.",
         "pt": "Fale apenas depois de pensar; que sua fala sirva, n\u00e3o impressione. Ou\u00e7a o dobro do que voc\u00ea fala.",
         "es": "Habla solo despu\u00e9s de pensar; que tu habla sirva, no impresione. Escucha el doble de lo que hablas."}

FRIENDSHIP = {"en": "True friendship is rare and precious. Choose few but trust them with everything.",
              "pt": "A verdadeira amizade \u00e9 rara e preciosa. Escolha poucos mas confie tudo a eles.",
              "es": "La verdadera amistad es rara y preciosa. Elige pocos pero conf\u00edales todo."}

FREEDOM = {"en": "Freedom is not absence of chains but mastery over desires. Free yourself from within first.",
           "pt": "A liberdade n\u00e3o \u00e9 a aus\u00eancia de correntes, mas o dom\u00ednio sobre os desejos. Liberte-se primeiro por dentro.",
           "es": "La libertad no es ausencia de cadenas sino dominio sobre los deseos. Lib\u00e9rate primero por dentro."}

FEAR = {"en": "What you fear is rarely as terrible as the fear itself. Look at it and watch it shrink.",
        "pt": "O que voc\u00ea teme raramente \u00e9 t\u00e3o terr\u00edvel quanto o pr\u00f3prio medo. Olhe para ele e veja-o encolher.",
        "es": "Lo que temes rara vez es tan terrible como el miedo mismo. M\u00edralo y obs\u00e9rvalo encogerse."}

MIND_GARDEN = {"en": "Your thoughts shape your life. Tend the garden of your mind as carefully as any other.",
               "pt": "Seus pensamentos moldam sua vida. Cuide do jardim da sua mente t\u00e3o cuidadosamente quanto qualquer outro.",
               "es": "Tus pensamientos moldean tu vida. Cuida el jard\u00edn de tu mente tan cuidadosamente como cualquier otro."}

ENDURANCE = {"en": "Bear what must be borne and abstain from what is harmful. Two words contain a whole philosophy.",
             "pt": "Suporte o que deve ser suportado e abstenha-se do que \u00e9 prejudicial. Duas palavras cont\u00eam toda uma filosofia.",
             "es": "Soporta lo que debe soportarse y abstente de lo da\u00f1ino. Dos palabras contienen toda una filosof\u00eda."}

HUMANITY = {"en": "We exist for one another; isolation poisons the soul. Reach out today.",
            "pt": "Existimos uns para os outros; o isolamento envenena a alma. Estenda a m\u00e3o hoje.",
            "es": "Existimos unos para los otros; el aislamiento envenena el alma. Tiende la mano hoy."}

PURPOSE = {"en": "Every action should have a clear purpose. Stop doing what does not serve your goals.",
           "pt": "Toda a\u00e7\u00e3o deve ter um prop\u00f3sito claro. Pare de fazer o que n\u00e3o serve aos seus objetivos.",
           "es": "Toda acci\u00f3n debe tener un prop\u00f3sito claro. Deja de hacer lo que no sirve a tus metas."}

reflections = [
    FREEDOM,  # 1
    QUALITY_TIME,  # 2
    PREPARATION,  # 3
    ADVERSITY,  # 4
    QUALITY_TIME,  # 5
    SELF_MASTERY,  # 6
    {"en": "Other people's opinions of you reveal more about them than about you. Stop carrying them.",
     "pt": "As opini\u00f5es dos outros sobre voc\u00ea revelam mais sobre eles do que sobre voc\u00ea. Pare de carreg\u00e1-las.",
     "es": "Las opiniones de los dem\u00e1s sobre ti revelan m\u00e1s de ellos que de ti. Deja de cargarlas."},  # 7
    PHILOSOPHY,  # 8
    {"en": "Difficult paths lead to extraordinary destinations. Welcome the climb that strengthens you.",
     "pt": "Caminhos dif\u00edceis levam a destinos extraordin\u00e1rios. Acolha a escalada que o fortalece.",
     "es": "Los caminos dif\u00edciles llevan a destinos extraordinarios. Acoge el ascenso que te fortalece."},  # 9
    {"en": "Wisdom is the result of intentional practice. Cultivate it today, not by accident but by design.",
     "pt": "A sabedoria \u00e9 resultado de pr\u00e1tica intencional. Cultive-a hoje, n\u00e3o por acaso mas por design.",
     "es": "La sabidur\u00eda es resultado de pr\u00e1ctica intencional. Cult\u00edvala hoy, no por accidente sino por dise\u00f1o."},  # 10
    {"en": "Good ideas belong to whoever uses them. Borrow freely from the wise.",
     "pt": "Boas ideias pertencem a quem as usa. Pegue emprestado livremente dos s\u00e1bios.",
     "es": "Las buenas ideas pertenecen a quien las usa. Toma prestado libremente de los sabios."},  # 11
    VIRTUE,  # 12
    JUDGMENT,  # 13
    JUDGMENT,  # 14
    {"en": "Listening well is harder than speaking well. Practice it as a discipline.",
     "pt": "Ouvir bem \u00e9 mais dif\u00edcil que falar bem. Pratique como disciplina.",
     "es": "Escuchar bien es m\u00e1s dif\u00edcil que hablar bien. Pract\u00edcalo como disciplina."},  # 15
    {"en": "Talking with the wise does not make you wise. Real wisdom must be earned through your own work.",
     "pt": "Conversar com os s\u00e1bios n\u00e3o o torna s\u00e1bio. A verdadeira sabedoria deve ser conquistada pelo seu pr\u00f3prio trabalho.",
     "es": "Conversar con los sabios no te hace sabio. La verdadera sabidur\u00eda debe ganarse con tu propio trabajo."},  # 16
    {"en": "When wronged, remember that the wrongdoer acted on their own perception of duty. Bear it gently.",
     "pt": "Quando sofrer injusti\u00e7a, lembre-se de que o agressor agiu segundo sua pr\u00f3pria percep\u00e7\u00e3o de dever. Suporte com gentileza.",
     "es": "Cuando seas agraviado, recuerda que el agresor actu\u00f3 seg\u00fan su propia percepci\u00f3n del deber. Sopor talo con gentileza."},  # 17
    {"en": "Crisis is opportunity in disguise. Every challenge offers something to learn or become.",
     "pt": "A crise \u00e9 oportunidade disfar\u00e7ada. Todo desafio oferece algo para aprender ou se tornar.",
     "es": "La crisis es oportunidad disfrazada. Todo desaf\u00edo ofrece algo que aprender o llegar a ser."},  # 18
    {"en": "We change bodies as we change clothes. The essence within outlasts every outer form.",
     "pt": "Trocamos de corpos como trocamos de roupas. A ess\u00eancia interior sobrevive a toda forma externa.",
     "es": "Cambiamos de cuerpos como cambiamos de ropa. La esencia interior sobrevive a toda forma externa."},  # 19
    PHILOSOPHY,  # 20
    {"en": "Solitude with yourself is a sign of inner order. Practice being alone without restlessness.",
     "pt": "A solid\u00e3o consigo mesmo \u00e9 sinal de ordem interior. Pratique ficar sozinho sem inquieta\u00e7\u00e3o.",
     "es": "La soledad contigo mismo es signo de orden interior. Practica estar solo sin inquietud."},  # 21
    CONTENTMENT,  # 22
    {"en": "Memory of past pleasures sometimes outlasts and outshines the experience itself. Cherish your good memories.",
     "pt": "A mem\u00f3ria dos prazeres passados \u00e0s vezes sobrevive e supera a pr\u00f3pria experi\u00eancia. Estime suas boas lembran\u00e7as.",
     "es": "La memoria de placeres pasados a veces sobrevive y supera la propia experiencia. Aprecia tus buenos recuerdos."},  # 23
    {"en": "You can choose what occupies your mind. Use that power to embrace the cosmos rather than petty worries.",
     "pt": "Voc\u00ea pode escolher o que ocupa sua mente. Use esse poder para abra\u00e7ar o cosmos em vez de preocupa\u00e7\u00f5es mesquinhas.",
     "es": "Puedes elegir lo que ocupa tu mente. Usa ese poder para abrazar el cosmos en lugar de preocupaciones mezquinas."},  # 24
    {"en": "Persisting in error is worse than the error itself. Correct your mistakes without shame.",
     "pt": "Persistir no erro \u00e9 pior que o pr\u00f3prio erro. Corrija seus erros sem vergonha.",
     "es": "Persistir en el error es peor que el error mismo. Corrige tus errores sin verg\u00fcenza."},  # 25
    {"en": "Aim for daily improvement, not perfection. Reduce one vice today and you have already won.",
     "pt": "Mire na melhoria di\u00e1ria, n\u00e3o na perfei\u00e7\u00e3o. Reduza um v\u00edcio hoje e voc\u00ea j\u00e1 venceu.",
     "es": "Apunta a la mejora diaria, no a la perfecci\u00f3n. Reduce un vicio hoy y ya has ganado."},  # 26
    {"en": "Better to be poor and free of fear than rich and full of worry. Choose peace over abundance.",
     "pt": "Melhor ser pobre e livre do medo do que rico e cheio de preocupa\u00e7\u00e3o. Escolha a paz em vez da abund\u00e2ncia.",
     "es": "Mejor ser pobre y libre de miedo que rico y lleno de preocupaci\u00f3n. Elige la paz sobre la abundancia."},  # 27
    {"en": "The wise person seeks truth in matters human and divine, never abandoning piety and justice.",
     "pt": "O s\u00e1bio busca a verdade nas coisas humanas e divinas, nunca abandonando a piedade e a justi\u00e7a.",
     "es": "El sabio busca la verdad en lo humano y lo divino, nunca abandonando la piedad y la justicia."},  # 28
    {"en": "Real happiness needs neither future hopes nor fears. Find sufficiency in what you already have.",
     "pt": "A verdadeira felicidade n\u00e3o precisa de esperan\u00e7as nem medos futuros. Encontre a sufici\u00eancia no que j\u00e1 tem.",
     "es": "La verdadera felicidad no necesita ni esperanzas ni miedos futuros. Encuentra suficiencia en lo que ya tienes."},  # 29
    SELF_MASTERY,  # 30
    CONTENTMENT,  # 31
    {"en": "Worry is suffering twice. Let go of what is beyond your control and your peace will return.",
     "pt": "Preocupar-se \u00e9 sofrer duas vezes. Solte o que est\u00e1 al\u00e9m do seu controle e sua paz retornar\u00e1.",
     "es": "Preocuparse es sufrir dos veces. Suelta lo que est\u00e1 m\u00e1s all\u00e1 de tu control y tu paz volver\u00e1."},  # 32
    {"en": "Death may come; lamenting helps nothing. Whatever happens, meet it with smiles and dignity.",
     "pt": "A morte pode chegar; lamentar n\u00e3o ajuda em nada. O que acontecer, encontre com sorrisos e dignidade.",
     "es": "La muerte puede llegar; lamentarse no ayuda en nada. Lo que suceda, enfr\u00e9ntalo con sonrisas y dignidad."},  # 33
    PHILOSOPHY,  # 34
    {"en": "The gods, however we conceive of them, do not relieve us of personal responsibility. Live as one who is fully accountable.",
     "pt": "Os deuses, como quer que os conceba, n\u00e3o o aliviam da responsabilidade pessoal. Viva como algu\u00e9m totalmente respons\u00e1vel.",
     "es": "Los dioses, como sea que los concibas, no te eximen de la responsabilidad personal. Vive como alguien totalmente responsable."},  # 35
    {"en": "If you want to be something, do the thing. Stop describing your dream and live it.",
     "pt": "Se voc\u00ea quer ser algo, fa\u00e7a a coisa. Pare de descrever seu sonho e viva-o.",
     "es": "Si quieres ser algo, haz la cosa. Deja de describir tu sue\u00f1o y v\u00edvelo."},  # 36
    {"en": "Sacred awe lives in quiet places. Step into nature today and let it remind you of the eternal.",
     "pt": "O temor sagrado vive em lugares tranquilos. Entre na natureza hoje e deixe que ela o lembre do eterno.",
     "es": "El asombro sagrado vive en lugares tranquilos. Entra en la naturaleza hoy y deja que te recuerde lo eterno."},  # 37
    {"en": "Both ruin and salvation come from within. Watch over the inner garden as if everything depended on it.",
     "pt": "Tanto a ru\u00edna quanto a salva\u00e7\u00e3o v\u00eam de dentro. Vigie o jardim interior como se tudo dependesse disso.",
     "es": "Tanto la ruina como la salvaci\u00f3n vienen de dentro. Vigila el jard\u00edn interior como si todo dependiera de ello."},  # 38
    {"en": "Real freedom requires real education. Train your mind to think clearly so your choices can be free.",
     "pt": "A verdadeira liberdade exige verdadeira educa\u00e7\u00e3o. Treine sua mente para pensar claramente para que suas escolhas possam ser livres.",
     "es": "La verdadera libertad requiere verdadera educaci\u00f3n. Entrena tu mente para pensar claramente para que tus elecciones puedan ser libres."},  # 39
    {"en": "First decide who you want to be, then act accordingly. Identity precedes action.",
     "pt": "Primeiro decida quem voc\u00ea quer ser, depois aja conforme. A identidade precede a a\u00e7\u00e3o.",
     "es": "Primero decide qui\u00e9n quieres ser, luego act\u00faa en consecuencia. La identidad precede a la acci\u00f3n."},  # 40
    QUALITY_TIME,  # 41
    TIME,  # 42
    {"en": "Books are food for the soul. Make time daily to nourish your inner life through reading.",
     "pt": "Os livros s\u00e3o alimento para a alma. Reserve tempo diariamente para nutrir sua vida interior atrav\u00e9s da leitura.",
     "es": "Los libros son alimento para el alma. Reserva tiempo diario para nutrir tu vida interior a trav\u00e9s de la lectura."},  # 43
    {"en": "Too much of anything, even books, becomes distraction. Choose quality over quantity.",
     "pt": "Excesso de qualquer coisa, mesmo livros, torna-se distra\u00e7\u00e3o. Escolha qualidade em vez de quantidade.",
     "es": "El exceso de cualquier cosa, incluso libros, se convierte en distracci\u00f3n. Elige calidad sobre cantidad."},  # 44
    JUDGMENT,  # 45
    {"en": "Imagine the worst as already happened, and you free yourself from worry. Acceptance precedes peace.",
     "pt": "Imagine o pior como j\u00e1 acontecido, e voc\u00ea se liberta da preocupa\u00e7\u00e3o. A aceita\u00e7\u00e3o precede a paz.",
     "es": "Imagina lo peor como ya sucedido, y te liberas de la preocupaci\u00f3n. La aceptaci\u00f3n precede a la paz."},  # 46
    {"en": "Beware flattery; it pleases precisely where it harms. Trust honest critics over sweet ones.",
     "pt": "Cuidado com a bajula\u00e7\u00e3o; ela agrada precisamente onde fere. Confie em cr\u00edticos honestos em vez de doces.",
     "es": "Cu\u00eddate de la adulaci\u00f3n; agrada precisamente donde da\u00f1a. Conf\u00eda en cr\u00edticos honestos m\u00e1s que en dulces."},  # 47
    {"en": "Courage liberates the soul. Cultivate it daily and freedom follows.",
     "pt": "A coragem liberta a alma. Cultive-a diariamente e a liberdade segue.",
     "es": "El coraje libera el alma. Cult\u00edvalo diariamente y la libertad sigue."},  # 48
    {"en": "Do not impose on others what you would not endure. Treat freedom as a universal right, not a personal privilege.",
     "pt": "N\u00e3o imponha aos outros o que voc\u00ea n\u00e3o suportaria. Trate a liberdade como direito universal, n\u00e3o privil\u00e9gio pessoal.",
     "es": "No impongas a otros lo que no soportar\u00edas. Trata la libertad como un derecho universal, no un privilegio personal."},  # 49
    DEATH,  # 50
    DEATH,  # 51
    QUALITY_TIME,  # 52
    {"en": "Treat yourself with the same kindness you give others. Stop inflicting needless pain on yourself.",
     "pt": "Trate a si mesmo com a mesma gentileza que d\u00e1 aos outros. Pare de infligir dor desnecess\u00e1ria a si mesmo.",
     "es": "Tr\u00e1tate con la misma amabilidad que das a otros. Deja de infligirte dolor innecesario."},  # 53
    {"en": "We naturally focus on our pain points. Notice this and gently redirect attention to what is well.",
     "pt": "Naturalmente focamos em nossos pontos de dor. Note isto e gentilmente redirecione a aten\u00e7\u00e3o para o que est\u00e1 bem.",
     "es": "Naturalmente nos enfocamos en nuestros puntos de dolor. Nota esto y gentilmente redirige la atenci\u00f3n a lo que est\u00e1 bien."},  # 54
    {"en": "Systematic curiosity expands the mind. Investigate everything with openness and care.",
     "pt": "A curiosidade sistem\u00e1tica expande a mente. Investigue tudo com abertura e cuidado.",
     "es": "La curiosidad sistem\u00e1tica expande la mente. Investiga todo con apertura y cuidado."},  # 55
    {"en": "Doing many things well is impossible. Focus on what truly matters and let the rest fall away.",
     "pt": "Fazer muitas coisas bem \u00e9 imposs\u00edvel. Foque no que realmente importa e deixe o resto cair.",
     "es": "Hacer muchas cosas bien es imposible. Enf\u00f3cate en lo que realmente importa y deja que el resto caiga."},  # 56
    {"en": "See things stripped of glamour and you will not be deceived. Vanity loses power when you see plainly.",
     "pt": "Veja as coisas despidas de brilho e voc\u00ea n\u00e3o ser\u00e1 enganado. A vaidade perde poder quando voc\u00ea v\u00ea com clareza.",
     "es": "Ve las cosas despojadas de glamour y no ser\u00e1s enga\u00f1ado. La vanidad pierde poder cuando ves con claridad."},  # 57
    {"en": "Both living well and dying well take a lifetime to learn. Begin practicing both today.",
     "pt": "Tanto viver bem quanto morrer bem levam uma vida para aprender. Comece a praticar ambos hoje.",
     "es": "Tanto vivir bien como morir bien requieren toda una vida para aprenderse. Comienza a practicar ambos hoy."},  # 58
    NATURE,  # 59
    NATURE,  # 60
    CHANGE,  # 61
    FRIENDSHIP,  # 62
    FRIENDSHIP,  # 63
    {"en": "Each person eventually faces consequences. Let nature handle justice and free yourself from anger.",
     "pt": "Cada pessoa eventualmente enfrenta consequ\u00eancias. Deixe a natureza cuidar da justi\u00e7a e liberte-se da raiva.",
     "es": "Cada persona eventualmente enfrenta consecuencias. Deja que la naturaleza maneje la justicia y lib\u00e9rate de la ira."},  # 64
    ADVERSITY,  # 65
    {"en": "Tears throughout life are appropriate; suffering is the price of caring. Grieve fully when needed.",
     "pt": "L\u00e1grimas ao longo da vida s\u00e3o apropriadas; o sofrimento \u00e9 o pre\u00e7o do cuidar. Lamente plenamente quando necess\u00e1rio.",
     "es": "Las l\u00e1grimas a lo largo de la vida son apropiadas; el sufrimiento es el precio de amar. Llora plenamente cuando sea necesario."},  # 66
    {"en": "Wealth tests character more than poverty does. Practice giving when you have more.",
     "pt": "A riqueza testa o car\u00e1ter mais que a pobreza. Pratique dar quando tiver mais.",
     "es": "La riqueza prueba el car\u00e1cter m\u00e1s que la pobreza. Practica dar cuando tengas m\u00e1s."},  # 67
    PURPOSE,  # 68
    {"en": "All things eventually fade. Let this knowledge make today vivid, not melancholy.",
     "pt": "Todas as coisas eventualmente desaparecem. Que este conhecimento torne hoje vivo, n\u00e3o melanc\u00f3lico.",
     "es": "Todas las cosas eventualmente se desvanecen. Que este conocimiento haga hoy vivo, no melanc\u00f3lico."},  # 69
    PRESENT,  # 70
    {"en": "Sometimes simply continuing to live takes courage. Honor that courage in yourself and others.",
     "pt": "\u00c0s vezes simplesmente continuar vivendo exige coragem. Honre essa coragem em si mesmo e nos outros.",
     "es": "A veces simplemente seguir viviendo requiere coraje. Honra ese coraje en ti mismo y en los dem\u00e1s."},  # 71
    {"en": "A small lapse in reason can undo much. Stay alert in small choices, not just big ones.",
     "pt": "Um pequeno deslize da raz\u00e3o pode desfazer muito. Mantenha-se alerta nas pequenas escolhas, n\u00e3o s\u00f3 nas grandes.",
     "es": "Un peque\u00f1o desliz de la raz\u00f3n puede deshacer mucho. Mant\u00e9nte alerta en peque\u00f1as elecciones, no solo en las grandes."},  # 72
    {"en": "Nature reveals her secrets gradually. Be patient with what you cannot yet understand.",
     "pt": "A natureza revela seus segredos gradualmente. Seja paciente com o que voc\u00ea ainda n\u00e3o pode entender.",
     "es": "La naturaleza revela sus secretos gradualmente. S\u00e9 paciente con lo que a\u00fan no puedes entender."},  # 73
    {"en": "Trust yourself to know what is right; if uncertain, consult the wise. Justice is the steadiest aim.",
     "pt": "Confie em si mesmo para saber o que \u00e9 certo; se incerto, consulte os s\u00e1bios. A justi\u00e7a \u00e9 o objetivo mais firme.",
     "es": "Conf\u00eda en ti mismo para saber lo que es correcto; si est\u00e1s incierto, consulta a los sabios. La justicia es el objetivo m\u00e1s firme."},  # 74
    {"en": "Two rules govern wise action: serve humanity and remain open to correction. Practice both daily.",
     "pt": "Duas regras governam a a\u00e7\u00e3o s\u00e1bia: servir a humanidade e permanecer aberto \u00e0 corre\u00e7\u00e3o. Pratique ambas diariamente.",
     "es": "Dos reglas gobiernan la acci\u00f3n sabia: servir a la humanidad y permanecer abierto a la correcci\u00f3n. Practica ambas diariamente."},  # 75
    JUDGMENT,  # 76
    JUDGMENT,  # 77
    MIND_GARDEN,  # 78
    {"en": "Death waits for everyone. While you can, be good and do good.",
     "pt": "A morte espera por todos. Enquanto pode, seja bom e fa\u00e7a o bem.",
     "es": "La muerte espera a todos. Mientras puedas, s\u00e9 bueno y haz el bien."},  # 79
    {"en": "Curiosity gives life its texture. Find something today that fills you with wonder.",
     "pt": "A curiosidade d\u00e1 textura \u00e0 vida. Encontre algo hoje que o encha de maravilha.",
     "es": "La curiosidad da textura a la vida. Encuentra algo hoy que te llene de maravilla."},  # 80
    CHANGE,  # 81
    QUALITY_TIME,  # 82
    {"en": "Beginners think they already know; learners admit they do not. Stay a learner.",
     "pt": "Iniciantes pensam que j\u00e1 sabem; aprendizes admitem que n\u00e3o sabem. Permane\u00e7a aprendiz.",
     "es": "Los principiantes creen que ya saben; los aprendices admiten que no. Mant\u00e9nte aprendiz."},  # 83
    JUDGMENT,  # 84
    {"en": "The world is your home, not your prison. Go where life calls you with bold steps.",
     "pt": "O mundo \u00e9 sua casa, n\u00e3o sua pris\u00e3o. V\u00e1 onde a vida o chama com passos ousados.",
     "es": "El mundo es tu hogar, no tu prisi\u00f3n. Ve a donde la vida te llame con pasos audaces."},  # 85
    {"en": "Stop waiting to become your best self. Begin today, in small acts and choices.",
     "pt": "Pare de esperar para se tornar sua melhor vers\u00e3o. Comece hoje, em pequenos atos e escolhas.",
     "es": "Deja de esperar para convertirte en tu mejor versi\u00f3n. Comienza hoy, en peque\u00f1os actos y elecciones."},  # 86
    DEATH,  # 87
    {"en": "Everything we love is on loan from time. Cherish your dear ones today, knowing they may not be there tomorrow.",
     "pt": "Tudo que amamos est\u00e1 emprestado pelo tempo. Estime seus queridos hoje, sabendo que podem n\u00e3o estar amanh\u00e3.",
     "es": "Todo lo que amamos est\u00e1 prestado por el tiempo. Aprecia a tus seres queridos hoy, sabiendo que pueden no estar ma\u00f1ana."},  # 88
    {"en": "You were born with everything you need. Stop accumulating and start using what you have.",
     "pt": "Voc\u00ea nasceu com tudo que precisa. Pare de acumular e comece a usar o que tem.",
     "es": "Naciste con todo lo que necesitas. Deja de acumular y empieza a usar lo que tienes."},  # 89
    {"en": "Time mends what reasoning cannot reach. Be patient with deep wounds.",
     "pt": "O tempo cura o que o racioc\u00ednio n\u00e3o pode alcan\u00e7ar. Seja paciente com feridas profundas.",
     "es": "El tiempo sana lo que la raz\u00f3n no puede alcanzar. S\u00e9 paciente con las heridas profundas."},  # 90
    JUDGMENT,  # 91
    {"en": "Every blessing is also a vulnerability. Hold success lightly, knowing it can change.",
     "pt": "Toda b\u00ean\u00e7\u00e3o tamb\u00e9m \u00e9 vulnerabilidade. Segure o sucesso levemente, sabendo que ele pode mudar.",
     "es": "Toda bendici\u00f3n es tambi\u00e9n una vulnerabilidad. Sost\u00e9n el \u00e9xito con ligereza, sabiendo que puede cambiar."},  # 92
    ADVERSITY,  # 93
    SELF_MASTERY,  # 94
    TIME,  # 95
    {"en": "Greatness often carries a touch of madness. Honor what is unusual in yourself.",
     "pt": "A grandeza frequentemente carrega um toque de loucura. Honre o que \u00e9 incomum em voc\u00ea.",
     "es": "La grandeza a menudo lleva un toque de locura. Honra lo que es inusual en ti."},  # 96
    HUMANITY,  # 97
    {"en": "Most people accept religion as comfort, not truth. Examine your beliefs to know what you really hold.",
     "pt": "A maioria aceita a religi\u00e3o como conforto, n\u00e3o como verdade. Examine suas cren\u00e7as para saber o que realmente sustenta.",
     "es": "La mayor\u00eda acepta la religi\u00f3n como consuelo, no como verdad. Examina tus creencias para saber qu\u00e9 sostienes realmente."},  # 98
    {"en": "Difficulty is not the obstacle; the lack of daring is. Try, and most things become possible.",
     "pt": "A dificuldade n\u00e3o \u00e9 o obst\u00e1culo; a falta de ousadia \u00e9. Tente, e a maioria das coisas se torna poss\u00edvel.",
     "es": "La dificultad no es el obst\u00e1culo; la falta de audacia s\u00ed lo es. Intenta, y la mayor\u00eda de las cosas se vuelven posibles."},  # 99
    {"en": "Public glory is bought at the price of life itself. Question what you sacrifice for status.",
     "pt": "A gl\u00f3ria p\u00fablica \u00e9 comprada ao pre\u00e7o da pr\u00f3pria vida. Questione o que voc\u00ea sacrifica por status.",
     "es": "La gloria p\u00fablica se compra al precio de la vida misma. Cuestiona qu\u00e9 sacrificas por estatus."},  # 100
    FRIENDSHIP,  # 101
    {"en": "We all have unique inner constitutions. Accept your nature rather than fighting it.",
     "pt": "Todos temos constitui\u00e7\u00f5es interiores \u00fanicas. Aceite sua natureza em vez de lutar contra ela.",
     "es": "Todos tenemos constituciones interiores \u00fanicas. Acepta tu naturaleza en lugar de pelear contra ella."},  # 102
    FREEDOM,  # 103
    {"en": "Envy reveals more about the envious than the envied. Watch this in yourself.",
     "pt": "A inveja revela mais sobre o invejoso do que sobre o invejado. Observe isto em si mesmo.",
     "es": "La envidia revela m\u00e1s sobre el envidioso que sobre el envidiado. Obs\u00e9rvalo en ti mismo."},  # 104
    {"en": "Reading should bring peace; if it does not, change what you read.",
     "pt": "A leitura deve trazer paz; se n\u00e3o trouxer, mude o que voc\u00ea l\u00ea.",
     "es": "La lectura debe traer paz; si no la trae, cambia lo que lees."},  # 105
    TIME,  # 106
    JUDGMENT,  # 107
    {"en": "Greatness needs time to ripen. Be patient with what you are growing.",
     "pt": "A grandeza precisa de tempo para amadurecer. Seja paciente com o que voc\u00ea est\u00e1 cultivando.",
     "es": "La grandeza necesita tiempo para madurar. S\u00e9 paciente con lo que est\u00e1s cultivando."},  # 108
    {"en": "Begin with small disciplines and build to greater ones. Tiny daily choices accumulate.",
     "pt": "Comece com pequenas disciplinas e construa para as maiores. Pequenas escolhas di\u00e1rias se acumulam.",
     "es": "Comienza con peque\u00f1as disciplinas y construye hacia las mayores. Las peque\u00f1as elecciones diarias se acumulan."},  # 109
    NATURE,  # 110
    {"en": "Astonishment at life's events is naive. Expect everything and you will not be surprised.",
     "pt": "O espanto diante dos eventos da vida \u00e9 ingenuidade. Espere tudo e voc\u00ea n\u00e3o se surpreender\u00e1.",
     "es": "El asombro ante los eventos de la vida es ingenuo. Esp\u00e9ralo todo y no te sorprender\u00e1s."},  # 111
    JUDGMENT,  # 112
    HUMANITY,  # 113
    NATURE,  # 114
    SELF_MASTERY,  # 115
    NATURE,  # 116
    {"en": "Every day brings new troubles, but also new opportunities. Greet each dawn ready.",
     "pt": "Todo dia traz novos problemas, mas tamb\u00e9m novas oportunidades. Sa\u00fade cada amanhecer pronto.",
     "es": "Cada d\u00eda trae nuevos problemas, pero tambi\u00e9n nuevas oportunidades. Saluda cada amanecer listo."},  # 117
    {"en": "No life is free of trouble; expect it and you will not be defeated by it.",
     "pt": "Nenhuma vida \u00e9 livre de problemas; espere-os e voc\u00ea n\u00e3o ser\u00e1 derrotado por eles.",
     "es": "Ninguna vida est\u00e1 libre de problemas; esp\u00e9ralos y no ser\u00e1s derrotado por ellos."},  # 118
    NATURE,  # 119
    ADVERSITY,  # 120
    FEAR,  # 121
    FEAR,  # 122
    ENDURANCE,  # 123
    {"en": "Many illnesses come from excess. Simplify what you consume.",
     "pt": "Muitas doen\u00e7as v\u00eam do excesso. Simplifique o que voc\u00ea consome.",
     "es": "Muchas enfermedades vienen del exceso. Simplifica lo que consumes."},  # 124
    CHANGE,  # 125
    CHANGE,  # 126
    {"en": "Remove unnecessary thoughts and unnecessary acts will follow. Begin with mental decluttering.",
     "pt": "Remova pensamentos desnecess\u00e1rios e atos desnecess\u00e1rios seguir\u00e3o. Comece com a desorganiza\u00e7\u00e3o mental.",
     "es": "Elimina los pensamientos innecesarios y los actos innecesarios seguir\u00e1n. Comienza con el desorden mental."},  # 127
    WORDS,  # 128
    {"en": "Familiarity dulls fear. Practice contact with what frightens you.",
     "pt": "A familiaridade embota o medo. Pratique o contato com o que o assusta.",
     "es": "La familiaridad embota el miedo. Practica el contacto con lo que te asusta."},  # 129
    {"en": "An untroubled spirit and clear sight are the two pillars of wisdom. Cultivate both daily.",
     "pt": "Um esp\u00edrito sereno e a vis\u00e3o clara s\u00e3o os dois pilares da sabedoria. Cultive ambos diariamente.",
     "es": "Un esp\u00edritu sereno y la vista clara son los dos pilares de la sabidur\u00eda. Cultiva ambos diariamente."},  # 130
    {"en": "When crisis comes, see it as training. The challenge is meant to make you a victor.",
     "pt": "Quando a crise vier, veja-a como treino. O desafio existe para faz\u00ea-lo um vencedor.",
     "es": "Cuando llegue la crisis, ve la como entrenamiento. El desaf\u00edo existe para hacerte un vencedor."},  # 131
    NATURE,  # 132
    {"en": "Cosmic challenges are designed to grow you. Embrace yours as an Olympic contestant would.",
     "pt": "Os desafios c\u00f3smicos s\u00e3o projetados para faz\u00ea-lo crescer. Abrace os seus como um competidor ol\u00edmpico faria.",
     "es": "Los desaf\u00edos c\u00f3smicos est\u00e1n dise\u00f1ados para hacerte crecer. Abraza los tuyos como un competidor ol\u00edmpico lo har\u00eda."},  # 133
    {"en": "Cruelty is never strength but weakness wearing a mask. Reject it within yourself.",
     "pt": "A crueldade nunca \u00e9 for\u00e7a, mas fraqueza com m\u00e1scara. Rejeite-a em si mesmo.",
     "es": "La crueldad nunca es fuerza, sino debilidad con m\u00e1scara. Rech\u00e1zala en ti mismo."},  # 134
    {"en": "Some will rejoice at any death; do not let this disturb you. Live not for the approval of others.",
     "pt": "Alguns se alegrar\u00e3o com qualquer morte; n\u00e3o deixe que isso o perturbe. N\u00e3o viva pela aprova\u00e7\u00e3o dos outros.",
     "es": "Algunos se alegrar\u00e1n con cualquier muerte; no dejes que esto te perturbe. No vivas por la aprobaci\u00f3n de los dem\u00e1s."},  # 135
    TIME,  # 136
    {"en": "Real growth takes time and cannot be forced. Trust the slow ripening of your own development.",
     "pt": "O verdadeiro crescimento leva tempo e n\u00e3o pode ser for\u00e7ado. Confie no amadurecimento lento do seu pr\u00f3prio desenvolvimento.",
     "es": "El crecimiento real lleva tiempo y no puede ser forzado. Conf\u00eda en la maduraci\u00f3n lenta de tu propio desarrollo."},  # 137
    {"en": "Drunkenness is voluntary madness. Examine the appetites that loosen your reason.",
     "pt": "A embriaguez \u00e9 loucura volunt\u00e1ria. Examine os apetites que afrouxam sua raz\u00e3o.",
     "es": "La embriaguez es locura voluntaria. Examina los apetitos que aflojan tu raz\u00f3n."},  # 138
    {"en": "Excess can be subtle; you can be drunk without staggering. Watch the small overindulgences.",
     "pt": "O excesso pode ser sutil; voc\u00ea pode estar b\u00eabado sem cambalear. Observe os pequenos excessos.",
     "es": "El exceso puede ser sutil; puedes estar borracho sin tambalearte. Observa los peque\u00f1os excesos."},  # 139
    ANGER,  # 140
    JUDGMENT,  # 141
    JUDGMENT,  # 142
    JUDGMENT,  # 143
    {"en": "Every accident is an invitation to use what you have. Look for the leverage in the obstacle.",
     "pt": "Todo acidente \u00e9 um convite para usar o que voc\u00ea tem. Procure a alavanca no obst\u00e1culo.",
     "es": "Todo accidente es una invitaci\u00f3n a usar lo que tienes. Busca la palanca en el obst\u00e1culo."},  # 144
    FRIENDSHIP,  # 145
    {"en": "Whatever nature gives you is fitting for you. Trust the wisdom of your circumstances.",
     "pt": "O que quer que a natureza lhe d\u00ea \u00e9 adequado para voc\u00ea. Confie na sabedoria das suas circunst\u00e2ncias.",
     "es": "Lo que sea que la naturaleza te d\u00e9 es apropiado para ti. Conf\u00eda en la sabidur\u00eda de tus circunstancias."},  # 146
    {"en": "Fate moves without recognizable order. Stop looking for cosmic justice and find your own.",
     "pt": "O destino se move sem ordem reconhec\u00edvel. Pare de procurar justi\u00e7a c\u00f3smica e encontre a sua.",
     "es": "El destino se mueve sin orden reconocible. Deja de buscar justicia c\u00f3smica y encuentra la tuya."},  # 147
    {"en": "Independence begins with simple needs. A satisfied stomach asks for less from the world.",
     "pt": "A independ\u00eancia come\u00e7a com necessidades simples. Um est\u00f4mago satisfeito pede menos ao mundo.",
     "es": "La independencia comienza con necesidades simples. Un est\u00f3mago satisfecho pide menos al mundo."},  # 148
    CONTENTMENT,  # 149
    {"en": "Gratitude is recognizing what you would miss if you did not have it. Practice this daily.",
     "pt": "A gratid\u00e3o \u00e9 reconhecer o que voc\u00ea sentiria falta se n\u00e3o tivesse. Pratique isto diariamente.",
     "es": "La gratitud es reconocer lo que extra\u00f1ar\u00edas si no lo tuvieras. Practica esto diariamente."},  # 150
    FREEDOM,  # 151
    CONTENTMENT,  # 152
    ENDURANCE,  # 153
    {"en": "What you chase reveals what you are. Choose worthy pursuits.",
     "pt": "O que voc\u00ea persegue revela o que voc\u00ea \u00e9. Escolha buscas dignas.",
     "es": "Lo que persigues revela lo que eres. Elige b\u00fasquedas dignas."},  # 154
    PURPOSE,  # 155
    {"en": "Decide who you want to be, then act accordingly. Identity precedes action.",
     "pt": "Decida quem voc\u00ea quer ser, depois aja conforme. A identidade precede a a\u00e7\u00e3o.",
     "es": "Decide qui\u00e9n quieres ser, luego act\u00faa en consecuencia. La identidad precede a la acci\u00f3n."},  # 156
    {"en": "Aim higher than you can comfortably reach. Your worth grows to meet your ambitions.",
     "pt": "Mire mais alto do que voc\u00ea consegue alcan\u00e7ar confortavelmente. Seu valor cresce para encontrar suas ambi\u00e7\u00f5es.",
     "es": "Apunta m\u00e1s alto de lo que puedes alcanzar c\u00f3modamente. Tu valor crece para alcanzar tus ambiciones."},  # 157
    {"en": "Doing what humans are made for brings real joy. Look for what is essentially yours to do.",
     "pt": "Fazer o que os humanos foram feitos para fazer traz alegria real. Procure o que \u00e9 essencialmente seu para fazer.",
     "es": "Hacer lo que los humanos est\u00e1n hechos para hacer trae alegr\u00eda real. Busca lo que es esencialmente tuyo para hacer."},  # 158
    VIRTUE,  # 159
    {"en": "The soul we cannot see deserves the same respect as the divine we cannot see. Honor what is invisible.",
     "pt": "A alma que n\u00e3o podemos ver merece o mesmo respeito que o divino que n\u00e3o podemos ver. Honre o invis\u00edvel.",
     "es": "El alma que no podemos ver merece el mismo respeto que lo divino que no podemos ver. Honra lo invisible."},  # 160
    {"en": "Leadership often means absorbing the hate of others without retaliation. Develop the strength to do this.",
     "pt": "A lideran\u00e7a frequentemente significa absorver o \u00f3dio dos outros sem retaliar. Desenvolva a for\u00e7a para fazer isto.",
     "es": "El liderazgo a menudo significa absorber el odio de otros sin tomar represalias. Desarrolla la fuerza para hacerlo."},  # 161
    {"en": "Wickedness ultimately punishes itself. Stop seeking revenge and let life work.",
     "pt": "A maldade ultimamente pune a si mesma. Pare de buscar vingan\u00e7a e deixe a vida agir.",
     "es": "La maldad finalmente se castiga a s\u00ed misma. Deja de buscar venganza y deja que la vida act\u00fae."},  # 162
    PHILOSOPHY,  # 163
    SELF_MASTERY,  # 164
    PHILOSOPHY,  # 165
    {"en": "Joy is a skill that can be practiced. Seek small moments of delight every day.",
     "pt": "A alegria \u00e9 uma habilidade que pode ser praticada. Busque pequenos momentos de deleite todos os dias.",
     "es": "La alegr\u00eda es una habilidad que puede practicarse. Busca peque\u00f1os momentos de deleite cada d\u00eda."},  # 166
    PHILOSOPHY,  # 167
    {"en": "An untroubled spirit and clear sight are the two pillars of wisdom. Cultivate both daily.",
     "pt": "Um esp\u00edrito sereno e a vis\u00e3o clara s\u00e3o os dois pilares da sabedoria. Cultive ambos diariamente.",
     "es": "Un esp\u00edritu sereno y la vista clara son los dos pilares de la sabidur\u00eda. Cultiva ambos diariamente."},  # 168
    SELF_INSIDE,  # 169
    SELF_MASTERY,  # 170
    {"en": "Doing what humans are made for brings real joy. Look for what is essentially yours to do.",
     "pt": "Fazer o que os humanos foram feitos para fazer traz alegria real. Procure o que \u00e9 essencialmente seu para fazer.",
     "es": "Hacer lo que los humanos est\u00e1n hechos para hacer trae alegr\u00eda real. Busca lo que es esencialmente tuyo para hacer."},  # 171
    MIND_GARDEN,  # 172
    PHILOSOPHY,  # 173
    {"en": "Those who wronged you also hate you. Stop expecting reconciliation from the wicked.",
     "pt": "Aqueles que o injuria tamb\u00e9m o odeiam. Pare de esperar reconcilia\u00e7\u00e3o dos maus.",
     "es": "Quienes te ofendieron tambi\u00e9n te odian. Deja de esperar reconciliaci\u00f3n de los malvados."},  # 174
    {"en": "We love ourselves but value others' opinions of us more. Notice this contradiction and step out of it.",
     "pt": "Amamos a n\u00f3s mesmos mas valorizamos mais as opini\u00f5es dos outros sobre n\u00f3s. Note essa contradi\u00e7\u00e3o e saia dela.",
     "es": "Nos amamos pero valoramos m\u00e1s las opiniones ajenas sobre nosotros. Nota esta contradicci\u00f3n y sal de ella."},  # 175
    {"en": "Hunger crowds out reason and justice. Address physical needs before expecting wisdom from anyone.",
     "pt": "A fome expulsa a raz\u00e3o e a justi\u00e7a. Aborde as necessidades f\u00edsicas antes de esperar sabedoria de algu\u00e9m.",
     "es": "El hambre expulsa la raz\u00f3n y la justicia. Atiende las necesidades f\u00edsicas antes de esperar sabidur\u00eda de nadie."},  # 176
    {"en": "Letting an insult pass is often nobler than avenging it. Choose silence as strength.",
     "pt": "Deixar um insulto passar \u00e9 frequentemente mais nobre que ving\u00e1-lo. Escolha o sil\u00eancio como for\u00e7a.",
     "es": "Dejar pasar un insulto es a menudo m\u00e1s noble que vengarlo. Elige el silencio como fuerza."},  # 177
    {"en": "Letting an insult pass is often nobler than avenging it. Choose silence as strength.",
     "pt": "Deixar um insulto passar \u00e9 frequentemente mais nobre que ving\u00e1-lo. Escolha o sil\u00eancio como for\u00e7a.",
     "es": "Dejar pasar un insulto es a menudo m\u00e1s noble que vengarlo. Elige el silencio como fuerza."},  # 178
    {"en": "Drunkenness is voluntary madness. Examine the appetites that loosen your reason.",
     "pt": "A embriaguez \u00e9 loucura volunt\u00e1ria. Examine os apetites que afrouxam sua raz\u00e3o.",
     "es": "La embriaguez es locura voluntaria. Examina los apetitos que aflojan tu raz\u00f3n."},  # 179
    NATURE,  # 180
    {"en": "Injustice cannot last forever. Trust this even when it seems to triumph today.",
     "pt": "A injusti\u00e7a n\u00e3o pode durar para sempre. Confie nisto mesmo quando parecer triunfar hoje.",
     "es": "La injusticia no puede durar para siempre. Conf\u00eda en esto incluso cuando parezca triunfar hoy."},  # 181
    {"en": "Justice requires hearing both sides. Practice this in every dispute, large or small.",
     "pt": "A justi\u00e7a exige ouvir ambos os lados. Pratique isto em cada disputa, grande ou pequena.",
     "es": "La justicia requiere escuchar a ambos lados. Practica esto en cada disputa, grande o peque\u00f1a."},  # 182
    {"en": "Teaching deepens understanding. Share what you know to learn it more deeply.",
     "pt": "Ensinar aprofunda o entendimento. Compartilhe o que voc\u00ea sabe para aprend\u00ea-lo mais profundamente.",
     "es": "Ense\u00f1ar profundiza la comprensi\u00f3n. Comparte lo que sabes para aprenderlo m\u00e1s profundamente."},  # 183
    QUALITY_TIME,  # 184
    {"en": "Living wisely is more like wrestling than dancing. Stay grounded and ready.",
     "pt": "Viver com sabedoria \u00e9 mais como lutar do que dan\u00e7ar. Mantenha-se firme e pronto.",
     "es": "Vivir sabiamente es m\u00e1s como luchar que como bailar. Mant\u00e9nte firme y listo."},  # 185
    QUALITY_TIME,  # 186
    CONTENTMENT,  # 187
    HUMANITY,  # 188
    {"en": "What was once vice can become custom. Beware the slow erosion of standards.",
     "pt": "O que outrora era v\u00edcio pode se tornar costume. Cuidado com a eros\u00e3o lenta dos padr\u00f5es.",
     "es": "Lo que una vez fue vicio puede convertirse en costumbre. Cuidado con la erosi\u00f3n lenta de los est\u00e1ndares."},  # 189
    ADVERSITY,  # 190
    SELF_MASTERY,  # 191
    {"en": "Hard times pass; joy returns. Hold on through the night.",
     "pt": "Tempos dif\u00edceis passam; a alegria retorna. Aguente a noite.",
     "es": "Los tiempos dif\u00edciles pasan; la alegr\u00eda regresa. Resiste la noche."},  # 192
    {"en": "Greatness needs time to ripen. Be patient with what you are growing.",
     "pt": "A grandeza precisa de tempo para amadurecer. Seja paciente com o que voc\u00ea est\u00e1 cultivando.",
     "es": "La grandeza necesita tiempo para madurar. S\u00e9 paciente con lo que est\u00e1s cultivando."},  # 193
    {"en": "Some appear busy but accomplish nothing. Distinguish movement from progress.",
     "pt": "Alguns parecem ocupados mas n\u00e3o realizam nada. Distinga movimento de progresso.",
     "es": "Algunos parecen ocupados pero no logran nada. Distingue movimiento de progreso."},  # 194
    {"en": "Principles only become yours through daily practice. Begin again today.",
     "pt": "Os princ\u00edpios s\u00f3 se tornam seus atrav\u00e9s da pr\u00e1tica di\u00e1ria. Comece de novo hoje.",
     "es": "Los principios solo se vuelven tuyos a trav\u00e9s de la pr\u00e1ctica diaria. Comienza de nuevo hoy."},  # 195
    {"en": "Death is coming for everyone. What do you wish to be doing when it arrives?",
     "pt": "A morte vem para todos. O que voc\u00ea deseja estar fazendo quando ela chegar?",
     "es": "La muerte viene para todos. \u00bfQu\u00e9 deseas estar haciendo cuando llegue?"},  # 196
    {"en": "Live each day as if it were your last; not in fear, but in fullness.",
     "pt": "Viva cada dia como se fosse o \u00faltimo; n\u00e3o no medo, mas na plenitude.",
     "es": "Vive cada d\u00eda como si fuera el \u00faltimo; no en el miedo, sino en la plenitud."},  # 197
    TIME,  # 198
    ADVERSITY,  # 199
    {"en": "An untroubled spirit and clear sight are the two pillars of wisdom. Cultivate both daily.",
     "pt": "Um esp\u00edrito sereno e a vis\u00e3o clara s\u00e3o os dois pilares da sabedoria. Cultive ambos diariamente.",
     "es": "Un esp\u00edritu sereno y la vista clara son los dos pilares de la sabidur\u00eda. Cultiva ambos diariamente."},  # 200
    SELF_INSIDE,  # 201
    ENDURANCE,  # 202
    PHILOSOPHY,  # 203
    MIND_GARDEN,  # 204
    MIND_GARDEN,  # 205
    {"en": "Imagine the worst as already happened, and you free yourself from worry. Acceptance precedes peace.",
     "pt": "Imagine o pior como j\u00e1 acontecido, e voc\u00ea se liberta da preocupa\u00e7\u00e3o. A aceita\u00e7\u00e3o precede a paz.",
     "es": "Imagina lo peor como ya sucedido, y te liberas de la preocupaci\u00f3n. La aceptaci\u00f3n precede a la paz."},  # 206
    {"en": "Power should be exercised lightly. The lightest touch is often most effective.",
     "pt": "O poder deve ser exercido com leveza. O toque mais leve \u00e9 frequentemente o mais eficaz.",
     "es": "El poder debe ejercerse con ligereza. El toque m\u00e1s ligero es a menudo el m\u00e1s eficaz."},  # 207
    {"en": "First ask for a clear conscience, then for health of mind, then of body. Order your prayers wisely.",
     "pt": "Primeiro pe\u00e7a uma boa consci\u00eancia, depois sa\u00fade mental, depois corporal. Ordene suas ora\u00e7\u00f5es com sabedoria.",
     "es": "Primero pide una buena conciencia, luego salud mental, luego corporal. Ordena tus oraciones sabiamente."},  # 208
    NATURE,  # 209
    {"en": "Revenge demeans both the giver and receiver. Drop it from your toolkit.",
     "pt": "A vingan\u00e7a degrada tanto quem d\u00e1 quanto quem recebe. Tire-a do seu arsenal.",
     "es": "La venganza degrada tanto a quien la da como a quien la recibe. Qu\u00edtala de tu arsenal."},  # 210
    NATURE,  # 211
    {"en": "Live as one whose life is on display, not in vanity but in integrity.",
     "pt": "Viva como algu\u00e9m cuja vida est\u00e1 em exibi\u00e7\u00e3o, n\u00e3o por vaidade mas por integridade.",
     "es": "Vive como alguien cuya vida est\u00e1 en exhibici\u00f3n, no por vanidad sino por integridad."},  # 212
    {"en": "Death is coming for everyone. What do you wish to be doing when it arrives?",
     "pt": "A morte vem para todos. O que voc\u00ea deseja estar fazendo quando ela chegar?",
     "es": "La muerte viene para todos. \u00bfQu\u00e9 deseas estar haciendo cuando llegue?"},  # 213
    {"en": "If you cannot keep your own secrets, do not expect others to keep them. Practice discretion.",
     "pt": "Se voc\u00ea n\u00e3o consegue guardar seus pr\u00f3prios segredos, n\u00e3o espere que os outros os guardem. Pratique a discri\u00e7\u00e3o.",
     "es": "Si no puedes guardar tus propios secretos, no esperes que los dem\u00e1s los guarden. Practica la discreci\u00f3n."},  # 214
    SELF_MASTERY,  # 215
    FREEDOM,  # 216
    {"en": "Both ruin and recovery come from within. Look inward when seeking either.",
     "pt": "Tanto a ru\u00edna quanto a recupera\u00e7\u00e3o v\u00eam de dentro. Olhe para dentro ao buscar qualquer uma.",
     "es": "Tanto la ruina como la recuperaci\u00f3n vienen de dentro. Mira hacia dentro al buscar cualquiera."},  # 217
    SELF_INSIDE,  # 218
    SELF_INSIDE,  # 219
    {"en": "Inner support is what holds character upright. Build the columns inside before facing the storms outside.",
     "pt": "O suporte interior \u00e9 o que mant\u00e9m o car\u00e1ter ereto. Construa as colunas por dentro antes de enfrentar as tempestades l\u00e1 fora.",
     "es": "El soporte interior es lo que mantiene erguido al car\u00e1cter. Construye las columnas por dentro antes de enfrentar las tormentas afuera."},  # 220
    {"en": "Mind your own business and you save yourself much grief. Let others' affairs be theirs.",
     "pt": "Cuide dos seus pr\u00f3prios assuntos e voc\u00ea se poupar\u00e1 muito sofrimento. Deixe os assuntos dos outros serem deles.",
     "es": "Oc\u00fapate de tus propios asuntos y te ahorrar\u00e1s mucho sufrimiento. Deja que los asuntos de los dem\u00e1s sean suyos."},  # 221
    PHILOSOPHY,  # 222
    {"en": "Your life is on loan to you. Take responsibility for its care and use.",
     "pt": "Sua vida est\u00e1 emprestada a voc\u00ea. Assuma a responsabilidade pelo seu cuidado e uso.",
     "es": "Tu vida te ha sido prestada. Toma responsabilidad por su cuidado y uso."},  # 223
    WORDS,  # 224
    PURPOSE,  # 225
    HUMANITY,  # 226
    {"en": "Good ideas belong to whoever uses them. Borrow freely from the wise.",
     "pt": "Boas ideias pertencem a quem as usa. Pegue emprestado livremente dos s\u00e1bios.",
     "es": "Las buenas ideas pertenecen a quien las usa. Toma prestado libremente de los sabios."},  # 227
    WORDS,  # 228
    WORDS,  # 229
    {"en": "Failure is often a teacher; success a flatterer. Learn from both.",
     "pt": "O fracasso \u00e9 frequentemente um professor; o sucesso, um adulador. Aprenda com ambos.",
     "es": "El fracaso es a menudo un maestro; el \u00e9xito, un adulador. Aprende de ambos."},  # 230
    {"en": "Life favors all without distinction. Notice this generosity in your day.",
     "pt": "A vida favorece a todos sem distin\u00e7\u00e3o. Note essa generosidade no seu dia.",
     "es": "La vida favorece a todos sin distinci\u00f3n. Nota esta generosidad en tu d\u00eda."},  # 231
    {"en": "Reason will be there when you need it. Stop worrying about tomorrow's troubles in advance.",
     "pt": "A raz\u00e3o estar\u00e1 l\u00e1 quando voc\u00ea precisar. Pare de se preocupar com os problemas de amanh\u00e3 com anteced\u00eancia.",
     "es": "La raz\u00f3n estar\u00e1 ah\u00ed cuando la necesites. Deja de preocuparte por los problemas de ma\u00f1ana con anticipaci\u00f3n."},  # 232
    PRESENT,  # 233
    PRESENT,  # 234
    PRESENT,  # 235
    PRESENT,  # 236
    {"en": "Time eventually reveals all truths. Be patient with what is hidden.",
     "pt": "O tempo eventualmente revela todas as verdades. Seja paciente com o que est\u00e1 escondido.",
     "es": "El tiempo eventualmente revela todas las verdades. S\u00e9 paciente con lo oculto."},  # 237
    TIME,  # 238
    {"en": "Begin with small disciplines and build to greater ones. Tiny daily choices accumulate.",
     "pt": "Comece com pequenas disciplinas e construa para as maiores. Pequenas escolhas di\u00e1rias se acumulam.",
     "es": "Comienza con peque\u00f1as disciplinas y construye hacia las mayores. Las peque\u00f1as elecciones diarias se acumulan."},  # 239
    CHANGE,  # 240
    {"en": "Even without a teacher, vice can be learned. Choose your environment carefully.",
     "pt": "Mesmo sem um professor, o v\u00edcio pode ser aprendido. Escolha seu ambiente cuidadosamente.",
     "es": "Incluso sin un maestro, el vicio puede aprenderse. Elige tu ambiente con cuidado."},  # 241
    {"en": "Cruelty is never strength but weakness wearing a mask. Reject it within yourself.",
     "pt": "A crueldade nunca \u00e9 for\u00e7a, mas fraqueza com m\u00e1scara. Rejeite-a em si mesmo.",
     "es": "La crueldad nunca es fuerza, sino debilidad con m\u00e1scara. Rech\u00e1zala en ti mismo."},  # 242
    {"en": "Life favors all without distinction. Notice this generosity in your day.",
     "pt": "A vida favorece a todos sem distin\u00e7\u00e3o. Note essa generosidade no seu dia.",
     "es": "La vida favorece a todos sin distinci\u00f3n. Nota esta generosidad en tu d\u00eda."},  # 243
    {"en": "Good and evil live in the will, not in things. Examine your choices, not the world.",
     "pt": "O bem e o mal vivem na vontade, n\u00e3o nas coisas. Examine suas escolhas, n\u00e3o o mundo.",
     "es": "El bien y el mal viven en la voluntad, no en las cosas. Examina tus elecciones, no el mundo."},  # 244
    {"en": "Activity is not the same as productivity. Make sure your busyness serves real ends.",
     "pt": "A atividade n\u00e3o \u00e9 o mesmo que produtividade. Certifique-se de que sua ocupa\u00e7\u00e3o serve a fins reais.",
     "es": "La actividad no es lo mismo que productividad. Aseg\u00farate de que tu ocupaci\u00f3n sirva a fines reales."},  # 245
    {"en": "If you want to be a reader, read; a writer, write. Identity follows action.",
     "pt": "Se voc\u00ea quer ser leitor, leia; escritor, escreva. A identidade segue a a\u00e7\u00e3o.",
     "es": "Si quieres ser lector, lee; escritor, escribe. La identidad sigue a la acci\u00f3n."},  # 246
    {"en": "Inner peace is independent of outer noise. Cultivate stillness within.",
     "pt": "A paz interior independe do ru\u00eddo exterior. Cultive a quietude por dentro.",
     "es": "La paz interior es independiente del ruido exterior. Cultiva la quietud dentro."},  # 247
    {"en": "Diversify your hopes as you would diversify your investments. Never rest your life on a single hope.",
     "pt": "Diversifique suas esperan\u00e7as como diversificaria seus investimentos. Nunca repouse sua vida numa \u00fanica esperan\u00e7a.",
     "es": "Diversifica tus esperanzas como diversificar\u00edas tus inversiones. Nunca descanses tu vida en una sola esperanza."},  # 248
    {"en": "Diversify your hopes as you would diversify your investments. Never rest your life on a single hope.",
     "pt": "Diversifique suas esperan\u00e7as como diversificaria seus investimentos. Nunca repouse sua vida numa \u00fanica esperan\u00e7a.",
     "es": "Diversifica tus esperanzas como diversificar\u00edas tus inversiones. Nunca descanses tu vida en una sola esperanza."},  # 249
    {"en": "Wisdom is a richer inheritance than wealth. Educate those you love.",
     "pt": "A sabedoria \u00e9 uma heran\u00e7a mais rica que a riqueza. Eduque aqueles que voc\u00ea ama.",
     "es": "La sabidur\u00eda es una herencia m\u00e1s rica que la riqueza. Educa a quienes amas."},  # 250
    NATURE,  # 251
    SELF_INSIDE,  # 252
    {"en": "Each day brings its own gifts. Look for them with attentive eyes.",
     "pt": "Cada dia traz seus pr\u00f3prios presentes. Procure-os com olhos atentos.",
     "es": "Cada d\u00eda trae sus propios regalos. B\u00fascalos con ojos atentos."},  # 253
    {"en": "Being alive is itself a privilege. Begin each day with this recognition.",
     "pt": "Estar vivo \u00e9 em si um privil\u00e9gio. Comece cada dia com este reconhecimento.",
     "es": "Estar vivo es en s\u00ed un privilegio. Comienza cada d\u00eda con este reconocimiento."},  # 254
    WORDS,  # 255
    WORDS,  # 256
    JUDGMENT,  # 257
    {"en": "Begin and the work is half done. Stop hesitating and act.",
     "pt": "Comece e o trabalho est\u00e1 meio feito. Pare de hesitar e aja.",
     "es": "Comienza y el trabajo est\u00e1 medio hecho. Deja de dudar y act\u00faa."},  # 258
    CHANGE,  # 259
    HUMANITY,  # 260
    {"en": "Welcome death as part of the cycle. Resistance only adds suffering to the inevitable.",
     "pt": "Acolha a morte como parte do ciclo. A resist\u00eancia s\u00f3 adiciona sofrimento ao inevit\u00e1vel.",
     "es": "Acoge la muerte como parte del ciclo. La resistencia solo a\u00f1ade sufrimiento a lo inevitable."},  # 261
    SELF_MASTERY,  # 262
    NATURE,  # 263
    CHANGE,  # 264
    NATURE,  # 265
    {"en": "Every ending is also a beginning. Look for what is being born in what is dying.",
     "pt": "Todo fim \u00e9 tamb\u00e9m um come\u00e7o. Procure o que est\u00e1 nascendo no que est\u00e1 morrendo.",
     "es": "Todo final es tambi\u00e9n un comienzo. Busca lo que est\u00e1 naciendo en lo que est\u00e1 muriendo."},  # 266
    {"en": "If something is humanly possible, it is possible for you. Believe in your capacity.",
     "pt": "Se algo \u00e9 humanamente poss\u00edvel, \u00e9 poss\u00edvel para voc\u00ea. Acredite na sua capacidade.",
     "es": "Si algo es humanamente posible, es posible para ti. Cree en tu capacidad."},  # 267
    {"en": "Death liberates from many burdens. Stop fearing what may turn out to be a release.",
     "pt": "A morte liberta de muitos fardos. Pare de temer o que pode ser uma liberta\u00e7\u00e3o.",
     "es": "La muerte libera de muchas cargas. Deja de temer lo que puede ser una liberaci\u00f3n."},  # 268
    {"en": "Choose your death as you choose your house. Live so that the choice when it comes is calm.",
     "pt": "Escolha sua morte como escolhe sua casa. Viva de forma que a escolha quando chegar seja calma.",
     "es": "Elige tu muerte como eliges tu casa. Vive de modo que la elecci\u00f3n cuando llegue sea calma."},  # 269
    FEAR,  # 270
    PHILOSOPHY,  # 271
    VIRTUE,  # 272
    {"en": "Tolerate religious differences; each person finds their own path to meaning.",
     "pt": "Tolere as diferen\u00e7as religiosas; cada pessoa encontra seu pr\u00f3prio caminho para o significado.",
     "es": "Tolera las diferencias religiosas; cada persona encuentra su propio camino al significado."},  # 273
    {"en": "Religion and treasure must align, or one will always sacrifice the other. Examine where you place your worship.",
     "pt": "Religi\u00e3o e tesouro devem se alinhar, ou um sempre sacrificar\u00e1 o outro. Examine onde voc\u00ea coloca sua adora\u00e7\u00e3o.",
     "es": "La religi\u00f3n y el tesoro deben alinearse, o uno siempre sacrificar\u00e1 al otro. Examina d\u00f3nde colocas tu adoraci\u00f3n."},  # 274
    {"en": "Greatness needs time to ripen. Be patient with what you are growing.",
     "pt": "A grandeza precisa de tempo para amadurecer. Seja paciente com o que voc\u00ea est\u00e1 cultivando.",
     "es": "La grandeza necesita tiempo para madurar. S\u00e9 paciente con lo que est\u00e1s cultivando."},  # 275
    TIME,  # 276
    {"en": "The hours saved by minding your own business are countless. Save them and use them well.",
     "pt": "As horas economizadas cuidando dos seus pr\u00f3prios assuntos s\u00e3o incont\u00e1veis. Economize-as e use-as bem.",
     "es": "Las horas ahorradas ocup\u00e1ndote de tus propios asuntos son incontables. Ah\u00f3rralas y \u00fasalas bien."},  # 277
    {"en": "Surround yourself with people who lift you. Companions shape who you become.",
     "pt": "Cerque-se de pessoas que o elevam. Os companheiros moldam quem voc\u00ea se torna.",
     "es": "Rod\u00e9ate de personas que te eleven. Los compa\u00f1eros moldean en lo que te conviertes."},  # 278
    CONTROL,  # 279
    {"en": "Imitating others wastes your originality. The best response to copies is to be unmistakable.",
     "pt": "Imitar os outros desperdi\u00e7a sua originalidade. A melhor resposta \u00e0s c\u00f3pias \u00e9 ser inconfund\u00edvel.",
     "es": "Imitar a otros desperdicia tu originalidad. La mejor respuesta a las copias es ser inconfundible."},  # 280
    {"en": "Outer beauty without inner depth is hollow. Cultivate both heart and presence.",
     "pt": "A beleza externa sem profundidade interior \u00e9 vazia. Cultive tanto o cora\u00e7\u00e3o quanto a presen\u00e7a.",
     "es": "La belleza exterior sin profundidad interior es hueca. Cultiva tanto el coraz\u00f3n como la presencia."},  # 281
    {"en": "Do good as naturally as a horse runs or a bee makes honey. Make virtue effortless.",
     "pt": "Fa\u00e7a o bem t\u00e3o naturalmente quanto um cavalo corre ou uma abelha faz mel. Torne a virtude sem esfor\u00e7o.",
     "es": "Haz el bien tan naturalmente como un caballo corre o una abeja hace miel. Haz la virtud sin esfuerzo."},  # 282
    {"en": "Reframe misfortune as good fortune. Bearing it well is its own kind of luck.",
     "pt": "Reformule o infort\u00fanio como boa sorte. Suport\u00e1-lo bem \u00e9 seu pr\u00f3prio tipo de sorte.",
     "es": "Reformula el infortunio como buena fortuna. Sopor talo bien es su propio tipo de suerte."},  # 283
    {"en": "Living happily is an inner power, not an external circumstance. Cultivate it within.",
     "pt": "Viver feliz \u00e9 um poder interior, n\u00e3o uma circunst\u00e2ncia externa. Cultive-o por dentro.",
     "es": "Vivir feliz es un poder interior, no una circunstancia externa. Cult\u00edvalo por dentro."},  # 284
    {"en": "Your life is on loan to you. Take responsibility for its care and use.",
     "pt": "Sua vida est\u00e1 emprestada a voc\u00ea. Assuma a responsabilidade pelo seu cuidado e uso.",
     "es": "Tu vida te ha sido prestada. Toma responsabilidad por su cuidado y uso."},  # 285
    {"en": "Existence is transformation; identity is opinion. Hold both lightly.",
     "pt": "A exist\u00eancia \u00e9 transforma\u00e7\u00e3o; a identidade \u00e9 opini\u00e3o. Segure ambos com leveza.",
     "es": "La existencia es transformaci\u00f3n; la identidad es opini\u00f3n. Sost\u00e9n ambos con ligereza."},  # 286
    {"en": "Aim higher than you can comfortably reach. Your worth grows to meet your ambitions.",
     "pt": "Mire mais alto do que voc\u00ea consegue alcan\u00e7ar confortavelmente. Seu valor cresce para encontrar suas ambi\u00e7\u00f5es.",
     "es": "Apunta m\u00e1s alto de lo que puedes alcanzar c\u00f3modamente. Tu valor crece para alcanzar tus ambiciones."},  # 287
    {"en": "Look at the design behind people's actions, including your own. Motives matter more than appearances.",
     "pt": "Olhe para o design por tr\u00e1s das a\u00e7\u00f5es das pessoas, incluindo as suas. Os motivos importam mais que as apar\u00eancias.",
     "es": "Mira el dise\u00f1o detr\u00e1s de las acciones de las personas, incluyendo las tuyas. Los motivos importan m\u00e1s que las apariencias."},  # 288
    {"en": "Choose a model character to follow. Imitation of the best becomes original character.",
     "pt": "Escolha um car\u00e1ter modelo para seguir. A imita\u00e7\u00e3o do melhor se torna car\u00e1ter original.",
     "es": "Elige un car\u00e1cter modelo a seguir. La imitaci\u00f3n de lo mejor se vuelve car\u00e1cter original."},  # 289
    {"en": "Talent comes from understanding; genius from reason and imagination. Cultivate both.",
     "pt": "O talento vem do entendimento; o g\u00eanio, da raz\u00e3o e da imagina\u00e7\u00e3o. Cultive ambos.",
     "es": "El talento viene del entendimiento; el genio, de la raz\u00f3n y la imaginaci\u00f3n. Cultiva ambos."},  # 290
    {"en": "Living wisely is more like wrestling than dancing. Stay grounded and ready.",
     "pt": "Viver com sabedoria \u00e9 mais como lutar do que dan\u00e7ar. Mantenha-se firme e pronto.",
     "es": "Vivir sabiamente es m\u00e1s como luchar que como bailar. Mant\u00e9nte firme y listo."},  # 291
    DEATH,  # 292
    FRIENDSHIP,  # 293
    {"en": "Education begins when we stop blaming others, deepens when we stop blaming ourselves, and completes when we blame neither.",
     "pt": "A educa\u00e7\u00e3o come\u00e7a quando paramos de culpar os outros, aprofunda-se quando paramos de culpar a n\u00f3s mesmos, e se completa quando n\u00e3o culpamos nenhum.",
     "es": "La educaci\u00f3n comienza cuando dejamos de culpar a otros, se profundiza cuando dejamos de culparnos, y se completa cuando no culpamos a ninguno."},  # 294
    {"en": "Natural ability without education has lifted more people to glory than education without ability. Use what you have.",
     "pt": "A habilidade natural sem educa\u00e7\u00e3o elevou mais pessoas \u00e0 gl\u00f3ria do que a educa\u00e7\u00e3o sem habilidade. Use o que voc\u00ea tem.",
     "es": "La habilidad natural sin educaci\u00f3n ha elevado a m\u00e1s personas a la gloria que la educaci\u00f3n sin habilidad. Usa lo que tienes."},  # 295
    JUDGMENT,  # 296
    HUMANITY,  # 297
    SELF_INSIDE,  # 298
    CONTENTMENT,  # 299
    QUALITY_TIME,  # 300
    QUALITY_TIME,  # 301
    NATURE,  # 302
    {"en": "Move forward as occasion offers, content with small victories. Even small results are not trivial.",
     "pt": "Avance conforme a ocasi\u00e3o se apresenta, contente com pequenas vit\u00f3rias. At\u00e9 pequenos resultados n\u00e3o s\u00e3o triviais.",
     "es": "Avanza seg\u00fan se presenten las ocasiones, contento con peque\u00f1as victorias. Incluso peque\u00f1os resultados no son triviales."},  # 303
    {"en": "Not every difficulty is suitable training. Choose challenges that move you toward your real goals.",
     "pt": "Nem toda dificuldade \u00e9 treinamento adequado. Escolha desafios que o movam em dire\u00e7\u00e3o aos seus objetivos reais.",
     "es": "No toda dificultad es entrenamiento adecuado. Elige desaf\u00edos que te muevan hacia tus metas reales."},  # 304
    {"en": "We love ourselves but value others' opinions of us more. Notice this contradiction and step out of it.",
     "pt": "Amamos a n\u00f3s mesmos mas valorizamos mais as opini\u00f5es dos outros sobre n\u00f3s. Note essa contradi\u00e7\u00e3o e saia dela.",
     "es": "Nos amamos pero valoramos m\u00e1s las opiniones ajenas sobre nosotros. Nota esta contradicci\u00f3n y sal de ella."},  # 305
    {"en": "Live as one whose life is on display, not in vanity but in integrity.",
     "pt": "Viva como algu\u00e9m cuja vida est\u00e1 em exibi\u00e7\u00e3o, n\u00e3o por vaidade mas por integridade.",
     "es": "Vive como alguien cuya vida est\u00e1 en exhibici\u00f3n, no por vanidad sino por integridad."},  # 306
    JUDGMENT,  # 307
    HUMANITY,  # 308
    {"en": "When offended, look at your own faults first. Anger usually softens with self-knowledge.",
     "pt": "Quando ofendido, olhe primeiro para suas pr\u00f3prias falhas. A raiva geralmente abranda com o autoconhecimento.",
     "es": "Cuando est\u00e9s ofendido, mira primero tus propias faltas. La ira generalmente se ablanda con el autoconocimiento."},  # 309
    {"en": "Anger that hides itself becomes lying. Honest anger is at least true.",
     "pt": "A raiva que se esconde torna-se mentira. A raiva honesta \u00e9 pelo menos verdadeira.",
     "es": "La ira que se esconde se convierte en mentira. La ira honesta es al menos verdadera."},  # 310
    {"en": "The universe changes; your life is what your thoughts make of it. Tend your mind.",
     "pt": "O universo muda; sua vida \u00e9 o que seus pensamentos fazem dela. Cuide da sua mente.",
     "es": "El universo cambia; tu vida es lo que tus pensamientos hacen de ella. Cuida tu mente."},  # 311
    FREEDOM,  # 312
    {"en": "The past illuminates the future. Study what came before to see clearly what comes next.",
     "pt": "O passado ilumina o futuro. Estude o que veio antes para ver claramente o que vem a seguir.",
     "es": "El pasado ilumina el futuro. Estudia lo que vino antes para ver claramente lo que viene despu\u00e9s."},  # 313
    {"en": "Enjoy the present in ways that do not poison the future. Pleasure has its costs.",
     "pt": "Desfrute do presente de maneiras que n\u00e3o envenenem o futuro. O prazer tem seus custos.",
     "es": "Disfruta el presente de maneras que no envenenen el futuro. El placer tiene sus costos."},  # 314
]

result = {}
for i, key in enumerate(keys):
    if i < len(reflections):
        result[key] = reflections[i]

with open('c:/Users/lalli/Flutter/coach_phrase_app/reflections_stoicism.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f'Generated {len(result)} stoicism reflections')
