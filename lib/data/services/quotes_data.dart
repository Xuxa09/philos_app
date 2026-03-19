// === Quotes Data ===

import '../models/quote_model.dart';

abstract class QuotesData {
  // === Stoicism — Marcus Aurelius, Seneca, Epictetus ===
  static const List<QuoteModel> stoicism = [
    QuoteModel(
      id: 'q001',
      authorEn: 'Marcus Aurelius', authorPt: 'Marco Aur\u00E9lio', authorEs: 'Marco Aurelio',
      textEn: 'The happiness of your life depends upon the quality of your thoughts.',
      textPt: 'A felicidade da sua vida depende da qualidade dos seus pensamentos.',
      textEs: 'La felicidad de tu vida depende de la calidad de tus pensamientos.',
      reflectionEn: 'Guard your mind carefully. Your thoughts are the seeds from which your entire life grows.',
      reflectionPt: 'Guarde sua mente com cuidado. Seus pensamentos s\u00E3o as sementes das quais toda a sua vida cresce.',
      reflectionEs: 'Cuida tu mente con esmero. Tus pensamientos son las semillas de las que crece toda tu vida.',
      category: 'stoicism',
    ),
    QuoteModel(
      id: 'q002',
      authorEn: 'Seneca', authorPt: 'S\u00EAneca', authorEs: 'S\u00E9neca',
      textEn: 'It is not that we have a short time to live, but that we waste a great deal of it.',
      textPt: 'N\u00E3o \u00E9 que tenhamos pouco tempo de vida, mas \u00E9 que desperdi\u00E7amos muito dele.',
      textEs: 'No es que tengamos poco tiempo de vida, sino que desperdiciamos mucho de \u00E9l.',
      reflectionEn: 'Time is your most precious resource. Are you spending it on what truly matters, or letting it slip away?',
      reflectionPt: 'O tempo \u00E9 seu recurso mais precioso. Voc\u00EA est\u00E1 gastando-o com o que realmente importa ou deixando-o escapar?',
      reflectionEs: '\u00BFEst\u00E1s gastando tu tiempo en lo que realmente importa o dej\u00E1ndolo escapar? El tiempo es tu recurso m\u00E1s preciado.',
      category: 'stoicism',
    ),
    QuoteModel(
      id: 'q003',
      authorEn: 'Epictetus', authorPt: 'Epicteto', authorEs: 'Epicteto',
      textEn: 'It is not what happens to you, but how you react to it that matters.',
      textPt: 'N\u00E3o \u00E9 o que acontece com voc\u00EA, mas como voc\u00EA reage que importa.',
      textEs: 'No es lo que te sucede, sino c\u00F3mo reaccionas lo que importa.',
      reflectionEn: 'You cannot control events, but you can always control your response. Your reaction defines your reality.',
      reflectionPt: 'Voc\u00EA n\u00E3o pode controlar os eventos, mas pode sempre controlar sua resposta. Sua rea\u00E7\u00E3o define sua realidade.',
      reflectionEs: 'No puedes controlar los eventos, pero siempre puedes controlar tu respuesta. Tu reacci\u00F3n define tu realidad.',
      category: 'stoicism',
    ),
  ];

