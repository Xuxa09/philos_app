"""Add batch 3 of classical translations (~130 more)."""
import json

with open('c:/Users/lalli/Flutter/coach_phrase_app/missing_classical.json', 'r', encoding='utf-8') as f:
    missing = json.load(f)

with open('c:/Users/lalli/Flutter/coach_phrase_app/translations_classical.json', 'r', encoding='utf-8') as f:
    tr = json.load(f)

batch = missing[:134]

tl = [
    # 1 - long Aristotle On the Soul - already translated in batch2, skip duplicate key
    ("O conhecimento da alma contribui grandemente para o avan\u00e7o da verdade em geral. Nosso objetivo \u00e9 apreender sua natureza essencial e suas propriedades. Alcan\u00e7ar qualquer conhecimento sobre a alma \u00e9 uma das coisas mais dif\u00edceis do mundo.", "El conocimiento del alma contribuye grandemente al avance de la verdad en general. Nuestro objetivo es aprehender su naturaleza esencial y sus propiedades. Alcanzar cualquier conocimiento sobre el alma es una de las cosas m\u00e1s dif\u00edciles del mundo."),
    # 2
    ("Tudo que engana pode ser dito que encanta.", "Todo lo que enga\u00f1a puede decirse que encanta."),
    # 3
    ("A pior forma de desigualdade \u00e9 tentar tornar iguais coisas desiguais.", "La peor forma de desigualdad es intentar hacer iguales cosas desiguales."),
    # 4
    ("Os meninos devem se abster de todo uso de vinho at\u00e9 o d\u00e9cimo oitavo ano, pois \u00e9 errado adicionar fogo ao fogo.", "Los ni\u00f1os deben abstenerse de todo uso de vino hasta el decimoctavo a\u00f1o, pues es incorrecto a\u00f1adir fuego al fuego."),
    # 5
    ("Todo aprendizado tem uma base emocional.", "Todo aprendizaje tiene una base emocional."),
    # 6
    ("Coisas excelentes s\u00e3o raras.", "Las cosas excelentes son raras."),
    # 7
    ("A fama \u00e9 o perfume dos feitos heroicos.", "La fama es el perfume de los hechos heroicos."),
    # 8
    ("A amizade \u00e9 uma \u00fanica alma habitando dois corpos.", "La amistad es una sola alma habitando dos cuerpos."),
    # 9
    ("Quantas coisas h\u00e1 que eu n\u00e3o quero.", "Cu\u00e1ntas cosas hay que no quiero."),
    # 10
    ("Se todos os infort\u00fanios fossem postos num monte comum de onde todos devessem tomar uma por\u00e7\u00e3o igual, a maioria ficaria contente em tomar os seus pr\u00f3prios e ir embora.", "Si todas las desgracias fueran puestas en un mont\u00f3n com\u00fan de donde todos debieran tomar una porci\u00f3n igual, la mayor\u00eda estar\u00eda contenta de tomar las suyas propias e irse."),
    # 11
    ("Sem amigos ningu\u00e9m escolheria viver, mesmo que tivesse todos os outros bens.", "Sin amigos nadie elegir\u00eda vivir, aunque tuviera todos los dem\u00e1s bienes."),
    # 12
    ("Um verdadeiro amigo \u00e9 uma alma em dois corpos.", "Un verdadero amigo es un alma en dos cuerpos."),
    # 13 - duplicate of 11
    ("Sem amigos ningu\u00e9m escolheria viver, mesmo que tivesse todos os outros bens.", "Sin amigos nadie elegir\u00eda vivir, aunque tuviera todos los dem\u00e1s bienes."),
    # 14
    ("Os amigos s\u00e3o aux\u00edlio para os jovens, para guard\u00e1-los do erro; para os idosos, para atender suas necessidades; para os que est\u00e3o no auge da vida, para assist\u00ed-los em feitos nobres.", "Los amigos son ayuda para los j\u00f3venes, para guardarlos del error; para los ancianos, para atender sus necesidades; para los que est\u00e1n en la plenitud de la vida, para asistirlos en hechos nobles."),
    # 15
    ("Devemos nos comportar com nossos amigos como gostar\u00edamos que eles se comportassem conosco.", "Debemos comportarnos con nuestros amigos como nos gustar\u00eda que ellos se comportaran con nosotros."),
    # 16
    ("Entre amigos n\u00e3o h\u00e1 necessidade de justi\u00e7a.", "Entre amigos no hay necesidad de justicia."),
    # 17
    ("Seja lento para cair na amizade, mas quando estiver nela, continue firme e constante.", "S\u00e9 lento para caer en la amistad, pero cuando est\u00e9s en ella, contin\u00faa firme y constante."),
    # 18
    ("Desejar ser amigos \u00e9 trabalho r\u00e1pido, mas a amizade \u00e9 um fruto de amadurecimento lento.", "Desear ser amigos es trabajo r\u00e1pido, pero la amistad es un fruto de madurez lenta."),
    # 19
    ("Meu melhor amigo \u00e9 o homem que, ao me desejar o bem, o deseja por minha causa.", "Mi mejor amigo es el hombre que, al desearme el bien, lo desea por mi causa."),
    # 20
    ("Na pobreza e em outros infort\u00fanios da vida, os verdadeiros amigos s\u00e3o um ref\u00fagio seguro.", "En la pobreza y en otros infortunios de la vida, los verdaderos amigos son un refugio seguro."),
    # 21 - dup of 8
    ("A amizade \u00e9 uma \u00fanica alma habitando dois corpos.", "La amistad es una sola alma habitando dos cuerpos."),
    # 22
    ("Seja lento para cair na amizade, mas quando estiver nela, continue firme e constante.", "S\u00e9 lento para caer en la amistad, pero cuando est\u00e9s en ella, contin\u00faa firme y constante."),
    # 23
    ("N\u00e3o h\u00e1 grande g\u00eanio sem uma mistura de loucura.", "No hay gran genio sin una mezcla de locura."),
    # 24
    ("Honras e recompensas cabem \u00e0queles que mostram suas boas qualidades em a\u00e7\u00e3o.", "Los honores y las recompensas corresponden a quienes muestran sus buenas cualidades en acci\u00f3n."),
    # 25
    ("Fazer \u00e9 ser.", "Hacer es ser."),
    # 26
    ("O que mais conta n\u00e3o \u00e9 viver, mas viver corretamente.", "Lo que m\u00e1s cuenta no es vivir, sino vivir correctamente."),
    # 27
    ("Todos os homens buscam um objetivo: sucesso ou felicidade.", "Todos los hombres buscan un objetivo: \u00e9xito o felicidad."),
    # 28
    ("Deus tem muitos nomes, embora seja apenas um Ser.", "Dios tiene muchos nombres, aunque es solo un Ser."),
    # 29
    ("Nenhum homem empreende um of\u00edcio que n\u00e3o aprendeu, nem mesmo o mais humilde; no entanto, todos se julgam suficientemente qualificados para o mais dif\u00edcil de todos os of\u00edcios \u2014 o de governo.", "Ning\u00fan hombre emprende un oficio que no ha aprendido, ni siquiera el m\u00e1s humilde; sin embargo, todos se juzgan suficientemente cualificados para el m\u00e1s dif\u00edcil de todos los oficios \u2014 el de gobierno."),
    # 30
    ("A felicidade \u00e9 o significado e o prop\u00f3sito da vida, o objetivo e o fim de toda a exist\u00eancia humana.", "La felicidad es el significado y el prop\u00f3sito de la vida, el objetivo y el fin de toda la existencia humana."),
    # 31
    ("Viver bem, belamente e com justi\u00e7a s\u00e3o uma \u00fanica coisa.", "Vivir bien, bellamente y con justicia son una sola cosa."),
    # 32
    ("Diferentes homens buscam a felicidade de diferentes maneiras e por diferentes meios.", "Diferentes hombres buscan la felicidad de diferentes maneras y por diferentes medios."),
    # 33
    ("O homem que faz tudo que leva \u00e0 felicidade depender de si mesmo, e n\u00e3o de outros homens, adotou o melhor plano para viver feliz.", "El hombre que hace que todo lo que conduce a la felicidad dependa de s\u00ed mismo, y no de otros hombres, ha adoptado el mejor plan para vivir feliz."),
    # 34
    ("A felicidade \u00e9 uma express\u00e3o da alma em a\u00e7\u00f5es ponderadas.", "La felicidad es una expresi\u00f3n del alma en acciones ponderadas."),
    # 35
    ("A felicidade parece exigir um m\u00ednimo de prosperidade externa.", "La felicidad parece exigir un m\u00ednimo de prosperidad externa."),
    # 36
    ("Temos dois ouvidos e apenas uma l\u00edngua para que possamos ouvir mais e falar menos.", "Tenemos dos o\u00eddos y solo una lengua para que podamos o\u00edr m\u00e1s y hablar menos."),
    # 37
    ("Seja gentil, pois todos que voc\u00ea encontra est\u00e3o travando uma dura batalha.", "S\u00e9 amable, porque todos los que encuentras est\u00e1n librando una dura batalla."),
    # 38
    ("A dignidade n\u00e3o consiste em possuir honras, mas em merecê-las.", "La dignidad no consiste en poseer honores, sino en merecerlos."),
    # 39
    ("N\u00e3o sou ateniense, nem grego, mas cidad\u00e3o do mundo.", "No soy ateniense, ni griego, sino ciudadano del mundo."),
    # 40
    ("O humor \u00e9 o \u00fanico teste da gravidade, e a gravidade do humor; pois um assunto que n\u00e3o suporta zombaria \u00e9 suspeito, e uma piada que n\u00e3o suporta exame s\u00e9rio \u00e9 falso esp\u00edrito.", "El humor es la \u00fanica prueba de la gravedad, y la gravedad del humor; pues un asunto que no soporta burla es sospechoso, y una broma que no soporta examen serio es falso ingenio."),
    # 41
    ("N\u00e3o \u00e9 apenas ocioso quem nada faz, mas tamb\u00e9m quem poderia estar melhor empregado.", "No es solo ocioso quien nada hace, sino tambi\u00e9n quien podr\u00eda estar mejor empleado."),
    # 42
    ("Aquele que comete injusti\u00e7a \u00e9 sempre mais miser\u00e1vel do que aquele que a sofre.", "Aquel que comete injusticia es siempre m\u00e1s miserable que aquel que la sufre."),
    # 43
    ("Nenhuma alma excelente est\u00e1 isenta de uma mistura de loucura.", "Ninguna alma excelente est\u00e1 exenta de una mezcla de locura."),
    # 44
    ("A cal\u00fania \u00e9 apenas o ru\u00eddo dos loucos.", "La calumnia es solo el ruido de los locos."),
    # 45
    ("Quatro coisas pertencem a um juiz: ouvir cortesmente, responder sabiamente, considerar sobriamente e decidir imparcialmente.", "Cuatro cosas pertenecen a un juez: o\u00edr cort\u00e9smente, responder sabiamente, considerar sobriamente y decidir imparcialmente."),
    # 46
    ("Todos os homens por natureza desejam conhecer.", "Todos los hombres por naturaleza desean conocer."),
    # 47
    ("O \u00fanico bem \u00e9 o conhecimento, e o \u00fanico mal \u00e9 a ignor\u00e2ncia.", "El \u00fanico bien es el conocimiento, y el \u00fanico mal es la ignorancia."),
    # 48
    ("Quanto a mim, tudo que sei \u00e9 que nada sei.", "En cuanto a m\u00ed, todo lo que s\u00e9 es que no s\u00e9 nada."),
    # 49
    ("A felicidade \u00e9 o significado e o prop\u00f3sito da vida, o objetivo e o fim de toda a exist\u00eancia humana.", "La felicidad es el significado y el prop\u00f3sito de la vida, el objetivo y el fin de toda la existencia humana."),
    # 50
    ("O amor \u2014 uma grave doen\u00e7a mental.", "El amor \u2014 una grave enfermedad mental."),
    # 51
    ("O m\u00e9dico cura, a Natureza restaura.", "El m\u00e9dico cura, la Naturaleza restaura."),
    # 52
    ("H\u00e1 tr\u00eas classes de homens: amantes da sabedoria, amantes da honra, amantes do ganho.", "Hay tres clases de hombres: amantes de la sabidur\u00eda, amantes del honor, amantes de la ganancia."),
    # 53
    ("\u00c9 melhor levantar-se da vida como de um banquete, nem sedento nem embriagado.", "Es mejor levantarse de la vida como de un banquete, ni sediento ni ebrio."),
    # 54
    ("O sol \u00e9 novo a cada dia.", "El sol es nuevo cada d\u00eda."),
    # 55
    ("O comportamento humano flui de tr\u00eas fontes principais: desejo, emo\u00e7\u00e3o e conhecimento.", "El comportamiento humano fluye de tres fuentes principales: deseo, emoci\u00f3n y conocimiento."),
    # 56
    ("Riqueza... e pobreza: uma \u00e9 m\u00e3e do luxo e da indol\u00eancia, e a outra da mesquinharia e do v\u00edcio, e ambas do descontentamento.", "Riqueza... y pobreza: una es madre del lujo y la indolencia, y la otra de la mezquindad y el vicio, y ambas del descontento."),
    # 57
    ("A necessidade, que \u00e9 a m\u00e3e de nossa inven\u00e7\u00e3o.", "La necesidad, que es la madre de nuestra invenci\u00f3n."),
    # 58
    ("Em todas as coisas da natureza h\u00e1 algo de maravilhoso.", "En todas las cosas de la naturaleza hay algo de maravilloso."),
    # 59
    ("Qualidade n\u00e3o \u00e9 um ato. \u00c9 um h\u00e1bito.", "La calidad no es un acto. Es un h\u00e1bito."),
    # 60
    ("Todo homem \u00e9 um poeta quando est\u00e1 apaixonado.", "Todo hombre es un poeta cuando est\u00e1 enamorado."),
    # 61
    ("\u00c9 Homero quem principalmente ensinou os outros poetas a arte de contar mentiras habilmente.", "Es Homero quien principalmente ha ense\u00f1ado a los otros poetas el arte de contar mentiras h\u00e1bilmente."),
    # 62
    ("Ningu\u00e9m est\u00e1 qualificado para ser estadista se for inteiramente ignorante dos problemas do trigo.", "Nadie est\u00e1 cualificado para ser estadista si es enteramente ignorante de los problemas del trigo."),
    # 63
    ("A penalidade mais pesada por decidir se envolver em pol\u00edtica \u00e9 ser governado por algu\u00e9m inferior a voc\u00ea.", "La penalidad m\u00e1s pesada por decidir involucrarse en pol\u00edtica es ser gobernado por alguien inferior a ti."),
    # 64
    ("O homem \u00e9 por natureza um animal c\u00edvico.", "El hombre es por naturaleza un animal c\u00edvico."),
    # 65
    ("Nos tornamos justos praticando a\u00e7\u00f5es justas, temperantes praticando a\u00e7\u00f5es temperantes, corajosos praticando a\u00e7\u00f5es corajosas.", "Nos volvemos justos practicando acciones justas, temperantes practicando acciones temperantes, valientes practicando acciones valientes."),
    # 66
    ("De um homem rico que era mesquinho, ele disse: \"Aquele homem n\u00e3o possui sua propriedade, sua propriedade \u00e9 que o possui.\"", "De un hombre rico que era mezquino, dijo: \"Ese hombre no posee su propiedad, su propiedad es la que lo posee.\""),
    # 67
    ("Nossas ora\u00e7\u00f5es devem ser por b\u00ean\u00e7\u00e3os em geral, pois Deus sabe melhor o que \u00e9 bom para n\u00f3s.", "Nuestras oraciones deben ser por bendiciones en general, pues Dios sabe mejor qu\u00e9 es bueno para nosotros."),
    # 68 - dup of 67
    ("Nossas ora\u00e7\u00f5es devem ser por b\u00ean\u00e7\u00e3os em geral, pois Deus sabe melhor o que \u00e9 bom para n\u00f3s.", "Nuestras oraciones deben ser por bendiciones en general, pues Dios sabe mejor qu\u00e9 es bueno para nosotros."),
    # 69
    ("Se todos os infort\u00fanios fossem postos num monte comum de onde todos devessem tomar uma por\u00e7\u00e3o igual, a maioria ficaria contente em tomar os seus e ir embora.", "Si todas las desgracias fueran puestas en un mont\u00f3n com\u00fan de donde todos debieran tomar una porci\u00f3n igual, la mayor\u00eda estar\u00eda contenta de tomar las suyas e irse."),
    # 70
    ("Quase nunca conheci um matem\u00e1tico que fosse capaz de raciocinar.", "Casi nunca he conocido a un matem\u00e1tico que fuera capaz de razonar."),
    # 71
    ("A vida \u00e9 cheia de acasos e mudan\u00e7as, e o mais pr\u00f3spero dos homens pode encontrar grandes infort\u00fanios.", "La vida est\u00e1 llena de azares y cambios, y el m\u00e1s pr\u00f3spero de los hombres puede encontrar grandes infortunios."),
    # 72
    ("Os inferiores se revoltam para serem iguais, e os iguais para serem superiores.", "Los inferiores se rebelan para ser iguales, y los iguales para ser superiores."),
    # 73
    ("As revolu\u00e7\u00f5es n\u00e3o s\u00e3o sobre trivialidades, mas brotam de trivialidades.", "Las revoluciones no son sobre trivialidades, pero brotan de trivialidades."),
    # 74
    ("Diferentes homens buscam a felicidade de diferentes maneiras e por diferentes meios, e assim criam para si diferentes modos de vida.", "Diferentes hombres buscan la felicidad de diferentes maneras y por diferentes medios, y as\u00ed crean para s\u00ed diferentes modos de vida."),
    # 75
    ("Cada cidad\u00e3o deve desempenhar seu papel na comunidade de acordo com seus dons individuais.", "Cada ciudadano debe desempe\u00f1ar su papel en la comunidad de acuerdo con sus dones individuales."),
    # 76 - dup of 10
    ("Se todos os infort\u00fanios fossem postos num monte comum de onde todos devessem tomar uma por\u00e7\u00e3o igual, a maioria ficaria contente em tomar os seus e ir embora.", "Si todas las desgracias fueran puestas en un mont\u00f3n com\u00fan de donde todos debieran tomar una porci\u00f3n igual, la mayor\u00eda estar\u00eda contenta de tomar las suyas e irse."),
    # 77
    ("Ci\u00eancia nada mais \u00e9 do que percep\u00e7\u00e3o.", "La ciencia no es m\u00e1s que percepci\u00f3n."),
    # 78
    ("O que est\u00e1 em nosso poder fazer, est\u00e1 em nosso poder n\u00e3o fazer.", "Lo que est\u00e1 en nuestro poder hacer, est\u00e1 en nuestro poder no hacer."),
    # 79
    ("Considero mais bravo aquele que vence seus desejos do que aquele que conquista seus inimigos; a vit\u00f3ria mais dif\u00edcil \u00e9 a vit\u00f3ria sobre si mesmo.", "Considero m\u00e1s valiente a aquel que vence sus deseos que a aquel que conquista a sus enemigos; la victoria m\u00e1s dif\u00edcil es la victoria sobre uno mismo."),
    # 80
    ("A vida que n\u00e3o \u00e9 examinada n\u00e3o vale a pena ser vivida.", "La vida que no es examinada no vale la pena ser vivida."),
    # 81
    ("Perguntaram a Tales o que era mais dif\u00edcil para o homem; ele respondeu: \"Conhecer a si mesmo.\"", "Preguntaron a Tales qu\u00e9 era lo m\u00e1s dif\u00edcil para el hombre; \u00e9l respondi\u00f3: \"Conocerse a s\u00ed mismo.\""),
    # 82
    ("O homem que faz tudo que leva \u00e0 felicidade depender de si mesmo adotou o melhor plano para viver feliz.", "El hombre que hace que todo lo que conduce a la felicidad dependa de s\u00ed mismo ha adoptado el mejor plan para vivir feliz."),
    # 83
    ("A vergonha \u00e9 um ornamento para os jovens, uma desgra\u00e7a para os velhos.", "La verg\u00fcenza es un ornamento para los j\u00f3venes, una desgracia para los viejos."),
    # 84
    ("Quanto menos desejos tivermos, mais nos assemelhamos aos deuses.", "Cuantos menos deseos tengamos, m\u00e1s nos asemejamos a los dioses."),
    # 85
    ("A ret\u00f3rica \u00e9 a arte de governar as mentes dos homens.", "La ret\u00f3rica es el arte de gobernar las mentes de los hombres."),
    # 86
    ("Os estados s\u00e3o como os homens; crescem a partir de caracteres humanos.", "Los estados son como los hombres; crecen a partir de caracteres humanos."),
    # 87
    ("Quando percebem a morte se aproximando, os cisnes cantam mais alegremente do que antes, por causa da alegria que t\u00eam em ir ao Deus que servem.", "Cuando perciben que la muerte se acerca, los cisnes cantan m\u00e1s alegremente que antes, por la alegr\u00eda que tienen de ir al Dios al que sirven."),
    # 88
    ("Uma grande cidade n\u00e3o deve ser confundida com uma populosa.", "Una gran ciudad no debe confundirse con una populosa."),
    # 89
    ("Quando a mente est\u00e1 pensando, est\u00e1 falando consigo mesma.", "Cuando la mente est\u00e1 pensando, est\u00e1 hablando consigo misma."),
    # 90
    ("As crian\u00e7as de hoje s\u00e3o tiranos. Contradizem seus pais, devoram sua comida e tiranizam seus professores.", "Los ni\u00f1os de hoy son tiranos. Contradicen a sus padres, devoran su comida y tiranizan a sus maestros."),
    # 91
    ("Todas as coisas fluem, nada permanece.", "Todas las cosas fluyen, nada permanece."),
    # 92
    ("Quanto a mim, tudo que sei \u00e9 que nada sei.", "En cuanto a m\u00ed, todo lo que s\u00e9 es que no s\u00e9 nada."),
    # 93
    ("Os homens melanc\u00f3licos s\u00e3o de todos os outros os mais espirituosos.", "Los hombres melanc\u00f3licos son de todos los dem\u00e1s los m\u00e1s ingeniosos."),
    # 94
    ("Se um homem quer mover o mundo, deve primeiro mover a si mesmo.", "Si un hombre quiere mover el mundo, debe primero moverse a s\u00ed mismo."),
    # 95
    ("A vida deve ser vivida como um jogo, jogando certos jogos, fazendo sacrif\u00edcios, cantando e dan\u00e7ando, e ent\u00e3o o homem poder\u00e1 propiciar os deuses e defender-se de seus inimigos.", "La vida debe vivirse como un juego, jugando ciertos juegos, haciendo sacrificios, cantando y bailando, y entonces el hombre podr\u00e1 propiciar a los dioses y defenderse de sus enemigos."),
    # 96 - long Heraclitus/Cratylus
    ("Observando que toda esta subst\u00e2ncia indeterminada est\u00e1 em movimento, supuseram que \u00e9 imposs\u00edvel fazer qualquer afirma\u00e7\u00e3o verdadeira sobre o que \u00e9 mut\u00e1vel em todos os sentidos. Desta suposi\u00e7\u00e3o floresceu a vis\u00e3o mais extrema, como a de Cr\u00e1tilo, que acabou pensando que n\u00e3o era preciso dizer nada, e apenas movia o dedo.", "Observando que toda esta sustancia indeterminada est\u00e1 en movimiento, supusieron que es imposible hacer cualquier afirmaci\u00f3n verdadera sobre lo que es mutable en todos los sentidos. De esta suposici\u00f3n floreci\u00f3 la visi\u00f3n m\u00e1s extrema, como la de Cr\u00e1tilo, que acab\u00f3 pensando que no hac\u00eda falta decir nada, y solo mov\u00eda el dedo."),
    # 97
    ("Os homens esquecem para onde o caminho leva e o que encontram todos os dias lhes parece estranho. N\u00e3o devemos agir nem falar como homens adormecidos.", "Los hombres olvidan adonde lleva el camino y lo que encuentran cada d\u00eda les parece extra\u00f1o. No debemos actuar ni hablar como hombres dormidos."),
    # 98
    ("Justi\u00e7a significa cuidar dos pr\u00f3prios assuntos e n\u00e3o se meter nos assuntos alheios.", "Justicia significa ocuparse de los propios asuntos y no entrometerse en los asuntos ajenos."),
    # 99
    ("\u00c9 claramente melhor que a propriedade seja privada, mas o uso dela comum; e o neg\u00f3cio especial do legislador \u00e9 criar nos homens esta disposi\u00e7\u00e3o benevolente.", "Es claramente mejor que la propiedad sea privada, pero el uso de ella com\u00fan; y el asunto especial del legislador es crear en los hombres esta disposici\u00f3n benevolente."),
    # 100
    ("Nossas ora\u00e7\u00f5es devem ser por b\u00ean\u00e7\u00e3os em geral, pois Deus sabe melhor o que \u00e9 bom para n\u00f3s.", "Nuestras oraciones deben ser por bendiciones en general, pues Dios sabe mejor qu\u00e9 es bueno para nosotros."),
    # 101
    ("A juventude \u00e9 facilmente enganada porque \u00e9 r\u00e1pida em esperar.", "La juventud es f\u00e1cilmente enga\u00f1ada porque es r\u00e1pida en esperar."),
    # 102
    ("N\u00e3o ficamos com raiva de pessoas que tememos ou respeitamos; n\u00e3o se pode ter medo de uma pessoa e ao mesmo tempo estar com raiva dela.", "No nos enojamos con personas que tememos o respetamos; no se puede tener miedo de una persona y al mismo tiempo estar enojado con ella."),
    # 103
    ("Pensar: a conversa da alma consigo mesma.", "Pensar: la conversaci\u00f3n del alma consigo misma."),
    # 104
    ("Fazemos guerra para que possamos viver em paz.", "Hacemos la guerra para poder vivir en paz."),
    # 105
    ("Quando o tirano se desfez dos inimigos externos por conquista ou tratado, e n\u00e3o h\u00e1 mais nada a temer, ele est\u00e1 sempre provocando alguma guerra ou outra, para que o povo precise de um l\u00edder.", "Cuando el tirano se ha deshecho de los enemigos externos por conquista o tratado, y no hay m\u00e1s nada que temer, siempre est\u00e1 provocando alguna guerra u otra, para que el pueblo necesite un l\u00edder."),
    # 106
    ("Deus \u00e9 dia e noite, inverno e ver\u00e3o, guerra e paz, fartura e fome.", "Dios es d\u00eda y noche, invierno y verano, guerra y paz, hartura y hambre."),
    # 107
    ("O amor \u00e9 a alegria dos bons, o espanto dos s\u00e1bios, o assombro dos deuses.", "El amor es la alegr\u00eda de los buenos, el asombro de los sabios, la admiraci\u00f3n de los dioses."),
    # 108
    ("Amar corretamente \u00e9 amar o que \u00e9 ordenado e belo de maneira educada e disciplinada.", "Amar correctamente es amar lo que es ordenado y bello de manera educada y disciplinada."),
    # 109
    ("Ao toque do amor todos se tornam poetas.", "Al toque del amor todos se convierten en poetas."),
    # 110
    ("O deus do amor vive num estado de necessidade. \u00c9 uma necessidade. \u00c9 um impulso. \u00c9 um desequil\u00edbrio homeost\u00e1tico. Como fome e sede, \u00e9 quase imposs\u00edvel extingu\u00ed-lo.", "El dios del amor vive en un estado de necesidad. Es una necesidad. Es un impulso. Es un desequilibrio homeost\u00e1tico. Como el hambre y la sed, es casi imposible extinguirlo."),
    # 111
    ("Que os pais legem a seus filhos n\u00e3o riquezas, mas o esp\u00edrito de rever\u00eancia.", "Que los padres leguen a sus hijos no riquezas, sino el esp\u00edritu de reverencia."),
    # 112
    ("Homens s\u00e1bios falam porque t\u00eam algo a dizer. Tolos porque t\u00eam que dizer algo.", "Los hombres sabios hablan porque tienen algo que decir. Los tontos porque tienen que decir algo."),
    # 113
    ("Voc\u00ea n\u00e3o pode entrar no mesmo rio duas vezes.", "No puedes entrar en el mismo r\u00edo dos veces."),
    # 114
    ("Pois boa cria\u00e7\u00e3o e educa\u00e7\u00e3o implantam boas constitui\u00e7\u00f5es.", "Pues buena crianza y educaci\u00f3n implantan buenas constituciones."),
    # 115
    ("O come\u00e7o \u00e9 a parte mais importante do trabalho.", "El comienzo es la parte m\u00e1s importante del trabajo."),
    # 116
    ("O fim do trabalho \u00e9 conquistar o lazer.", "El fin del trabajo es conquistar el ocio."),
    # 117
    ("O homem \u00e9 por natureza um animal pol\u00edtico.", "El hombre es por naturaleza un animal pol\u00edtico."),
    # 118
    ("Em todas as coisas da natureza h\u00e1 algo de maravilhoso.", "En todas las cosas de la naturaleza hay algo de maravilloso."),
    # 119
    ("Todas as a\u00e7\u00f5es humanas t\u00eam uma ou mais destas sete causas: acaso, natureza, compuls\u00f5es, h\u00e1bito, raz\u00e3o, paix\u00e3o, desejo.", "Todas las acciones humanas tienen una o m\u00e1s de estas siete causas: azar, naturaleza, compulsiones, h\u00e1bito, raz\u00f3n, pasi\u00f3n, deseo."),
    # 120
    ("A natureza nada faz em v\u00e3o.", "La naturaleza nada hace en vano."),
    # 121
    ("Preferir o mal ao bem n\u00e3o est\u00e1 na natureza humana; e quando um homem \u00e9 obrigado a escolher entre dois males, ningu\u00e9m escolher\u00e1 o maior quando pode escolher o menor.", "Preferir el mal al bien no est\u00e1 en la naturaleza humana; y cuando un hombre se ve obligado a elegir entre dos males, nadie elegir\u00e1 el mayor cuando puede elegir el menor."),
    # 122
    ("Aquele que \u00e9 de natureza calma e feliz dificilmente sentir\u00e1 a press\u00e3o da idade, mas para aquele de disposi\u00e7\u00e3o oposta, juventude e velhice s\u00e3o igualmente um fardo.", "Aquel que es de naturaleza tranquila y feliz dif\u00edcilmente sentir\u00e1 la presi\u00f3n de la edad, pero para aquel de disposici\u00f3n opuesta, juventud y vejez son igualmente una carga."),
    # 123
    ("A natureza costuma se esconder.", "La naturaleza suele esconderse."),
    # 124
    ("O sol tamb\u00e9m brilha nas fossas e n\u00e3o \u00e9 polu\u00eddo.", "El sol tambi\u00e9n brilla en las cloacas y no se contamina."),
    # 125
    ("Todos os homens s\u00e3o por natureza iguais, feitos da mesma terra por um \u00fanico Artífice; e por mais que nos enganemos, t\u00e3o caro a Deus \u00e9 o pobre campon\u00eas quanto o poderoso pr\u00edncipe.", "Todos los hombres son por naturaleza iguales, hechos de la misma tierra por un solo Art\u00edfice; y por m\u00e1s que nos enga\u00f1emos, tan querido por Dios es el pobre campesino como el poderoso pr\u00edncipe."),
    # 126
    ("As virtudes morais n\u00e3o s\u00e3o produzidas em n\u00f3s pela natureza nem contra a natureza. A natureza prepara em n\u00f3s o terreno para sua recep\u00e7\u00e3o, mas sua forma\u00e7\u00e3o completa \u00e9 produto do h\u00e1bito.", "Las virtudes morales no son producidas en nosotros por la naturaleza ni contra la naturaleza. La naturaleza prepara en nosotros el terreno para su recepci\u00f3n, pero su formaci\u00f3n completa es producto del h\u00e1bito."),
    # 127
    ("Se um caminho \u00e9 melhor que outro, pode ter certeza de que \u00e9 o caminho da natureza.", "Si un camino es mejor que otro, puedes estar seguro de que es el camino de la naturaleza."),
    # 128
    ("Quando olho para marinheiros, homens de ci\u00eancia e fil\u00f3sofos, o homem \u00e9 o mais s\u00e1bio de todos os seres; quando olho para sacerdotes e profetas, nada \u00e9 t\u00e3o desprez\u00edvel quanto o homem.", "Cuando miro a marineros, hombres de ciencia y fil\u00f3sofos, el hombre es el m\u00e1s sabio de todos los seres; cuando miro a sacerdotes y profetas, nada es tan despreciable como el hombre."),
    # 129
    ("Ci\u00eancia nada mais \u00e9 do que percep\u00e7\u00e3o.", "La ciencia no es m\u00e1s que percepci\u00f3n."),
    # 130
    ("Portanto, o bem do homem deve ser o fim da ci\u00eancia pol\u00edtica.", "Por lo tanto, el bien del hombre debe ser el fin de la ciencia pol\u00edtica."),
    # 131
    ("A sabedoria \u00e9 a \u00fanica ci\u00eancia das outras ci\u00eancias.", "La sabidur\u00eda es la \u00fanica ciencia de las otras ciencias."),
    # 132
    ("O \u00fanico sinal exclusivo de conhecimento completo \u00e9 o poder de ensinar.", "La \u00fanica se\u00f1al exclusiva de conocimiento completo es el poder de ense\u00f1ar."),
    # 133
    ("Por que n\u00e3o chicotear o professor quando o aluno se comporta mal?", "\u00bfPor qu\u00e9 no azotar al maestro cuando el alumno se porta mal?"),
    # 134
    ("A morte pode ser a maior de todas as b\u00ean\u00e7\u00e3os humanas.", "La muerte puede ser la mayor de todas las bendiciones humanas."),
]

for i, key in enumerate(batch):
    if i < len(tl):
        tr[key] = {"pt": tl[i][0], "es": tl[i][1]}

with open('c:/Users/lalli/Flutter/coach_phrase_app/translations_classical.json', 'w', encoding='utf-8') as f:
    json.dump(tr, f, ensure_ascii=False, indent=2)

print(f'Classical translations total: {len(tr)}')
