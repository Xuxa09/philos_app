// === Moods Data ===

import '../models/quote_model.dart';

abstract class MoodsData {
  // === All Quotes by Mood ===
  static Map<String, List<QuoteModel>> get moods => {
        'unmotivated': _unmotivatedQuotes,
        'anxious': _anxiousQuotes,
        'frustrated': _frustratedQuotes,
        'fearful': _fearfulQuotes,
        'lost': _lostQuotes,
        'grateful': _gratefulQuotes,
        'ambitious': _ambitiousQuotes,
        'tired': _tiredQuotes,
      };

  // === Unmotivated ===
  static final List<QuoteModel> _unmotivatedQuotes = [
    const QuoteModel(
      id: 'mood_unmotivated_1',
      authorEn: 'Les Brown', authorPt: 'Les Brown', authorEs: 'Les Brown',
      textEn: 'You don\'t have to be great to get started, but you have to get started to be great.',
      textPt: 'Voc\u00EA n\u00E3o precisa ser \u00F3timo para come\u00E7ar, mas precisa come\u00E7ar para ser \u00F3timo.',
      textEs: 'No tienes que ser genial para empezar, pero tienes que empezar para ser genial.',
      reflectionEn: 'The hardest part is starting. Take one small action right now.',
      reflectionPt: 'A parte mais dif\u00EDcil \u00E9 come\u00E7ar. Tome uma pequena a\u00E7\u00E3o agora.',
      reflectionEs: 'La parte m\u00E1s dif\u00EDcil es empezar. Toma una peque\u00F1a acci\u00F3n ahora.',
      category: 'pragmatism',
    ),
    const QuoteModel(
      id: 'mood_unmotivated_2',
      authorEn: 'Tony Robbins', authorPt: 'Tony Robbins', authorEs: 'Tony Robbins',
      textEn: 'The secret of getting ahead is getting started.',
      textPt: 'O segredo de progredir \u00E9 come\u00E7ar.',
      textEs: 'El secreto de avanzar es empezar.',
      reflectionEn: 'Progress requires motion. Even a tiny step forward breaks the cycle of inaction.',
      reflectionPt: 'Progresso requer movimento. At\u00E9 um passo min\u00FAsculo quebra o ciclo de ina\u00E7\u00E3o.',
      reflectionEs: 'El progreso requiere movimiento. Incluso un paso min\u00FAsculo rompe el ciclo de inacci\u00F3n.',
      category: 'pragmatism',
    ),
  ];

  // === Anxious ===
  static final List<QuoteModel> _anxiousQuotes = [
    const QuoteModel(
      id: 'mood_anxious_1',
      authorEn: 'Marcus Aurelius', authorPt: 'Marco Aur\u00E9lio', authorEs: 'Marco Aurelio',
      textEn: 'You have power over your mind \u2014 not outside events. Realize this, and you will find strength.',
      textPt: 'Voc\u00EA tem poder sobre sua mente \u2014 n\u00E3o sobre eventos externos. Perceba isso e encontrar\u00E1 for\u00E7a.',
      textEs: 'Tienes poder sobre tu mente \u2014 no sobre los eventos externos. Date cuenta de esto y encontrar\u00E1s fuerza.',
      reflectionEn: 'Anxiety often comes from trying to control the uncontrollable. Focus on what\'s within your power.',
      reflectionPt: 'A ansiedade muitas vezes vem de tentar controlar o incontrol\u00E1vel. Foque no que est\u00E1 ao seu alcance.',
      reflectionEs: 'La ansiedad a menudo viene de intentar controlar lo incontrolable. Enf\u00F3cate en lo que est\u00E1 a tu alcance.',
      category: 'stoicism',
    ),
    const QuoteModel(
      id: 'mood_anxious_2',
      authorEn: 'Eckhart Tolle', authorPt: 'Eckhart Tolle', authorEs: 'Eckhart Tolle',
      textEn: 'Realize deeply that the present moment is all you have. Make the Now the primary focus of your life.',
      textPt: 'Perceba profundamente que o momento presente \u00E9 tudo que voc\u00EA tem. Fa\u00E7a do Agora o foco principal da sua vida.',
      textEs: 'Date cuenta profundamente de que el momento presente es todo lo que tienes. Haz del Ahora el foco principal de tu vida.',
      reflectionEn: 'Anxiety lives in the future. Bring your attention back to this moment \u2014 it\'s all that truly exists.',
      reflectionPt: 'A ansiedade vive no futuro. Traga sua aten\u00E7\u00E3o de volta para este momento \u2014 \u00E9 tudo que realmente existe.',
      reflectionEs: 'La ansiedad vive en el futuro. Trae tu atenci\u00F3n de vuelta a este momento \u2014 es todo lo que realmente existe.',
      category: 'eastern',
    ),
  ];

  // === Frustrated ===
  static final List<QuoteModel> _frustratedQuotes = [
    const QuoteModel(
      id: 'mood_frustrated_1',
      authorEn: 'Thomas Edison', authorPt: 'Thomas Edison', authorEs: 'Thomas Edison',
      textEn: 'I have not failed. I\'ve just found 10,000 ways that won\'t work.',
      textPt: 'Eu n\u00E3o falhei. Apenas encontrei 10.000 maneiras que n\u00E3o funcionam.',
      textEs: 'No he fracasado. He encontrado 10.000 formas que no funcionan.',
      reflectionEn: 'Frustration is a sign you\'re pushing boundaries. Reframe it as progress.',
      reflectionPt: 'A frustra\u00E7\u00E3o \u00E9 sinal de que est\u00E1 ultrapassando limites. Reinterprete como progresso.',
      reflectionEs: 'La frustraci\u00F3n es se\u00F1al de que est\u00E1s superando l\u00EDmites. Reinterpr\u00E9tala como progreso.',
      category: 'pragmatism',
    ),
  ];