  // === Classical Greek — Socrates, Plato, Aristotle ===
  static const List<QuoteModel> classical = [
    QuoteModel(
      id: 'q004',
      authorEn: 'Socrates', authorPt: 'S\u00F3crates', authorEs: 'S\u00F3crates',
      textEn: 'The unexamined life is not worth living.',
      textPt: 'Uma vida n\u00E3o examinada n\u00E3o vale a pena ser vivida.',
      textEs: 'Una vida no examinada no vale la pena ser vivida.',
      reflectionEn: 'Self-awareness is the foundation of wisdom. Take time to reflect on your beliefs, actions, and the direction of your life.',
      reflectionPt: 'O autoconhecimento \u00E9 a base da sabedoria. Reserve tempo para refletir sobre suas cren\u00E7as, a\u00E7\u00F5es e a dire\u00E7\u00E3o da sua vida.',
      reflectionEs: 'El autoconocimiento es la base de la sabidur\u00EDa. Toma tiempo para reflexionar sobre tus creencias, acciones y la direcci\u00F3n de tu vida.',
      category: 'classical',
    ),
    QuoteModel(
      id: 'q005',
      authorEn: 'Plato', authorPt: 'Plat\u00E3o', authorEs: 'Plat\u00F3n',
      textEn: 'Be kind, for everyone you meet is fighting a hard battle.',
      textPt: 'Seja gentil, pois cada pessoa que voc\u00EA encontra est\u00E1 travando uma batalha dif\u00EDcil.',
      textEs: 'S\u00E9 amable, porque cada persona que encuentras est\u00E1 librando una batalla dif\u00EDcil.',
      reflectionEn: 'Compassion is the highest form of intelligence. Behind every face is a story of struggle you may never know.',
      reflectionPt: 'A compaix\u00E3o \u00E9 a forma mais elevada de intelig\u00EAncia. Por tr\u00E1s de cada rosto h\u00E1 uma hist\u00F3ria de luta que voc\u00EA talvez nunca conhe\u00E7a.',
      reflectionEs: 'La compasi\u00F3n es la forma m\u00E1s elevada de inteligencia. Detr\u00E1s de cada rostro hay una historia de lucha que quiz\u00E1s nunca conozcas.',
      category: 'classical',
    ),
    QuoteModel(
      id: 'q006',
      authorEn: 'Aristotle', authorPt: 'Arist\u00F3teles', authorEs: 'Arist\u00F3teles',
      textEn: 'We are what we repeatedly do. Excellence, then, is not an act, but a habit.',
      textPt: 'N\u00F3s somos aquilo que fazemos repetidamente. A excel\u00EAncia, portanto, n\u00E3o \u00E9 um ato, mas um h\u00E1bito.',
      textEs: 'Somos lo que hacemos repetidamente. La excelencia, entonces, no es un acto, sino un h\u00E1bito.',
      reflectionEn: 'Your daily habits define who you become. Focus on building routines that align with the person you want to be.',
      reflectionPt: 'Seus h\u00E1bitos di\u00E1rios definem quem voc\u00EA se torna. Foque em construir rotinas alinhadas com a pessoa que deseja ser.',
      reflectionEs: 'Tus h\u00E1bitos diarios definen en qui\u00E9n te conviertes. Enf\u00F3cate en construir rutinas alineadas con la persona que quieres ser.',
      category: 'classical',
    ),
  ];

  // === Existentialism — Nietzsche, Kierkegaard, Sartre ===
  static const List<QuoteModel> existentialism = [
    QuoteModel(
      id: 'q007',
      authorEn: 'Friedrich Nietzsche', authorPt: 'Friedrich Nietzsche', authorEs: 'Friedrich Nietzsche',
      textEn: 'He who has a why to live can bear almost any how.',
      textPt: 'Quem tem um porqu\u00EA para viver pode suportar quase qualquer como.',
      textEs: 'Quien tiene un porqu\u00E9 para vivir puede soportar casi cualquier c\u00F3mo.',
      reflectionEn: 'Purpose is the ultimate source of resilience. When you know why you endure, no obstacle is too great.',
      reflectionPt: 'O prop\u00F3sito \u00E9 a fonte suprema de resili\u00EAncia. Quando voc\u00EA sabe por que persevera, nenhum obst\u00E1culo \u00E9 grande demais.',
      reflectionEs: 'El prop\u00F3sito es la fuente suprema de resiliencia. Cuando sabes por qu\u00E9 perseveras, ning\u00FAn obst\u00E1culo es demasiado grande.',
      category: 'existentialism',
    ),
    QuoteModel(
      id: 'q008',
      authorEn: 'S\u00F8ren Kierkegaard', authorPt: 'S\u00F8ren Kierkegaard', authorEs: 'S\u00F8ren Kierkegaard',
      textEn: 'Life can only be understood backwards; but it must be lived forwards.',
      textPt: 'A vida s\u00F3 pode ser compreendida olhando para tr\u00E1s; mas s\u00F3 pode ser vivida olhando para frente.',
      textEs: 'La vida solo puede ser comprendida mirando hacia atr\u00E1s; pero solo puede ser vivida mirando hacia adelante.',
      reflectionEn: 'Do not wait for clarity before you act. Live boldly now and trust that the meaning will reveal itself in time.',
      reflectionPt: 'N\u00E3o espere clareza antes de agir. Viva com ousadia agora e confie que o sentido se revelar\u00E1 com o tempo.',
      reflectionEs: 'No esperes claridad antes de actuar. Vive con audacia ahora y conf\u00EDa en que el sentido se revelar\u00E1 con el tiempo.',
      category: 'existentialism',
    ),
    QuoteModel(
      id: 'q009',
      authorEn: 'Jean-Paul Sartre', authorPt: 'Jean-Paul Sartre', authorEs: 'Jean-Paul Sartre',
      textEn: 'Man is condemned to be free; because once thrown into the world, he is responsible for everything he does.',
      textPt: 'O homem est\u00E1 condenado a ser livre; porque uma vez lan\u00E7ado ao mundo, \u00E9 respons\u00E1vel por tudo o que faz.',
      textEs: 'El hombre est\u00E1 condenado a ser libre; porque una vez arrojado al mundo, es responsable de todo lo que hace.',
      reflectionEn: 'Freedom and responsibility are inseparable. Every choice you make shapes who you are becoming.',
      reflectionPt: 'Liberdade e responsabilidade s\u00E3o insepar\u00E1veis. Cada escolha que voc\u00EA faz molda quem voc\u00EA est\u00E1 se tornando.',
      reflectionEs: 'Libertad y responsabilidad son inseparables. Cada elecci\u00F3n que tomas moldea en qui\u00E9n te est\u00E1s convirtiendo.',
      category: 'existentialism',
    ),
  ];

