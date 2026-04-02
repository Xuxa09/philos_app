import csv
import json
import random

# === Mapping: escola (CSV) -> app category ===
ESCOLA_TO_CATEGORY = {
    "Estoicismo": "stoicism",
    "Platonismo": "classical",
    "Peripatico / Aristotelismo": "classical",
    "Filosofia Socrtica": "classical",
    "Pr-socrtico": "classical",
    "Cinismo": "classical",
    "Epicurismo": "epicureanism",
    "Epicurismo (influncia)": "epicureanism",
    "Existencialismo": "existentialism",
    "Existencialismo / Absurdismo": "existentialism",
    "Existencialismo Cristo": "existentialism",
    "Existencialismo (influncia) / Absurdo": "existentialism",
    "Existencialismo / Feminismo": "existentialism",
    "Fenomenologia / Existencialismo": "existentialism",
    "Niilismo / Existencialismo (precursor)": "existentialism",
    "Jansenismo / Existencialismo Cristo (precursor)": "existentialism",
    "Teatro do Absurdo": "absurdism",
    "Taoismo": "eastern",
    "Confucionismo": "eastern",
    "Budismo": "eastern",
    "Filosofia Militar Chinesa": "eastern",
    "Sufismo": "eastern",
    "Racionalismo": "rationalism",
    "Idealismo Transcendental": "rationalism",
    "Idealismo Alemo": "rationalism",
    "Filosofia Analtica": "rationalism",
    "Pragmatismo": "pragmatism",
    "Neopragmatismo": "pragmatism",
    "Transcendentalismo": "pragmatism",
}

# Fix keys with accented chars (read from CSV with proper encoding)
_fixed = {}
for k, v in list(ESCOLA_TO_CATEGORY.items()):
    _fixed[k] = v
ESCOLA_TO_CATEGORY = _fixed

# Re-define with proper strings
ESCOLA_TO_CATEGORY = {
    "Estoicismo": "stoicism",
    "Platonismo": "classical",
    "Peripat\u00e9tico / Aristotelismo": "classical",
    "Filosofia Socr\u00e1tica": "classical",
    "Pr\u00e9-socr\u00e1tico": "classical",
    "Cinismo": "classical",
    "Epicurismo": "epicureanism",
    "Epicurismo (influ\u00eancia)": "epicureanism",
    "Existencialismo": "existentialism",
    "Existencialismo / Absurdismo": "existentialism",
    "Existencialismo Crist\u00e3o": "existentialism",
    "Existencialismo (influ\u00eancia) / Absurdo": "existentialism",
    "Existencialismo / Feminismo": "existentialism",
    "Fenomenologia / Existencialismo": "existentialism",
    "Niilismo / Existencialismo (precursor)": "existentialism",
    "Jansenismo / Existencialismo Crist\u00e3o (precursor)": "existentialism",
    "Teatro do Absurdo": "absurdism",
    "Taoismo": "eastern",
    "Confucionismo": "eastern",
    "Budismo": "eastern",
    "Filosofia Militar Chinesa": "eastern",
    "Sufismo": "eastern",
    "Racionalismo": "rationalism",
    "Idealismo Transcendental": "rationalism",
    "Idealismo Alem\u00e3o": "rationalism",
    "Filosofia Anal\u00edtica": "rationalism",
    "Pragmatismo": "pragmatism",
    "Neopragmatismo": "pragmatism",
    "Transcendentalismo": "pragmatism",
}