  // === Fearful ===
  static final List<QuoteModel> _fearfulQuotes = [
    const QuoteModel(
      id: 'mood_fearful_1',
      authorEn: 'Nelson Mandela', authorPt: 'Nelson Mandela', authorEs: 'Nelson Mandela',
      textEn: 'I learned that courage was not the absence of fear, but the triumph over it.',
      textPt: 'Aprendi que a coragem n\u00E3o \u00E9 a aus\u00EAncia do medo, mas o triunfo sobre ele.',
      textEs: 'Aprend\u00ED que el coraje no es la ausencia del miedo, sino el triunfo sobre \u00E9l.',
      reflectionEn: 'Fear is natural. Courage is acting despite the fear. You are braver than you think.',
      reflectionPt: 'O medo \u00E9 natural. A coragem \u00E9 agir apesar do medo. Voc\u00EA \u00E9 mais corajoso do que pensa.',
      reflectionEs: 'El miedo es natural. El coraje es actuar a pesar del miedo. Eres m\u00E1s valiente de lo que crees.',
      category: 'stoicism',
    ),
  ];

  // === Lost ===
  static final List<QuoteModel> _lostQuotes = [
    const QuoteModel(
      id: 'mood_lost_1',
      authorEn: 'Steve Jobs', authorPt: 'Steve Jobs', authorEs: 'Steve Jobs',
      textEn: 'You can\'t connect the dots looking forward; you can only connect them looking backwards.',
      textPt: 'Voc\u00EA n\u00E3o pode conectar os pontos olhando para frente; s\u00F3 pode conect\u00E1-los olhando para tr\u00E1s.',
      textEs: 'No puedes conectar los puntos mirando hacia adelante; solo puedes conectarlos mirando hacia atr\u00E1s.',
      reflectionEn: 'Trust that every experience is preparing you for something greater. The path will make sense in time.',
      reflectionPt: 'Confie que cada experi\u00EAncia est\u00E1 te preparando para algo maior. O caminho far\u00E1 sentido com o tempo.',
      reflectionEs: 'Conf\u00EDa en que cada experiencia te est\u00E1 preparando para algo m\u00E1s grande. El camino tendr\u00E1 sentido con el tiempo.',
      category: 'existentialism',
    ),
  ];

  // === Grateful ===
  static final List<QuoteModel> _gratefulQuotes = [
    const QuoteModel(
      id: 'mood_grateful_1',
      authorEn: 'Oprah Winfrey', authorPt: 'Oprah Winfrey', authorEs: 'Oprah Winfrey',
      textEn: 'Be thankful for what you have; you\'ll end up having more.',
      textPt: 'Seja grato pelo que tem; voc\u00EA acabar\u00E1 tendo mais.',
      textEs: 'Agradece lo que tienes; terminar\u00E1s teniendo m\u00E1s.',
      reflectionEn: 'Gratitude attracts abundance. The more thankful you are, the more you receive.',
      reflectionPt: 'A gratid\u00E3o atrai abund\u00E2ncia. Quanto mais grato, mais voc\u00EA recebe.',
      reflectionEs: 'La gratitud atrae abundancia. Cuanto m\u00E1s agradecido est\u00E9s, m\u00E1s recibes.',
      category: 'epicureanism',
    ),
  ];

  // === Ambitious ===
  static final List<QuoteModel> _ambitiousQuotes = [
    const QuoteModel(
      id: 'mood_ambitious_1',
      authorEn: 'Elon Musk', authorPt: 'Elon Musk', authorEs: 'Elon Musk',
      textEn: 'When something is important enough, you do it even if the odds are not in your favor.',
      textPt: 'Quando algo \u00E9 importante o suficiente, voc\u00EA faz mesmo que as probabilidades n\u00E3o estejam a seu favor.',
      textEs: 'Cuando algo es lo suficientemente importante, lo haces aunque las probabilidades no est\u00E9n a tu favor.',
      reflectionEn: 'Ambition fueled by purpose is unstoppable. Let your vision drive you beyond limitations.',
      reflectionPt: 'Ambi\u00E7\u00E3o alimentada por prop\u00F3sito \u00E9 impar\u00E1vel. Deixe sua vis\u00E3o te levar al\u00E9m das limita\u00E7\u00F5es.',
      reflectionEs: 'La ambici\u00F3n alimentada por el prop\u00F3sito es imparable. Deja que tu visi\u00F3n te lleve m\u00E1s all\u00E1 de las limitaciones.',
      category: 'classical',
    ),
  ];

  // === Tired ===
  static final List<QuoteModel> _tiredQuotes = [
    const QuoteModel(
      id: 'mood_tired_1',
      authorEn: 'Vince Lombardi', authorPt: 'Vince Lombardi', authorEs: 'Vince Lombardi',
      textEn: 'It\'s not whether you get knocked down, it\'s whether you get up.',
      textPt: 'N\u00E3o \u00E9 se voc\u00EA cai, mas se voc\u00EA se levanta.',
      textEs: 'No importa si caes, sino si te levantas.',
      reflectionEn: 'Rest if you must, but never quit. Your strength is greater than your fatigue.',
      reflectionPt: 'Descanse se precisar, mas nunca desista. Sua for\u00E7a \u00E9 maior que seu cansa\u00E7o.',
      reflectionEs: 'Descansa si es necesario, pero nunca te rindas. Tu fuerza es mayor que tu cansancio.',
      category: 'stoicism',
    ),
  ];
}
