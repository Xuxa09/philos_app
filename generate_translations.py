"""
Generate translations JSON for epicureanism and rationalism quotes.
Reads quotes_to_translate.json and produces translations_extra.json
"""
import json

# Read source quotes
with open('c:/Users/lalli/Flutter/coach_phrase_app/quotes_to_translate.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

translations = {}

# === EPICUREANISM TRANSLATIONS ===
epic = {
    "Death, therefore, the most awful of evils, is nothing to us, seeing that, when we are, death is not come, and, when death is come, we are not.": {
        "pt": "A morte, portanto, o mais terrível dos males, nada é para nós, visto que, quando existimos, a morte não chegou, e, quando a morte chega, nós não existimos.",
        "es": "La muerte, por tanto, el más terrible de los males, nada es para nosotros, ya que, cuando existimos, la muerte no ha llegado, y, cuando la muerte llega, nosotros no existimos."
    },
    "He who is not satisfied with a little, is satisfied with nothing .": {
        "pt": "Aquele que não se satisfaz com pouco, não se satisfaz com nada.",
        "es": "Aquel que no se satisface con poco, no se satisface con nada."
    },
    "Never say that I have taken it, only that I have given it back.": {
        "pt": "Nunca diga que eu tomei, apenas que eu devolvi.",
        "es": "Nunca digas que lo he tomado, solo que lo he devuelto."
    },
    'Pactum serva" - "Keep the faith': {
        "pt": 'Pactum serva" - "Mantenha a fé',
        "es": 'Pactum serva" - "Mantén la fe'
    },
    "If you wish to make Pythocles rich, do not add to his store of money, but subtract from his desires.": {
        "pt": "Se deseja tornar Pítocles rico, não acrescente ao seu estoque de dinheiro, mas subtraia de seus desejos.",
        "es": "Si deseas hacer rico a Pitocles, no añadas a su reserva de dinero, sino resta de sus deseos."
    },
    "He who says either that the time for philosophy has not yet come or that it has passed is like someone who says that the time for happiness has not yet come or that it has passed.": {
        "pt": "Aquele que diz que o tempo para a filosofia ainda não chegou ou que já passou é como alguém que diz que o tempo para a felicidade ainda não chegou ou que já passou.",
        "es": "Quien dice que el tiempo para la filosofía aún no ha llegado o que ya ha pasado es como quien dice que el tiempo para la felicidad aún no ha llegado o que ya ha pasado."
    },
    "Empty is the argument of the philosopher which does not relieve any human suffering.": {
        "pt": "Vazio é o argumento do filósofo que não alivia nenhum sofrimento humano.",
        "es": "Vacío es el argumento del filósofo que no alivia ningún sufrimiento humano."
    },
    "Let no one delay the study of philosophy while young nor weary of it when old.": {
        "pt": "Que ninguém adie o estudo da filosofia enquanto jovem nem se canse dele quando velho.",
        "es": "Que nadie postergue el estudio de la filosofía mientras es joven ni se canse de él cuando sea viejo."
    },
    "Is God willing to prevent evil, but not able? Then he is not omnipotent. Is he able, but not willing? Then he is malevolent. Is he both able and willing? Then whence cometh evil? Is he neither able nor willing? Then why call him God?": {
        "pt": "Deus está disposto a prevenir o mal, mas não é capaz? Então ele não é onipotente. Ele é capaz, mas não está disposto? Então ele é malevolente. Ele é tanto capaz quanto disposto? Então de onde vem o mal? Ele não é nem capaz nem disposto? Então por que chamá-lo de Deus?",
        "es": "¿Dios está dispuesto a prevenir el mal, pero no es capaz? Entonces no es omnipotente. ¿Es capaz, pero no está dispuesto? Entonces es malévolo. ¿Es capaz y está dispuesto? Entonces, ¿de dónde viene el mal? ¿No es capaz ni está dispuesto? Entonces, ¿por qué llamarlo Dios?"
    },
    "Begin, be bold, and venture to be wise.": {
        "pt": "Comece, seja ousado e atreva-se a ser sábio.",
        "es": "Comienza, sé audaz y atrévete a ser sabio."
    },
    "The noble man is chiefly concerned with wisdom and friendship; of these, the former is a mortal good, the latter and immortal one.": {
        "pt": "O homem nobre se preocupa principalmente com a sabedoria e a amizade; destas, a primeira é um bem mortal, a segunda um bem imortal.",
        "es": "El hombre noble se preocupa principalmente por la sabiduría y la amistad; de estas, la primera es un bien mortal, la segunda un bien inmortal."
    },
    "he who is greedy is always in want": {
        "pt": "aquele que é ganancioso está sempre em necessidade",
        "es": "aquel que es codicioso siempre está en necesidad"
    },
    "Rule your mind or it will rule you.": {
        "pt": "Governe sua mente ou ela governará você.",
        "es": "Gobierna tu mente o ella te gobernará."
    },
    "It is not so much our friends' help that helps us as the confident knowledge that they will help us.": {
        "pt": "Não é tanto a ajuda dos nossos amigos que nos ajuda, mas o conhecimento confiante de que eles nos ajudarão.",
        "es": "No es tanto la ayuda de nuestros amigos lo que nos ayuda, sino el conocimiento seguro de que nos ayudarán."
    },
    "In love there are two evils: war and peace.": {
        "pt": "No amor há dois males: a guerra e a paz.",
        "es": "En el amor hay dos males: la guerra y la paz."
    },
    "Make money, money by fair means if you can, if not, but any means money.": {
        "pt": "Ganhe dinheiro, dinheiro por meios honestos se puder, se não, por quaisquer meios, dinheiro.",
        "es": "Gana dinero, dinero por medios honestos si puedes, si no, por cualquier medio, dinero."
    },
    "He who postpones the hour of living rightly is like the rustic who waits for the river to run out before he crosses.": {
        "pt": "Aquele que adia a hora de viver corretamente é como o camponês que espera o rio secar antes de atravessá-lo.",
        "es": "Aquel que pospone la hora de vivir correctamente es como el rústico que espera a que el río se seque antes de cruzarlo."
    },
    "There are words and accents by which this grief can be assuaged, and the disease in a great measure removed.": {
        "pt": "Há palavras e acentos pelos quais essa dor pode ser aliviada, e a doença em grande medida removida.",
        "es": "Hay palabras y acentos con los que este dolor puede ser aliviado, y la enfermedad en gran medida eliminada."
    },
    "Captive Greece captured her rude conqueror": {
        "pt": "A Grécia cativa capturou seu rude conquistador",
        "es": "La Grecia cautiva capturó a su rudo conquistador"
    },
    "Anger is a brief madness.": {
        "pt": "A raiva é uma breve loucura.",
        "es": "La ira es una breve locura."
    },
    "So long as we exist, death is not with us; but when death comes, then we do not exist": {
        "pt": "Enquanto existimos, a morte não está conosco; mas quando a morte chega, então nós não existimos",
        "es": "Mientras existimos, la muerte no está con nosotros; pero cuando la muerte llega, entonces no existimos"
    },
    "He has half the deed done who has made a beginning.": {
        "pt": "Já fez metade da obra aquele que começou.",
        "es": "Ya ha hecho la mitad de la obra quien ha comenzado."
    },
    "He who least needs tomorrow, will most gladly greet tomorrow.": {
        "pt": "Aquele que menos precisa do amanhã, mais alegremente saudará o amanhã.",
        "es": "Aquel que menos necesita del mañana, con más alegría recibirá el mañana."
    },
    "The time when you should most of all withdraw into yourself is when you are forced to be in a crowd.": {
        "pt": "O momento em que você mais deve se recolher é quando é forçado a estar no meio da multidão.",
        "es": "El momento en que más debes recogerte en ti mismo es cuando te ves forzado a estar entre la multitud."
    },
    "Capture your reader, let him not depart, from dull beginnings that refuse to start": {
        "pt": "Capture seu leitor, não o deixe partir, de começos monótonos que se recusam a começar",
        "es": "Captura a tu lector, no lo dejes partir, de comienzos aburridos que se niegan a empezar"
    },
    "Nothing is sufficient for the person who finds sufficiency too little": {
        "pt": "Nada é suficiente para a pessoa que acha a suficiência muito pouco",
        "es": "Nada es suficiente para quien encuentra la suficiencia demasiado poca"
    },
    "Faults are soon copied.": {
        "pt": "Os defeitos são logo copiados.",
        "es": "Los defectos se copian pronto."
    },
    "If the gods listened to the prayers of men, all men would quickly have perished: for they are forever praying for evil against one another": {
        "pt": "Se os deuses ouvissem as orações dos homens, todos os homens teriam perecido rapidamente: pois estão sempre rezando por males uns contra os outros",
        "es": "Si los dioses escucharan las oraciones de los hombres, todos los hombres habrían perecido rápidamente: pues siempre están rezando por males unos contra otros"
    },
    "If thou wilt make a man happy, add not unto his riches but take away from his desires.": {
        "pt": "Se queres fazer um homem feliz, não acrescentes às suas riquezas, mas subtraia de seus desejos.",
        "es": "Si quieres hacer feliz a un hombre, no añadas a sus riquezas sino quita de sus deseos."
    },
    "Pale Death with impartial tread beats at the poor man's cottage door and at the palaces of kings.": {
        "pt": "A pálida Morte com passo imparcial bate à porta da cabana do pobre e nos palácios dos reis.",
        "es": "La pálida Muerte con paso imparcial golpea la puerta de la cabaña del pobre y los palacios de los reyes."
    },
    "Now is the time to drink!": {
        "pt": "Agora é hora de beber!",
        "es": "¡Ahora es el momento de beber!"
    },
    "What it is forbidden to be put right becomes lighter by acceptance.": {
        "pt": "Aquilo que é proibido corrigir se torna mais leve pela aceitação.",
        "es": "Lo que está prohibido corregir se vuelve más ligero con la aceptación."
    },
    "Better to accept whatever happens.": {
        "pt": "Melhor aceitar o que quer que aconteça.",
        "es": "Mejor aceptar lo que sea que suceda."
    },
    "Adversity has the effect of eliciting talents  which  in prosperous circumstances  would have lain dormant.": {
        "pt": "A adversidade tem o efeito de revelar talentos que, em circunstâncias prósperas, teriam permanecido adormecidos.",
        "es": "La adversidad tiene el efecto de revelar talentos que, en circunstancias prósperas, habrían permanecido dormidos."
    },
    "Adversity reveals genius  prosperity conceals it.": {
        "pt": "A adversidade revela o gênio, a prosperidade o esconde.",
        "es": "La adversidad revela el genio, la prosperidad lo oculta."
    },
    "Whatever advice you give  be short.": {
        "pt": "Qualquer conselho que dê, seja breve.",
        "es": "Cualquier consejo que des, sé breve."
    },
    "Anger is momentary madness  so control your passion or it will control you.": {
        "pt": "A raiva é uma loucura momentânea, portanto controle sua paixão ou ela controlará você.",
        "es": "La ira es una locura momentánea, así que controla tu pasión o ella te controlará."
    },
    "A picture is a poem without words.": {
        "pt": "Uma imagem é um poema sem palavras.",
        "es": "Una imagen es un poema sin palabras."
    },
    "Well begun is half done.": {
        "pt": "Bem começado é meio caminho andado.",
        "es": "Lo bien comenzado está medio hecho."
    },
    "In times of stress  be bold and valiant.": {
        "pt": "Em tempos de estresse, seja ousado e valente.",
        "es": "En tiempos de estrés, sé audaz y valiente."
    },
    "Fools  through false shame  conceal their open wounds.": {
        "pt": "Os tolos, por falsa vergonha, escondem suas feridas abertas.",
        "es": "Los necios, por falsa vergüenza, ocultan sus heridas abiertas."
    },
    "It is courage  courage  courage  that raises the blood of life to crimson splendor. Live bravely and present a brave front to adversity!": {
        "pt": "É a coragem, coragem, coragem que eleva o sangue da vida ao esplendor carmesim. Viva bravamente e apresente uma frente corajosa à adversidade!",
        "es": "Es el coraje, coraje, coraje lo que eleva la sangre de la vida al esplendor carmesí. ¡Vive con valentía y presenta un frente valiente ante la adversidad!"
    },
    "Dare to begin! He who postpones living rightly is like the rustic who waits for the river to run out before he crosses.": {
        "pt": "Ouse começar! Aquele que adia viver corretamente é como o camponês que espera o rio secar antes de atravessá-lo.",
        "es": "¡Atrévete a comenzar! Aquel que pospone vivir correctamente es como el rústico que espera a que el río se seque antes de cruzarlo."
    },
    "The time when  most of all  you should withdraw into yourself is when you are forced to be in a crowd.": {
        "pt": "O momento em que, acima de tudo, você deve se recolher em si mesmo é quando é forçado a estar no meio da multidão.",
        "es": "El momento en que, sobre todo, debes recogerte en ti mismo es cuando te ves forzado a estar entre la multitud."
    },
    "The art of living well and the art of dying well are one.": {
        "pt": "A arte de viver bem e a arte de morrer bem são uma só.",
        "es": "El arte de vivir bien y el arte de morir bien son uno solo."
    },
    "He who postpones the hour of living is like the rustic who waits for the river to run out before he crosses.": {
        "pt": "Aquele que adia a hora de viver é como o camponês que espera o rio secar antes de atravessá-lo.",
        "es": "Aquel que pospone la hora de vivir es como el rústico que espera a que el río se seque antes de cruzarlo."
    },
    "If matters go badly now  they will not always be so.": {
        "pt": "Se as coisas vão mal agora, nem sempre será assim.",
        "es": "Si las cosas van mal ahora, no siempre será así."
    },
    "In adversity  remember to keep an even mind.": {
        "pt": "Na adversidade, lembre-se de manter a mente equilibrada.",
        "es": "En la adversidad, recuerda mantener la mente serena."
    },
    "Of all the things which wisdom provides to make us entirely happy  much the greatest is the possession of friendship.": {
        "pt": "De todas as coisas que a sabedoria proporciona para nos tornar inteiramente felizes, a maior é a posse da amizade.",
        "es": "De todas las cosas que la sabiduría proporciona para hacernos completamente felices, la mayor es la posesión de la amistad."
    },
    "Your own property is concerned when your neighbor's house is on fire.": {
        "pt": "Sua própria propriedade está em risco quando a casa do vizinho está pegando fogo.",
        "es": "Tu propia propiedad está en riesgo cuando la casa del vecino está en llamas."
    },
    "Anger is a short madness.": {
        "pt": "A raiva é uma breve loucura.",
        "es": "La ira es una breve locura."
    },
    "Only a stomach that rarely feels hungry scorns common things.": {
        "pt": "Só um estômago que raramente sente fome despreza as coisas comuns.",
        "es": "Solo un estómago que rara vez siente hambre desprecia las cosas comunes."
    },
    "The summit of pleasure is the elimination of all that gives pain.": {
        "pt": "O ápice do prazer é a eliminação de tudo que causa dor.",
        "es": "La cumbre del placer es la eliminación de todo lo que causa dolor."
    },
    "Do not spoil what you have by desiring what you have not  remember that what you now have was once among the things only hoped for.": {
        "pt": "Não estrague o que você tem desejando o que não tem; lembre-se de que o que você agora tem já esteve entre as coisas apenas esperadas.",
        "es": "No estropees lo que tienes deseando lo que no tienes; recuerda que lo que ahora tienes estuvo una vez entre las cosas solo esperadas."
    },
    "Let him who has enough wish for nothing more.": {
        "pt": "Que aquele que tem o suficiente não deseje nada mais.",
        "es": "Que aquel que tiene suficiente no desee nada más."
    },
    "Nothing is enough to the man for whom enough is too little.": {
        "pt": "Nada é suficiente para o homem para quem o suficiente é muito pouco.",
        "es": "Nada es suficiente para el hombre para quien lo suficiente es muy poco."
    },
    "Whoever does not regard what he has as most ample wealth is unhappy  though he is master of the world.": {
        "pt": "Quem não considera o que tem como a mais ampla riqueza é infeliz, ainda que seja senhor do mundo.",
        "es": "Quien no considera lo que tiene como la más amplia riqueza es infeliz, aunque sea dueño del mundo."
    },
    "Were a man to order his life by the rules of true reason  a frugal substance joined to a contented mind is for him great riches.": {
        "pt": "Se um homem ordenasse sua vida pelas regras da verdadeira razão, uma substância frugal unida a uma mente contente seria para ele grande riqueza.",
        "es": "Si un hombre ordenara su vida por las reglas de la verdadera razón, una sustancia frugal unida a una mente contenta sería para él gran riqueza."
    },
    "Of all the things which wisdom provides to make life entirely happy  much the greatest is the possession of friendship.": {
        "pt": "De todas as coisas que a sabedoria proporciona para tornar a vida inteiramente feliz, a maior é a posse da amizade.",
        "es": "De todas las cosas que la sabiduría proporciona para hacer la vida completamente feliz, la mayor es la posesión de la amistad."
    },
    "It is not so much our friends' help that helps us  as the confidence of their help.": {
        "pt": "Não é tanto a ajuda dos nossos amigos que nos ajuda, mas a confiança de sua ajuda.",
        "es": "No es tanto la ayuda de nuestros amigos lo que nos ayuda, sino la confianza en su ayuda."
    },
    "He who is greedy is always in want.": {
        "pt": "Aquele que é ganancioso está sempre em necessidade.",
        "es": "Aquel que es codicioso siempre está en necesidad."
    },
    "You will live wisely if you are happy in your lot.": {
        "pt": "Viverá sabiamente se estiver feliz com sua sorte.",
        "es": "Vivirás sabiamente si estás feliz con tu suerte."
    },
    "Never despair.": {
        "pt": "Nunca desespere.",
        "es": "Nunca desesperes."
    },
    "I teach that all men are mad.": {
        "pt": "Ensino que todos os homens são loucos.",
        "es": "Enseño que todos los hombres están locos."
    },
    "Acquittal of the guilty damns the judge.": {
        "pt": "A absolvição do culpado condena o juiz.",
        "es": "La absolución del culpable condena al juez."
    },
    "One cannot know everything.": {
        "pt": "Não se pode saber tudo.",
        "es": "No se puede saber todo."
    },
    "The musician who always plays on the same string  is laughed at.": {
        "pt": "O músico que sempre toca a mesma corda é motivo de riso.",
        "es": "El músico que siempre toca la misma cuerda es objeto de risa."
    },
    "When your neighbor's house is afire your own property is at stake.": {
        "pt": "Quando a casa do vizinho está pegando fogo, sua própria propriedade está em risco.",
        "es": "Cuando la casa del vecino está en llamas, tu propia propiedad está en juego."
    },
    "The drops of rain make a hole in the stone not by violence  but by oft falling.": {
        "pt": "As gotas de chuva fazem um buraco na pedra não pela violência, mas pela queda frequente.",
        "es": "Las gotas de lluvia hacen un agujero en la piedra no por la violencia, sino por caer con frecuencia."
    },
    "Live mindful of how brief your life is.": {
        "pt": "Viva consciente de quão breve é sua vida.",
        "es": "Vive consciente de cuán breve es tu vida."
    },
    "Gladly accept the gifts of the present hour.": {
        "pt": "Aceite com alegria os presentes da hora presente.",
        "es": "Acepta con alegría los regalos de la hora presente."
    },
    "No one is content with his own lot.": {
        "pt": "Ninguém está contente com sua própria sorte.",
        "es": "Nadie está contento con su propia suerte."
    },
    "In Rome you long for the country. In the country you praise to the skies the distant town.": {
        "pt": "Em Roma você anseia pelo campo. No campo você elogia aos céus a cidade distante.",
        "es": "En Roma anhelas el campo. En el campo alabas hasta los cielos la ciudad distante."
    },
    "Pale death with impartial tread beats at the poor man's cottage door and at the palaces of kings.": {
        "pt": "A pálida morte com passo imparcial bate à porta da cabana do pobre e nos palácios dos reis.",
        "es": "La pálida muerte con paso imparcial golpea la puerta de la cabaña del pobre y los palacios de los reyes."
    },
    "Any device whatever by which one frees himself from fear is a natural good.": {
        "pt": "Qualquer recurso pelo qual alguém se liberta do medo é um bem natural.",
        "es": "Cualquier recurso por el cual uno se libera del miedo es un bien natural."
    },
    "The man is either mad or he is making verses.": {
        "pt": "O homem ou está louco ou está fazendo versos.",
        "es": "El hombre o está loco o está haciendo versos."
    },
    "Let your poem be kept nine years.": {
        "pt": "Guarde seu poema por nove anos.",
        "es": "Guarda tu poema por nueve años."
    },
    "It is vain to ask of the gods what man is capable of supplying for himself.": {
        "pt": "É vão pedir aos deuses o que o homem é capaz de fornecer a si mesmo.",
        "es": "Es vano pedir a los dioses lo que el hombre es capaz de proporcionarse a sí mismo."
    },
    "The greater the difficulty  the more glory in surmounting it.": {
        "pt": "Quanto maior a dificuldade, mais glória em superá-la.",
        "es": "Cuanto mayor la dificultad, más gloria en superarla."
    },
    "We set up harsh and unkind rules against ourselves. No one is born without faults. That man is best who has fewest.": {
        "pt": "Estabelecemos regras duras e cruéis contra nós mesmos. Ninguém nasce sem defeitos. O melhor homem é aquele que tem menos.",
        "es": "Establecemos reglas duras y crueles contra nosotros mismos. Nadie nace sin defectos. El mejor hombre es el que tiene menos."
    },
    "Dismiss the old horse in good time  lest he fail in the lists and the spectators laugh.": {
        "pt": "Dispense o velho cavalo a tempo, para que ele não falhe na arena e os espectadores riam.",
        "es": "Despide al viejo caballo a tiempo, para que no falle en la arena y los espectadores se rían."
    },
    "Choose a subject equal to your abilities  think carefully what your shoulders may refuse  and what they are capable of bearing.": {
        "pt": "Escolha um assunto igual às suas habilidades; pense cuidadosamente no que seus ombros podem recusar e no que são capazes de suportar.",
        "es": "Elige un tema igual a tus habilidades; piensa cuidadosamente qué pueden rechazar tus hombros y qué son capaces de soportar."
    },
    "Sport begets tumultuous strife and wrath  and wrath begets fierce quarrels and war to the death.": {
        "pt": "O esporte gera conflito tumultuoso e ira, e a ira gera ferozes disputas e guerra até a morte.",
        "es": "El deporte engendra contienda tumultuosa e ira, y la ira engendra feroces disputas y guerra a muerte."
    },
    "Cease to inquire what the future has in store  and take as a gift whatever the day brings forth.": {
        "pt": "Pare de perguntar o que o futuro reserva e aceite como presente o que o dia traz.",
        "es": "Deja de preguntar qué depara el futuro y acepta como regalo lo que el día trae."
    },
    "The flesh endures the storms of the present alone  the mind  those of the past and future as well as the present.": {
        "pt": "A carne suporta apenas as tempestades do presente; a mente, as do passado e do futuro, além do presente.",
        "es": "La carne soporta solo las tormentas del presente; la mente, las del pasado y del futuro, además del presente."
    },
    "Seize the day  and put the least possible trust in tomorrow.": {
        "pt": "Aproveite o dia e deposite a menor confiança possível no amanhã.",
        "es": "Aprovecha el día y deposita la menor confianza posible en el mañana."
    },
    "The flesh endures the storms of the present alone  the mind those of the past and future as well.": {
        "pt": "A carne suporta apenas as tempestades do presente; a mente, também as do passado e do futuro.",
        "es": "La carne soporta solo las tormentas del presente; la mente, también las del pasado y del futuro."
    },
    "Who knows if the gods above will add tomorrow's span to this day's sum?": {
        "pt": "Quem sabe se os deuses acima acrescentarão o prazo de amanhã à soma deste dia?",
        "es": "¿Quién sabe si los dioses de arriba añadirán el plazo de mañana a la suma de este día?"
    },
    "The man least dependent upon the morrow goes to meet the morrow most cheerfully.": {
        "pt": "O homem menos dependente do amanhã vai ao encontro do amanhã com mais alegria.",
        "es": "El hombre menos dependiente del mañana va al encuentro del mañana con más alegría."
    },
    "The changing year's progressive plan Proclaims mortality to man.": {
        "pt": "O plano progressivo do ano que muda proclama a mortalidade ao homem.",
        "es": "El plan progresivo del año cambiante proclama la mortalidad al hombre."
    },
    "Enjoy the present day  trusting very little to the morrow.": {
        "pt": "Aproveite o dia presente, confiando muito pouco no amanhã.",
        "es": "Disfruta el día presente, confiando muy poco en el mañana."
    },
    "Riches either serve or govern the possessor.": {
        "pt": "As riquezas ou servem ou governam o possuidor.",
        "es": "Las riquezas o sirven o gobiernan al poseedor."
    },
    "He who begun has half done. Dare to be wise  begin.": {
        "pt": "Quem começou já fez metade. Ouse ser sábio, comece.",
        "es": "Quien ha comenzado ha hecho la mitad. Atrévete a ser sabio, comienza."
    },
    "To be rich is not the end  but only a change  of worries.": {
        "pt": "Ser rico não é o fim, mas apenas uma mudança de preocupações.",
        "es": "Ser rico no es el fin, sino solo un cambio de preocupaciones."
    },
    "Do not spoil what you have by desiring what you have not remember that what you now have was once among the things you only hoped for.": {
        "pt": "Não estrague o que você tem desejando o que não tem; lembre-se de que o que você agora tem já esteve entre as coisas que apenas esperava.",
        "es": "No estropees lo que tienes deseando lo que no tienes; recuerda que lo que ahora tienes estuvo una vez entre las cosas que solo esperabas."
    },
    "The pen is the tongue of the mind.": {
        "pt": "A caneta é a língua da mente.",
        "es": "La pluma es la lengua de la mente."
    },
    "The envious man grows lean at the success of his neighbor.": {
        "pt": "O invejoso emagrece com o sucesso do vizinho.",
        "es": "El envidioso adelgaza con el éxito de su vecino."
    },
    "Life grants nothing to us mortals without hard work.": {
        "pt": "A vida não concede nada a nós mortais sem trabalho árduo.",
        "es": "La vida no concede nada a los mortales sin trabajo duro."
    },
    "It is the false shame of fools to try to conceal wounds that have not healed.": {
        "pt": "É a falsa vergonha dos tolos tentar esconder feridas que não cicatrizaram.",
        "es": "Es la falsa vergüenza de los necios intentar ocultar heridas que no han sanado."
    },
    "Pale Death beats equally at the poor man's gate and at the palaces of kings.": {
        "pt": "A pálida Morte bate igualmente no portão do pobre e nos palácios dos reis.",
        "es": "La pálida Muerte golpea igualmente en la puerta del pobre y en los palacios de los reyes."
    },
    "It is possible to provide security against other ills, but as far as death is concerned, we men live in a city without walls.": {
        "pt": "É possível se proteger contra outros males, mas no que diz respeito à morte, nós homens vivemos numa cidade sem muros.",
        "es": "Es posible protegerse contra otros males, pero en lo que respecta a la muerte, los hombres vivimos en una ciudad sin muros."
    },
    "You traverse the world in search of happiness, which is within the reach of every man. A contented mind confers it on all.": {
        "pt": "Você percorre o mundo em busca da felicidade, que está ao alcance de todo homem. Uma mente contente a confere a todos.",
        "es": "Recorres el mundo en busca de la felicidad, que está al alcance de todo hombre. Una mente contenta la confiere a todos."
    },
    "What is food to one man is bitter poison to others.": {
        "pt": "O que é alimento para um homem é veneno amargo para outros.",
        "es": "Lo que es alimento para un hombre es veneno amargo para otros."
    },
    "So potent was religion in persuading to evil deeds.": {
        "pt": "Tão poderosa era a religião em persuadir a atos malignos.",
        "es": "Tan poderosa era la religión en persuadir a actos malvados."
    },
    "Such are the heights of wickedness to which men are driven by religion.": {
        "pt": "Tais são as alturas de maldade às quais os homens são levados pela religião.",
        "es": "Tales son las alturas de maldad a las que los hombres son llevados por la religión."
    },
    "A heart well prepared for adversity in bad times hopes, and in good times fears for a change in fortune.": {
        "pt": "Um coração bem preparado para a adversidade espera nos maus tempos, e nos bons tempos teme uma mudança na fortuna.",
        "es": "Un corazón bien preparado para la adversidad espera en los malos tiempos, y en los buenos tiempos teme un cambio en la fortuna."
    },
    "It is folly for a man to pray to the gods for that which he has the power to obtain by himself.": {
        "pt": "É tolice um homem orar aos deuses por aquilo que tem o poder de obter por si mesmo.",
        "es": "Es locura que un hombre rece a los dioses por aquello que tiene el poder de obtener por sí mismo."
    },
    "If God listened to the prayers of men, all men would quickly have perished: for they are forever praying for evil against one another.": {
        "pt": "Se Deus ouvisse as orações dos homens, todos os homens teriam perecido rapidamente: pois estão sempre orando por males uns contra os outros.",
        "es": "Si Dios escuchara las oraciones de los hombres, todos los hombres habrían perecido rápidamente: pues siempre están rezando por males unos contra otros."
    },
    "Knowledge without education is but armed injustice.": {
        "pt": "Conhecimento sem educação é apenas injustiça armada.",
        "es": "Conocimiento sin educación es solo injusticia armada."
    },
    "Suffering is but another name for the teaching of experience, which is the parent of instruction and the schoolmaster of life.": {
        "pt": "O sofrimento é apenas outro nome para o ensinamento da experiência, que é a mãe da instrução e o mestre-escola da vida.",
        "es": "El sufrimiento es solo otro nombre para la enseñanza de la experiencia, que es la madre de la instrucción y el maestro de la vida."
    },
    "It is better for you to be free of fear lying upon a pallet, than to have a golden couch and a rich table and be full of trouble.": {
        "pt": "É melhor para você estar livre do medo deitado numa esteira do que ter um sofá dourado e uma mesa farta e estar cheio de problemas.",
        "es": "Es mejor para ti estar libre de miedo acostado en un jergón que tener un sofá dorado y una mesa rica y estar lleno de problemas."
    },
    "It is courage, courage, courage, that raises the blood of life to crimson splendor. Live bravely and present a brave front to adversity.": {
        "pt": "É a coragem, coragem, coragem que eleva o sangue da vida ao esplendor carmesim. Viva bravamente e apresente uma frente corajosa à adversidade.",
        "es": "Es el coraje, coraje, coraje lo que eleva la sangre de la vida al esplendor carmesí. Vive con valentía y presenta un frente valiente ante la adversidad."
    },
    "It is great wealth to a soul to live frugally with a contented mind.": {
        "pt": "É grande riqueza para a alma viver frugalmente com uma mente contente.",
        "es": "Es gran riqueza para el alma vivir frugalmente con una mente contenta."
    },
    "Seize the day, and put the least possible trust in tomorrow.": {
        "pt": "Aproveite o dia e deposite a menor confiança possível no amanhã.",
        "es": "Aprovecha el día y deposita la menor confianza posible en el mañana."
    },
    "Of all the things which wisdom provides to make us entirely happy, much the greatest is the possession of friendship.": {
        "pt": "De todas as coisas que a sabedoria proporciona para nos tornar inteiramente felizes, a maior é a posse da amizade.",
        "es": "De todas las cosas que la sabiduría proporciona para hacernos completamente felices, la mayor es la posesión de la amistad."
    },
    "It is not so much our friends' help that helps us, as the confidence of their help.": {
        "pt": "Não é tanto a ajuda dos nossos amigos que nos ajuda, mas a confiança de sua ajuda.",
        "es": "No es tanto la ayuda de nuestros amigos lo que nos ayuda, sino la confianza en su ayuda."
    },
    "Sad people dislike the happy, and the happy the sad; the quick thinking the sedate, and the careless the busy and industrious.": {
        "pt": "As pessoas tristes não gostam das felizes, e as felizes das tristes; os de pensamento rápido, dos serenos, e os descuidados, dos ocupados e industriosos.",
        "es": "Las personas tristes no gustan de las felices, y las felices de las tristes; los de pensamiento rápido, de los serenos, y los descuidados, de los ocupados e industriosos."
    },
    "Don't think, just do.": {
        "pt": "Não pense, apenas faça.",
        "es": "No pienses, solo hazlo."
    },
    "The fall of dropping water wears away the Stone.": {
        "pt": "A queda da gota d'água desgasta a pedra.",
        "es": "La caída de la gota de agua desgasta la piedra."
    },
    "Wisdom is not wisdom when it is derived from books alone.": {
        "pt": "A sabedoria não é sabedoria quando é derivada apenas dos livros.",
        "es": "La sabiduría no es sabiduría cuando se deriva solo de los libros."
    },
    "Life is largely a matter of expectation.": {
        "pt": "A vida é em grande parte uma questão de expectativa.",
        "es": "La vida es en gran parte una cuestión de expectativa."
    },
    "Remember when life's path is steep to keep your mind even.": {
        "pt": "Lembre-se, quando o caminho da vida for íngreme, de manter a mente equilibrada.",
        "es": "Recuerda, cuando el camino de la vida sea empinado, mantener la mente serena."
    },
    "No poems can please for long or live that are written by water drinkers.": {
        "pt": "Nenhum poema pode agradar por muito tempo ou viver que seja escrito por bebedores de água.",
        "es": "Ningún poema puede agradar por mucho tiempo o vivir que sea escrito por bebedores de agua."
    },
    "There is no such thing as justice in the abstract it is merely a compact between men.": {
        "pt": "Não existe tal coisa como justiça no abstrato; é meramente um pacto entre os homens.",
        "es": "No existe tal cosa como la justicia en abstracto; es meramente un pacto entre los hombres."
    },
    "The one who cannot restrain their anger will wish undone, what their temper and irritation prompted them to do.": {
        "pt": "Aquele que não consegue conter sua raiva desejará desfazer o que seu temperamento e irritação o levaram a fazer.",
        "es": "Aquel que no puede contener su ira deseará deshacer lo que su temperamento e irritación lo llevaron a hacer."
    },
    "Lawyers are men who hire out their words and anger.": {
        "pt": "Advogados são homens que alugam suas palavras e raiva.",
        "es": "Los abogados son hombres que alquilan sus palabras y su ira."
    },
    "Undeservedly you will atone for the sins of your fathers.": {
        "pt": "Imerecidamente você expiará os pecados de seus pais.",
        "es": "Inmerecidamente expiarás los pecados de tus padres."
    },
    "Cease to inquire what the future has in store, and take as a gift whatever the day brings forth.": {
        "pt": "Pare de perguntar o que o futuro reserva e aceite como presente o que o dia traz.",
        "es": "Deja de preguntar qué depara el futuro y acepta como regalo lo que el día trae."
    },
    "We must exercise ourselves in the things which bring happiness, since, if that be present, we have everything, and, if that be absent, all our actions are directed toward attaining it.": {
        "pt": "Devemos nos exercitar nas coisas que trazem felicidade, pois, se ela estiver presente, temos tudo, e, se estiver ausente, todas as nossas ações são direcionadas para alcançá-la.",
        "es": "Debemos ejercitarnos en las cosas que traen felicidad, pues, si está presente, lo tenemos todo, y, si está ausente, todas nuestras acciones se dirigen a alcanzarla."
    },
    "Let no one be slow to seek wisdom when he is young nor weary in the search of it when he has grown old. For no age is too early or too late for the health of the soul.": {
        "pt": "Que ninguém seja lento em buscar a sabedoria quando jovem, nem se canse na busca quando envelhecer. Pois nenhuma idade é cedo ou tarde demais para a saúde da alma.",
        "es": "Que nadie sea lento en buscar la sabiduría cuando es joven, ni se canse en la búsqueda cuando haya envejecido. Pues ninguna edad es demasiado temprana o tardía para la salud del alma."
    },
    "Death does not concern us, because as long as we exist, death is not here. And when it does come, we no longer exist.": {
        "pt": "A morte não nos diz respeito, porque enquanto existimos, a morte não está aqui. E quando ela chega, nós já não existimos.",
        "es": "La muerte no nos concierne, porque mientras existimos, la muerte no está aquí. Y cuando llega, nosotros ya no existimos."
    },
    "I was not, I was, I am not, I care not. (Non fui, fui, non sum, non curo)": {
        "pt": "Eu não era, eu era, eu não sou, não me importo. (Non fui, fui, non sum, non curo)",
        "es": "No fui, fui, no soy, no me importa. (Non fui, fui, non sum, non curo)"
    },
}

# === RATIONALISM TRANSLATIONS (shorter quotes only - skip very long Kant excerpts) ===
rat = {
    "One who makes himself a worm cannot complain afterwards if people step on him.": {
        "pt": "Aquele que se faz de verme não pode reclamar depois se as pessoas pisam nele.",
        "es": "Quien se hace gusano no puede quejarse después si la gente lo pisa."
    },
    "Common sense is the most widely shared commodity in the world, for every man is convinced that he is well supplied with it.": {
        "pt": "O bom senso é a coisa mais bem distribuída do mundo, pois cada homem está convencido de que é bem provido dele.",
        "es": "El sentido común es lo mejor repartido del mundo, pues cada hombre está convencido de que está bien provisto de él."
    },
    "The highest activity a human being can attain is learning for understanding, because to understand is to be free.": {
        "pt": "A mais alta atividade que um ser humano pode alcançar é aprender para compreender, porque compreender é ser livre.",
        "es": "La más alta actividad que un ser humano puede alcanzar es aprender para comprender, porque comprender es ser libre."
    },
    "I do not know how to teach philosophy without becoming a disturber of the peace.": {
        "pt": "Não sei como ensinar filosofia sem me tornar um perturbador da paz.",
        "es": "No sé cómo enseñar filosofía sin convertirme en un perturbador de la paz."
    },
    "Except our own thoughts, there is nothing absolutely in our power.": {
        "pt": "Exceto nossos próprios pensamentos, não há nada absolutamente em nosso poder.",
        "es": "Excepto nuestros propios pensamientos, no hay nada absolutamente en nuestro poder."
    },
    "I have made a ceaseless effort not to ridicule, not to bewail, not to scorn human actions, but to understand them.": {
        "pt": "Fiz um esforço incessante para não ridicularizar, não lamentar, não desprezar as ações humanas, mas para compreendê-las.",
        "es": "He hecho un esfuerzo incesante por no ridiculizar, no lamentar, no despreciar las acciones humanas, sino por comprenderlas."
    },
    "Act only according to that maxim whereby you can at the same time will that it should become a universal law.": {
        "pt": "Aja apenas segundo a máxima pela qual você possa ao mesmo tempo querer que ela se torne uma lei universal.",
        "es": "Actúa solo según la máxima por la cual puedas al mismo tiempo querer que se convierta en una ley universal."
    },
    "He alone is free who lives with free consent under the entire guidance of reason": {
        "pt": "Somente é livre aquele que vive com livre consentimento sob a inteira orientação da razão",
        "es": "Solo es libre aquel que vive con libre consentimiento bajo la entera guía de la razón"
    },
    "Things which are accidentally the causes either of hope or fear are called good or evil omens.": {
        "pt": "As coisas que são acidentalmente causas de esperança ou medo são chamadas de bons ou maus presságios.",
        "es": "Las cosas que son accidentalmente causas de esperanza o miedo se llaman buenos o malos presagios."
    },
    "If you would be a real seeker after truth, it is necessary that at least once in your life you doubt, as far as possible, all things.": {
        "pt": "Se você quer ser um verdadeiro buscador da verdade, é necessário que ao menos uma vez na vida duvide, na medida do possível, de todas as coisas.",
        "es": "Si quieres ser un verdadero buscador de la verdad, es necesario que al menos una vez en tu vida dudes, en la medida de lo posible, de todas las cosas."
    },
    "You just keep pushing. You just keep pushing. I made every mistake that could be made. But I just kept pushing.": {
        "pt": "Você continua insistindo. Você continua insistindo. Cometi todos os erros que podiam ser cometidos. Mas continuei insistindo.",
        "es": "Sigues insistiendo. Sigues insistiendo. Cometí todos los errores que se podían cometer. Pero seguí insistiendo."
    },
    "There is nothing more ancient than the truth.": {
        "pt": "Não há nada mais antigo que a verdade.",
        "es": "No hay nada más antiguo que la verdad."
    },
    "Don't cry and don't rage. Understand.": {
        "pt": "Não chore e não se enfureça. Compreenda.",
        "es": "No llores y no te enfurezcas. Comprende."
    },
    "To live without philosophizing is in truth the same as keeping the eyes closed without attempting to open them.": {
        "pt": "Viver sem filosofar é na verdade o mesmo que manter os olhos fechados sem tentar abri-los.",
        "es": "Vivir sin filosofar es en verdad lo mismo que mantener los ojos cerrados sin intentar abrirlos."
    },
    "The death of dogma is the birth of morality.": {
        "pt": "A morte do dogma é o nascimento da moralidade.",
        "es": "La muerte del dogma es el nacimiento de la moralidad."
    },
    "I should not really object to dying were it not followed by death.": {
        "pt": "Na verdade eu não me oporia a morrer se isso não fosse seguido pela morte.",
        "es": "En realidad no me opondría a morir si no fuera seguido por la muerte."
    },
    "Science is organized knowledge. Wisdom is organized life": {
        "pt": "Ciência é conhecimento organizado. Sabedoria é vida organizada.",
        "es": "La ciencia es conocimiento organizado. La sabiduría es vida organizada."
    },
    "Treat people as an end, and never as a means to an end": {
        "pt": "Trate as pessoas como um fim, e nunca como um meio para um fim",
        "es": "Trata a las personas como un fin, y nunca como un medio para un fin"
    },
    "But in my opinion, all things in nature occur mathematically.": {
        "pt": "Mas na minha opinião, todas as coisas na natureza ocorrem matematicamente.",
        "es": "Pero en mi opinión, todas las cosas en la naturaleza ocurren matemáticamente."
    },
    "In every department of physical science there is only so much science, properly so-called, as there is mathematics.": {
        "pt": "Em cada departamento da ciência física, há apenas tanta ciência, propriamente dita, quanto há de matemática.",
        "es": "En cada departamento de la ciencia física, solo hay tanta ciencia, propiamente dicha, como hay matemática."
    },
    "The reading of all good books is like conversation with the finest men of past centuries.": {
        "pt": "A leitura de todos os bons livros é como uma conversa com os melhores homens dos séculos passados.",
        "es": "La lectura de todos los buenos libros es como una conversación con los mejores hombres de siglos pasados."
    },
    "Seek not the favor of the multitude; it is seldom got by honest and lawful means. But seek the testimony of few; and number not voices, but weigh them.": {
        "pt": "Não busque o favor da multidão; raramente se obtém por meios honestos e legais. Mas busque o testemunho de poucos; e não conte vozes, mas pese-as.",
        "es": "No busques el favor de la multitud; rara vez se obtiene por medios honestos y legales. Pero busca el testimonio de pocos; y no cuentes voces, sino pésalas."
    },
    "The enjoyment of power inevitably corrupts the judgement of reason, and perverts its liberty.": {
        "pt": "O gozo do poder inevitavelmente corrompe o julgamento da razão e perverte sua liberdade.",
        "es": "El goce del poder inevitablemente corrompe el juicio de la razón y pervierte su libertad."
    },
    "From the crooked timber of humanity, a straight board cannot be hewn.": {
        "pt": "Da madeira torta da humanidade, uma tábua reta não pode ser talhada.",
        "es": "De la madera torcida de la humanidad, una tabla recta no puede ser tallada."
    },
    "Those who know the true use of money, and regulate the measure of wealth according to their needs, live contented with few things.": {
        "pt": "Aqueles que conhecem o verdadeiro uso do dinheiro, e regulam a medida da riqueza de acordo com suas necessidades, vivem contentes com poucas coisas.",
        "es": "Aquellos que conocen el verdadero uso del dinero, y regulan la medida de la riqueza según sus necesidades, viven contentos con pocas cosas."
    },
    "The human will to believe is inexhaustible": {
        "pt": "A vontade humana de crer é inesgotável",
        "es": "La voluntad humana de creer es inagotable"
    },
    "Give me matter, and I will construct a world out of it!": {
        "pt": "Dê-me matéria e eu construirei um mundo a partir dela!",
        "es": "¡Dame materia y construiré un mundo a partir de ella!"
    },
    "We are not rich by what we possess but by what we can do without.": {
        "pt": "Não somos ricos pelo que possuímos, mas pelo que podemos dispensar.",
        "es": "No somos ricos por lo que poseemos, sino por lo que podemos prescindir."
    },
    "If you could blow the brain up to the size of a mill and walk about inside, you would not find consciousness.": {
        "pt": "Se você pudesse ampliar o cérebro até o tamanho de um moinho e caminhar por dentro, não encontraria a consciência.",
        "es": "Si pudieras ampliar el cerebro hasta el tamaño de un molino y caminar por dentro, no encontrarías la conciencia."
    },
    "An action, to have moral worth, must be done from duty.": {
        "pt": "Uma ação, para ter valor moral, deve ser feita por dever.",
        "es": "Una acción, para tener valor moral, debe ser hecha por deber."
    },
    "But although all our knowledge begins with experience, it does not follow that it arises from experience.": {
        "pt": "Mas embora todo o nosso conhecimento comece com a experiência, não se segue que ele surja da experiência.",
        "es": "Pero aunque todo nuestro conocimiento comienza con la experiencia, no se sigue que surja de la experiencia."
    },
    "Experience without theory is blind, but theory without experience is mere intellectual play.": {
        "pt": "Experiência sem teoria é cega, mas teoria sem experiência é mero jogo intelectual.",
        "es": "Experiencia sin teoría es ciega, pero teoría sin experiencia es mero juego intelectual."
    },
    "He who is cruel to animals becomes hard also in his dealings with men. We can judge the heart of a man by his treatment of animals.": {
        "pt": "Aquele que é cruel com os animais torna-se duro também em seus tratos com os homens. Podemos julgar o coração de um homem pelo seu tratamento dos animais.",
        "es": "Aquel que es cruel con los animales se vuelve duro también en su trato con los hombres. Podemos juzgar el corazón de un hombre por su trato con los animales."
    },
    "When a man is prey to his emotions, he is not his own master.": {
        "pt": "Quando um homem é presa de suas emoções, ele não é senhor de si mesmo.",
        "es": "Cuando un hombre es presa de sus emociones, no es dueño de sí mismo."
    },
    "Simply to acquiesce in skepticism can never suffice to overcome the restlessness of reason.": {
        "pt": "Simplesmente aquiescer no ceticismo nunca será suficiente para superar a inquietação da razão.",
        "es": "Simplemente aquietarse en el escepticismo nunca será suficiente para superar la inquietud de la razón."
    },
    "Nihil est sine ratione.\n[There is nothing without a reason.]": {
        "pt": "Nihil est sine ratione.\n[Não há nada sem uma razão.]",
        "es": "Nihil est sine ratione.\n[No hay nada sin una razón.]"
    },
    "I call him free who is led solely by reason.": {
        "pt": "Chamo de livre aquele que é guiado unicamente pela razão.",
        "es": "Llamo libre a aquel que es guiado únicamente por la razón."
    },
    "The more clearly you understand yourself and your emotions, the more you become a lover of what is.": {
        "pt": "Quanto mais claramente você compreende a si mesmo e suas emoções, mais se torna um amante do que é.",
        "es": "Cuanto más claramente te comprendes a ti mismo y tus emociones, más te conviertes en un amante de lo que es."
    },
    "Human beings are never to be treated as a means but always as ends.": {
        "pt": "Os seres humanos nunca devem ser tratados como um meio, mas sempre como fins.",
        "es": "Los seres humanos nunca deben ser tratados como un medio, sino siempre como fines."
    },
    "I do not know how to teach philosophy without becoming a disturber of established religion.": {
        "pt": "Não sei como ensinar filosofia sem me tornar um perturbador da religião estabelecida.",
        "es": "No sé cómo enseñar filosofía sin convertirme en un perturbador de la religión establecida."
    },
    "self-preservation is the primary and only foundation of virtue.": {
        "pt": "a autopreservação é a base primeira e única da virtude.",
        "es": "la autopreservación es el fundamento primero y único de la virtud."
    },
    "With me, everything turns into mathematics.": {
        "pt": "Comigo, tudo se transforma em matemática.",
        "es": "Conmigo, todo se transforma en matemáticas."
    },
    "I took especially great pleasure in mathematics because of the certainty and the evidence of its arguments.": {
        "pt": "Tive especial prazer na matemática por causa da certeza e da evidência de seus argumentos.",
        "es": "Tuve especial placer en las matemáticas por la certeza y la evidencia de sus argumentos."
    },
    "Dignity is a value that creates irreplaceability.": {
        "pt": "A dignidade é um valor que cria a insubstituibilidade.",
        "es": "La dignidad es un valor que crea la irreemplazabilidad."
    },
    "Do not weep  do not wax indignant. Understand.": {
        "pt": "Não chore, não se indigne. Compreenda.",
        "es": "No llores, no te indignes. Comprende."
    },
    "The death of dogma is the birth of reality.": {
        "pt": "A morte do dogma é o nascimento da realidade.",
        "es": "La muerte del dogma es el nacimiento de la realidad."
    },
    "Faith is nothing but obedience and piety.": {
        "pt": "A fé não é nada além de obediência e piedade.",
        "es": "La fe no es más que obediencia y piedad."
    },
    "To be what we are  and to become what we are capable of becoming  is the only end of life.": {
        "pt": "Ser o que somos e nos tornar aquilo de que somos capazes é o único fim da vida.",
        "es": "Ser lo que somos y convertirnos en lo que somos capaces de ser es el único fin de la vida."
    },
    "Every man is to be respected as an absolute end in himself: and it is a crime against the dignity that belongs to him as a human being  to use him as a mere means for some external purpose.": {
        "pt": "Todo homem deve ser respeitado como um fim absoluto em si mesmo: e é um crime contra a dignidade que lhe pertence como ser humano usá-lo como mero meio para algum propósito externo.",
        "es": "Todo hombre debe ser respetado como un fin absoluto en sí mismo: y es un crimen contra la dignidad que le pertenece como ser humano usarlo como mero medio para algún propósito externo."
    },
    "There is no hope unmingled with fear  and no fear unmingled with hope.": {
        "pt": "Não há esperança sem mistura de medo, nem medo sem mistura de esperança.",
        "es": "No hay esperanza sin mezcla de miedo, ni miedo sin mezcla de esperanza."
    },
    "Everything in nature acts in conformity with law.": {
        "pt": "Tudo na natureza age em conformidade com a lei.",
        "es": "Todo en la naturaleza actúa en conformidad con la ley."
    },
    "We can always get along better by reason and love of truth than by worry of conscience and remorse. Harmful are these  and evil.": {
        "pt": "Sempre podemos nos sair melhor pela razão e amor à verdade do que pela preocupação da consciência e remorso. Prejudiciais são estes, e maus.",
        "es": "Siempre podemos salir mejor por la razón y el amor a la verdad que por la preocupación de la conciencia y el remordimiento. Dañinos son estos, y malos."
    },
    "There is no hope unmingled with fear, and no fear unmingled with hope.": {
        "pt": "Não há esperança sem mistura de medo, nem medo sem mistura de esperança.",
        "es": "No hay esperanza sin mezcla de miedo, ni miedo sin mezcla de esperanza."
    },
    "What can I know? What ought I to do? What can I hope?": {
        "pt": "O que posso saber? O que devo fazer? O que posso esperar?",
        "es": "¿Qué puedo saber? ¿Qué debo hacer? ¿Qué puedo esperar?"
    },
    "All the interests of my reason, speculative as well as practical, combine in the three following questions: 1. What can I know? 2. What ought I to do? 3. What may I hope?": {
        "pt": "Todos os interesses da minha razão, especulativos e práticos, combinam-se nas três seguintes perguntas: 1. O que posso saber? 2. O que devo fazer? 3. O que posso esperar?",
        "es": "Todos los intereses de mi razón, especulativos y prácticos, se combinan en las tres siguientes preguntas: 1. ¿Qué puedo saber? 2. ¿Qué debo hacer? 3. ¿Qué puedo esperar?"
    },
    "Fear cannot be without hope nor hope without fear.": {
        "pt": "O medo não pode existir sem esperança, nem a esperança sem medo.",
        "es": "El miedo no puede existir sin esperanza, ni la esperanza sin miedo."
    },
    "Even philosophers will praise war as ennobling mankind, forgetting the Greek who said: 'War is bad in that it begets more evil than it kills.'": {
        "pt": "Até filósofos elogiarão a guerra como enobrecedora da humanidade, esquecendo o grego que disse: 'A guerra é ruim porque gera mais mal do que mata.'",
        "es": "Incluso los filósofos elogiarán la guerra como ennoblecedora de la humanidad, olvidando al griego que dijo: 'La guerra es mala porque engendra más mal del que mata.'"
    },
    "Peace is not an absence of war, it is a virtue, a state of mind, a disposition for benevolence, confidence, justice.": {
        "pt": "A paz não é ausência de guerra, é uma virtude, um estado de espírito, uma disposição para benevolência, confiança, justiça.",
        "es": "La paz no es ausencia de guerra, es una virtud, un estado de ánimo, una disposición para la benevolencia, la confianza, la justicia."
    },
    "For peace is not mere absence of war, but is a virtue that springs from, a state of mind, a disposition for benevolence, confidence, justice.": {
        "pt": "Pois a paz não é mera ausência de guerra, mas é uma virtude que nasce de um estado de espírito, uma disposição para benevolência, confiança, justiça.",
        "es": "Pues la paz no es mera ausencia de guerra, sino una virtud que nace de un estado de ánimo, una disposición para la benevolencia, la confianza, la justicia."
    },
    "To be is to do.": {
        "pt": "Ser é fazer.",
        "es": "Ser es hacer."
    },
    "I would warn you that I do not attribute to nature either beauty or deformity, order or confusion. Only in relation to our imagination can things be called beautiful or ugly, well-ordered or confused.": {
        "pt": "Eu o advertiria de que não atribuo à natureza nem beleza nem deformidade, ordem nem confusão. Somente em relação à nossa imaginação as coisas podem ser chamadas de belas ou feias, bem-ordenadas ou confusas.",
        "es": "Te advertiría que no atribuyo a la naturaleza ni belleza ni deformidad, orden ni confusión. Solo en relación con nuestra imaginación las cosas pueden llamarse bellas o feas, bien ordenadas o confusas."
    },
    "Only that thing is free which exists by the necessities of its own nature, and is determined in its actions by itself alone.": {
        "pt": "Somente é livre aquilo que existe pelas necessidades de sua própria natureza e é determinado em suas ações por si mesmo.",
        "es": "Solo es libre aquello que existe por las necesidades de su propia naturaleza y es determinado en sus acciones por sí mismo."
    },
    "Freedom is absolutely necessary for the progress in science and the liberal arts.": {
        "pt": "A liberdade é absolutamente necessária para o progresso na ciência e nas artes liberais.",
        "es": "La libertad es absolutamente necesaria para el progreso en la ciencia y las artes liberales."
    },
    "Peace is not the absence of war, but a virtue based on strength of character.": {
        "pt": "A paz não é a ausência de guerra, mas uma virtude baseada na força de caráter.",
        "es": "La paz no es la ausencia de guerra, sino una virtud basada en la fuerza de carácter."
    },
    "One and the same thing can at the same time be good, bad, and indifferent, e.g., music is good to the melancholy, bad to those who mourn, and neither good nor bad to the deaf.": {
        "pt": "Uma e a mesma coisa pode ao mesmo tempo ser boa, má e indiferente; por exemplo, a música é boa para os melancólicos, má para os que lamentam, e nem boa nem má para os surdos.",
        "es": "Una y la misma cosa puede al mismo tiempo ser buena, mala e indiferente; por ejemplo, la música es buena para los melancólicos, mala para los que lloran, y ni buena ni mala para los sordos."
    },
    "Morality is not the doctrine of how we may make ourselves happy, but how we may make ourselves worthy of happiness.": {
        "pt": "A moralidade não é a doutrina de como podemos nos fazer felizes, mas como podemos nos tornar dignos da felicidade.",
        "es": "La moralidad no es la doctrina de cómo podemos hacernos felices, sino cómo podemos hacernos dignos de la felicidad."
    },
    "Happiness is not an ideal of reason, but of imagination.": {
        "pt": "A felicidade não é um ideal da razão, mas da imaginação.",
        "es": "La felicidad no es un ideal de la razón, sino de la imaginación."
    },
    "Genius is the ability to independently arrive at and understand concepts that would normally have to be taught by another person.": {
        "pt": "Gênio é a capacidade de chegar independentemente a conceitos e compreendê-los, que normalmente teriam que ser ensinados por outra pessoa.",
        "es": "El genio es la capacidad de llegar independientemente a conceptos y comprenderlos, que normalmente tendrían que ser enseñados por otra persona."
    },
    "The main point of enlightenment is man's release from his self-caused immaturity, primarily in matters of religion.": {
        "pt": "O ponto principal do esclarecimento é a libertação do homem de sua imaturidade autoimposta, principalmente em questões de religião.",
        "es": "El punto principal de la ilustración es la liberación del hombre de su inmadurez autoimpuesta, principalmente en asuntos de religión."
    },
    "Woman wants control, man self-control .": {
        "pt": "A mulher quer controle, o homem autocontrole.",
        "es": "La mujer quiere control, el hombre autocontrol."
    },
}

# Merge all translations
translations.update(epic)
translations.update(rat)

# Write output
with open('c:/Users/lalli/Flutter/coach_phrase_app/translations_extra.json', 'w', encoding='utf-8') as f:
    json.dump(translations, f, ensure_ascii=False, indent=2)

print(f"Total translations: {len(translations)}")
print(f"  Epicureanism: {len(epic)}")
print(f"  Rationalism: {len(rat)}")