  // === Eastern Philosophy — Confucius, Lao Tzu, Buddha ===
  static const List<QuoteModel> eastern = [
    QuoteModel(
      id: 'q010',
      authorEn: 'Confucius', authorPt: 'Conf\u00FAcio', authorEs: 'Confucio',
      textEn: 'It does not matter how slowly you go as long as you do not stop.',
      textPt: 'N\u00E3o importa o qu\u00E3o devagar voc\u00EA v\u00E1, contanto que n\u00E3o pare.',
      textEs: 'No importa lo lento que vayas, siempre y cuando no te detengas.',
      reflectionEn: 'Progress, no matter how small, is still progress. Keep moving forward and trust the process.',
      reflectionPt: 'Progresso, por menor que seja, ainda \u00E9 progresso. Continue avan\u00E7ando e confie no processo.',
      reflectionEs: 'El progreso, por peque\u00F1o que sea, sigue siendo progreso. Sigue avanzando y conf\u00EDa en el proceso.',
      category: 'eastern',
    ),
    QuoteModel(
      id: 'q011',
      authorEn: 'Lao Tzu', authorPt: 'Lao Tzu', authorEs: 'Lao Tzu',
      textEn: 'A journey of a thousand miles begins with a single step.',
      textPt: 'Uma jornada de mil milhas come\u00E7a com um \u00FAnico passo.',
      textEs: 'Un viaje de mil millas comienza con un solo paso.',
      reflectionEn: 'Do not be paralyzed by the magnitude of your dreams. The most important thing is to start.',
      reflectionPt: 'N\u00E3o se paralise pela grandeza dos seus sonhos. O mais importante \u00E9 come\u00E7ar.',
      reflectionEs: 'No te paralices por la magnitud de tus sue\u00F1os. Lo m\u00E1s importante es empezar.',
      category: 'eastern',
    ),
    QuoteModel(
      id: 'q012',
      authorEn: 'Buddha', authorPt: 'Buda', authorEs: 'Buda',
      textEn: 'What you think, you become. What you feel, you attract. What you imagine, you create.',
      textPt: 'O que voc\u00EA pensa, voc\u00EA se torna. O que voc\u00EA sente, voc\u00EA atrai. O que voc\u00EA imagina, voc\u00EA cria.',
      textEs: 'Lo que piensas, te conviertes. Lo que sientes, atraes. Lo que imaginas, creas.',
      reflectionEn: 'Your thoughts, emotions, and imagination are powerful forces. Align them with what you truly desire.',
      reflectionPt: 'Seus pensamentos, emo\u00E7\u00F5es e imagina\u00E7\u00E3o s\u00E3o for\u00E7as poderosas. Alinhe-os com o que voc\u00EA realmente deseja.',
      reflectionEs: 'Tus pensamientos, emociones e imaginaci\u00F3n son fuerzas poderosas. Al\u00EDnealos con lo que realmente deseas.',
      category: 'eastern',
    ),
  ];

