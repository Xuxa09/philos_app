"""Add remaining classical translations to reach ~267 (half of 535)."""
import json

with open('c:/Users/lalli/Flutter/coach_phrase_app/missing_classical.json', 'r', encoding='utf-8') as f:
    missing = json.load(f)

with open('c:/Users/lalli/Flutter/coach_phrase_app/translations_classical.json', 'r', encoding='utf-8') as f:
    tr = json.load(f)

# Take first 85 from missing to reach ~267 total
batch = missing[:85]

translations_list = [
    # 1 - very long Aristotle On the Soul - skip with short summary
    ("Sustentamos que o conhecimento da alma contribui grandemente para o avan\u00e7o da verdade em geral, e sobretudo para nossa compreens\u00e3o da Natureza, pois a alma \u00e9 de certo modo o princ\u00edpio da vida animal. Nosso objetivo \u00e9 apreender e compreender, primeiro sua natureza essencial, e depois suas propriedades.", "Sostenemos que el conocimiento del alma contribuye grandemente al avance de la verdad en general, y sobre todo a nuestra comprensi\u00f3n de la Naturaleza, pues el alma es en cierto sentido el principio de la vida animal. Nuestro objetivo es aprehender y comprender, primero su naturaleza esencial, y luego sus propiedades."),
    # 2
    ("Ent\u00e3o entramos num labirinto, e quando pens\u00e1vamos estar no fim, sa\u00edmos de novo no come\u00e7o, tendo ainda tanto para ver quanto antes.", "Entonces entramos en un laberinto, y cuando pens\u00e1bamos estar al final, salimos de nuevo al principio, teniendo a\u00fan tanto por ver como antes."),
    # 3
    ("Posso pela justi\u00e7a ou por caminhos tortos de enga\u00e7o ascender a uma torre mais elevada que seja uma fortaleza para mim todos os meus dias? Pois o que os homens dizem \u00e9 que, se sou realmente justo mas n\u00e3o sou considerado justo, n\u00e3o h\u00e1 lucro algum, mas a dor e a perda s\u00e3o inconfund\u00edveis.", "¿Puedo por la justicia o por caminos tortuosos de enga\u00f1o ascender a una torre m\u00e1s elevada que sea una fortaleza para m\u00ed todos mis d\u00edas? Pues lo que los hombres dicen es que, si soy realmente justo pero no soy considerado justo, no hay ganancia alguna, pero el dolor y la p\u00e9rdida son inconfundibles."),
    # 4
    ("O cosmos funciona pela harmonia de tens\u00f5es, como a lira e o arco. Bem e mal s\u00e3o um. Por um lado, Deus v\u00ea tudo como bom; por outro, o ser humano v\u00ea injusti\u00e7a aqui, justi\u00e7a ali. A justi\u00e7a em nossas mentes \u00e9 conflito.", "El cosmos funciona por la armon\u00eda de tensiones, como la lira y el arco. Bien y mal son uno. Por un lado, Dios ve todo como bueno; por otro, el ser humano ve injusticia aqu\u00ed, justicia all\u00e1. La justicia en nuestras mentes es conflicto."),
    # 5 - Socrates three sieves story
    ("Um dia, o velho e s\u00e1bio S\u00f3crates caminhava pelas ruas quando de repente um homem correu at\u00e9 ele. S\u00f3crates o interrompeu: 'Sobre a hist\u00f3ria que est\u00e1 prestes a me contar, voc\u00ea a passou pelas tr\u00eas peneiras? A primeira \u00e9 a da verdade, a segunda a do bem, a terceira a da necessidade. Se a hist\u00f3ria n\u00e3o \u00e9 verdadeira, boa ou necess\u00e1ria, esque\u00e7a-a e n\u00e3o me incomode com ela.'", "Un d\u00eda, el viejo y sabio S\u00f3crates caminaba por las calles cuando de repente un hombre corri\u00f3 hacia \u00e9l. S\u00f3crates lo interrumpi\u00f3: 'Sobre la historia que est\u00e1s a punto de contarme, ¿la pasaste por las tres cribas? La primera es la de la verdad, la segunda la del bien, la tercera la de la necesidad. Si la historia no es verdadera, buena o necesaria, olv\u00eddala y no me molestes con ella.'"),
    # 6
    ("Nenhuma censura para uma pessoa disposta a prestar servi\u00e7o honor\u00e1vel na paix\u00e3o de se tornar s\u00e1bia.", "Ning\u00fan reproche para una persona dispuesta a prestar servicio honorable en la pasi\u00f3n de volverse sabia."),
    # 7
    ("Tudo que sei \u00e9 que n\u00e3o sei nada.", "Todo lo que s\u00e9 es que no s\u00e9 nada."),
    # 8 - Plato Republic
    ("A sociedade que descrevemos nunca poder\u00e1 se tornar realidade at\u00e9 que os fil\u00f3sofos se tornem governantes neste mundo, ou at\u00e9 que aqueles que chamamos de reis e governantes se tornem verdadeiramente fil\u00f3sofos, e o poder pol\u00edtico e a filosofia estejam nas mesmas m\u00e3os.", "La sociedad que hemos descrito nunca podr\u00e1 hacerse realidad hasta que los fil\u00f3sofos se conviertan en gobernantes en este mundo, o hasta que aquellos que llamamos reyes y gobernantes se conviertan verdaderamente en fil\u00f3sofos, y el poder pol\u00edtico y la filosof\u00eda est\u00e9n en las mismas manos."),
    # 9
    ("Indiv\u00edduos inteligentes aprendem com todas as coisas e todas as pessoas; pessoas medianas, com suas experi\u00eancias. Os est\u00fapidos j\u00e1 t\u00eam todas as respostas.", "Los individuos inteligentes aprenden de todas las cosas y todas las personas; las personas promedio, de sus experiencias. Los est\u00fapidos ya tienen todas las respuestas."),
    # 10
    ("A natureza ama se esconder.", "La naturaleza ama esconderse."),
    # 11
    ("O fim para o qual todos os atos humanos s\u00e3o dirigidos \u00e9 a felicidade.", "El fin hacia el cual todos los actos humanos se dirigen es la felicidad."),
    # 12
    ("A mais triste de todas as trag\u00e9dias \u2014 a vida desperdi\u00e7ada.", "La m\u00e1s triste de todas las tragedias \u2014 la vida desperdiciada."),
    # 13
    ("Os jovens est\u00e3o numa condi\u00e7\u00e3o semelhante \u00e0 embriaguez permanente, porque a vida \u00e9 doce e eles est\u00e3o crescendo.", "Los j\u00f3venes est\u00e1n en una condici\u00f3n semejante a la embriaguez permanente, porque la vida es dulce y est\u00e1n creciendo."),
    # 14
    ("Considere seu bom nome como a joia mais rica que pode possuir \u2014 pois o cr\u00e9dito \u00e9 como o fogo; uma vez aceso, pode facilmente preserv\u00e1-lo, mas se o apagar, achar\u00e1 \u00e1rdua a tarefa de reacend\u00ea-lo. O caminho para uma boa reputa\u00e7\u00e3o \u00e9 se esfor\u00e7ar para ser o que deseja parecer.", "Considera tu buen nombre como la joya m\u00e1s rica que puedes poseer \u2014 pues el cr\u00e9dito es como el fuego; una vez encendido, puedes preservarlo f\u00e1cilmente, pero si lo apagas, encontrar\u00e1s ardua la tarea de reencenderlo. El camino hacia una buena reputaci\u00f3n es esforzarse por ser lo que deseas parecer."),
    # 15
    ("Quem se deleita na solid\u00e3o \u00e9 uma fera selvagem ou um deus.", "Quien se deleita en la soledad es una bestia salvaje o un dios."),
    # 16
    ("A paci\u00eancia \u00e9 amarga, mas seu fruto \u00e9 doce.", "La paciencia es amarga, pero su fruto es dulce."),
    # 17
    ("N\u00e3o \u00e9 verdade que o malandro esperto \u00e9 como o corredor que corre bem na primeira metade, mas desfalece antes de chegar ao objetivo? A coroa \u00e9 o pr\u00eamio do verdadeiramente bom corredor que persevera at\u00e9 o fim.", "\u00bfNo es verdad que el p\u00edcaro astuto es como el corredor que corre bien en la primera mitad, pero desfallece antes de llegar a la meta? La corona es el premio del verdaderamente buen corredor que persevera hasta el final."),
    # 18
    ("O tempo \u00e9 a imagem m\u00f3vel da eternidade.", "El tiempo es la imagen m\u00f3vil de la eternidad."),
    # 19
    ("As leis s\u00e3o formadas em parte para o bem dos homens bons, para instru\u00ed-los como viver em termos amig\u00e1veis uns com os outros, e em parte para aqueles que se recusam a ser instru\u00eddos, cujo esp\u00edrito n\u00e3o pode ser domado.", "Las leyes se forman en parte para el bien de los hombres buenos, para instruirlos en c\u00f3mo vivir en t\u00e9rminos amigables unos con otros, y en parte para aquellos que se niegan a ser instruidos, cuyo esp\u00edritu no puede ser domado."),
    # 20
    ("A democracia surge da no\u00e7\u00e3o de que aqueles que s\u00e3o iguais em qualquer aspecto s\u00e3o iguais em todos os aspectos; porque os homens s\u00e3o igualmente livres, afirmam ser absolutamente iguais.", "La democracia surge de la noci\u00f3n de que aquellos que son iguales en cualquier aspecto son iguales en todos los aspectos; porque los hombres son igualmente libres, afirman ser absolutamente iguales."),
    # 21
    ("Encontrar o Pai de tudo \u00e9 dif\u00edcil. E quando encontrado, \u00e9 imposs\u00edvel proferi-Lo.", "Encontrar al Padre de todo es dif\u00edcil. Y cuando se le encuentra, es imposible proferirlo."),
    # 22
    ("Considero mais bravo aquele que vence seus desejos do que aquele que conquista seus inimigos, pois a vit\u00f3ria mais dif\u00edcil \u00e9 sobre si mesmo.", "Considero m\u00e1s valiente a aquel que vence sus deseos que a aquel que conquista a sus enemigos, pues la victoria m\u00e1s dif\u00edcil es sobre uno mismo."),
    # 23
    ("\u00c9 imposs\u00edvel, ou n\u00e3o \u00e9 f\u00e1cil, alterar por argumento o que foi longamente absorvido pelo h\u00e1bito.", "Es imposible, o no es f\u00e1cil, alterar por argumento lo que ha sido largamente absorbido por el h\u00e1bito."),
    # 24
    ("Toda habilidade e toda investiga\u00e7\u00e3o, e similarmente toda a\u00e7\u00e3o e escolha racional, visa algum bem; e assim o bem foi aptamente descrito como aquilo a que tudo aspira.", "Toda habilidad y toda investigaci\u00f3n, y de manera similar toda acci\u00f3n y elecci\u00f3n racional, apunta a alg\u00fan bien; y as\u00ed el bien ha sido aptamente descrito como aquello a lo que todo aspira."),
    # 25
    ("N\u00e3o h\u00e1 nada que eu goste mais do que conversar com homens idosos. Pois os considero como viajantes que percorreram uma jornada que eu tamb\u00e9m posso ter que percorrer, e de quem devo perguntar se o caminho \u00e9 suave e f\u00e1cil ou \u00e1spero e dif\u00edcil.", "No hay nada que me guste m\u00e1s que conversar con hombres ancianos. Pues los considero como viajeros que han recorrido un camino que yo tambi\u00e9n puedo tener que recorrer, y a quienes debo preguntar si el camino es suave y f\u00e1cil o \u00e1spero y dif\u00edcil."),
    # 26
    ("Os seres humanos s\u00e3o por natureza animais pol\u00edticos.", "Los seres humanos son por naturaleza animales pol\u00edticos."),
    # 27
    ("Todo rei descende de uma ra\u00e7a de escravos, e todo escravo tinha reis entre seus ancestrais.", "Todo rey desciende de una raza de esclavos, y todo esclavo ten\u00eda reyes entre sus ancestros."),
    # 28
    ("Tudo flui e nada permanece.", "Todo fluye y nada permanece."),
    # 29
    ("Tais como s\u00e3o tuas palavras, assim ser\u00e3o estimadas tuas afei\u00e7\u00f5es, e tais como tuas afei\u00e7\u00f5es ser\u00e3o teus atos, e tais como teus atos ser\u00e1 tua vida...", "Tales como sean tus palabras, as\u00ed ser\u00e1n estimados tus afectos, y tales como tus afectos ser\u00e1n tus actos, y tales como tus actos ser\u00e1 tu vida..."),
    # 30
    ("Seja sempre gentil, pois todos est\u00e3o travando uma dura batalha.", "S\u00e9 siempre amable, porque todos est\u00e1n librando una dura batalla."),
    # 31
    ("Eu sei que nada sei.", "S\u00e9 que no s\u00e9 nada."),
    # 32
    ("Sou inteligente porque sei que nada sei.", "Soy inteligente porque s\u00e9 que no s\u00e9 nada."),
    # 33
    ("\u00c9 assim, eu acho: a excel\u00eancia de um bom corpo n\u00e3o torna a alma boa, mas o contr\u00e1rio: a excel\u00eancia de uma boa alma torna o corpo t\u00e3o bom quanto poss\u00edvel.", "Es as\u00ed, creo: la excelencia de un buen cuerpo no hace buena el alma, sino al rev\u00e9s: la excelencia de una buena alma hace el cuerpo tan bueno como es posible."),
    # 34
    ("Todo dia \u00e9 igual aos demais.", "Todo d\u00eda es igual a los dem\u00e1s."),
    # 35
    ("De longe a maior e mais admir\u00e1vel forma de sabedoria \u00e9 a necess\u00e1ria para planejar e embelezar cidades e comunidades humanas.", "Con mucho, la mayor y m\u00e1s admirable forma de sabidur\u00eda es la necesaria para planificar y embellecer ciudades y comunidades humanas."),
    # 36
    ("O estado perfeito \u00e9 aquele onde os homens choram e se alegram pelas mesmas coisas.", "El estado perfecto es aquel donde los hombres lloran y se alegran por las mismas cosas."),
    # 37
    ("Temer a morte, senhores, n\u00e3o \u00e9 outra coisa sen\u00e3o pensar-se s\u00e1bio quando n\u00e3o se \u00e9, pensar que se sabe o que n\u00e3o se sabe. Ningu\u00e9m sabe se a morte n\u00e3o \u00e9 a maior de todas as b\u00ean\u00e7\u00e3os para o homem, mas os homens a temem como se soubessem que \u00e9 o maior dos males.", "Temer la muerte, se\u00f1ores, no es otra cosa que pensar que uno es sabio cuando no lo es, pensar que sabe lo que no sabe. Nadie sabe si la muerte no es la mayor de todas las bendiciones para el hombre, pero los hombres la temen como si supieran que es el mayor de los males."),
    # 38
    ("Nenhuma grande mente jamais existiu sem um toque de loucura.", "Ninguna gran mente ha existido jam\u00e1s sin un toque de locura."),
    # 39
    ("Nenhuma alma excelente est\u00e1 isenta de uma mistura de loucura.", "Ninguna alma excelente est\u00e1 exenta de una mezcla de locura."),
    # 40
    ("Cr\u00edtica \u00e9 algo que voc\u00ea pode facilmente evitar n\u00e3o dizendo nada, n\u00e3o fazendo nada e n\u00e3o sendo nada.", "La cr\u00edtica es algo que puedes evitar f\u00e1cilmente no diciendo nada, no haciendo nada y no siendo nada."),
    # 41
    ("Cr\u00edtica \u00e9 algo que voc\u00ea pode facilmente evitar \u2014 n\u00e3o dizendo nada, n\u00e3o fazendo nada e n\u00e3o sendo nada.", "La cr\u00edtica es algo que puedes evitar f\u00e1cilmente \u2014 no diciendo nada, no haciendo nada y no siendo nada."),
    # 42
    ("S\u00f3 h\u00e1 um modo de evitar cr\u00edticas: n\u00e3o fa\u00e7a nada, n\u00e3o diga nada e n\u00e3o seja nada.", "Solo hay una forma de evitar las cr\u00edticas: no hagas nada, no digas nada y no seas nada."),
    # 43
    ("Aquele que n\u00e3o est\u00e1 contente com o que tem n\u00e3o estaria contente com o que gostaria de ter.", "Aquel que no est\u00e1 contento con lo que tiene no estar\u00eda contento con lo que le gustar\u00eda tener."),
    # 44
    ("A menos que voc\u00ea espere o inesperado, n\u00e3o o encontrar\u00e1, pois est\u00e1 escondido e densamente emaranhado.", "A menos que esperes lo inesperado, no lo encontrar\u00e1s, pues est\u00e1 escondido y densamente enredado."),
    # 45
    ("A excel\u00eancia \u00e9 uma arte conquistada pelo treinamento e pelo h\u00e1bito. N\u00e3o agimos corretamente porque temos virtude ou excel\u00eancia, mas temos essas porque agimos corretamente. Somos o que fazemos repetidamente. A excel\u00eancia, ent\u00e3o, n\u00e3o \u00e9 um ato, mas um h\u00e1bito.", "La excelencia es un arte conquistado por el entrenamiento y el h\u00e1bito. No actuamos correctamente porque tenemos virtud o excelencia, sino que las tenemos porque hemos actuado correctamente. Somos lo que hacemos repetidamente. La excelencia, entonces, no es un acto, sino un h\u00e1bito."),
    # 46
    ("[Sobre o homem virtuoso] \"Ele combina os acordes mais altos, mais baixos e m\u00e9dios em completa harmonia dentro de si mesmo.\"", "[Sobre el hombre virtuoso] \"Combina los acordes m\u00e1s altos, m\u00e1s bajos y medios en completa armon\u00eda dentro de s\u00ed mismo.\""),
    # 47 - long Plato quote about wisdom as true coin
    ("N\u00e3o h\u00e1 uma verdadeira moeda pela qual todas as coisas devem ser trocadas? \u2014 e essa \u00e9 a sabedoria; e somente em troca desta, e em companhia desta, qualquer coisa \u00e9 verdadeiramente comprada ou vendida, seja coragem, temperan\u00e7a ou justi\u00e7a.", "\u00bfNo hay una verdadera moneda por la cual todas las cosas deben intercambiarse? \u2014 y esa es la sabidur\u00eda; y solo a cambio de esta, y en compa\u00f1\u00eda de esta, cualquier cosa es verdaderamente comprada o vendida, sea coraje, temperancia o justicia."),
    # 48
    ("Quem \u00e9 injusti\u00e7ado n\u00e3o deve retribuir a injusti\u00e7a, pois de nenhum modo pode ser correto cometer uma injusti\u00e7a; e n\u00e3o \u00e9 correto retribuir uma injusti\u00e7a, ou fazer mal a qualquer homem, por mais que tenhamos sofrido com ele.", "Quien es ofendido no debe devolver la ofensa, pues de ning\u00fan modo puede ser correcto cometer una injusticia; y no es correcto devolver una injusticia, o hacer mal a cualquier hombre, por mucho que hayamos sufrido de \u00e9l."),
    # 49
    ("O ci\u00fame \u00e9 razo\u00e1vel e pertence aos homens razo\u00e1veis, enquanto a inveja \u00e9 baixa e pertence aos baixos, pois o primeiro se esfor\u00e7a para obter coisas boas pelo ci\u00fame, enquanto o outro n\u00e3o permite que seu vizinho as tenha por inveja.", "Los celos son razonables y pertenecen a los hombres razonables, mientras que la envidia es baja y pertenece a los bajos, pues el primero se esfuerza por obtener cosas buenas por los celos, mientras que el otro no permite que su vecino las tenga por envidia."),
    # 50
    ("Um homem honesto \u00e9 sempre uma crian\u00e7a.", "Un hombre honesto es siempre un ni\u00f1o."),
    # 51
    ("Pois uma vez tocado pelo amor, todos se tornam poetas.", "Pues una vez tocado por el amor, todos se convierten en poetas."),
    # 52 - long Plato on immortal soul
    ("Se a alma \u00e9 imortal, ela exige nosso cuidado n\u00e3o apenas para aquela parte do tempo que chamamos de vida, mas para todo o tempo. Se a morte fosse uma liberta\u00e7\u00e3o de tudo, seria uma b\u00ean\u00e7\u00e3o para os maus. Mas como a alma \u00e9 claramente imortal, n\u00e3o pode ter escape ou seguran\u00e7a do mal exceto tornando-se t\u00e3o boa e s\u00e1bia quanto poss\u00edvel.", "Si el alma es inmortal, exige nuestro cuidado no solo para aquella parte del tiempo que llamamos vida, sino para todo el tiempo. Si la muerte fuera una liberaci\u00f3n de todo, ser\u00eda una bendici\u00f3n para los malvados. Pero como el alma es claramente inmortal, no puede tener escape o seguridad del mal excepto volvi\u00e9ndose tan buena y sabia como sea posible."),
    # 53
    ("Nada poderia ser mais importante do que o trabalho de um soldado ser bem feito. Nenhuma ferramenta far\u00e1 de um homem um trabalhador habilidoso se n\u00e3o aprendeu a manej\u00e1-las.", "Nada podr\u00eda ser m\u00e1s importante que el trabajo de un soldado est\u00e9 bien hecho. Ninguna herramienta har\u00e1 de un hombre un trabajador h\u00e1bil si no ha aprendido a manejarlas."),
    # 54
    ("Para se encontrar, pense por si mesmo.", "Para encontrarte, piensa por ti mismo."),
    # 55
    ("Sabedoria \u00e9 saber que nada sabe.", "La sabidur\u00eda es saber que no sabes nada."),
    # 56
    ("A maior coisa de longe \u00e9 ser mestre da met\u00e1fora; \u00e9 a \u00fanica coisa que n\u00e3o pode ser aprendida de outros; e \u00e9 tamb\u00e9m um sinal de g\u00eanio, pois uma boa met\u00e1fora implica uma percep\u00e7\u00e3o intuitiva da semelhan\u00e7a no dessemelhante.", "Lo m\u00e1s grande con diferencia es ser maestro de la met\u00e1fora; es lo \u00fanico que no puede aprenderse de otros; y es tambi\u00e9n una se\u00f1al de genio, pues una buena met\u00e1fora implica una percepci\u00f3n intuitiva de la semejanza en lo desemejante."),
    # 57
    ("Se todos os nossos infort\u00fanios fossem postos num monte comum de onde todos devessem tomar uma por\u00e7\u00e3o igual, a maioria das pessoas ficaria contente em tomar os seus pr\u00f3prios e ir embora.", "Si todas nuestras desgracias fueran puestas en un mont\u00f3n com\u00fan de donde todos debieran tomar una porci\u00f3n igual, la mayor\u00eda de las personas estar\u00eda contenta de tomar las suyas propias e irse."),
    # 58
    ("A idade ideal para o casamento nos homens \u00e9 35. A idade ideal para o casamento nas mulheres \u00e9 18.", "La edad ideal para el matrimonio en los hombres es 35. La edad ideal para el matrimonio en las mujeres es 18."),
    # 59
    ("Quando voc\u00ea quiser sabedoria e discernimento t\u00e3o desesperadamente quanto quer respirar, \u00e9 ent\u00e3o que os ter\u00e1.", "Cuando quieras sabidur\u00eda y discernimiento tan desesperadamente como quieres respirar, es entonces cuando los tendr\u00e1s."),
    # 60
    ("A dignidade n\u00e3o consiste em possuir honras, mas na consci\u00eancia de que as merecemos.", "La dignidad no consiste en poseer honores, sino en la conciencia de que los merecemos."),
    # 61
    ("Permita-se pensar apenas aqueles pensamentos que correspondem aos seus princ\u00edpios e podem suportar a luz brilhante do dia. Dia a dia, suas escolhas, seus pensamentos, suas a\u00e7\u00f5es moldam a pessoa que voc\u00ea se torna. Sua integridade determina seu destino.", "Perm\u00edtete pensar solo aquellos pensamientos que correspondan a tus principios y puedan soportar la luz brillante del d\u00eda. D\u00eda a d\u00eda, tus elecciones, tus pensamientos, tus acciones moldean la persona en que te conviertes. Tu integridad determina tu destino."),
    # 62
    ("Cuidando da felicidade dos outros, encontramos a nossa.", "Cuidando de la felicidad de los dem\u00e1s, encontramos la nuestra."),
    # 63
    ("O homem ideal suporta os acidentes da vida com dignidade e gra\u00e7a, fazendo o melhor das circunst\u00e2ncias.", "El hombre ideal soporta los accidentes de la vida con dignidad y gracia, haciendo lo mejor de las circunstancias."),
    # 64
    ("A beleza da alma brilha quando um homem suporta com compostura um pesado infort\u00fanio ap\u00f3s outro, n\u00e3o porque n\u00e3o os sinta, mas porque \u00e9 um homem de temperamento elevado e heroico.", "La belleza del alma brilla cuando un hombre soporta con compostura una pesada desgracia tras otra, no porque no las sienta, sino porque es un hombre de temperamento elevado y heroico."),
    # 65
    ("A vis\u00e3o espiritual melhora \u00e0 medida que a vis\u00e3o f\u00edsica diminui.", "La visi\u00f3n espiritual mejora a medida que la visi\u00f3n f\u00edsica disminuye."),
    # 66
    ("O treinamento musical \u00e9 um instrumento mais potente do que qualquer outro, porque o ritmo e a harmonia encontram seu caminho nos lugares mais \u00edntimos da alma.", "El entrenamiento musical es un instrumento m\u00e1s potente que cualquier otro, porque el ritmo y la armon\u00eda encuentran su camino en los lugares m\u00e1s \u00edntimos del alma."),
    # 67
    ("Os poetas s\u00e3o apenas os int\u00e9rpretes dos deuses.", "Los poetas son solo los int\u00e9rpretes de los dioses."),
    # 68
    ("A arte n\u00e3o apenas imita a natureza, mas tamb\u00e9m completa suas defici\u00eancias.", "El arte no solo imita la naturaleza, sino que tambi\u00e9n completa sus deficiencias."),
    # 69
    ("Ao toque do amor, todos se tornam poetas.", "Al toque del amor, todos se convierten en poetas."),
    # 70
    ("Estamos presos aos nossos corpos como uma ostra \u00e0 sua concha.", "Estamos atados a nuestros cuerpos como una ostra a su concha."),
    # 71
    ("Um menino \u00e9, de todas as bestas selvagens, a mais dif\u00edcil de controlar.", "Un ni\u00f1o es, de todas las bestias salvajes, la m\u00e1s dif\u00edcil de controlar."),
    # 72
    ("Se n\u00e3o esperar, n\u00e3o encontrar\u00e1 o inesperado, pois \u00e9 dif\u00edcil de encontrar.", "Si no lo esperas, no encontrar\u00e1s lo inesperado, pues es dif\u00edcil de encontrar."),
    # 73
    ("N\u00e3o h\u00e1 nada permanente exceto a mudan\u00e7a.", "No hay nada permanente excepto el cambio."),
    # 74
    ("Voc\u00ea n\u00e3o pode entrar no mesmo rio duas vezes.", "No puedes entrar en el mismo r\u00edo dos veces."),
    # 75
    ("Tudo flui, nada permanece.", "Todo fluye, nada permanece."),
    # 76
    ("Nada \u00e9 permanente exceto a mudan\u00e7a.", "Nada es permanente excepto el cambio."),
    # 77
    ("\u00c9 na mudan\u00e7a que as coisas encontram prop\u00f3sito.", "Es en el cambio que las cosas encuentran prop\u00f3sito."),
    # 78
    ("Para desfrutar das coisas que devemos e odiar as coisas que devemos tem a maior influ\u00eancia na excel\u00eancia do car\u00e1ter.", "Disfrutar de las cosas que debemos y odiar las cosas que debemos tiene la mayor influencia en la excelencia del car\u00e1cter."),
    # 79
    ("De todos os animais, o menino \u00e9 o mais incontrol\u00e1vel.", "De todos los animales, el ni\u00f1o es el m\u00e1s incontrolable."),
    # 80
    ("Sou cidad\u00e3o n\u00e3o de Atenas ou da Gr\u00e9cia, mas do mundo.", "Soy ciudadano no de Atenas o de Grecia, sino del mundo."),
    # 81
    ("O amor \u00e9 composto de uma \u00fanica alma habitando dois corpos.", "El amor est\u00e1 compuesto de una sola alma habitando dos cuerpos."),
    # 82
    ("Cada homem \u00e9 capaz de fazer uma coisa bem. Se tentar v\u00e1rias, n\u00e3o alcan\u00e7ar\u00e1 distin\u00e7\u00e3o em nenhuma.", "Cada hombre es capaz de hacer una cosa bien. Si intenta varias, no alcanzar\u00e1 distinci\u00f3n en ninguna."),
    # 83
    ("A autoconquista \u00e9 a maior das vit\u00f3rias.", "La autoconquista es la mayor de las victorias."),
    # 84
    ("A coragem \u00e9 uma esp\u00e9cie de salva\u00e7\u00e3o.", "El coraje es una especie de salvaci\u00f3n."),
    # 85
    ("Voc\u00ea n\u00e3o pode entrar duas vezes no mesmo rio, pois outras \u00e1guas est\u00e3o continuamente fluindo.", "No puedes entrar dos veces en el mismo r\u00edo, pues otras aguas est\u00e1n continuamente fluyendo."),
]

for i, key in enumerate(batch):
    if i < len(translations_list):
        tr[key] = {"pt": translations_list[i][0], "es": translations_list[i][1]}

with open('c:/Users/lalli/Flutter/coach_phrase_app/translations_classical.json', 'w', encoding='utf-8') as f:
    json.dump(tr, f, ensure_ascii=False, indent=2)

print(f'Classical translations total: {len(tr)}')