# === Absurdism translations (EN -> PT, ES) ===
ABSURDISM_TRANSLATIONS = {
    "You're on Earth. There's no cure for that.": {
        "pt": "Voc\u00ea est\u00e1 na Terra. N\u00e3o h\u00e1 cura para isso.",
        "es": "Est\u00e1s en la Tierra. No hay cura para eso.",
    },
    "No, I regret nothing, all I regret is having been born, dying is such a long tiresome business I always found.": {
        "pt": "N\u00e3o, n\u00e3o me arrependo de nada, s\u00f3 me arrependo de ter nascido, morrer \u00e9 um neg\u00f3cio t\u00e3o longo e cansativo, sempre achei.",
        "es": "No, no me arrepiento de nada, solo me arrepiento de haber nacido, morir es un asunto tan largo y tedioso, siempre pens\u00e9.",
    },
    "Try again. Fail again. Fail better.": {
        "pt": "Tente de novo. Fracasse de novo. Fracasse melhor.",
        "es": "Int\u00e9ntalo de nuevo. Fracasa de nuevo. Fracasa mejor.",
    },
    "Why do people always expect authors to answer questions? I am an author because I want to ask questions. If I had answers, I'd be a politician.": {
        "pt": "Por que as pessoas sempre esperam que os autores respondam perguntas? Sou autor porque quero fazer perguntas. Se eu tivesse respostas, seria pol\u00edtico.",
        "es": "\u00bfPor qu\u00e9 la gente siempre espera que los autores respondan preguntas? Soy autor porque quiero hacer preguntas. Si tuviera respuestas, ser\u00eda pol\u00edtico.",
    },
    "Words are the clothes thoughts wear.": {
        "pt": "As palavras s\u00e3o as roupas que os pensamentos vestem.",
        "es": "Las palabras son la ropa que visten los pensamientos.",
    },
    "Realism falls short of reality. It shrinks it, attenuates it, falsifies it; it does not take into account our basic truths and our fundamental obsessions: love, death, astonishment. It presents man in a reduced and estranged perspective. Truth is in our dreams, in the imagination.": {
        "pt": "O realismo fica aqu\u00e9m da realidade. Ele a encolhe, a atenua, a falsifica; n\u00e3o leva em conta nossas verdades b\u00e1sicas e nossas obsess\u00f5es fundamentais: amor, morte, espanto. Apresenta o homem numa perspectiva reduzida e alienada. A verdade est\u00e1 nos nossos sonhos, na imagina\u00e7\u00e3o.",
        "es": "El realismo se queda corto ante la realidad. La encoge, la aten\u00faa, la falsifica; no tiene en cuenta nuestras verdades b\u00e1sicas y nuestras obsesiones fundamentales: amor, muerte, asombro. Presenta al hombre en una perspectiva reducida y enajenada. La verdad est\u00e1 en nuestros sue\u00f1os, en la imaginaci\u00f3n.",
    },
    "If you do not love me I shall not be loved. If I do not love you I shall not love.": {
        "pt": "Se voc\u00ea n\u00e3o me amar, n\u00e3o serei amado. Se eu n\u00e3o te amar, n\u00e3o amarei.",
        "es": "Si no me amas, no ser\u00e9 amado. Si no te amo, no amar\u00e9.",
    },
    "The only sin is the sin of being born": {
        "pt": "O \u00fanico pecado \u00e9 o pecado de ter nascido.",
        "es": "El \u00fanico pecado es el pecado de haber nacido.",
    },
    "One day we were born, one day we shall die, the same day, the same second.": {
        "pt": "Um dia nascemos, um dia morreremos, no mesmo dia, no mesmo segundo.",
        "es": "Un d\u00eda nacimos, un d\u00eda moriremos, el mismo d\u00eda, el mismo segundo.",
    },
    "Ever Tried. Ever Failed. No matter. Try again. Fail again. Fail better.": {
        "pt": "J\u00e1 tentou. J\u00e1 fracassou. N\u00e3o importa. Tente de novo. Fracasse de novo. Fracasse melhor.",
        "es": "Alguna vez lo intentaste. Alguna vez fracasaste. No importa. Int\u00e9ntalo de nuevo. Fracasa de nuevo. Fracasa mejor.",
    },
    "It was long since I had longed for anything and the effect on me was horrible.": {
        "pt": "Fazia muito tempo que eu n\u00e3o desejava nada, e o efeito em mim foi horr\u00edvel.",
        "es": "Hac\u00eda mucho tiempo que no deseaba nada, y el efecto en m\u00ed fue horrible.",
    },
    "Vladimir, be reasonable, you haven't yet tried everything. And I resumed the struggle.": {
        "pt": "Vladimir, seja razo\u00e1vel, voc\u00ea ainda n\u00e3o tentou tudo. E eu retomei a luta.",
        "es": "Vladimir, s\u00e9 razonable, a\u00fan no lo has intentado todo. Y retom\u00e9 la lucha.",
    },
    "The light of memory, or rather the light that memory lends to things, is the palest light of all. I am not quite sure whether I am dreaming or remembering, whether I have lived my life or dreamed it. Just as dreams do, memory makes me profoundly aware of the unreality, the evanescence of the world, a fleeting image in the moving water.": {
        "pt": "A luz da mem\u00f3ria, ou melhor, a luz que a mem\u00f3ria empresta \u00e0s coisas, \u00e9 a mais p\u00e1lida de todas. N\u00e3o tenho certeza se estou sonhando ou lembrando, se vivi minha vida ou a sonhei. Assim como os sonhos, a mem\u00f3ria me torna profundamente consciente da irrealidade, da evanesc\u00eancia do mundo, uma imagem fugaz na \u00e1gua em movimento.",
        "es": "La luz de la memoria, o m\u00e1s bien la luz que la memoria presta a las cosas, es la m\u00e1s p\u00e1lida de todas. No estoy seguro de si estoy so\u00f1ando o recordando, si he vivido mi vida o la he so\u00f1ado. Como los sue\u00f1os, la memoria me hace profundamente consciente de la irrealidad, la evanescencia del mundo, una imagen fugaz en el agua en movimiento.",
    },
    "You can only predict things after they have happened.": {
        "pt": "S\u00f3 se pode prever as coisas depois que elas aconteceram.",
        "es": "Solo se pueden predecir las cosas despu\u00e9s de que han sucedido.",
    },
    "All I know is what the words know, and dead things, and that makes a handsome little sum, with a beginning and a middle and an end, as in the well-built phrase and the long sonata of the dead.": {
        "pt": "Tudo o que sei \u00e9 o que as palavras sabem, e coisas mortas, e isso faz uma bela pequena soma, com um come\u00e7o, um meio e um fim, como na frase bem constru\u00edda e na longa sonata dos mortos.",
        "es": "Todo lo que s\u00e9 es lo que saben las palabras, y las cosas muertas, y eso hace una hermosa peque\u00f1a suma, con un principio, un medio y un final, como en la frase bien construida y la larga sonata de los muertos.",
    },
    "Dying for dark - the darker the worse. Strange.": {
        "pt": "Morrendo pela escurid\u00e3o \u2013 quanto mais escuro, pior. Estranho.",
        "es": "Muriendo por la oscuridad \u2013 cuanto m\u00e1s oscuro, peor. Extra\u00f1o.",
    },
    "Habit is a great deadener.": {
        "pt": "O h\u00e1bito \u00e9 um grande anestesiador.",
        "es": "El h\u00e1bito es un gran anestesiador.",
    },
    "We are all born mad. Some remain so.": {
        "pt": "Todos n\u00f3s nascemos loucos. Alguns permanecem assim.",
        "es": "Todos nacemos locos. Algunos siguen as\u00ed.",
    },
    "There's never an end for the sea.": {
        "pt": "N\u00e3o h\u00e1 nunca um fim para o mar.",
        "es": "Nunca hay un final para el mar.",
    },
    "If you do not love me I shall not be loved If I do not love you I shall not love.": {
        "pt": "Se voc\u00ea n\u00e3o me amar, n\u00e3o serei amado. Se eu n\u00e3o te amar, n\u00e3o amarei.",
        "es": "Si no me amas, no ser\u00e9 amado. Si no te amo, no amar\u00e9.",
    },
    "Words are all we have.": {
        "pt": "Palavras s\u00e3o tudo o que temos.",
        "es": "Las palabras son todo lo que tenemos.",
    },
    "I can't go on. I'll go on.": {
        "pt": "N\u00e3o consigo continuar. Vou continuar.",
        "es": "No puedo seguir. Seguir\u00e9.",
    },
    "Birth was the death of him.": {
        "pt": "O nascimento foi a morte dele.",
        "es": "El nacimiento fue su muerte.",
    },
    "Poets are the sense, philosophers the intelligence of humanity.": {
        "pt": "Os poetas s\u00e3o o sentido, os fil\u00f3sofos a intelig\u00eancia da humanidade.",
        "es": "Los poetas son el sentido, los fil\u00f3sofos la inteligencia de la humanidad.",
    },
    "What do I know of man's destiny? I could tell you more about radishes.": {
        "pt": "O que sei eu do destino do homem? Poderia lhe contar mais sobre rabanetes.",
        "es": "\u00bfQu\u00e9 s\u00e9 yo del destino del hombre? Podr\u00eda contarte m\u00e1s sobre r\u00e1banos.",
    },
    "Ever tried. Ever failed. No matter. Try Again. Fail again. Fail better.": {
        "pt": "J\u00e1 tentou. J\u00e1 fracassou. N\u00e3o importa. Tente de novo. Fracasse de novo. Fracasse melhor.",
        "es": "Alguna vez lo intentaste. Alguna vez fracasaste. No importa. Int\u00e9ntalo de nuevo. Fracasa de nuevo. Fracasa mejor.",
    },
    "A writer never takes a vacation. For a writer life consists of either writing or thinking about writing": {
        "pt": "Um escritor nunca tira f\u00e9rias. Para um escritor, a vida consiste em escrever ou pensar em escrever.",
        "es": "Un escritor nunca se toma vacaciones. Para un escritor, la vida consiste en escribir o pensar en escribir.",
    },
    "The poet cannot invent new words every time, of course. He uses the words of the tribe. But the handling of the word, the accent, a new articulation, renew them.": {
        "pt": "O poeta n\u00e3o pode inventar palavras novas toda vez, \u00e9 claro. Ele usa as palavras da tribo. Mas o manuseio da palavra, o sotaque, uma nova articula\u00e7\u00e3o, as renovam.",
        "es": "El poeta no puede inventar palabras nuevas cada vez, por supuesto. Usa las palabras de la tribu. Pero el manejo de la palabra, el acento, una nueva articulaci\u00f3n, las renuevan.",
    },
    "There are two moments worthwhile in writing, the one when you start and the other when you throw it in the waste-paper basket.": {
        "pt": "H\u00e1 dois momentos que valem a pena na escrita: quando voc\u00ea come\u00e7a e quando joga tudo na cesta de lixo.",
        "es": "Hay dos momentos que valen la pena al escribir: cuando empiezas y cuando lo tiras a la papelera.",
    },
    "I always thought old age would be a writer\u2019s best chance. Whenever I read the late work of Goethe or W. B. Yeats I had the impertinence to identify with it. Now, my memory\u2019s gone, all the old fluency\u2019s disappeared. I don\u2019t write a single sentence without saying to myself, \u2018It\u2019s a lie!\u2019 So I know I was right. It\u2019s the best chance I\u2019ve ever had.": {
        "pt": "Sempre pensei que a velhice seria a melhor chance de um escritor. Sempre que lia a obra tardia de Goethe ou W. B. Yeats, eu tinha a impert\u00eancia de me identificar com ela. Agora, minha mem\u00f3ria se foi, toda a velha flu\u00eancia desapareceu. N\u00e3o escrevo uma \u00fanica frase sem dizer a mim mesmo: \u201c\u00c9 mentira!\u201d Ent\u00e3o sei que eu estava certo. \u00c9 a melhor chance que j\u00e1 tive.",
        "es": "Siempre pens\u00e9 que la vejez ser\u00eda la mejor oportunidad de un escritor. Cada vez que le\u00eda la obra tard\u00eda de Goethe o W. B. Yeats, ten\u00eda la impertinencia de identificarme con ella. Ahora mi memoria se fue, toda la vieja fluidez desapareci\u00f3. No escribo una sola frase sin decirme: \u00ab\u00a1Es mentira!\u00bb As\u00ed que s\u00e9 que ten\u00eda raz\u00f3n. Es la mejor oportunidad que he tenido.",
    },
    "drill one hole after another into [language] until that which lurks behind, be it something or nothing, starts seeping through \u2013 I cannot imagine a higher goal for today\u2019s writer.": {
        "pt": "Perfurar um buraco ap\u00f3s outro na [linguagem] at\u00e9 que aquilo que se esconde por tr\u00e1s, seja algo ou nada, comece a vazar \u2013 n\u00e3o consigo imaginar um objetivo mais elevado para o escritor de hoje.",
        "es": "Perforar un agujero tras otro en el [lenguaje] hasta que lo que acecha detr\u00e1s, sea algo o nada, comience a filtrarse \u2013 no puedo imaginar un objetivo m\u00e1s elevado para el escritor de hoy.",
    },
    "Estragon: You see, you feel worse when I'm with you. I feel better alone, too.Vladmir: Then why do you always come crawling back?Estragon: I don't know.": {
        "pt": "Estragon: Veja, voc\u00ea se sente pior quando estou com voc\u00ea. Eu tamb\u00e9m me sinto melhor sozinho. Vladimir: Ent\u00e3o por que voc\u00ea sempre volta rastejando? Estragon: N\u00e3o sei.",
        "es": "Estrag\u00f3n: Ves, te sientes peor cuando estoy contigo. Yo tambi\u00e9n me siento mejor solo. Vladimir: \u00bfEntonces por qu\u00e9 siempre vuelves arrastr\u00e1ndote? Estrag\u00f3n: No s\u00e9.",
    },
    "Memories are killing. So you must not think of certain things, of those that are dear to you, or rather you must think of them, for if you don\u2019t there is the danger of finding them, in your mind, little by little.": {
        "pt": "As lembran\u00e7as s\u00e3o assassinas. Ent\u00e3o voc\u00ea n\u00e3o deve pensar em certas coisas, naquelas que lhe s\u00e3o queridas, ou melhor, deve pensar nelas, pois se n\u00e3o o fizer, h\u00e1 o perigo de encontr\u00e1-las, em sua mente, pouco a pouco.",
        "es": "Los recuerdos son asesinos. As\u00ed que no debes pensar en ciertas cosas, en las que te son queridas, o m\u00e1s bien debes pensar en ellas, pues si no lo haces, existe el peligro de encontrarlas, en tu mente, poco a poco.",
    },
    "The earth makes a sound as of sighs and the last drops fall from the emptied cloudless sky. A small boy, stretching out his hands and looking up at the blue sky, asked his mother how such a thing was possible. Fuck off, she said.": {
        "pt": "A terra faz um som como de suspiros e as \u00faltimas gotas caem do c\u00e9u vazio e sem nuvens. Um menino, estendendo as m\u00e3os e olhando para o c\u00e9u azul, perguntou \u00e0 m\u00e3e como tal coisa era poss\u00edvel. V\u00e1 se foder, ela disse.",
        "es": "La tierra emite un sonido como de suspiros y las \u00faltimas gotas caen del cielo vac\u00edo y sin nubes. Un ni\u00f1o peque\u00f1o, extendiendo las manos y mirando al cielo azul, le pregunt\u00f3 a su madre c\u00f3mo era posible tal cosa. Vete a la mierda, dijo ella.",
    },
    "Estragon: They're too bigVladimir: Perhaps you'll have socks some day": {
        "pt": "Estragon: S\u00e3o grandes demais. Vladimir: Talvez um dia voc\u00ea tenha meias.",
        "es": "Estrag\u00f3n: Son demasiado grandes. Vladimir: Quiz\u00e1s alg\u00fan d\u00eda tengas calcetines.",
    },
    "When we are reading, a voice comes to us as in the dark and whispers, \"Imagine!\" Samuel Beckettas told by Bill Moyer in the Foreword he wrote for, The Public Library: A Photographic Essay by Robert Dawson. Afterword by Ann Patchett": {
        "pt": "Quando estamos lendo, uma voz chega at\u00e9 n\u00f3s como na escurid\u00e3o e sussurra: \u201cImagine!\u201d",
        "es": "Cuando leemos, una voz llega a nosotros como en la oscuridad y susurra: \u00ab\u00a1Imagina!\u00bb",
    },
    "Poets are the sense, philosophers\u00ad\u00ad the intelligence\u00ad\u00ad of humanity.": {
        "pt": "Os poetas s\u00e3o o sentido, os fil\u00f3sofos a intelig\u00eancia da humanidade.",
        "es": "Los poetas son el sentido, los fil\u00f3sofos la inteligencia de la humanidad.",
    },
    "Estragon: And if he doesn't come?Vladimir: (after a moment of bewilderment) We'll see when the time comes.": {
        "pt": "Estragon: E se ele n\u00e3o vier? Vladimir: (ap\u00f3s um momento de perplexidade) Veremos quando chegar a hora.",
        "es": "Estrag\u00f3n: \u00bfY si no viene? Vladimir: (tras un momento de desconcierto) Ya veremos cuando llegue el momento.",
    },
    "Cascando\"why not merely the despaired ofoccasion ofwordshedis it not better abort than be barrenthe hours after you are gone are so leadenthey will always start dragging too soonthe grapples clawing blindly the bed of wantbringing up the bones the old lovessockets filled once with eyes like yoursall always is it better too soon than neverthe black want splashing their facessaying again nine days never floated the lovednor nine monthsnor nine livessaying againif you do not teach me I shall not learnsaying again there is a lasteven of last timeslast times of begginglast times of lovingof knowing not knowing pretendinga last even of last times of sayingif you do not love me I shall not be lovedif I do not love you I shall not lovethe churn of stale words in the heart againlove love love thud of the old plungerpestling the unalterablewhey of wordsterrified againof not lovingof loving and not youof being loved and not by youof knowing not knowing pretendingpretendingI and all the others that will love youif they love youunless they love you": {
        "pt": "Se voc\u00ea n\u00e3o me ensinar, n\u00e3o aprenderei. Se voc\u00ea n\u00e3o me amar, n\u00e3o serei amado. Se eu n\u00e3o te amar, n\u00e3o amarei.",
        "es": "Si no me ense\u00f1as, no aprender\u00e9. Si no me amas, no ser\u00e9 amado. Si no te amo, no amar\u00e9.",
    },
}


