"""Generate reflections for 189 eastern quotes."""
import json

with open('c:/Users/lalli/Flutter/coach_phrase_app/eastern_keys.json', 'r', encoding='utf-8') as f:
    keys = json.load(f)

# Reusable themes
LOVE = {"en": "Love is both a source of strength and an act of courage. Practice it as both gift and discipline.",
        "pt": "O amor \u00e9 ao mesmo tempo fonte de for\u00e7a e ato de coragem. Pratique-o como presente e disciplina.",
        "es": "El amor es a la vez fuente de fuerza y acto de coraje. Practi\u00edcalo como regalo y disciplina."}

PERSISTENCE = {"en": "Pace matters less than direction. Keep moving toward what matters and the distance closes itself.",
               "pt": "O ritmo importa menos que a dire\u00e7\u00e3o. Continue avan\u00e7ando para o que importa e a dist\u00e2ncia se fecha sozinha.",
               "es": "El ritmo importa menos que la direcci\u00f3n. Sigue avanzando hacia lo que importa y la distancia se cierra sola."}

EMPTINESS = {"en": "What is empty is what makes things useful. Honor the spaces in your life as much as the substance.",
             "pt": "O que est\u00e1 vazio \u00e9 o que torna as coisas \u00fateis. Honre os espa\u00e7os em sua vida tanto quanto a subst\u00e2ncia.",
             "es": "Lo vac\u00edo es lo que hace \u00fatiles las cosas. Honra los espacios en tu vida tanto como la sustancia."}

LET_GO = {"en": "Holding tightly often loses what we want to keep. Release with open hands and see what remains.",
          "pt": "Segurar com for\u00e7a frequentemente perde o que queremos manter. Solte com m\u00e3os abertas e veja o que permanece.",
          "es": "Sostener con fuerza a menudo pierde lo que queremos guardar. Suelta con manos abiertas y mira lo que queda."}

SELF_MASTERY = {"en": "Conquering yourself is harder and more lasting than conquering others. Begin within.",
                "pt": "Conquistar a si mesmo \u00e9 mais dif\u00edcil e mais duradouro do que conquistar os outros. Comece por dentro.",
                "es": "Conquistarse a uno mismo es m\u00e1s dif\u00edcil y duradero que conquistar a otros. Comienza por dentro."}

SIMPLICITY = {"en": "Life is simple when we stop adding to it. Subtract before you add today.",
              "pt": "A vida \u00e9 simples quando paramos de adicionar a ela. Subtraia antes de adicionar hoje.",
              "es": "La vida es simple cuando dejamos de a\u00f1adirle cosas. Resta antes de a\u00f1adir hoy."}

PRESENT = {"en": "The present moment is all you ever truly have. Inhabit it fully before reaching for the next.",
           "pt": "O momento presente \u00e9 tudo que voc\u00ea realmente tem. Habite-o plenamente antes de buscar o pr\u00f3ximo.",
           "es": "El momento presente es todo lo que verdaderamente tienes. Hab\u00edtalo plenamente antes de alcanzar el pr\u00f3ximo."}

KINDNESS = {"en": "Kindness costs little and creates much. Practice it especially with those who do not return it.",
            "pt": "A gentileza custa pouco e cria muito. Pratique-a especialmente com aqueles que n\u00e3o a retribuem.",
            "es": "La amabilidad cuesta poco y crea mucho. Pract\u00edcala especialmente con quienes no la devuelven."}

WISDOM_ACTION = {"en": "True wisdom shows in action, not in words. Let your life teach more than your speech.",
                 "pt": "A verdadeira sabedoria se mostra na a\u00e7\u00e3o, n\u00e3o em palavras. Deixe sua vida ensinar mais que sua fala.",
                 "es": "La verdadera sabidur\u00eda se muestra en la acci\u00f3n, no en palabras. Deja que tu vida ense\u00f1e m\u00e1s que tu discurso."}

ANGER = {"en": "Anger held longer harms you more than its target. Drop the burning coal from your hand.",
         "pt": "A raiva mantida por mais tempo o machuca mais que seu alvo. Solte o carv\u00e3o em brasa da sua m\u00e3o.",
         "es": "La ira sostenida m\u00e1s tiempo te da\u00f1a m\u00e1s que a su blanco. Suelta el carb\u00f3n encendido de tu mano."}

FEAR = {"en": "Fear is largely an illusion built by imagination. Examine what you fear and watch it shrink.",
        "pt": "O medo \u00e9 em grande parte uma ilus\u00e3o constru\u00edda pela imagina\u00e7\u00e3o. Examine o que voc\u00ea teme e veja-o encolher.",
        "es": "El miedo es en gran parte una ilusi\u00f3n construida por la imaginaci\u00f3n. Examina lo que temes y m\u00edralo encogerse."}

WISDOM = {"en": "Wisdom is not stored knowledge but living understanding. Practice it in the smallest decisions.",
          "pt": "A sabedoria n\u00e3o \u00e9 conhecimento armazenado, mas entendimento vivo. Pratique-a nas menores decis\u00f5es.",
          "es": "La sabidur\u00eda no es conocimiento almacenado sino comprensi\u00f3n viva. Pract\u00edcala en las decisiones m\u00e1s peque\u00f1as."}

CONTENT = {"en": "Contentment is the rare wealth that no fortune can buy. Cultivate it in what you already have.",
           "pt": "O contentamento \u00e9 a rara riqueza que nenhuma fortuna pode comprar. Cultive-o no que voc\u00ea j\u00e1 tem.",
           "es": "El contentamiento es la rara riqueza que ninguna fortuna puede comprar. Cult\u00edvalo en lo que ya tienes."}

WAR = {"en": "Even victory in war should be mourned, not celebrated. Avoid every conflict that can be avoided.",
       "pt": "At\u00e9 a vit\u00f3ria na guerra deve ser lamentada, n\u00e3o celebrada. Evite todo conflito que possa ser evitado.",
       "es": "Incluso la victoria en la guerra debe ser lamentada, no celebrada. Evita todo conflicto que pueda evitarse."}

SOFT_STRONG = {"en": "What is soft outlasts what is hard. Yield where rigid things break.",
               "pt": "O que \u00e9 macio dura mais que o que \u00e9 duro. Ceda onde coisas r\u00edgidas quebram.",
               "es": "Lo blando dura m\u00e1s que lo duro. Cede donde las cosas r\u00edgidas se rompen."}

MISTAKE = {"en": "Mistakes are only mistakes when uncorrected. Notice yours and adjust without shame.",
           "pt": "Os erros s\u00f3 s\u00e3o erros quando n\u00e3o corrigidos. Note os seus e ajuste sem vergonha.",
           "es": "Los errores solo son errores cuando no se corrigen. Nota los tuyos y ajusta sin verg\u00fcenza."}