  // === Epicureanism — Epicurus, Lucretius, Horace ===
  static const List<QuoteModel> epicureanism = [
    QuoteModel(
      id: 'q013',
      authorEn: 'Epicurus', authorPt: 'Epicuro', authorEs: 'Epicuro',
      textEn: 'Do not spoil what you have by desiring what you have not; remember that what you now have was once among the things you only hoped for.',
      textPt: 'N\u00E3o estrague o que voc\u00EA tem desejando o que n\u00E3o tem; lembre-se de que o que voc\u00EA agora tem j\u00E1 foi algo que voc\u00EA apenas esperava.',
      textEs: 'No arruines lo que tienes deseando lo que no tienes; recuerda que lo que ahora tienes fue una vez algo que solo esperabas.',
      reflectionEn: 'Gratitude is the art of appreciating the present. Look around \u2014 many of your past dreams are now your reality.',
      reflectionPt: 'A gratid\u00E3o \u00E9 a arte de apreciar o presente. Olhe ao redor \u2014 muitos dos seus sonhos passados agora s\u00E3o sua realidade.',
      reflectionEs: 'La gratitud es el arte de apreciar el presente. Mira a tu alrededor \u2014 muchos de tus sue\u00F1os pasados ahora son tu realidad.',
      category: 'epicureanism',
    ),
    QuoteModel(
      id: 'q014',
      authorEn: 'Lucretius', authorPt: 'Lucr\u00E9cio', authorEs: 'Lucrecio',
      textEn: 'The drops of rain make a hole in the stone, not by violence, but by oft falling.',
      textPt: 'As gotas de chuva fazem um buraco na pedra, n\u00E3o pela viol\u00EAncia, mas por ca\u00EDrem repetidamente.',
      textEs: 'Las gotas de lluvia hacen un agujero en la piedra, no por la violencia, sino por caer repetidamente.',
      reflectionEn: 'Persistence overcomes all obstacles. Small, consistent efforts achieve what brute force cannot.',
      reflectionPt: 'A persist\u00EAncia supera todos os obst\u00E1culos. Pequenos esfor\u00E7os consistentes alcan\u00E7am o que a for\u00E7a bruta n\u00E3o consegue.',
      reflectionEs: 'La persistencia supera todos los obst\u00E1culos. Peque\u00F1os esfuerzos consistentes logran lo que la fuerza bruta no puede.',
      category: 'epicureanism',
    ),
    QuoteModel(
      id: 'q015',
      authorEn: 'Horace', authorPt: 'Hor\u00E1cio', authorEs: 'Horacio',
      textEn: 'Seize the day, put very little trust in tomorrow.',
      textPt: 'Aproveite o dia, confie muito pouco no amanh\u00E3.',
      textEs: 'Aprovecha el d\u00EDa, conf\u00EDa muy poco en el ma\u00F1ana.',
      reflectionEn: 'The present moment is all we truly have. Live fully today instead of postponing your life for an uncertain tomorrow.',
      reflectionPt: 'O momento presente \u00E9 tudo que realmente temos. Viva plenamente hoje ao inv\u00E9s de adiar sua vida para um amanh\u00E3 incerto.',
      reflectionEs: 'El momento presente es todo lo que realmente tenemos. Vive plenamente hoy en lugar de posponer tu vida para un ma\u00F1ana incierto.',
      category: 'epicureanism',
    ),
  ];