def escape_dart(s):
    """Escape special characters for Dart single-quoted strings, converting non-ASCII to \\uXXXX."""
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


# Load extra translations (epicureanism + rationalism) from JSON
EXTRA_TRANSLATIONS = {}
try:
    with open('c:/Users/lalli/Flutter/coach_phrase_app/translations_extra.json', 'r', encoding='utf-8') as _f:
        EXTRA_TRANSLATIONS = json.load(_f)
except FileNotFoundError:
    pass

# Merge all translation sources
ALL_TRANSLATIONS = {}
ALL_TRANSLATIONS.update(EXTRA_TRANSLATIONS)
ALL_TRANSLATIONS.update(ABSURDISM_TRANSLATIONS)


def get_translation(text, lang):
    """Look up PT/ES translation for any category with translations."""
    tr = ALL_TRANSLATIONS.get(text)
    if tr:
        return tr.get(lang, text)
    return text


def main():
    quotes_by_category = {
        "stoicism": [],
        "classical": [],
        "existentialism": [],
        "eastern": [],
        "epicureanism": [],
        "rationalism": [],
        "absurdism": [],
        "pragmatism": [],
    }

    csv_path = "c:/Users/lalli/Flutter/coach_phrase_app/phrases.csv"

    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        idx = 0
        skipped = 0
        for row in reader:
            escola = row.get("escola", "").strip()
            category = ESCOLA_TO_CATEGORY.get(escola)
            if not category:
                skipped += 1
                continue

            quote_text = row.get("quote", "").strip()
            author = row.get("author", "").strip()

            if not quote_text or not author:
                skipped += 1
                continue

            idx += 1
            quote_id = f"csv_{idx:04d}"

            quotes_by_category[category].append({
                "id": quote_id,
                "author": author,
                "text": quote_text,
                "category": category,
            })

    # Limit categories that are too large
    CATEGORY_LIMITS = {
        "existentialism": 800,
    }
    for cat, limit in CATEGORY_LIMITS.items():
        if len(quotes_by_category[cat]) > limit:
            random.seed(42)
            quotes_by_category[cat] = random.sample(quotes_by_category[cat], limit)

    # Generate Dart file
    lines = []
    lines.append("// === Quotes Data ===")
    lines.append("// Generated from phrases.csv")
    lines.append("")
    lines.append("import '../models/quote_model.dart';")
    lines.append("")
    lines.append("abstract class QuotesData {")

    for category, quotes in quotes_by_category.items():
        lines.append(f"  // === {category.capitalize()} ({len(quotes)} quotes) ===")
        lines.append(f"  static const List<QuoteModel> {category} = [")

        for q in quotes:
            text_en = q["text"]
            author = q["author"]
            cat = q["category"]
            qid = q["id"]

            # Use translations if available; otherwise duplicate EN
            text_pt = get_translation(text_en, "pt")
            text_es = get_translation(text_en, "es")

            lines.append(f"    QuoteModel(")
            lines.append(f"      id: '{qid}',")
            lines.append(f"      authorEn: '{escape_dart(author)}', authorPt: '{escape_dart(author)}', authorEs: '{escape_dart(author)}',")
            lines.append(f"      textEn: '{escape_dart(text_en)}',")
            lines.append(f"      textPt: '{escape_dart(text_pt)}',")
            lines.append(f"      textEs: '{escape_dart(text_es)}',")
            lines.append(f"      reflectionEn: '',")
            lines.append(f"      reflectionPt: '',")
            lines.append(f"      reflectionEs: '',")
            lines.append(f"      category: '{cat}',")
            lines.append(f"    ),")

        lines.append(f"  ];")
        lines.append("")

    lines.append("}")
    lines.append("")

    out_path = "c:/Users/lalli/Flutter/coach_phrase_app/lib/data/services/quotes_data.dart"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # Print summary
    total = sum(len(q) for q in quotes_by_category.values())
    print(f"Generated {total} quotes ({skipped} skipped)")
    for cat, quotes in quotes_by_category.items():
        print(f"  {cat}: {len(quotes)}")

    # Check translation coverage per category
    print("\nTranslation coverage:")
    for cat, quotes in quotes_by_category.items():
        translated = sum(1 for q in quotes if q["text"] in ALL_TRANSLATIONS)
        if translated > 0:
            print(f"  {cat}: {translated}/{len(quotes)}")


if __name__ == "__main__":
    main()