reflections = [
    LOVE,  # 1
    {"en": "Good things require effort, bad things only inertia. Choose the harder, more rewarding path today.",
     "pt": "Coisas boas exigem esfor\u00e7o, coisas ruins apenas in\u00e9rcia. Escolha o caminho mais dif\u00edcil e gratificante hoje.",
     "es": "Las cosas buenas requieren esfuerzo, las malas solo inercia. Elige el camino m\u00e1s dif\u00edcil y gratificante hoy."},  # 2
    EMPTINESS,  # 3
    LOVE,  # 4
    {"en": "True travel is openness, not destination. Wander your day without insisting on outcomes.",
     "pt": "O verdadeiro viajar \u00e9 abertura, n\u00e3o destino. Vagueie pelo seu dia sem insistir em resultados.",
     "es": "El verdadero viajar es apertura, no destino. Deambula tu d\u00eda sin insistir en resultados."},  # 5
    PERSISTENCE,  # 6
    {"en": "Holding grudges drains us; remembering kindness nourishes us. Choose what to keep alive in memory.",
     "pt": "Guardar rancores nos drena; lembrar da gentileza nos nutre. Escolha o que manter vivo na mem\u00f3ria.",
     "es": "Guardar rencores nos drena; recordar la amabilidad nos nutre. Elige qu\u00e9 mantener vivo en la memoria."},  # 7
    {"en": "Lasting help is teaching, not giving. Offer skills before charity whenever you can.",
     "pt": "A ajuda duradoura \u00e9 ensinar, n\u00e3o dar. Ofere\u00e7a habilidades antes de caridade sempre que puder.",
     "es": "La ayuda duradera es ense\u00f1ar, no dar. Ofrece habilidades antes que caridad siempre que puedas."},  # 8
    SIMPLICITY,  # 9
    LET_GO,  # 10
    MISTAKE,  # 11
    LET_GO,  # 12
    {"en": "Others are mirrors for your growth. Let good people inspire you and difficult people teach you.",
     "pt": "Os outros s\u00e3o espelhos para seu crescimento. Deixe pessoas boas o inspirarem e pessoas dif\u00edceis o ensinarem.",
     "es": "Los dem\u00e1s son espejos para tu crecimiento. Deja que las personas buenas te inspiren y las dif\u00edciles te ense\u00f1en."},  # 13
    {"en": "Failing to appreciate others is a deeper poverty than being unappreciated. Practice generous attention.",
     "pt": "Falhar em apreciar os outros \u00e9 uma pobreza mais profunda do que n\u00e3o ser apreciado. Pratique a aten\u00e7\u00e3o generosa.",
     "es": "Fallar en apreciar a los dem\u00e1s es una pobreza m\u00e1s profunda que no ser apreciado. Practica la atenci\u00f3n generosa."},  # 14
    PRESENT,  # 15
    {"en": "Belief shapes reality more than circumstance. Watch what you tell yourself you can or cannot do.",
     "pt": "A cren\u00e7a molda a realidade mais que a circunst\u00e2ncia. Observe o que voc\u00ea diz a si mesmo que pode ou n\u00e3o fazer.",
     "es": "La creencia moldea la realidad m\u00e1s que la circunstancia. Observa lo que te dices que puedes o no puedes hacer."},  # 16
    PRESENT,  # 17
    {"en": "Serenity comes after the work, not instead of it. Do what is yours, then let go of the result.",
     "pt": "A serenidade vem depois do trabalho, n\u00e3o em vez dele. Fa\u00e7a o que \u00e9 seu, depois solte o resultado.",
     "es": "La serenidad viene despu\u00e9s del trabajo, no en su lugar. Haz lo que es tuyo, luego suelta el resultado."},  # 18
    FEAR,  # 19
    PERSISTENCE,  # 20
    LOVE,  # 21
    {"en": "Big things are made of small ones. Care for the small details and the great deeds will follow.",
     "pt": "Grandes coisas s\u00e3o feitas de pequenas. Cuide dos pequenos detalhes e os grandes feitos seguir\u00e3o.",
     "es": "Las grandes cosas est\u00e1n hechas de peque\u00f1as. Cuida los peque\u00f1os detalles y las grandes haza\u00f1as seguir\u00e1n."},  # 22
    {"en": "Learn with humility, urgency, and reverence. Treat every lesson as precious and fleeting.",
     "pt": "Aprenda com humildade, urg\u00eancia e rever\u00eancia. Trate cada li\u00e7\u00e3o como preciosa e fugaz.",
     "es": "Aprende con humildad, urgencia y reverencia. Trata cada lecci\u00f3n como preciosa y ef\u00edmera."},  # 23
    SIMPLICITY,  # 24
    {"en": "All tools wear with use, even the finest. Care for what you cherish and accept its limits.",
     "pt": "Todas as ferramentas se desgastam com o uso, mesmo as melhores. Cuide do que estima e aceite seus limites.",
     "es": "Todas las herramientas se desgastan con el uso, incluso las mejores. Cuida lo que aprecias y acepta sus l\u00edmites."},  # 25
    {"en": "Action without purpose wastes more than rest. Pause and ask if your busyness serves anything real.",
     "pt": "A\u00e7\u00e3o sem prop\u00f3sito desperdi\u00e7a mais que o descanso. Pause e pergunte se sua ocupa\u00e7\u00e3o serve a algo real.",
     "es": "La acci\u00f3n sin prop\u00f3sito desperdicia m\u00e1s que el descanso. Detente y pregunta si tu ocupaci\u00f3n sirve a algo real."},  # 26
    {"en": "Take your thoughts lightly; even the serious ones. Laughter loosens the grip of obsession.",
     "pt": "Leve seus pensamentos levemente; mesmo os s\u00e9rios. O riso solta o aperto da obsess\u00e3o.",
     "es": "Toma tus pensamientos con ligereza, incluso los serios. La risa afloja el agarre de la obsesi\u00f3n."},  # 27
    {"en": "What you wish for the world begins to appear in those around you. Wish well, broadly.",
     "pt": "O que voc\u00ea deseja para o mundo come\u00e7a a aparecer naqueles ao seu redor. Deseje o bem, amplamente.",
     "es": "Lo que deseas para el mundo comienza a aparecer en quienes te rodean. Desea el bien, ampliamente."},  # 28
    SELF_MASTERY,  # 29
    {"en": "Words define what is beyond words. Use them gently and know their limits.",
     "pt": "As palavras definem o que est\u00e1 al\u00e9m das palavras. Use-as com gentileza e conhe\u00e7a seus limites.",
     "es": "Las palabras definen lo que est\u00e1 m\u00e1s all\u00e1 de las palabras. \u00dasalas con gentileza y conoce sus l\u00edmites."},  # 30
    {"en": "Distance brings clarity that involvement obscures. Step back when stuck.",
     "pt": "A dist\u00e2ncia traz a clareza que o envolvimento obscurece. Recue quando estiver preso.",
     "es": "La distancia trae la claridad que la implicaci\u00f3n oscurece. Da un paso atr\u00e1s cuando est\u00e9s atascado."},  # 31
    {"en": "Most divine wrath we imagine is just nature acting on the tallest things. Stop assigning meaning to randomness.",
     "pt": "A maior parte da ira divina que imaginamos \u00e9 apenas a natureza agindo nas coisas mais altas. Pare de atribuir sentido ao acaso.",
     "es": "La mayor\u00eda de la ira divina que imaginamos es solo la naturaleza actuando sobre lo m\u00e1s alto. Deja de asignar sentido al azar."},  # 32
    {"en": "Reflection is the noblest path to wisdom. Spend more time thinking than acquiring.",
     "pt": "A reflex\u00e3o \u00e9 o caminho mais nobre para a sabedoria. Passe mais tempo pensando do que adquirindo.",
     "es": "La reflexi\u00f3n es el camino m\u00e1s noble hacia la sabidur\u00eda. Pasa m\u00e1s tiempo pensando que adquiriendo."},  # 33
    {"en": "Knowing is incomplete until questioned from many sides. Stay curious about what you think you know.",
     "pt": "O conhecimento \u00e9 incompleto at\u00e9 ser questionado de v\u00e1rios lados. Mantenha-se curioso sobre o que voc\u00ea pensa que sabe.",
     "es": "El conocimiento es incompleto hasta ser cuestionado desde varios lados. Mant\u00e9nte curioso sobre lo que crees que sabes."},  # 34
    {"en": "The simplest answers are usually overlooked. Look at what is in plain sight.",
     "pt": "As respostas mais simples geralmente s\u00e3o ignoradas. Olhe para o que est\u00e1 \u00e0 vista.",
     "es": "Las respuestas m\u00e1s simples son usualmente pasadas por alto. Mira lo que est\u00e1 a la vista."},  # 35
    {"en": "Most people resist change even when it would save them. Decide which kind of person you want to be.",
     "pt": "A maioria resiste \u00e0 mudan\u00e7a mesmo quando ela os salvaria. Decida que tipo de pessoa voc\u00ea quer ser.",
     "es": "La mayor\u00eda resiste el cambio incluso cuando los salvar\u00eda. Decide qu\u00e9 tipo de persona quieres ser."},  # 36
    SOFT_STRONG,  # 37
    {"en": "Time cannot be stopped or recovered. Use this hour as if it were your only one.",
     "pt": "O tempo n\u00e3o pode ser detido ou recuperado. Use esta hora como se fosse a \u00fanica.",
     "es": "El tiempo no puede ser detenido ni recuperado. Usa esta hora como si fuera la \u00fanica."},  # 38
    LET_GO,  # 39
    WISDOM,  # 40
    {"en": "True teachers connect past to present, tradition to today. Learn from those who do both.",
     "pt": "Verdadeiros mestres conectam passado e presente, tradi\u00e7\u00e3o e hoje. Aprenda com aqueles que fazem ambos.",
     "es": "Los verdaderos maestros conectan pasado y presente, tradici\u00f3n y hoy. Aprende de quienes hacen ambos."},  # 41
    {"en": "Respect is what separates us from animals. Cultivate it for yourself, others, and life itself.",
     "pt": "O respeito \u00e9 o que nos separa dos animais. Cultive-o por si mesmo, pelos outros e pela pr\u00f3pria vida.",
     "es": "El respeto es lo que nos separa de los animales. Cult\u00edvalo por ti mismo, por los dem\u00e1s y por la vida misma."},  # 42
    {"en": "Frugality today saves agony tomorrow. Live below your means and gain peace.",
     "pt": "A frugalidade hoje poupa a agonia de amanh\u00e3. Viva abaixo dos seus meios e ganhe paz.",
     "es": "La frugalidad hoy ahorra la agon\u00eda de ma\u00f1ana. Vive por debajo de tus medios y gana paz."},  # 43
    {"en": "Move through the world without leaving wounds. Speak without diminishing others.",
     "pt": "Mova-se pelo mundo sem deixar feridas. Fale sem diminuir os outros.",
     "es": "Mu\u00e9vete por el mundo sin dejar heridas. Habla sin disminuir a otros."},  # 44
    CONTENT,  # 45
    WISDOM,  # 46
    {"en": "Honesty about what you know and don't know is the foundation of real knowledge.",
     "pt": "A honestidade sobre o que voc\u00ea sabe e n\u00e3o sabe \u00e9 a base do conhecimento real.",
     "es": "La honestidad sobre lo que sabes y no sabes es la base del conocimiento real."},  # 47
    {"en": "Winning without fighting is the greatest skill. Find ways to resolve conflict before it begins.",
     "pt": "Vencer sem lutar \u00e9 a maior habilidade. Encontre maneiras de resolver o conflito antes que come\u00e7e.",
     "es": "Vencer sin luchar es la mayor habilidad. Encuentra formas de resolver el conflicto antes de que empiece."},  # 48
    PRESENT,  # 49
    {"en": "Modesty makes words trustworthy. Speak less of yourself and more will reach others.",
     "pt": "A modestia torna as palavras confi\u00e1veis. Fale menos de si mesmo e mais alcan\u00e7ar\u00e1 os outros.",
     "es": "La modestia hace las palabras confiables. Habla menos de ti mismo y m\u00e1s llegar\u00e1 a otros."},  # 50
    {"en": "Half-presence is the modern disease. Wherever you go, bring your full attention.",
     "pt": "A meia presen\u00e7a \u00e9 a doen\u00e7a moderna. Onde quer que voc\u00ea v\u00e1, leve sua aten\u00e7\u00e3o plena.",
     "es": "La media presencia es la enfermedad moderna. Adondequiera que vayas, lleva tu atenci\u00f3n plena."},  # 51
    WISDOM,  # 52
    {"en": "Honoring those who came before keeps us grounded. Let your ancestors guide your steps.",
     "pt": "Honrar aqueles que vieram antes nos mant\u00e9m enraizados. Deixe seus ancestrais guiarem seus passos.",
     "es": "Honrar a quienes vinieron antes nos mantiene arraigados. Deja que tus ancestros gu\u00eden tus pasos."},  # 53
    {"en": "Look inside before you look outside. The change you seek begins where you stand.",
     "pt": "Olhe para dentro antes de olhar para fora. A mudan\u00e7a que voc\u00ea busca come\u00e7a onde voc\u00ea est\u00e1.",
     "es": "Mira dentro antes de mirar fuera. El cambio que buscas comienza donde est\u00e1s."},  # 54
    {"en": "Constant practice and deep friendships are the truest joys. Cultivate both daily.",
     "pt": "A pr\u00e1tica constante e amizades profundas s\u00e3o as alegrias mais verdadeiras. Cultive ambas diariamente.",
     "es": "La pr\u00e1ctica constante y las amistades profundas son las alegr\u00edas m\u00e1s verdaderas. Cultiva ambas diariamente."},  # 55
    {"en": "Stop searching for what isn't there. Trust your senses and look at what is.",
     "pt": "Pare de procurar o que n\u00e3o est\u00e1 l\u00e1. Confie em seus sentidos e olhe para o que est\u00e1.",
     "es": "Deja de buscar lo que no est\u00e1. Conf\u00eda en tus sentidos y mira lo que est\u00e1."},  # 56
    {"en": "When teachings become rigid rules, they lose their life. Keep your understanding flexible.",
     "pt": "Quando os ensinamentos se tornam regras r\u00edgidas, perdem sua vida. Mantenha seu entendimento flex\u00edvel.",
     "es": "Cuando las ense\u00f1anzas se vuelven reglas r\u00edgidas, pierden su vida. Mant\u00e9n tu comprensi\u00f3n flexible."},  # 57
    {"en": "Concern yourself less with what cannot be known. Focus on living well today.",
     "pt": "Preocupe-se menos com o que n\u00e3o pode ser conhecido. Foque em viver bem hoje.",
     "es": "Preoc\u00fapate menos por lo que no puede conocerse. Enf\u00f3cate en vivir bien hoy."},  # 58
    {"en": "Recognizing your own ignorance is the first step toward wisdom. Cherish your unknowing.",
     "pt": "Reconhecer sua pr\u00f3pria ignor\u00e2ncia \u00e9 o primeiro passo para a sabedoria. Estime seu n\u00e3o-saber.",
     "es": "Reconocer tu propia ignorancia es el primer paso hacia la sabidur\u00eda. Aprecia tu no-saber."},  # 59
    {"en": "Knowledge without practice is empty. Apply today what you learned yesterday.",
     "pt": "Conhecimento sem pr\u00e1tica \u00e9 vazio. Aplique hoje o que aprendeu ontem.",
     "es": "El conocimiento sin pr\u00e1ctica est\u00e1 vac\u00edo. Aplica hoy lo que aprendiste ayer."},  # 60
    WISDOM,  # 61
    MISTAKE,  # 62
    {"en": "Education leads to confidence, hope, and peace in that order. Begin with learning to find peace.",
     "pt": "A educa\u00e7\u00e3o leva \u00e0 confian\u00e7a, esperan\u00e7a e paz nessa ordem. Comece aprendendo para encontrar paz.",
     "es": "La educaci\u00f3n lleva a la confianza, esperanza y paz en ese orden. Comienza con el aprendizaje para encontrar la paz."},  # 63
    {"en": "Learning and thinking must accompany each other. Read with reflection, reflect with reading.",
     "pt": "O aprendizado e o pensamento devem se acompanhar. Leia com reflex\u00e3o, reflita com leitura.",
     "es": "El aprendizaje y el pensamiento deben acompa\u00f1arse. Lee con reflexi\u00f3n, reflexiona con lectura."},  # 64
    {"en": "Time is created by how we use it. Stop saying you have none and start choosing what matters.",
     "pt": "O tempo \u00e9 criado por como o usamos. Pare de dizer que n\u00e3o tem e comece a escolher o que importa.",
     "es": "El tiempo se crea por c\u00f3mo lo usamos. Deja de decir que no lo tienes y empieza a elegir lo que importa."},  # 65
    {"en": "Behind humor often lies sorrow. Be gentle with those who make you laugh; they may be hurting.",
     "pt": "Por tr\u00e1s do humor frequentemente est\u00e1 a tristeza. Seja gentil com aqueles que o fazem rir; podem estar sofrendo.",
     "es": "Detr\u00e1s del humor a menudo se esconde la tristeza. S\u00e9 gentil con quienes te hacen re\u00edr; pueden estar sufriendo."},  # 66
    {"en": "Books open doors that experience never could. Read something new today.",
     "pt": "Os livros abrem portas que a experi\u00eancia jamais poderia. Leia algo novo hoje.",
     "es": "Los libros abren puertas que la experiencia jam\u00e1s podr\u00eda. Lee algo nuevo hoy."},  # 67
    SELF_MASTERY,  # 68
    {"en": "Words have power; they shape lives and societies. Choose them with care.",
     "pt": "As palavras t\u00eam poder; moldam vidas e sociedades. Escolha-as com cuidado.",
     "es": "Las palabras tienen poder; moldean vidas y sociedades. El\u00edgelas con cuidado."},  # 69
    {"en": "Understanding your enemy requires empathy. The same is true for those you love.",
     "pt": "Entender seu inimigo exige empatia. O mesmo vale para aqueles que voc\u00ea ama.",
     "es": "Entender a tu enemigo requiere empat\u00eda. Lo mismo vale para quienes amas."},  # 70
    {"en": "Choose your battles, and choose how to fight them. Some are best refused entirely.",
     "pt": "Escolha suas batalhas e escolha como lut\u00e1-las. Algumas \u00e9 melhor recusar inteiramente.",
     "es": "Elige tus batallas y elige c\u00f3mo lucharlas. Algunas es mejor rechazarlas por completo."},  # 71
    KINDNESS,  # 72
    {"en": "Avoid direct confrontation when you can. Move around obstacles rather than through them.",
     "pt": "Evite confronto direto quando puder. Contorne obst\u00e1culos em vez de atravess\u00e1-los.",
     "es": "Evita la confrontaci\u00f3n directa cuando puedas. Rodea los obst\u00e1culos en lugar de atravesarlos."},  # 73
    WAR,  # 74
    {"en": "What you nourish your dreams with matters. Feed them optimism and possibility, not worry.",
     "pt": "O que voc\u00ea alimenta seus sonhos importa. Alimente-os com otimismo e possibilidade, n\u00e3o preocupa\u00e7\u00e3o.",
     "es": "Con qu\u00e9 alimentas tus sue\u00f1os importa. Alim\u00e9ntalos con optimismo y posibilidad, no preocupaci\u00f3n."},  # 75
    {"en": "Beauty is everywhere for those who learn to see. Practice seeing it today.",
     "pt": "A beleza est\u00e1 em toda parte para aqueles que aprendem a ver. Pratique v\u00ea-la hoje.",
     "es": "La belleza est\u00e1 en todas partes para quienes aprenden a ver. Practica verla hoy."},  # 76
    {"en": "What you seek determines what you find. Want less and you will see more.",
     "pt": "O que voc\u00ea busca determina o que voc\u00ea encontra. Deseje menos e voc\u00ea ver\u00e1 mais.",
     "es": "Lo que buscas determina lo que encuentras. Desea menos y ver\u00e1s m\u00e1s."},  # 77
    {"en": "Gentleness, frugality, and humility are the three treasures. Cultivate them and become a true leader.",
     "pt": "Gentileza, frugalidade e humildade s\u00e3o os tr\u00eas tesouros. Cultive-os e torne-se um verdadeiro l\u00edder.",
     "es": "La gentileza, la frugalidad y la humildad son los tres tesoros. Cult\u00edvalos y conviertete en un verdadero l\u00edder."},  # 78
    {"en": "True leadership empowers others to feel ownership. Step back so they can shine.",
     "pt": "A verdadeira lideran\u00e7a empodera os outros a se sentirem donos. Recue para que eles possam brilhar.",
     "es": "El verdadero liderazgo empodera a otros a sentirse due\u00f1os. D\u00e9jate atr\u00e1s para que ellos puedan brillar."},  # 79
    {"en": "Rule yourself well before trying to govern others. Inner order creates outer order.",
     "pt": "Governe-se bem antes de tentar governar os outros. A ordem interior cria a ordem exterior.",
     "es": "Gobi\u00e9rnate bien antes de intentar gobernar a otros. El orden interior crea el orden exterior."},  # 80
    {"en": "The best leaders serve. Lead by walking behind, not in front.",
     "pt": "Os melhores l\u00edderes servem. Lidere caminhando atr\u00e1s, n\u00e3o \u00e0 frente.",
     "es": "Los mejores l\u00edderes sirven. Lidera caminando detr\u00e1s, no delante."},  # 81
    {"en": "What you love guides you more truly than reason. Listen to your deepest pull.",
     "pt": "O que voc\u00ea ama o guia mais verdadeiramente do que a raz\u00e3o. Escute seu chamado mais profundo.",
     "es": "Lo que amas te gu\u00eda m\u00e1s verdaderamente que la raz\u00f3n. Escucha tu llamado m\u00e1s profundo."},  # 82
    {"en": "The past illuminates the future. Study what came before to see clearly what comes next.",
     "pt": "O passado ilumina o futuro. Estude o que veio antes para ver claramente o que vem a seguir.",
     "es": "El pasado ilumina el futuro. Estudia lo que vino antes para ver claramente lo que viene despu\u00e9s."},  # 83
    PRESENT,  # 84
    {"en": "Inner virtue ripples outward through family, community, and world. Begin with your own heart.",
     "pt": "A virtude interior se irradia para fora atrav\u00e9s da fam\u00edlia, comunidade e mundo. Comece com seu pr\u00f3prio cora\u00e7\u00e3o.",
     "es": "La virtud interior se irradia hacia afuera a trav\u00e9s de la familia, la comunidad y el mundo. Comienza con tu propio coraz\u00f3n."},  # 85
    {"en": "Music speaks across all boundaries. Listen as a way of touching the universe.",
     "pt": "A m\u00fasica fala atrav\u00e9s de todas as fronteiras. Escute como um modo de tocar o universo.",
     "es": "La m\u00fasica habla a trav\u00e9s de todas las fronteras. Escucha como una forma de tocar el universo."},  # 86
    {"en": "Culture reveals what laws cannot. Listen to the music of a place to know its soul.",
     "pt": "A cultura revela o que as leis n\u00e3o podem. Escute a m\u00fasica de um lugar para conhecer sua alma.",
     "es": "La cultura revela lo que las leyes no pueden. Escucha la m\u00fasica de un lugar para conocer su alma."},  # 87
    WISDOM,  # 88
    LOVE,  # 89
    {"en": "Words reveal more than they say. Listen to the heart that speaks them.",
     "pt": "As palavras revelam mais do que dizem. Escute o cora\u00e7\u00e3o que as fala.",
     "es": "Las palabras revelan m\u00e1s de lo que dicen. Escucha al coraz\u00f3n que las habla."},  # 90
    {"en": "Your inner thoughts shape outer reality. Tend the garden of your mind carefully.",
     "pt": "Seus pensamentos interiores moldam a realidade exterior. Cuide do jardim da sua mente cuidadosamente.",
     "es": "Tus pensamientos interiores moldean la realidad exterior. Cuida el jard\u00edn de tu mente cuidadosamente."},  # 91
    LOVE,  # 92
    {"en": "Stillness reveals what motion hides. Be quiet and the universe answers.",
     "pt": "A quietude revela o que o movimento esconde. Fique quieto e o universo responde.",
     "es": "La quietud revela lo que el movimiento oculta. Qu\u00e9date quieto y el universo responde."},  # 93
    {"en": "The most real things cannot be touched. Honor the invisible as much as the visible.",
     "pt": "As coisas mais reais n\u00e3o podem ser tocadas. Honre o invis\u00edvel tanto quanto o vis\u00edvel.",
     "es": "Las cosas m\u00e1s reales no pueden tocarse. Honra lo invisible tanto como lo visible."},  # 94
    {"en": "Stop performing for others or fearing them. Reclaim your hours for what is your own.",
     "pt": "Pare de performar para os outros ou de tem\u00ea-los. Recupere suas horas para o que \u00e9 seu.",
     "es": "Deja de actuar para los dem\u00e1s o temerlos. Recupera tus horas para lo que es tuyo."},  # 95
    {"en": "Thoughts become words, words become acts, acts become character. Begin at the source.",
     "pt": "Pensamentos se tornam palavras, palavras se tornam atos, atos se tornam car\u00e1ter. Comece pela fonte.",
     "es": "Los pensamientos se vuelven palabras, las palabras se vuelven actos, los actos se vuelven car\u00e1cter. Comienza por la fuente."},  # 96
    {"en": "Words shape perception. Without language, knowledge cannot grow.",
     "pt": "As palavras moldam a percep\u00e7\u00e3o. Sem linguagem, o conhecimento n\u00e3o pode crescer.",
     "es": "Las palabras moldean la percepci\u00f3n. Sin lenguaje, el conocimiento no puede crecer."},  # 97
    {"en": "Some things slip through every form of expression. Sit with mysteries that words cannot hold.",
     "pt": "Algumas coisas escapam de toda forma de express\u00e3o. Sente-se com mist\u00e9rios que as palavras n\u00e3o podem conter.",
     "es": "Algunas cosas escapan a toda forma de expresi\u00f3n. Si\u00e9ntate con misterios que las palabras no pueden contener."},  # 98
    {"en": "Your word is your worth. Keep promises and society will trust you.",
     "pt": "Sua palavra \u00e9 seu valor. Cumpra promessas e a sociedade confiar\u00e1 em voc\u00ea.",
     "es": "Tu palabra es tu valor. Cumple promesas y la sociedad confiar\u00e1 en ti."},  # 99
    {"en": "True power does not seek itself. Practice doing without trying.",
     "pt": "O verdadeiro poder n\u00e3o se busca. Pratique fazer sem tentar.",
     "es": "El verdadero poder no se busca a s\u00ed mismo. Practica hacer sin intentar."},  # 100
    SELF_MASTERY,  # 101
    {"en": "A life unfolds in stages. Honor where you are without rushing the next decade.",
     "pt": "Uma vida se desdobra em est\u00e1gios. Honre onde voc\u00ea est\u00e1 sem apressar a pr\u00f3xima d\u00e9cada.",
     "es": "Una vida se despliega en etapas. Honra donde est\u00e1s sin apresurar la pr\u00f3xima d\u00e9cada."},  # 102
    {"en": "The way to do is to be. Stop trying so hard and let your nature guide you.",
     "pt": "O caminho do fazer \u00e9 ser. Pare de se esfor\u00e7ar tanto e deixe sua natureza gui\u00e1-lo.",
     "es": "El camino para hacer es ser. Deja de esforzarte tanto y deja que tu naturaleza te gu\u00ede."},  # 103
    {"en": "Silence is where the deepest truths emerge. Make room for it daily.",
     "pt": "O sil\u00eancio \u00e9 onde as verdades mais profundas emergem. Fa\u00e7a espa\u00e7o para ele diariamente.",
     "es": "El silencio es donde las verdades m\u00e1s profundas emergen. Haz espacio para \u00e9l diariamente."},  # 104
    {"en": "Suspicion poisons relationships more than betrayal. Trust freely, accept the cost.",
     "pt": "A suspeita envenena as rela\u00e7\u00f5es mais que a trai\u00e7\u00e3o. Confie livremente, aceite o custo.",
     "es": "La sospecha envenena las relaciones m\u00e1s que la traici\u00f3n. Conf\u00eda libremente, acepta el costo."},  # 105
    {"en": "Trustworthiness is earned by being trustworthy. Match your inside to your outside.",
     "pt": "A confiabilidade \u00e9 conquistada sendo confi\u00e1vel. Combine seu interior com seu exterior.",
     "es": "La confiabilidad se gana siendo confiable. Iguala tu interior con tu exterior."},  # 106
    {"en": "Old wounds only sting if you pick at them. Let healing replace remembering.",
     "pt": "Velhas feridas s\u00f3 doem se voc\u00ea as cutuca. Deixe a cura substituir a lembran\u00e7a.",
     "es": "Las viejas heridas solo duelen si las hurgas. Deja que la sanaci\u00f3n reemplace al recuerdo."},  # 107
    KINDNESS,  # 108
    KINDNESS,  # 109
    KINDNESS,  # 110
    KINDNESS,  # 111
    {"en": "Generosity multiplies what is given. The more you share, the more you have.",
     "pt": "A generosidade multiplica o que \u00e9 dado. Quanto mais voc\u00ea compartilha, mais voc\u00ea tem.",
     "es": "La generosidad multiplica lo que se da. Cuanto m\u00e1s compartes, m\u00e1s tienes."},  # 112
    KINDNESS,  # 113
    PERSISTENCE,  # 114
    {"en": "Inner conscience is the highest law. Live by what is right, not by what is allowed.",
     "pt": "A consci\u00eancia interior \u00e9 a lei mais alta. Viva pelo que \u00e9 certo, n\u00e3o pelo que \u00e9 permitido.",
     "es": "La conciencia interior es la ley m\u00e1s alta. Vive por lo que es correcto, no por lo que est\u00e1 permitido."},  # 115
    {"en": "Health, contentment, and confidence are the truest possessions. Cultivate all three.",
     "pt": "Sa\u00fade, contentamento e confian\u00e7a s\u00e3o as posses mais verdadeiras. Cultive as tr\u00eas.",
     "es": "Salud, contentamiento y confianza son las posesiones m\u00e1s verdaderas. Cultiva las tres."},  # 116
    {"en": "Desire blinds; freedom from desire reveals. Practice wanting nothing in this moment.",
     "pt": "O desejo cega; a liberdade do desejo revela. Pratique n\u00e3o querer nada neste momento.",
     "es": "El deseo ciega; la libertad del deseo revela. Practica no querer nada en este momento."},  # 117
    {"en": "What you seek in others lives first in yourself. Mirror inward before pointing outward.",
     "pt": "O que voc\u00ea procura nos outros vive primeiro em si mesmo. Espelhe para dentro antes de apontar para fora.",
     "es": "Lo que buscas en otros vive primero en ti mismo. Refleja hacia dentro antes de se\u00f1alar hacia afuera."},  # 118
    ANGER,  # 119
    {"en": "Test others through small situations to know them deeply. Pay attention to what reveals character.",
     "pt": "Teste os outros atrav\u00e9s de pequenas situa\u00e7\u00f5es para conhec\u00ea-los profundamente. Preste aten\u00e7\u00e3o ao que revela o car\u00e1ter.",
     "es": "Prueba a otros a trav\u00e9s de peque\u00f1as situaciones para conocerlos profundamente. Presta atenci\u00f3n a lo que revela el car\u00e1cter."},  # 120
    {"en": "Some problems only thinking creates. Stop the loop and many will dissolve.",
     "pt": "Alguns problemas s\u00f3 o pensar cria. Pare o ciclo e muitos se dissolver\u00e3o.",
     "es": "Algunos problemas solo el pensar los crea. Detente el ciclo y muchos se disolver\u00e1n."},  # 121
    {"en": "Judge ideas on their own merit, not by who says them. Truth has no master.",
     "pt": "Julgue as ideias por seu pr\u00f3prio m\u00e9rito, n\u00e3o por quem as diz. A verdade n\u00e3o tem dono.",
     "es": "Juzga las ideas por su propio m\u00e9rito, no por qui\u00e9n las dice. La verdad no tiene amo."},  # 122
    {"en": "Silence is where the deepest truths emerge. Make room for it daily.",
     "pt": "O sil\u00eancio \u00e9 onde as verdades mais profundas emergem. Fa\u00e7a espa\u00e7o para ele diariamente.",
     "es": "El silencio es donde las verdades m\u00e1s profundas emergen. Haz espacio para \u00e9l diariamente."},  # 123
    {"en": "Excessive rules create rebellion. The lighter the touch, the more harmonious the order.",
     "pt": "Regras excessivas criam rebeli\u00e3o. Quanto mais leve o toque, mais harmoniosa a ordem.",
     "es": "Las reglas excesivas crean rebeli\u00f3n. Cuanto m\u00e1s ligero el toque, m\u00e1s armonioso el orden."},  # 124
    {"en": "Imperfection is part of value. A flawed treasure is worth more than a flawless trifle.",
     "pt": "A imperfei\u00e7\u00e3o faz parte do valor. Um tesouro imperfeito vale mais que uma trivialidade perfeita.",
     "es": "La imperfecci\u00f3n es parte del valor. Un tesoro imperfecto vale m\u00e1s que una trivialidad perfecta."},  # 125
    {"en": "Growth requires expanding your awareness. Open to dimensions you have not yet seen.",
     "pt": "O crescimento exige expandir sua consci\u00eancia. Abra-se a dimens\u00f5es que voc\u00ea ainda n\u00e3o viu.",
     "es": "El crecimiento requiere expandir tu conciencia. \u00c1brete a dimensiones que a\u00fan no has visto."},  # 126
    {"en": "Wandering freely is its own kind of arrival. Stop forcing every step to lead somewhere.",
     "pt": "Vaguear livremente \u00e9 sua pr\u00f3pria forma de chegada. Pare de for\u00e7ar cada passo para levar a algum lugar.",
     "es": "Vagar libremente es su propia forma de llegada. Deja de forzar cada paso para que lleve a alg\u00fan lugar."},  # 127
    WISDOM,  # 128
    {"en": "Subtle laws catch what obvious rules miss. Trust the natural justice of things.",
     "pt": "Leis sutis pegam o que regras \u00f3bvias deixam escapar. Confie na justi\u00e7a natural das coisas.",
     "es": "Las leyes sutiles atrapan lo que las reglas obvias pasan por alto. Conf\u00eda en la justicia natural de las cosas."},  # 129
    {"en": "Not seeking approval makes insults harmless. Free yourself from the need to be respected.",
     "pt": "N\u00e3o buscar aprova\u00e7\u00e3o torna os insultos inofensivos. Liberte-se da necessidade de ser respeitado.",
     "es": "No buscar aprobaci\u00f3n hace inofensivos los insultos. Lib\u00e9rate de la necesidad de ser respetado."},  # 130
    {"en": "Speak only when necessary. Brevity is the natural way of wisdom.",
     "pt": "Fale apenas quando necess\u00e1rio. A brevidade \u00e9 o caminho natural da sabedoria.",
     "es": "Habla solo cuando sea necesario. La brevedad es el camino natural de la sabidur\u00eda."},  # 131
    {"en": "Self-acceptance attracts the world's acceptance. Begin within and the rest follows.",
     "pt": "A autoaceita\u00e7\u00e3o atrai a aceita\u00e7\u00e3o do mundo. Comece por dentro e o resto segue.",
     "es": "La autoaceptaci\u00f3n atrae la aceptaci\u00f3n del mundo. Comienza por dentro y el resto sigue."},  # 132
    {"en": "Return to stillness as a tree returns to its root. Quietude is your true home.",
     "pt": "Retorne \u00e0 quietude como uma \u00e1rvore retorna \u00e0 sua raiz. A quietude \u00e9 sua verdadeira casa.",
     "es": "Vuelve a la quietud como un \u00e1rbol vuelve a su ra\u00edz. La quietud es tu verdadero hogar."},  # 133
    {"en": "Speed sometimes saves and sometimes loses; wisdom knows when. Cultivate timing.",
     "pt": "A velocidade \u00e0s vezes salva e \u00e0s vezes perde; a sabedoria sabe quando. Cultive o timing.",
     "es": "La velocidad a veces salva y a veces pierde; la sabidur\u00eda sabe cu\u00e1ndo. Cultiva el timing."},  # 134
    {"en": "Knowing yourself is the deepest knowing. Look inward as carefully as outward.",
     "pt": "Conhecer a si mesmo \u00e9 o conhecimento mais profundo. Olhe para dentro com tanto cuidado quanto para fora.",
     "es": "Conocerse a uno mismo es el conocimiento m\u00e1s profundo. Mira hacia dentro con tanto cuidado como hacia fuera."},  # 135
    {"en": "Set your heart on the Way, not on appearances. Focus on what is essential to your becoming.",
     "pt": "Coloque seu cora\u00e7\u00e3o no Caminho, n\u00e3o nas apar\u00eancias. Foque no que \u00e9 essencial para o seu tornar-se.",
     "es": "Pon tu coraz\u00f3n en el Camino, no en las apariencias. Enf\u00f3cate en lo que es esencial para tu llegar a ser."},  # 136
    {"en": "Profit-driven action breeds resentment. Let purpose guide you instead of gain.",
     "pt": "A a\u00e7\u00e3o movida pelo lucro gera ressentimento. Deixe o prop\u00f3sito gui\u00e1-lo em vez do ganho.",
     "es": "La acci\u00f3n motivada por el beneficio engendra resentimiento. Deja que el prop\u00f3sito te gu\u00ede en vez de la ganancia."},  # 137
    {"en": "The noble person sees what is right; the small person sees what is profitable. Choose your vision.",
     "pt": "A pessoa nobre v\u00ea o que \u00e9 certo; a pessoa pequena v\u00ea o que \u00e9 lucrativo. Escolha sua vis\u00e3o.",
     "es": "La persona noble ve lo que es correcto; la persona peque\u00f1a ve lo que es lucrativo. Elige tu visi\u00f3n."},  # 138
    {"en": "Wealth and honor must be acquired rightly to be worth having. Means matter as much as ends.",
     "pt": "Riqueza e honra devem ser adquiridas corretamente para valerem. Os meios importam tanto quanto os fins.",
     "es": "Riqueza y honor deben adquirirse correctamente para valer la pena. Los medios importan tanto como los fines."},  # 139
    {"en": "A noble person cannot be reduced to a function. Refuse to be used as a mere tool.",
     "pt": "Uma pessoa nobre n\u00e3o pode ser reduzida a uma fun\u00e7\u00e3o. Recuse ser usado como mera ferramenta.",
     "es": "Una persona noble no puede ser reducida a una funci\u00f3n. Rech\u00e1zate ser usado como mera herramienta."},  # 140
    {"en": "Big problems begin small. Solve issues while they are still tiny.",
     "pt": "Grandes problemas come\u00e7am pequenos. Resolva quest\u00f5es enquanto ainda s\u00e3o min\u00fasculas.",
     "es": "Los grandes problemas comienzan peque\u00f1os. Resuelve los asuntos mientras a\u00fan son diminutos."},  # 141
    {"en": "Excessive purity isolates you from others. Engage with the world rather than retreating from it.",
     "pt": "A pureza excessiva o isola dos outros. Engaje-se com o mundo em vez de se afastar dele.",
     "es": "La pureza excesiva te a\u00edsla de los dem\u00e1s. Compromet\u00e9te con el mundo en lugar de retirarte de \u00e9l."},  # 142
    CONTENT,  # 143
    {"en": "Securing the good of others secures your own. Practice generosity as enlightened self-interest.",
     "pt": "Assegurar o bem dos outros assegura o seu pr\u00f3prio. Pratique a generosidade como interesse pr\u00f3prio esclarecido.",
     "es": "Asegurar el bien de los dem\u00e1s asegura el tuyo propio. Practica la generosidad como inter\u00e9s propio iluminado."},  # 144
    {"en": "Virtue, wisdom, and courage free you from anxiety, perplexity, and fear. Cultivate all three.",
     "pt": "Virtude, sabedoria e coragem o libertam da ansiedade, perplexidade e medo. Cultive os tr\u00eas.",
     "es": "Virtud, sabidur\u00eda y coraje te liberan de la ansiedad, la perplejidad y el miedo. Cultiva los tres."},  # 145
    {"en": "Past wrongdoing does not define a person. Look at who someone is now.",
     "pt": "Erros passados n\u00e3o definem uma pessoa. Olhe para quem algu\u00e9m \u00e9 agora.",
     "es": "Los errores pasados no definen a una persona. Mira qui\u00e9n es alguien ahora."},  # 146
    {"en": "Material and infinite are inseparable. Honor both the visible and invisible.",
     "pt": "O material e o infinito s\u00e3o insepar\u00e1veis. Honre tanto o vis\u00edvel quanto o invis\u00edvel.",
     "es": "Lo material y lo infinito son inseparables. Honra tanto lo visible como lo invisible."},  # 147
    SIMPLICITY,  # 148
    {"en": "Five virtues complete a person: gravity, generosity, sincerity, earnestness, and kindness.",
     "pt": "Cinco virtudes completam uma pessoa: gravidade, generosidade, sinceridade, ardor e gentileza.",
     "es": "Cinco virtudes completan a una persona: gravedad, generosidad, sinceridad, fervor y amabilidad."},  # 149
    WAR,  # 150
    {"en": "Strategy depends on accurate self-knowledge. Start by knowing your real strengths.",
     "pt": "A estrat\u00e9gia depende de autoconhecimento preciso. Comece por conhecer suas reais for\u00e7as.",
     "es": "La estrategia depende del autoconocimiento preciso. Comienza por conocer tus reales fortalezas."},  # 151
    WAR,  # 152
    {"en": "The skilled tactician disrupts what their opponent has carefully arranged. Find the loose thread.",
     "pt": "O t\u00e1tico habilidoso desfaz o que seu oponente arranjou cuidadosamente. Encontre o fio solto.",
     "es": "El t\u00e1ctico h\u00e1bil deshace lo que su oponente ha arreglado cuidadosamente. Encuentra el hilo suelto."},  # 153
    {"en": "Common minds wonder at the rare; wise minds wonder at the everyday. Look at the ordinary closely.",
     "pt": "Mentes comuns se maravilham com o raro; mentes s\u00e1bias se maravilham com o cotidiano. Olhe o comum de perto.",
     "es": "Las mentes comunes se maravillan con lo raro; las mentes sabias con lo cotidiano. Mira lo ordinario de cerca."},  # 154
    {"en": "True power does not seek itself. Practice doing without trying.",
     "pt": "O verdadeiro poder n\u00e3o se busca. Pratique fazer sem tentar.",
     "es": "El verdadero poder no se busca a s\u00ed mismo. Practica hacer sin intentar."},  # 155
    {"en": "To lead is to serve from behind. Put others in front of you and watch growth happen.",
     "pt": "Liderar \u00e9 servir de tr\u00e1s. Coloque os outros \u00e0 sua frente e veja o crescimento acontecer.",
     "es": "Liderar es servir desde atr\u00e1s. Pon a los dem\u00e1s delante de ti y observa cr\u00e9cer."},  # 156
    CONTENT,  # 157
    {"en": "True victory comes before the fight begins. Win by preparation and avoidance.",
     "pt": "A verdadeira vit\u00f3ria vem antes da luta come\u00e7ar. Ven\u00e7a pela prepara\u00e7\u00e3o e evita\u00e7\u00e3o.",
     "es": "La verdadera victoria viene antes de que comience la lucha. Vence por preparaci\u00f3n y evitaci\u00f3n."},  # 158
    {"en": "The evil you should fight is the one within. Begin every reform at home.",
     "pt": "O mal que voc\u00ea deve combater \u00e9 o que est\u00e1 dentro. Comece toda reforma em casa.",
     "es": "El mal que debes combatir es el que est\u00e1 dentro. Comienza toda reforma en casa."},  # 159
    {"en": "True leaders make themselves unnecessary. Empower others until they no longer need you.",
     "pt": "Verdadeiros l\u00edderes se tornam desnecess\u00e1rios. Empodere os outros at\u00e9 que n\u00e3o precisem mais de voc\u00ea.",
     "es": "Los verdaderos l\u00edderes se vuelven innecesarios. Empodera a otros hasta que ya no te necesiten."},  # 160
    {"en": "You do not need to perform to be valuable. Simply being yourself is enough.",
     "pt": "Voc\u00ea n\u00e3o precisa performar para ter valor. Simplesmente ser voc\u00ea mesmo \u00e9 suficiente.",
     "es": "No necesitas actuar para tener valor. Simplemente ser t\u00fa mismo es suficiente."},  # 161
    SIMPLICITY,  # 162
    {"en": "Identification with thoughts is exhausting. Watch them pass without becoming them.",
     "pt": "A identifica\u00e7\u00e3o com pensamentos \u00e9 exaustiva. Observe-os passar sem se tornar eles.",
     "es": "La identificaci\u00f3n con pensamientos es agotadora. Obs\u00e9rvalos pasar sin convertirte en ellos."},  # 163
    SOFT_STRONG,  # 164
    {"en": "Small advantages distract from great achievements. Keep your eyes on what truly matters.",
     "pt": "Pequenas vantagens distraem das grandes conquistas. Mantenha seus olhos no que verdadeiramente importa.",
     "es": "Las peque\u00f1as ventajas distraen de los grandes logros. Mant\u00e9n los ojos en lo que verdaderamente importa."},  # 165
    {"en": "Speak less, do more. Let your actions complete what your words begin.",
     "pt": "Fale menos, fa\u00e7a mais. Deixe suas a\u00e7\u00f5es completarem o que suas palavras come\u00e7aram.",
     "es": "Habla menos, haz m\u00e1s. Deja que tus acciones completen lo que tus palabras comenzaron."},  # 166
    {"en": "Friction polishes; trials perfect. Welcome resistance as part of becoming.",
     "pt": "A fric\u00e7\u00e3o pole; as provas aperfei\u00e7oam. Acolha a resist\u00eancia como parte do tornar-se.",
     "es": "La fricci\u00f3n pule; las pruebas perfeccionan. Acoge la resistencia como parte del llegar a ser."},  # 167
    {"en": "Let what you love be how you spend your hours. There are countless ways to honor life.",
     "pt": "Que o que voc\u00ea ama seja como passa suas horas. H\u00e1 incont\u00e1veis modos de honrar a vida.",
     "es": "Que lo que amas sea como pasas tus horas. Hay innumerables formas de honrar la vida."},  # 168
    {"en": "Caution prevents most errors. Pause briefly before each consequential choice.",
     "pt": "A cautela previne a maioria dos erros. Pause brevemente antes de cada escolha consequente.",
     "es": "La cautela previene la mayor\u00eda de los errores. Pausa brevemente antes de cada elecci\u00f3n consecuente."},  # 169
    {"en": "Pursue the difficult first; success follows naturally. Stop chasing easy wins.",
     "pt": "Persiga o dif\u00edcil primeiro; o sucesso segue naturalmente. Pare de perseguir vit\u00f3rias f\u00e1ceis.",
     "es": "Persigue lo dif\u00edcil primero; el \u00e9xito sigue naturalmente. Deja de perseguir victorias f\u00e1ciles."},  # 170
    {"en": "Knowing without doing is its own kind of failure. Act on what you already know.",
     "pt": "Saber sem fazer \u00e9 seu pr\u00f3prio tipo de fracasso. Aja sobre o que voc\u00ea j\u00e1 sabe.",
     "es": "Saber sin hacer es su propio tipo de fracaso. Act\u00faa sobre lo que ya sabes."},  # 171
    {"en": "The worst cowardice is knowing what is right and not doing it. Live up to your understanding.",
     "pt": "A pior covardia \u00e9 saber o que \u00e9 certo e n\u00e3o fazer. Viva \u00e0 altura do seu entendimento.",
     "es": "La peor cobard\u00eda es saber lo que es correcto y no hacerlo. Vive a la altura de tu comprensi\u00f3n."},  # 172
    {"en": "Frugality today saves agony tomorrow. Live below your means and gain peace.",
     "pt": "A frugalidade hoje poupa a agonia de amanh\u00e3. Viva abaixo dos seus meios e ganhe paz.",
     "es": "La frugalidad hoy ahorra la agon\u00eda de ma\u00f1ana. Vive por debajo de tus medios y gana paz."},  # 173
    {"en": "Zeal builds knowledge; lukewarmness loses it. Bring fire to what you study.",
     "pt": "O zelo constr\u00f3i conhecimento; a tibieza o perde. Traga fogo ao que voc\u00ea estuda.",
     "es": "El celo construye conocimiento; la tibieza lo pierde. Trae fuego a lo que estudias."},  # 174
    {"en": "Caution prevents most errors. Pause briefly before each consequential choice.",
     "pt": "A cautela previne a maioria dos erros. Pause brevemente antes de cada escolha consequente.",
     "es": "La cautela previene la mayor\u00eda de los errores. Pausa brevemente antes de cada elecci\u00f3n consecuente."},  # 175
    MISTAKE,  # 176
    {"en": "Long-term thinking prevents near-term sorrow. Plan ahead even when comfortable.",
     "pt": "O pensamento de longo prazo previne tristezas pr\u00f3ximas. Planeje com anteced\u00eancia mesmo quando confort\u00e1vel.",
     "es": "El pensamiento a largo plazo previene tristezas cercanas. Planifica con anticipaci\u00f3n incluso cuando est\u00e9s c\u00f3modo."},  # 177
    {"en": "Old wounds only sting if you pick at them. Let healing replace remembering.",
     "pt": "Velhas feridas s\u00f3 doem se voc\u00ea as cutuca. Deixe a cura substituir a lembran\u00e7a.",
     "es": "Las viejas heridas solo duelen si las hurgas. Deja que la sanaci\u00f3n reemplace al recuerdo."},  # 178
    ANGER,  # 179
    {"en": "Releasing resentment brings the peace it withheld from you. Forgive for your own sake.",
     "pt": "Soltar o ressentimento traz a paz que ele lhe negava. Perdoe pelo seu pr\u00f3prio bem.",
     "es": "Soltar el resentimiento trae la paz que te negaba. Perdona por tu propio bien."},  # 180
    {"en": "Surround yourself with people who lift you. Companions shape who you become.",
     "pt": "Cerque-se de pessoas que o elevam. Os companheiros moldam quem voc\u00ea se torna.",
     "es": "Rod\u00e9ate de personas que te eleven. Los compa\u00f1eros moldean en lo que te conviertes."},  # 181
    KINDNESS,  # 182
    {"en": "Virtue, wisdom, and courage free you from anxiety, perplexity, and fear. Cultivate all three.",
     "pt": "Virtude, sabedoria e coragem o libertam da ansiedade, perplexidade e medo. Cultive os tr\u00eas.",
     "es": "Virtud, sabidur\u00eda y coraje te liberan de la ansiedad, la perplejidad y el miedo. Cultiva los tres."},  # 183
    {"en": "Pursue the difficult first; success follows naturally. Stop chasing easy wins.",
     "pt": "Persiga o dif\u00edcil primeiro; o sucesso segue naturalmente. Pare de perseguir vit\u00f3rias f\u00e1ceis.",
     "es": "Persigue lo dif\u00edcil primero; el \u00e9xito sigue naturalmente. Deja de perseguir victorias f\u00e1ciles."},  # 184
    {"en": "Knowing without doing is its own kind of failure. Act on what you already know.",
     "pt": "Saber sem fazer \u00e9 seu pr\u00f3prio tipo de fracasso. Aja sobre o que voc\u00ea j\u00e1 sabe.",
     "es": "Saber sin hacer es su propio tipo de fracaso. Act\u00faa sobre lo que ya sabes."},  # 185
    {"en": "Learning and thinking must accompany each other. Read with reflection, reflect with reading.",
     "pt": "O aprendizado e o pensamento devem se acompanhar. Leia com reflex\u00e3o, reflita com leitura.",
     "es": "El aprendizaje y el pensamiento deben acompa\u00f1arse. Lee con reflexi\u00f3n, reflexiona con lectura."},  # 186
    {"en": "Good things require effort, bad things only inertia. Choose the harder, more rewarding path today.",
     "pt": "Coisas boas exigem esfor\u00e7o, coisas ruins apenas in\u00e9rcia. Escolha o caminho mais dif\u00edcil e gratificante hoje.",
     "es": "Las cosas buenas requieren esfuerzo, las malas solo inercia. Elige el camino m\u00e1s dif\u00edcil y gratificante hoy."},  # 187
    {"en": "Caution prevents most errors. Pause briefly before each consequential choice.",
     "pt": "A cautela previne a maioria dos erros. Pause brevemente antes de cada escolha consequente.",
     "es": "La cautela previene la mayor\u00eda de los errores. Pausa brevemente antes de cada elecci\u00f3n consecuente."},  # 188
    {"en": "Releasing resentment brings the peace it withheld from you. Forgive for your own sake.",
     "pt": "Soltar o ressentimento traz a paz que ele lhe negava. Perdoe pelo seu pr\u00f3prio bem.",
     "es": "Soltar el resentimiento trae la paz que te negaba. Perdona por tu propio bien."},  # 189
]

result = {}
for i, key in enumerate(keys):
    if i < len(reflections):
        result[key] = reflections[i]

with open('c:/Users/lalli/Flutter/coach_phrase_app/reflections_eastern.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f'Generated {len(result)} eastern reflections')
