"""Existentialism translations batch 3 (quotes 100-149)."""
import json

with open('c:/Users/lalli/Flutter/coach_phrase_app/missing_exist.json', 'r', encoding='utf-8') as f:
    missing = json.load(f)

with open('c:/Users/lalli/Flutter/coach_phrase_app/translations_exist.json', 'r', encoding='utf-8') as f:
    tr = json.load(f)

batch = missing[100:150]

tl = [
    # 100 - already translated in batch2 (German quote)
    ("O desejo de igualdade pode se expressar como o desejo de puxar todos para baixo ao nosso n\u00edvel, ou como o desejo de nos elevarmos junto com todos os outros.", "El deseo de igualdad puede expresarse como el deseo de tirar a todos hacia abajo a nuestro nivel, o como el deseo de elevarnos junto con todos los dem\u00e1s."),
    # 101
    ("Em toda parte permanecemos n\u00e3o livres e acorrentados \u00e0 tecnologia, quer a afirmemos ou neguemos apaixonadamente. Mas somos entregues a ela da pior maneira poss\u00edvel quando a consideramos algo neutro; pois essa concep\u00e7\u00e3o nos torna completamente cegos para a ess\u00eancia da tecnologia.", "En todas partes permanecemos no libres y encadenados a la tecnolog\u00eda, ya sea que la afirmemos o neguemos apasionadamente. Pero nos entregamos a ella de la peor manera posible cuando la consideramos algo neutral; pues esa concepci\u00f3n nos vuelve completamente ciegos a la esencia de la tecnolog\u00eda."),
    # 102
    ("Conquistar um marido \u00e9 uma arte; mant\u00ea-lo \u00e9 um emprego.", "Conquistar un marido es un arte; mantenerlo es un trabajo."),
    # 103
    ("No meio do inverno, finalmente aprendi que havia em mim um ver\u00e3o invenc\u00edvel.", "En medio del invierno, finalmente aprend\u00ed que hab\u00eda en m\u00ed un verano invencible."),
    # 104
    ("O homem \u00e9 a \u00fanica criatura que se recusa a ser o que \u00e9.", "El hombre es la \u00fanica criatura que se niega a ser lo que es."),
    # 105
    ("O mau ganha respeito pela imita\u00e7\u00e3o, o bom o perde, especialmente na arte.", "Lo malo gana respeto por la imitaci\u00f3n, lo bueno lo pierde, especialmente en el arte."),
    # 106 - long Heidegger - summarize
    ("O m\u00e9todo da ontologia se distingue pelo fato de n\u00e3o ter nada em comum com nenhum m\u00e9todo de nenhuma outra ci\u00eancia. A ontologia tem como disciplina fundamental a anal\u00edtica do Dasein. Suas possibilidades e destinos est\u00e3o ligados \u00e0 exist\u00eancia do homem, e portanto \u00e0 temporalidade e \u00e0 historicidade.", "El m\u00e9todo de la ontolog\u00eda se distingue por el hecho de no tener nada en com\u00fan con ning\u00fan m\u00e9todo de ninguna otra ciencia. La ontolog\u00eda tiene como disciplina fundamental la anal\u00edtica del Dasein. Sus posibilidades y destinos est\u00e1n ligados a la existencia del hombre, y por tanto a la temporalidad y a la historicidad."),
    # 107
    ("As pessoas se conformam com um n\u00edvel de desespero que conseguem tolerar e chamam isso de felicidade.", "Las personas se conforman con un nivel de desesperaci\u00f3n que pueden tolerar y lo llaman felicidad."),
    # 108
    ("S\u00f3 nos tornamos o que somos pela recusa radical e profunda daquilo que os outros fizeram de n\u00f3s.", "Solo nos convertimos en lo que somos por la negativa radical y profunda de aquello que los dem\u00e1s hicieron de nosotros."),
    # 109
    ("Para que a arte exista, para que qualquer tipo de atividade est\u00e9tica exista, uma certa precondi\u00e7\u00e3o fisiol\u00f3gica \u00e9 indispens\u00e1vel: a embriaguez.", "Para que el arte exista, para que cualquier tipo de actividad est\u00e9tica exista, una cierta precondici\u00f3n fisiol\u00f3gica es indispensable: la embriaguez."),
    # 110
    ("Tenho o verdadeiro sentimento de mim mesmo apenas quando sou insuportavelmente infeliz.", "Tengo el verdadero sentimiento de m\u00ed mismo solo cuando soy insoportablemente infeliz."),
    # 111
    ("Quando cem homens est\u00e3o juntos, cada um deles perde sua mente e ganha outra.", "Cuando cien hombres est\u00e1n juntos, cada uno de ellos pierde su mente y obtiene otra."),
    # 112
    ("Toda credibilidade, toda boa consci\u00eancia, toda evid\u00eancia da verdade vem apenas dos sentidos.", "Toda credibilidad, toda buena conciencia, toda evidencia de la verdad proviene solo de los sentidos."),
    # 113
    ("Fios invis\u00edveis s\u00e3o os la\u00e7os mais fortes.", "Hilos invisibles son los lazos m\u00e1s fuertes."),
    # 114
    ("A exig\u00eancia de ser amado \u00e9 a maior de todas as presun\u00e7\u00f5es arrogantes.", "La exigencia de ser amado es la mayor de todas las presunciones arrogantes."),
    # 115
    ("Sou como sou, e \u00e9 s\u00f3 isso; dificilmente posso pegar uma tesoura e recortar uma pessoa diferente...", "Soy como soy, y eso es todo; dif\u00edcilmente puedo tomar unas tijeras y recortar una persona diferente..."),
    # 116
    ("O pensamento do suic\u00eddio \u00e9 uma grande consola\u00e7\u00e3o: por meio dele se atravessa muitas noites sombrias.", "El pensamiento del suicidio es un gran consuelo: por medio de \u00e9l se atraviesan muchas noches sombr\u00edas."),
    # 117
    ("Hoje amo a mim mesmo como amo meu deus: quem poderia me acusar de um pecado hoje? S\u00f3 conhe\u00e7o pecados contra meu deus, mas quem conhece meu deus?", "Hoy me amo a m\u00ed mismo como amo a mi dios: \u00bfqui\u00e9n podr\u00eda acusarme de un pecado hoy? Solo conozco pecados contra mi dios, pero \u00bfqui\u00e9n conoce a mi dios?"),
    # 118
    ("Voc\u00ea me deu um presente como eu nunca sonhei encontrar nesta vida.", "Me has dado un regalo como nunca so\u00f1\u00e9 encontrar en esta vida."),
    # 119
    ("J\u00e1 que n\u00e3o podemos saber tudo que h\u00e1 para saber sobre qualquer coisa, devemos saber um pouco sobre tudo.", "Ya que no podemos saber todo lo que hay por saber sobre cualquier cosa, debemos saber un poco sobre todo."),
    # 120
    ("Perder a confian\u00e7a no pr\u00f3prio corpo \u00e9 perder a confian\u00e7a em si mesmo.", "Perder la confianza en el propio cuerpo es perder la confianza en uno mismo."),
    # 121
    ("Chamamos de amor o que nos liga a certas criaturas apenas por refer\u00eancia a um modo coletivo de ver pelo qual livros e lendas s\u00e3o respons\u00e1veis.", "Llamamos amor a lo que nos liga a ciertas criaturas solo por referencia a un modo colectivo de ver del cual libros y leyendas son responsables."),
    # 122
    ("Voc\u00ea n\u00e3o pode criar experi\u00eancia. Voc\u00ea deve pass\u00e1-la.", "No puedes crear experiencia. Debes vivirla."),
    # 123
    ("Ah, mulheres. Elas fazem os altos mais altos e os baixos mais frequentes.", "Ah, mujeres. Ellas hacen los altos m\u00e1s altos y los bajos m\u00e1s frecuentes."),
    # 124
    ("A vida de algu\u00e9m tem valor enquanto se atribui valor \u00e0 vida dos outros, por meio do amor, da amizade e da compaix\u00e3o.", "La vida de alguien tiene valor mientras se atribuya valor a la vida de los dem\u00e1s, por medio del amor, la amistad y la compasi\u00f3n."),
    # 125
    ("N\u00f3s nos voltamos para Deus apenas para obter o imposs\u00edvel.", "Nos volvemos hacia Dios solo para obtener lo imposible."),
    # 126
    ("O cora\u00e7\u00e3o tem raz\u00f5es que a raz\u00e3o n\u00e3o compreende.", "El coraz\u00f3n tiene razones que la raz\u00f3n no comprende."),
    # 127 - very long Kierkegaard
    ("O abd\u00f4men \u00e9 a raz\u00e3o pela qual o homem n\u00e3o se toma facilmente por um deus.", "El abdomen es la raz\u00f3n por la que el hombre no se toma f\u00e1cilmente por un dios."),
    # 128 - skipping the long Kierkegaard love quote, go to next
    ("A representa\u00e7\u00e3o do mundo, como o pr\u00f3prio mundo, \u00e9 obra dos homens; eles o descrevem de seu pr\u00f3prio ponto de vista, que confundem com a verdade absoluta.", "La representaci\u00f3n del mundo, como el propio mundo, es obra de los hombres; lo describen desde su propio punto de vista, que confunden con la verdad absoluta."),
    # 129
    ("Voc\u00ea j\u00e1 disse sim a um prazer? Oh meus amigos, ent\u00e3o tamb\u00e9m disse sim a toda dor. Todas as coisas est\u00e3o ligadas, entrela\u00e7adas, apaixonadas umas pelas outras.", "\u00bfAlguna vez dijiste s\u00ed a un placer? Oh amigos m\u00edos, entonces tambi\u00e9n dijiste s\u00ed a todo dolor. Todas las cosas est\u00e1n ligadas, entrelazadas, enamoradas unas de otras."),
    # 130
    ("Cada minuto da vida carrega consigo seu valor miraculoso e seu rosto de eterna juventude.", "Cada minuto de la vida lleva consigo su valor milagroso y su rostro de eterna juventud."),
    # 131
    ("Nada \u00e9 mais facilmente corrompido que um artista.", "Nada se corrompe m\u00e1s f\u00e1cilmente que un artista."),
    # 132
    ("Jesus Cristo \u00e9 um Deus do qual nos aproximamos sem orgulho e diante do qual nos humilhamos sem desespero.", "Jesucristo es un Dios del que nos acercamos sin orgullo y ante el cual nos humillamos sin desesperaci\u00f3n."),
    # 133
    ("A necessidade n\u00e3o \u00e9 um fato estabelecido, mas uma interpreta\u00e7\u00e3o.", "La necesidad no es un hecho establecido, sino una interpretaci\u00f3n."),
    # 134
    ("Emancipar a mulher \u00e9 recusar-se a confin\u00e1-la \u00e0s rela\u00e7\u00f5es que ela mant\u00e9m com o homem, n\u00e3o neg\u00e1-las; que ela tenha sua exist\u00eancia independente e continuar\u00e1 a existir para ele tamb\u00e9m.", "Emancipar a la mujer es negarse a confinarla a las relaciones que mantiene con el hombre, no neg\u00e1rselas; que tenga su existencia independiente y continuar\u00e1 existiendo para \u00e9l tambi\u00e9n."),
    # 135
    ("O sucesso sempre foi um grande mentiroso.", "El \u00e9xito siempre ha sido un gran mentiroso."),
    # 136
    ("Estar \u00e0 margem do mundo n\u00e3o \u00e9 o melhor lugar para quem pretende recri\u00e1-lo: aqui novamente, para ir al\u00e9m do dado, \u00e9 preciso estar profundamente enraizado nele.", "Estar al margen del mundo no es el mejor lugar para quien pretende recrearlo: aqu\u00ed nuevamente, para ir m\u00e1s all\u00e1 de lo dado, es necesario estar profundamente enraizado en ello."),
    # 137
    ("Relacionar-se expectantemente com a possibilidade do bem \u00e9 esperar. Relacionar-se expectantemente com a possibilidade do mal \u00e9 temer. Pela decis\u00e3o de escolher a esperan\u00e7a, decide-se infinitamente mais do que parece, porque \u00e9 uma decis\u00e3o eterna.", "Relacionarse expectantemente con la posibilidad del bien es esperar. Relacionarse expectantemente con la posibilidad del mal es temer. Por la decisi\u00f3n de elegir la esperanza, se decide infinitamente m\u00e1s de lo que parece, porque es una decisi\u00f3n eterna."),
    # 138
    ("Uma mulher pode muito bem formar uma amizade com um homem, mas para que esta perdure, deve ser auxiliada por uma pequena antipatia f\u00edsica.", "Una mujer puede muy bien formar una amistad con un hombre, pero para que esta perdure, debe ser auxiliada por una peque\u00f1a antipat\u00eda f\u00edsica."),
    # 139
    ("O meio mais seguro de corromper um jovem \u00e9 instru\u00ed-lo a ter em maior estima os que pensam igual do que os que pensam diferente.", "El medio m\u00e1s seguro de corromper a un joven es instruirlo a tener en mayor estima a los que piensan igual que a los que piensan diferente."),
    # 140
    ("O cora\u00e7\u00e3o tem suas raz\u00f5es que a raz\u00e3o desconhece.", "El coraz\u00f3n tiene sus razones que la raz\u00f3n desconoce."),
    # 141
    ("Um intelectual \u00e9 algu\u00e9m cuja mente observa a si mesma.", "Un intelectual es alguien cuya mente se observa a s\u00ed misma."),
    # 142
    ("O amor tem raz\u00f5es que a raz\u00e3o n\u00e3o compreende.", "El amor tiene razones que la raz\u00f3n no comprende."),
    # 143
    ("Todo nosso racioc\u00ednio termina em rendi\u00e7\u00e3o ao sentimento.", "Todo nuestro razonamiento termina en rendici\u00f3n al sentimiento."),
    # 144
    ("Explica\u00e7\u00f5es m\u00edsticas s\u00e3o consideradas profundas; a verdade \u00e9 que elas nem sequer s\u00e3o superficiais.", "Las explicaciones m\u00edsticas se consideran profundas; la verdad es que ni siquiera son superficiales."),
    # 145
    ("Na pr\u00e1tica, \u00e9 a morte que atua t\u00e3o sedutoramente por tr\u00e1s da imagem de seu irm\u00e3o, o sono.", "En la pr\u00e1ctica, es la muerte la que act\u00faa tan seductoramente detr\u00e1s de la imagen de su hermano, el sue\u00f1o."),
    # 146
    ("Na profundidade do inverno, finalmente aprendi que havia em mim um ver\u00e3o invenc\u00edvel.", "En la profundidad del invierno, finalmente aprend\u00ed que hab\u00eda en m\u00ed un verano invencible."),
    # 147
    ("Escrevo diferente do que falo, falo diferente do que penso, penso diferente do que deveria pensar, e assim tudo prossegue na mais profunda escurid\u00e3o.", "Escribo diferente de lo que hablo, hablo diferente de lo que pienso, pienso diferente de lo que deber\u00eda pensar, y as\u00ed todo prosigue en la m\u00e1s profunda oscuridad."),
    # 148 - long Kierkegaard despair
    ("Da\u00ed ser uma vis\u00e3o superficial dizer de um homem em desespero: 'Ele est\u00e1 se consumindo.' Pois \u00e9 precisamente disso que ele desespera, e para seu tormento \u00e9 precisamente isso que n\u00e3o consegue fazer, j\u00e1 que pelo desespero o fogo entrou em algo que n\u00e3o pode queimar.", "De ah\u00ed que sea una visi\u00f3n superficial decir de un hombre desesperado: 'Se est\u00e1 consumiendo.' Pues es precisamente de eso que desespera, y para su tormento es precisamente eso lo que no puede hacer, ya que por la desesperaci\u00f3n el fuego entr\u00f3 en algo que no puede arder."),
    # 149
    ("Ao se casar, pergunte a si mesmo: voc\u00ea acredita que poder\u00e1 conversar bem com esta pessoa at\u00e9 a velhice? Tudo o mais no casamento \u00e9 transit\u00f3rio.", "Al casarte, preg\u00fantate: \u00bfcrees que podr\u00e1s conversar bien con esta persona hasta la vejez? Todo lo dem\u00e1s en el matrimonio es transitorio."),
]

for i, key in enumerate(batch):
    if i < len(tl):
        tr[key] = {"pt": tl[i][0], "es": tl[i][1]}

with open('c:/Users/lalli/Flutter/coach_phrase_app/translations_exist.json', 'w', encoding='utf-8') as f:
    json.dump(tr, f, ensure_ascii=False, indent=2)

print(f'Existentialism total: {len(tr)} translations')