  // === Rationalism — Descartes, Spinoza, Leibniz ===
  static const List<QuoteModel> rationalism = [
    QuoteModel(
      id: 'q016',
      authorEn: 'Ren\u00E9 Descartes', authorPt: 'Ren\u00E9 Descartes', authorEs: 'Ren\u00E9 Descartes',
      textEn: 'I think, therefore I am.',
      textPt: 'Penso, logo existo.',
      textEs: 'Pienso, luego existo.',
      reflectionEn: 'Your capacity to think is the proof of your existence. Use this gift wisely \u2014 question everything and never stop seeking truth.',
      reflectionPt: 'Sua capacidade de pensar \u00E9 a prova da sua exist\u00EAncia. Use esse dom com sabedoria \u2014 questione tudo e nunca pare de buscar a verdade.',
      reflectionEs: 'Tu capacidad de pensar es la prueba de tu existencia. Usa este don con sabidur\u00EDa \u2014 cuestiona todo y nunca dejes de buscar la verdad.',
      category: 'rationalism',
    ),
    QuoteModel(
      id: 'q017',
      authorEn: 'Baruch Spinoza', authorPt: 'Baruch Spinoza', authorEs: 'Baruch Spinoza',
      textEn: 'Peace is not the absence of war, it is a virtue, a state of mind, a disposition for benevolence, confidence, justice.',
      textPt: 'A paz n\u00E3o \u00E9 a aus\u00EAncia de guerra, \u00E9 uma virtude, um estado de esp\u00EDrito, uma disposi\u00E7\u00E3o para a benevol\u00EAncia, confian\u00E7a, justi\u00E7a.',
      textEs: 'La paz no es la ausencia de guerra, es una virtud, un estado mental, una disposici\u00F3n para la benevolencia, confianza, justicia.',
      reflectionEn: 'True peace is not the absence of conflict but an inner state you cultivate through virtue and understanding.',
      reflectionPt: 'A verdadeira paz n\u00E3o \u00E9 a aus\u00EAncia de conflito, mas um estado interior que voc\u00EA cultiva atrav\u00E9s da virtude e compreens\u00E3o.',
      reflectionEs: 'La verdadera paz no es la ausencia de conflicto, sino un estado interior que cultivas a trav\u00E9s de la virtud y la comprensi\u00F3n.',
      category: 'rationalism',
    ),
    QuoteModel(
      id: 'q018',
      authorEn: 'Gottfried Leibniz', authorPt: 'Gottfried Leibniz', authorEs: 'Gottfried Leibniz',
      textEn: 'He who understands everything about himself and his surroundings has found the key to happiness.',
      textPt: 'Quem compreende tudo sobre si mesmo e sobre o que o cerca encontrou a chave da felicidade.',
      textEs: 'Quien comprende todo sobre s\u00ED mismo y su entorno ha encontrado la clave de la felicidad.',
      reflectionEn: 'Self-knowledge and awareness of the world around you are the foundations of a fulfilling life.',
      reflectionPt: 'O autoconhecimento e a consci\u00EAncia do mundo ao seu redor s\u00E3o os pilares de uma vida plena.',
      reflectionEs: 'El autoconocimiento y la conciencia del mundo que te rodea son los pilares de una vida plena.',
      category: 'rationalism',
    ),
  ];

  // === Absurdism — Camus, Kafka, Cioran ===
  static const List<QuoteModel> absurdism = [
    QuoteModel(
      id: 'q019',
      authorEn: 'Albert Camus', authorPt: 'Albert Camus', authorEs: 'Albert Camus',
      textEn: 'In the midst of winter, I found there was, within me, an invincible summer.',
      textPt: 'No meio do inverno, descobri que havia, dentro de mim, um ver\u00E3o invenc\u00EDvel.',
      textEs: 'En medio del invierno, descubr\u00ED que hab\u00EDa, dentro de m\u00ED, un verano invencible.',
      reflectionEn: 'Even in your darkest moments, there is an inner strength that cannot be extinguished. Trust in your own resilience.',
      reflectionPt: 'Mesmo nos seus momentos mais sombrios, h\u00E1 uma for\u00E7a interior que n\u00E3o pode ser extinta. Confie na sua pr\u00F3pria resili\u00EAncia.',
      reflectionEs: 'Incluso en tus momentos m\u00E1s oscuros, hay una fuerza interior que no puede extinguirse. Conf\u00EDa en tu propia resiliencia.',
      category: 'absurdism',
    ),
    QuoteModel(
      id: 'q020',
      authorEn: 'Franz Kafka', authorPt: 'Franz Kafka', authorEs: 'Franz Kafka',
      textEn: 'Paths are made by walking.',
      textPt: 'Os caminhos se fazem ao caminhar.',
      textEs: 'Los caminos se hacen al andar.',
      reflectionEn: 'There is no predefined path waiting for you. Your journey is created step by step through your own choices and actions.',
      reflectionPt: 'N\u00E3o existe um caminho predefinido esperando por voc\u00EA. Sua jornada \u00E9 criada passo a passo pelas suas pr\u00F3prias escolhas e a\u00E7\u00F5es.',
      reflectionEs: 'No existe un camino predefinido esper\u00E1ndote. Tu viaje se crea paso a paso a trav\u00E9s de tus propias elecciones y acciones.',
      category: 'absurdism',
    ),
    QuoteModel(
      id: 'q021',
      authorEn: 'Emil Cioran', authorPt: 'Emil Cioran', authorEs: 'Emil Cioran',
      textEn: 'Only those who have the capacity to suffer greatly can know happiness in all its fullness.',
      textPt: 'Somente aqueles que t\u00EAm a capacidade de sofrer imensamente podem conhecer a felicidade em toda a sua plenitude.',
      textEs: 'Solo aquellos que tienen la capacidad de sufrir inmensamente pueden conocer la felicidad en toda su plenitud.',
      reflectionEn: 'Pain and joy are two sides of the same coin. Embrace all of life\u2019s experiences \u2014 they deepen your capacity to feel alive.',
      reflectionPt: 'A dor e a alegria s\u00E3o dois lados da mesma moeda. Abrace todas as experi\u00EAncias da vida \u2014 elas aprofundam sua capacidade de se sentir vivo.',
      reflectionEs: 'El dolor y la alegr\u00EDa son dos caras de la misma moneda. Abraza todas las experiencias de la vida \u2014 profundizan tu capacidad de sentirte vivo.',
      category: 'absurdism',
    ),
  ];

