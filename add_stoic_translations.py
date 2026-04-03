import json

with open('c:/Users/lalli/Flutter/coach_phrase_app/translations_stoicism.json', 'r', encoding='utf-8') as f:
    tr = json.load(f)

new = {
    "Nothing great is created suddenly  any more than a bunch of grapes or a fig. If you tell me that you desire a fig  I answer you that there must be time. Let it first blossom  then bear fruit  then ripen.": {
        "pt": "Nada grandioso \u00e9 criado de repente, assim como um cacho de uvas ou um figo. Se me diz que deseja um figo, respondo que \u00e9 preciso tempo. Deixe-o primeiro florescer, depois dar fruto, depois amadurecer.",
        "es": "Nada grandioso se crea de repente, como un racimo de uvas o un higo. Si me dices que deseas un higo, te respondo que hace falta tiempo. D\u00e9jalo primero florecer, luego dar fruto, luego madurar."
    },
    "Practice yourself  for heaven's sake  in little things  and thence proceed to greater.": {
        "pt": "Pratique, pelo amor de Deus, nas pequenas coisas, e depois prossiga para as maiores.",
        "es": "Practica, por el amor de Dios, en las cosas peque\u00f1as, y luego avanza hacia las mayores."
    },
    "Ask not that events should happen as you will  but let your will be that events should happen as they do  and you shall have peace.": {
        "pt": "N\u00e3o pe\u00e7a que os eventos aconte\u00e7am como voc\u00ea quer, mas deixe que sua vontade seja que os eventos aconte\u00e7am como acontecem, e voc\u00ea ter\u00e1 paz.",
        "es": "No pidas que los eventos sucedan como t\u00fa quieres, sino deja que tu voluntad sea que los eventos sucedan como suceden, y tendr\u00e1s paz."
    },
    "Vex not thy spirit at the course of things  they heed not thy vexation. How ludicrous and outlandish is astonishment at anything that may happen in life.": {
        "pt": "N\u00e3o aflija seu esp\u00edrito com o curso das coisas; elas n\u00e3o se importam com sua afli\u00e7\u00e3o. Qu\u00e3o rid\u00edculo e absurdo \u00e9 o espanto diante de qualquer coisa que possa acontecer na vida.",
        "es": "No aflijas tu esp\u00edritu con el curso de las cosas; ellas no se preocupan por tu aflicci\u00f3n. Cu\u00e1n rid\u00edculo y absurdo es el asombro ante cualquier cosa que pueda suceder en la vida."
    },
    "Here is a rule to remember when anything tempts you to feel bitter: not  \"This is a misfortune \" but \"To bear this worthily is good fortune.\"": {
        "pt": "Eis uma regra para lembrar quando algo o tenta a se sentir amargurado: n\u00e3o \"Isto \u00e9 um infort\u00fanio\", mas \"Suportar isto com dignidade \u00e9 boa sorte.\"",
        "es": "He aqu\u00ed una regla para recordar cuando algo te tienta a sentirte amargado: no \"Esto es una desgracia\", sino \"Soportar esto dignamente es buena fortuna.\""
    },
    "Adapt yourself to the things among which your lot has been cast and love sincerely the fellow creatures with whom destiny has ordained that you shall live.": {
        "pt": "Adapte-se \u00e0s coisas entre as quais sua sorte foi lan\u00e7ada e ame sinceramente as criaturas com quem o destino ordenou que voc\u00ea viva.",
        "es": "Ad\u00e1ptate a las cosas entre las que tu suerte ha sido echada y ama sinceramente a las criaturas con quienes el destino ha ordenado que vivas."
    },
    "Love only what befalls you and is spun for you by fate.": {
        "pt": "Ame apenas o que lhe acontece e \u00e9 tecido para voc\u00ea pelo destino.",
        "es": "Ama solo lo que te sucede y es tejido para ti por el destino."
    },
    "There is only one way to happiness  and that is to cease worrying about things which are beyond the power of our will.": {
        "pt": "S\u00f3 existe um caminho para a felicidade, e \u00e9 parar de se preocupar com coisas que est\u00e3o al\u00e9m do poder da nossa vontade.",
        "es": "Solo hay un camino hacia la felicidad, y es dejar de preocuparse por cosas que est\u00e1n m\u00e1s all\u00e1 del poder de nuestra voluntad."
    },
    "Night brings our troubles to the light rather than banishes them.": {
        "pt": "A noite traz nossos problemas \u00e0 luz em vez de bani-los.",
        "es": "La noche trae nuestros problemas a la luz en vez de desterrarlos."
    },
    "No untroubled day has ever dawned for me.": {
        "pt": "Nenhum dia tranquilo jamais amanheceu para mim.",
        "es": "Ning\u00fan d\u00eda tranquilo ha amanecido jam\u00e1s para m\u00ed."
    },
    "Nothing befalls a man except what is in his nature to endure.": {
        "pt": "Nada acontece a um homem exceto o que est\u00e1 em sua natureza suportar.",
        "es": "Nada le sucede a un hombre excepto lo que est\u00e1 en su naturaleza soportar."
    },
    "Difficulties are things that show what men are.": {
        "pt": "As dificuldades s\u00e3o coisas que mostram o que os homens s\u00e3o.",
        "es": "Las dificultades son cosas que muestran lo que son los hombres."
    },
    "It is not death that a man should fear  he should fear never beginning to live.": {
        "pt": "N\u00e3o \u00e9 a morte que um homem deve temer; ele deve temer nunca come\u00e7ar a viver.",
        "es": "No es la muerte lo que un hombre debe temer; debe temer nunca comenzar a vivir."
    },
    "It is not death or pain that is to be dreaded  but the fear of pain or death.": {
        "pt": "N\u00e3o \u00e9 a morte ou a dor que devem ser temidas, mas o medo da dor ou da morte.",
        "es": "No es la muerte o el dolor lo que debe temerse, sino el miedo al dolor o a la muerte."
    },
    "All philosophy in two words  - sustain and abstain.": {
        "pt": "Toda a filosofia em duas palavras \u2014 suporte e abstenha-se.",
        "es": "Toda la filosof\u00eda en dos palabras \u2014 soporta y abst\u00e9nte."
    },
    "If you are surprised at the number of our maladies  count our cooks.": {
        "pt": "Se voc\u00ea se surpreende com o n\u00famero de nossas doen\u00e7as, conte nossos cozinheiros.",
        "es": "Si te sorprende el n\u00famero de nuestras enfermedades, cuenta nuestros cocineros."
    },
    "Why do we shrink from change? What can come into being save by change?": {
        "pt": "Por que recuamos diante da mudan\u00e7a? O que pode surgir sen\u00e3o pela mudan\u00e7a?",
        "es": "\u00bfPor qu\u00e9 retrocedemos ante el cambio? \u00bfQu\u00e9 puede surgir sino por el cambio?"
    },
    "There is change in all things. You yourself are subject to continual change and some decay  and this is common to the entire universe.": {
        "pt": "H\u00e1 mudan\u00e7a em todas as coisas. Voc\u00ea mesmo est\u00e1 sujeito a mudan\u00e7a cont\u00ednua e algum decl\u00ednio, e isso \u00e9 comum a todo o universo.",
        "es": "Hay cambio en todas las cosas. T\u00fa mismo est\u00e1s sujeto a cambio continuo y cierto declive, y esto es com\u00fan a todo el universo."
    },
    "A man should remove not only unnecessary acts  but also unnecessary thoughts  for then superfluous activity will not follow.": {
        "pt": "Um homem deve remover n\u00e3o apenas atos desnecess\u00e1rios, mas tamb\u00e9m pensamentos desnecess\u00e1rios, pois ent\u00e3o atividades sup\u00e9rfluas n\u00e3o seguir\u00e3o.",
        "es": "Un hombre debe eliminar no solo los actos innecesarios, sino tambi\u00e9n los pensamientos innecesarios, pues entonces las actividades superfluas no seguir\u00e1n."
    },
    "When I think over what I have said  I envy dumb people.": {
        "pt": "Quando penso sobre o que disse, invejo as pessoas mudas.",
        "es": "Cuando pienso en lo que he dicho, envidio a las personas mudas."
    },
    "Constant exposure to dangers will breed contempt for them.": {
        "pt": "A exposi\u00e7\u00e3o constante aos perigos gera desprezo por eles.",
        "es": "La exposici\u00f3n constante a los peligros genera desprecio por ellos."
    },
    "The first rule is to keep an untroubled spirit. The second is to look things in the face and know them for what they are.": {
        "pt": "A primeira regra \u00e9 manter o esp\u00edrito sereno. A segunda \u00e9 olhar as coisas de frente e conhec\u00ea-las pelo que s\u00e3o.",
        "es": "La primera regla es mantener el esp\u00edritu sereno. La segunda es mirar las cosas de frente y conocerlas por lo que son."
    },
    "So when the crisis is upon you  remember that God  like a trainer of wrestlers  has matched you with a tough and stalwart antagonist... that you may prove a victor at the Great Games.": {
        "pt": "Ent\u00e3o, quando a crise estiver sobre voc\u00ea, lembre-se de que Deus, como um treinador de lutadores, o colocou contra um antagonista duro e robusto... para que voc\u00ea prove ser um vencedor nos Grandes Jogos.",
        "es": "Entonces, cuando la crisis est\u00e9 sobre ti, recuerda que Dios, como un entrenador de luchadores, te ha enfrentado con un antagonista duro y robusto... para que pruebes ser un vencedor en los Grandes Juegos."
    },
    "All cruelty springs from weakness.": {
        "pt": "Toda crueldade nasce da fraqueza.",
        "es": "Toda crueldad nace de la debilidad."
    },
    "There is no man so blessed that some who stand by his deathbed won't hail the occasion with delight.": {
        "pt": "N\u00e3o h\u00e1 homem t\u00e3o aben\u00e7oado que alguns que estejam junto ao seu leito de morte n\u00e3o sa\u00fadem a ocasi\u00e3o com deleite.",
        "es": "No hay hombre tan bendecido que algunos que est\u00e9n junto a su lecho de muerte no celebren la ocasi\u00f3n con deleite."
    },
    "Time is like a river of fleeting events  and its current is strong  as soon as something comes into sight  it is swept past us  and something else takes its place  and that too will be swept away.": {
        "pt": "O tempo \u00e9 como um rio de eventos fugazes, e sua corrente \u00e9 forte; assim que algo surge \u00e0 vista, \u00e9 arrastado para al\u00e9m de n\u00f3s, e outra coisa toma seu lugar, e essa tamb\u00e9m ser\u00e1 levada.",
        "es": "El tiempo es como un r\u00edo de eventos fugaces, y su corriente es fuerte; tan pronto como algo aparece a la vista, es arrastrado m\u00e1s all\u00e1 de nosotros, y otra cosa toma su lugar, y esa tambi\u00e9n ser\u00e1 arrastrada."
    },
    "No great thing is created suddenly  any more than a bunch of grapes or a fig. If you tell me that you desire a fig  I answer you that there must be time. Let it first blossom  then bear fruit  then ripen.": {
        "pt": "Nada grandioso \u00e9 criado de repente, assim como um cacho de uvas ou um figo. Se me diz que deseja um figo, respondo que \u00e9 preciso tempo. Deixe-o primeiro florescer, depois dar fruto, depois amadurecer.",
        "es": "Nada grandioso se crea de repente, como un racimo de uvas o un higo. Si me dices que deseas un higo, te respondo que hace falta tiempo. D\u00e9jalo primero florecer, luego dar fruto, luego madurar."
    },
    "Drunkenness is nothing but voluntary madness.": {
        "pt": "A embriaguez nada mais \u00e9 do que loucura volunt\u00e1ria.",
        "es": "La embriaguez no es m\u00e1s que locura voluntaria."
    },
    "He is a drunkard who takes more than three glasses  though he be not drunk.": {
        "pt": "\u00c9 b\u00eabado aquele que toma mais de tr\u00eas copos, mesmo que n\u00e3o esteja embriagado.",
        "es": "Es borracho aquel que toma m\u00e1s de tres vasos, aunque no est\u00e9 ebrio."
    },
    "Consider how much more you often suffer from your anger and grief than from those very things for which you are angry and grieved.": {
        "pt": "Considere quanto mais voc\u00ea frequentemente sofre com sua raiva e tristeza do que com aquelas coisas pelas quais est\u00e1 com raiva e triste.",
        "es": "Considera cu\u00e1nto m\u00e1s sufres a menudo por tu ira y tu pena que por aquellas mismas cosas por las que est\u00e1s enojado y apenado."
    },
    "We are not troubled by things  but by the opinion which we have of things.": {
        "pt": "N\u00e3o somos perturbados pelas coisas, mas pela opini\u00e3o que temos delas.",
        "es": "No nos perturban las cosas, sino la opini\u00f3n que tenemos de ellas."
    },
    "If you are distressed by anything external  the pain is not due to the thing itself but to your own estimate of it  and this you have the power to revoke at any moment.": {
        "pt": "Se voc\u00ea est\u00e1 angustiado por algo externo, a dor n\u00e3o se deve \u00e0 coisa em si, mas \u00e0 sua pr\u00f3pria avalia\u00e7\u00e3o dela, e isso voc\u00ea tem o poder de revogar a qualquer momento.",
        "es": "Si est\u00e1s angustiado por algo externo, el dolor no se debe a la cosa en s\u00ed, sino a tu propia valoraci\u00f3n de ella, y esto tienes el poder de revocarlo en cualquier momento."
    },
    "Men are not influenced by things  but by their thoughts about things.": {
        "pt": "Os homens n\u00e3o s\u00e3o influenciados pelas coisas, mas por seus pensamentos sobre as coisas.",
        "es": "Los hombres no son influenciados por las cosas, sino por sus pensamientos sobre las cosas."
    },
    "On the occasion of every accident that befalls you ... inquire what power you have for turning it to use.": {
        "pt": "Na ocasi\u00e3o de cada acidente que lhe acontece... pergunte que poder voc\u00ea tem para transform\u00e1-lo em algo \u00fatil.",
        "es": "En la ocasi\u00f3n de cada accidente que te sucede... pregunta qu\u00e9 poder tienes para convertirlo en algo \u00fatil."
    },
    "What a great blessing is a friend with a heart so trusty you may safely bury all your secrets in it.": {
        "pt": "Que grande b\u00ean\u00e7\u00e3o \u00e9 um amigo com um cora\u00e7\u00e3o t\u00e3o confi\u00e1vel que voc\u00ea pode seguramente enterrar todos os seus segredos nele.",
        "es": "Qu\u00e9 gran bendici\u00f3n es un amigo con un coraz\u00f3n tan confiable que puedes enterrar con seguridad todos tus secretos en \u00e9l."
    },
    "Whatever the universal nature assigns to any man at any time is for the good of that man at that time.": {
        "pt": "O que quer que a natureza universal atribua a qualquer homem em qualquer momento \u00e9 para o bem desse homem naquele momento.",
        "es": "Lo que la naturaleza universal asigna a cualquier hombre en cualquier momento es para el bien de ese hombre en ese momento."
    },
    "Fate rules the affairs of mankind with no recognizable order.": {
        "pt": "O destino governa os assuntos da humanidade sem nenhuma ordem reconhec\u00edvel.",
        "es": "El destino gobierna los asuntos de la humanidad sin ning\u00fan orden reconocible."
    },
    "A great step toward independence is a good-humoured stomach.": {
        "pt": "Um grande passo em dire\u00e7\u00e3o \u00e0 independ\u00eancia \u00e9 um est\u00f4mago de bom humor.",
        "es": "Un gran paso hacia la independencia es un est\u00f3mago de buen humor."
    },
    "He is a man of sense who does not grieve for what he has not  but rejoices in what he has.": {
        "pt": "\u00c9 um homem sensato aquele que n\u00e3o se lamenta pelo que n\u00e3o tem, mas se alegra com o que tem.",
        "es": "Es un hombre sensato aquel que no se lamenta por lo que no tiene, sino que se alegra con lo que tiene."
    },
    "Take full account of the excellencies which you possess  and in gratitude remember how you would hanker after them  if you had them not.": {
        "pt": "Leve em plena conta as excel\u00eancias que voc\u00ea possui, e com gratid\u00e3o lembre como as desejaria se n\u00e3o as tivesse.",
        "es": "Ten en plena cuenta las excelencias que posees, y con gratitud recuerda cu\u00e1nto las desear\u00edas si no las tuvieras."
    },
    "Freedom is not procured by a full enjoyment of what is desired  but by controlling the desire.": {
        "pt": "A liberdade n\u00e3o \u00e9 obtida pelo pleno gozo do que se deseja, mas pelo controle do desejo.",
        "es": "La libertad no se obtiene por el pleno goce de lo que se desea, sino por el control del deseo."
    },
    "Try to live the life of the good man who is more than content with what is allocated to him.": {
        "pt": "Tente viver a vida do homem bom que est\u00e1 mais do que contente com o que lhe \u00e9 destinado.",
        "es": "Intenta vivir la vida del hombre bueno que est\u00e1 m\u00e1s que contento con lo que le es asignado."
    },
    "Bear and forbear.": {
        "pt": "Suporte e tolere.",
        "es": "Soporta y tolera."
    },
    "The true worth of a man is to be measured by the objects he pursues.": {
        "pt": "O verdadeiro valor de um homem deve ser medido pelos objetos que persegue.",
        "es": "El verdadero valor de un hombre se mide por los objetos que persigue."
    },
    "Without a purpose  nothing should be done.": {
        "pt": "Sem um prop\u00f3sito, nada deve ser feito.",
        "es": "Sin un prop\u00f3sito, nada debe hacerse."
    },
    "First say to yourself what you would be  and then do what you have to do.": {
        "pt": "Primeiro diga a si mesmo o que gostaria de ser, e ent\u00e3o fa\u00e7a o que tem que fazer.",
        "es": "Primero dite a ti mismo lo que te gustar\u00eda ser, y luego haz lo que tengas que hacer."
    },
    "A man's worth is no greater than the worth of his ambitions.": {
        "pt": "O valor de um homem n\u00e3o \u00e9 maior que o valor de suas ambi\u00e7\u00f5es.",
        "es": "El valor de un hombre no es mayor que el valor de sus ambiciones."
    },
    "A man's happiness: to do the things proper to man.": {
        "pt": "A felicidade de um homem: fazer as coisas pr\u00f3prias do homem.",
        "es": "La felicidad de un hombre: hacer las cosas propias del hombre."
    },
    "The one thing worth living for is to keep one's soul pure.": {
        "pt": "A \u00fanica coisa pela qual vale a pena viver \u00e9 manter a alma pura.",
        "es": "La \u00fanica cosa por la que vale la pena vivir es mantener el alma pura."
    },
    "The foremost art of kings is the power to endure hatred.": {
        "pt": "A principal arte dos reis \u00e9 o poder de suportar o \u00f3dio.",
        "es": "El principal arte de los reyes es el poder de soportar el odio."
    },
    "Life will follow the path it started upon, and will neither reverse nor check its course; it will make no noise, it will not remind you of its swiftness. Silent it will glide on; it will not prolong itself at the command of a king, or at the applause of the populace. Just as it was started on its first day, so it will run; nowhere will it turn aside, nowhere will it delay.": {
        "pt": "A vida seguir\u00e1 o caminho em que come\u00e7ou, e n\u00e3o reverter\u00e1 nem deter\u00e1 seu curso; n\u00e3o far\u00e1 barulho, n\u00e3o o lembrar\u00e1 de sua rapidez. Silenciosa, deslizar\u00e1; n\u00e3o se prolongar\u00e1 ao comando de um rei, ou ao aplauso do povo.",
        "es": "La vida seguir\u00e1 el camino en que comenz\u00f3, y no revertir\u00e1 ni detendr\u00e1 su curso; no har\u00e1 ruido, no te recordar\u00e1 su rapidez. Silenciosa se deslizar\u00e1; no se prolongar\u00e1 al mandato de un rey, ni al aplauso del pueblo."
    },
    "Pain is slight if opinion has added nothing to it; ... in thinking it slight, you will make it slight. Everything depends on opinion. It is according to opinion that we suffer. A man is as wretched as he has convinced himself that he is.": {
        "pt": "A dor \u00e9 leve se a opini\u00e3o nada lhe acrescentou; ... pensando que \u00e9 leve, voc\u00ea a tornar\u00e1 leve. Tudo depende da opini\u00e3o. \u00c9 de acordo com a opini\u00e3o que sofremos. Um homem \u00e9 t\u00e3o miser\u00e1vel quanto se convenceu de que \u00e9.",
        "es": "El dolor es leve si la opini\u00f3n nada le ha a\u00f1adido; ... pensando que es leve, lo har\u00e1s leve. Todo depende de la opini\u00f3n. Es seg\u00fan la opini\u00f3n que sufrimos. Un hombre es tan miserable como se ha convencido de que es."
    },
    "If thou workest at that which is before thee ... expecting nothing  fearing nothing  but satisfied with thy present activity according to Nature  and with heroic truth in every word and sound which thou utterest  thou wilt live happy. And there is no man who is able to prevent this.": {
        "pt": "Se trabalhares naquilo que est\u00e1 diante de ti... sem esperar nada, sem temer nada, mas satisfeito com tua atividade presente segundo a Natureza, e com verdade heroica em cada palavra e som que proferires, viver\u00e1s feliz. E n\u00e3o h\u00e1 homem que possa impedir isto.",
        "es": "Si trabajas en lo que est\u00e1 ante ti... sin esperar nada, sin temer nada, sino satisfecho con tu actividad presente seg\u00fan la Naturaleza, y con verdad heroica en cada palabra y sonido que pronuncies, vivir\u00e1s feliz. Y no hay hombre que pueda impedirlo."
    },
    "There is only one way to happiness and that is to cease worrying about things which are beyond the power of our will.": {
        "pt": "S\u00f3 existe um caminho para a felicidade e \u00e9 parar de se preocupar com coisas que est\u00e3o al\u00e9m do poder da nossa vontade.",
        "es": "Solo hay un camino hacia la felicidad y es dejar de preocuparse por cosas que est\u00e1n m\u00e1s all\u00e1 del poder de nuestra voluntad."
    },
    "Learn how to feel joy.": {
        "pt": "Aprenda a sentir alegria.",
        "es": "Aprende a sentir alegr\u00eda."
    },
    "To live happily is an inward power of the soul.": {
        "pt": "Viver feliz \u00e9 um poder interior da alma.",
        "es": "Vivir feliz es un poder interior del alma."
    },
    "The happiness of your life depends upon the quality of your thoughts.": {
        "pt": "A felicidade da sua vida depende da qualidade dos seus pensamentos.",
        "es": "La felicidad de tu vida depende de la calidad de tus pensamientos."
    },
    "Whom they have injured  they also hate.": {
        "pt": "A quem feriram, tamb\u00e9m odeiam.",
        "es": "A quienes han herido, tambi\u00e9n odian."
    },
    "I often marvel how it is that though each man loves himself beyond all else  he should yet value his own opinion of himself less than that of others.": {
        "pt": "Frequentemente me maravilho como \u00e9 que, embora cada homem ame a si mesmo acima de tudo, ele ainda valorize menos sua pr\u00f3pria opini\u00e3o sobre si mesmo do que a dos outros.",
        "es": "A menudo me maravillo de c\u00f3mo, aunque cada hombre se ama a s\u00ed mismo por encima de todo, a\u00fan valora menos su propia opini\u00f3n de s\u00ed mismo que la de los dem\u00e1s."
    },
    "A hungry people listens not to reason  nor cares for justice  nor is bent by any prayers.": {
        "pt": "Um povo faminto n\u00e3o escuta a raz\u00e3o, nem se importa com a justi\u00e7a, nem se dobra por nenhuma prece.",
        "es": "Un pueblo hambriento no escucha a la raz\u00f3n, ni se preocupa por la justicia, ni se dobla por ninguna plegaria."
    },
    "It is often better not to see an insult than to avenge it.": {
        "pt": "Muitas vezes \u00e9 melhor n\u00e3o ver um insulto do que ving\u00e1-lo.",
        "es": "Muchas veces es mejor no ver un insulto que vengarlo."
    },
    "It is often better not to see an insult  than to avenge it.": {
        "pt": "Muitas vezes \u00e9 melhor n\u00e3o ver um insulto do que ving\u00e1-lo.",
        "es": "Muchas veces es mejor no ver un insulto que vengarlo."
    },
    "Accept the things To which fate binds you and Love the people with whom fate Brings you together But do so with all your heart.": {
        "pt": "Aceite as coisas \u00e0s quais o destino o prende e ame as pessoas com quem o destino o re\u00fane. Mas fa\u00e7a-o com todo o seu cora\u00e7\u00e3o.",
        "es": "Acepta las cosas a las que el destino te ata y ama a las personas con quienes el destino te re\u00fane. Pero hazlo con todo tu coraz\u00f3n."
    },
    "Injustice never rules forever.": {
        "pt": "A injusti\u00e7a nunca reina para sempre.",
        "es": "La injusticia nunca reina para siempre."
    },
    "He who decides a case without hearing the other side  though he decide justly  cannot be considered just.": {
        "pt": "Aquele que decide um caso sem ouvir o outro lado, embora decida com justi\u00e7a, n\u00e3o pode ser considerado justo.",
        "es": "Aquel que decide un caso sin escuchar al otro lado, aunque decida con justicia, no puede ser considerado justo."
    },
    "Men learn while they teach.": {
        "pt": "Os homens aprendem enquanto ensinam.",
        "es": "Los hombres aprenden mientras ense\u00f1an."
    },
    "Life is a stranger's sojourn  a night at an inn.": {
        "pt": "A vida \u00e9 a estadia de um estrangeiro, uma noite numa estalagem.",
        "es": "La vida es la estad\u00eda de un extranjero, una noche en una posada."
    },
    "The art of living is more like that of wrestling than of dancing. The main thing is to stand firm and be ready for an unforeseen attack.": {
        "pt": "A arte de viver \u00e9 mais parecida com a da luta do que com a da dan\u00e7a. O principal \u00e9 ficar firme e estar pronto para um ataque imprevisto.",
        "es": "El arte de vivir se parece m\u00e1s al de la lucha que al de la danza. Lo principal es mantenerse firme y estar listo para un ataque imprevisto."
    },
    "As is a tale  so is life: not how long it is  but how good it is  is what matters.": {
        "pt": "Assim como um conto, assim \u00e9 a vida: n\u00e3o importa qu\u00e3o longa ela \u00e9, mas qu\u00e3o boa ela \u00e9.",
        "es": "Como un cuento, as\u00ed es la vida: no importa cu\u00e1n larga sea, sino cu\u00e1n buena sea."
    },
}

tr.update(new)

with open('c:/Users/lalli/Flutter/coach_phrase_app/translations_stoicism.json', 'w', encoding='utf-8') as f:
    json.dump(tr, f, ensure_ascii=False, indent=2)

print(f'Total stoicism translations: {len(tr)}')