  // === Pragmatism — William James, John Dewey, Emerson ===
  static const List<QuoteModel> pragmatism = [
    QuoteModel(
      id: 'q022',
      authorEn: 'William James', authorPt: 'William James', authorEs: 'William James',
      textEn: 'Act as if what you do makes a difference. It does.',
      textPt: 'Aja como se o que voc\u00EA faz fizesse diferen\u00E7a. Faz.',
      textEs: 'Act\u00FAa como si lo que haces marcara la diferencia. La marca.',
      reflectionEn: 'Every action counts. Even the smallest gesture can ripple outward and transform the world around you.',
      reflectionPt: 'Toda a\u00E7\u00E3o conta. At\u00E9 o menor gesto pode se espalhar e transformar o mundo ao seu redor.',
      reflectionEs: 'Toda acci\u00F3n cuenta. Incluso el gesto m\u00E1s peque\u00F1o puede expandirse y transformar el mundo a tu alrededor.',
      category: 'pragmatism',
    ),
    QuoteModel(
      id: 'q023',
      authorEn: 'John Dewey', authorPt: 'John Dewey', authorEs: 'John Dewey',
      textEn: 'Education is not preparation for life; education is life itself.',
      textPt: 'A educa\u00E7\u00E3o n\u00E3o \u00E9 prepara\u00E7\u00E3o para a vida; a educa\u00E7\u00E3o \u00E9 a pr\u00F3pria vida.',
      textEs: 'La educaci\u00F3n no es preparaci\u00F3n para la vida; la educaci\u00F3n es la vida misma.',
      reflectionEn: 'Learning never stops. Every experience, every challenge, every conversation is an opportunity to grow.',
      reflectionPt: 'O aprendizado nunca para. Cada experi\u00EAncia, cada desafio, cada conversa \u00E9 uma oportunidade de crescer.',
      reflectionEs: 'El aprendizaje nunca se detiene. Cada experiencia, cada desaf\u00EDo, cada conversaci\u00F3n es una oportunidad de crecer.',
      category: 'pragmatism',
    ),
    QuoteModel(
      id: 'q024',
      authorEn: 'Ralph Waldo Emerson', authorPt: 'Ralph Waldo Emerson', authorEs: 'Ralph Waldo Emerson',
      textEn: 'What lies behind us and what lies before us are tiny matters compared to what lies within us.',
      textPt: 'O que est\u00E1 atr\u00E1s de n\u00F3s e o que est\u00E1 diante de n\u00F3s s\u00E3o coisas pequenas comparadas ao que est\u00E1 dentro de n\u00F3s.',
      textEs: 'Lo que est\u00E1 detr\u00E1s de nosotros y lo que est\u00E1 ante nosotros son cosas peque\u00F1as comparadas con lo que est\u00E1 dentro de nosotros.',
      reflectionEn: 'Your greatest resource is your inner world. Cultivate your character and your outer circumstances will follow.',
      reflectionPt: 'Seu maior recurso \u00E9 seu mundo interior. Cultive seu car\u00E1ter e suas circunst\u00E2ncias externas seguir\u00E3o.',
      reflectionEs: 'Tu mayor recurso es tu mundo interior. Cultiva tu car\u00E1cter y tus circunstancias externas seguir\u00E1n.',
      category: 'pragmatism',
    ),
  ];
}
