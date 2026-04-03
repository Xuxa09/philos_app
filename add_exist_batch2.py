"""Existentialism translations batch 2 (quotes 50-99)."""
import json

with open('c:/Users/lalli/Flutter/coach_phrase_app/missing_exist.json', 'r', encoding='utf-8') as f:
    missing = json.load(f)

with open('c:/Users/lalli/Flutter/coach_phrase_app/translations_exist.json', 'r', encoding='utf-8') as f:
    tr = json.load(f)

batch = missing[50:100]

tl = [
    # 50
    ("O F\u00fchrer sozinho \u00e9 a presente e futura realidade alem\u00e3 e sua lei. Aprenda a conhecer cada vez mais profundamente: de agora em diante cada coisa exige decis\u00e3o, e cada a\u00e7\u00e3o responsabilidade.", "El F\u00fchrer solo es la presente y futura realidad alemana y su ley. Aprende a conocer cada vez m\u00e1s profundamente: de ahora en adelante cada cosa exige decisi\u00f3n, y cada acci\u00f3n responsabilidad."),
    # 51
    ("Os fan\u00e1ticos s\u00e3o pitorescos; a humanidade prefere ver gestos do que ouvir raz\u00f5es.", "Los fan\u00e1ticos son pintorescos; la humanidad prefiere ver gestos que escuchar razones."),
    # 52
    ("Ser\u00e1 que a sabedoria aparece na terra como um corvo inspirado pelo cheiro de carca\u00e7a?", "\u00bfAcaso la sabidur\u00eda aparece en la tierra como un cuervo inspirado por el olor a carro\u00f1a?"),
    # 53
    ("S\u00f3 existem dois tipos de homens: os justos que se acham pecadores e os pecadores que se acham justos.", "Solo existen dos tipos de hombres: los justos que se creen pecadores y los pecadores que se creen justos."),
    # 54
    ("\u00c9 a velhice, e n\u00e3o a morte, que deve ser contrastada com a vida. A velhice \u00e9 a par\u00f3dia da vida, enquanto a morte transforma a vida em destino: de certo modo a preserva ao dar-lhe a dimens\u00e3o absoluta. A morte acaba com o tempo.", "Es la vejez, y no la muerte, lo que debe contrastarse con la vida. La vejez es la parodia de la vida, mientras que la muerte transforma la vida en destino: de cierto modo la preserva al darle la dimensi\u00f3n absoluta. La muerte acaba con el tiempo."),
    # 55
    ("Se h\u00e1 um pecado contra a vida, consiste talvez n\u00e3o tanto em desesperar da vida quanto em esperar por outra, e em iludir a grandeza implac\u00e1vel desta vida.", "Si hay un pecado contra la vida, consiste quiz\u00e1s no tanto en desesperar de la vida como en esperar por otra, y en eludir la grandeza implacable de esta vida."),
    # 56
    ("Se examinarmos nossos pensamentos, os encontraremos sempre ocupados com o passado e o futuro.", "Si examinamos nuestros pensamientos, los encontraremos siempre ocupados con el pasado y el futuro."),
    # 57
    ("Eu vos ensino o Al\u00e9m-do-Homem (super-homem). O homem \u00e9 algo que deve ser superado. O que fizestes para super\u00e1-lo?", "Yo os ense\u00f1o el M\u00e1s-all\u00e1-del-Hombre (superhombre). El hombre es algo que debe ser superado. \u00bfQu\u00e9 hab\u00e9is hecho para superarlo?"),
    # 58
    ("A insanidade nos indiv\u00edduos \u00e9 algo raro \u2014 mas nos grupos, partidos, na\u00e7\u00f5es e \u00e9pocas \u00e9 a regra.", "La locura en los individuos es algo raro \u2014 pero en los grupos, partidos, naciones y \u00e9pocas es la regla."),
    # 59
    ("Um sistema moral v\u00e1lido para todos \u00e9 basicamente imoral.", "Un sistema moral v\u00e1lido para todos es b\u00e1sicamente inmoral."),
    # 60
    ("At\u00e9 a mais bela paisagem n\u00e3o tem mais garantia do nosso amor depois de termos vivido nela por tr\u00eas meses, e alguma costa distante atrai nossa avar\u00edcia: as posses s\u00e3o geralmente diminu\u00eddas pela posse.", "Incluso el paisaje m\u00e1s bello ya no tiene la garant\u00eda de nuestro amor despu\u00e9s de haber vivido en \u00e9l por tres meses, y alguna costa distante atrae nuestra avaricia: las posesiones son generalmente disminuidas por la posesi\u00f3n."),
    # 61
    ("Todos os homens s\u00e3o Profetas ou ent\u00e3o Deus n\u00e3o existe.", "Todos los hombres son Profetas o entonces Dios no existe."),
    # 62
    ("Ao ver a multid\u00e3o de pessoas ao redor, ao se ocupar com assuntos mundanos, tal pessoa esquece de si mesma num sentido divino, n\u00e3o ousa acreditar em si mesma, acha ser si mesma muito arriscado. Esta forma de desespero passa praticamente despercebida no mundo.", "Al ver la multitud de personas alrededor, al ocuparse con asuntos mundanos, tal persona se olvida de s\u00ed misma en un sentido divino, no se atreve a creer en s\u00ed misma, encuentra que ser s\u00ed misma es demasiado arriesgado. Esta forma de desesperaci\u00f3n pasa pr\u00e1cticamente desapercibida en el mundo."),
    # 63
    ("A verdadeira generosidade para com o futuro consiste em dar tudo ao presente.", "La verdadera generosidad hacia el futuro consiste en darlo todo al presente."),
    # 64
    ("Ela n\u00e3o acreditava em nada. S\u00f3 seu ceticismo a impedia de ser ate\u00edsta.", "Ella no cre\u00eda en nada. Solo su escepticismo la imped\u00eda de ser ate\u00edsta."),
    # 65
    ("Ah! sim, eu sei: aqueles que me veem raramente confiam na minha palavra: devo parecer inteligente demais para cumpri-la.", "\u00a1Ah! s\u00ed, lo s\u00e9: aquellos que me ven rara vez conf\u00edan en mi palabra: debo parecer demasiado inteligente para cumplirla."),
    # 66
    ("Um sentimento intenso carrega consigo seu pr\u00f3prio universo, magn\u00edfico ou miser\u00e1vel conforme o caso.", "Un sentimiento intenso lleva consigo su propio universo, magn\u00edfico o miserable seg\u00fan el caso."),
    # 67
    ("A vida n\u00e3o tem significado a priori\u2026 Cabe a voc\u00ea dar-lhe um significado, e o valor n\u00e3o \u00e9 nada al\u00e9m do significado que voc\u00ea escolhe.", "La vida no tiene significado a priori\u2026 Te corresponde darle un significado, y el valor no es nada m\u00e1s que el significado que t\u00fa eliges."),
    # 68
    ("Estou estranhamente cansado, n\u00e3o de ter falado tanto, mas s\u00f3 de pensar no que ainda tenho a dizer.", "Estoy extra\u00f1amente cansado, no de haber hablado tanto, sino solo de pensar en lo que a\u00fan tengo que decir."),
    # 69
    ("N\u00e3o h\u00e1 fatos eternos, assim como n\u00e3o h\u00e1 verdades absolutas.", "No hay hechos eternos, as\u00ed como no hay verdades absolutas."),
    # 70 - long Heidegger Being and Time - summarize
    ("A curiosidade e a tagarelice controlam at\u00e9 os modos como se pode ser curioso. Elas dizem o que se 'deve' ter lido e visto. Fornecem a garantia de uma 'vida' que, supostamente, \u00e9 genuinamente 'viva'.", "La curiosidad y la charla controlan incluso los modos en que se puede ser curioso. Dicen lo que se 'debe' haber le\u00eddo y visto. Proporcionan la garant\u00eda de una 'vida' que, supuestamente, es genuinamente 'viva'."),
    # 71
    ("O fim de uma melodia n\u00e3o \u00e9 seu objetivo: mas, no entanto, se a melodia n\u00e3o tivesse alcan\u00e7ado seu fim, tamb\u00e9m n\u00e3o teria alcan\u00e7ado seu objetivo. Uma par\u00e1bola.", "El fin de una melod\u00eda no es su objetivo: pero, sin embargo, si la melod\u00eda no hubiera alcanzado su fin, tampoco habr\u00eda alcanzado su objetivo. Una par\u00e1bola."),
    # 72
    ("A sociedade cuida do indiv\u00edduo apenas na medida em que ele \u00e9 lucrativo.", "La sociedad cuida del individuo solo en la medida en que es rentable."),
    # 73
    ("Devemos enfrentar nosso destino com coragem.", "Debemos enfrentar nuestro destino con coraje."),
    # 74
    ("Se, afinal, os homens nem sempre podem fazer a hist\u00f3ria ter um sentido, podem sempre agir para que suas pr\u00f3prias vidas tenham um.", "Si, al fin, los hombres no siempre pueden hacer que la historia tenga un sentido, siempre pueden actuar para que sus propias vidas tengan uno."),
    # 75
    ("E se prazer e desprazer estivessem t\u00e3o ligados que quem quisesse ter o m\u00e1ximo de um tamb\u00e9m precisasse ter o m\u00e1ximo do outro? Voc\u00ea tem uma escolha na vida: ou o m\u00ednimo de desprazer poss\u00edvel, ou o m\u00e1ximo de desprazer como pre\u00e7o por uma abund\u00e2ncia de prazeres sutis e alegrias.", "\u00bfY si placer y displacer estuvieran tan ligados que quien quisiera tener el m\u00e1ximo de uno tambi\u00e9n necesitara tener el m\u00e1ximo del otro? Tienes una elecci\u00f3n en la vida: o el m\u00ednimo de displacer posible, o el m\u00e1ximo de displacer como precio por una abundancia de placeres sutiles y alegr\u00edas."),
    # 76 - long Nietzsche on truth - summarize
    ("A verdade \u00e9 um ex\u00e9rcito m\u00f3vel de met\u00e1foras, meton\u00edmias e antropomorfismos; verdades s\u00e3o ilus\u00f5es das quais esquecemos que s\u00e3o ilus\u00f5es, met\u00e1foras que se desgastaram pelo uso frequente e perderam toda a for\u00e7a sensorial.", "La verdad es un ej\u00e9rcito m\u00f3vil de met\u00e1foras, metonimias y antropomorfismos; las verdades son ilusiones de las que hemos olvidado que son ilusiones, met\u00e1foras que se han desgastado por el uso frecuente y han perdido toda fuerza sensorial."),
    # 77
    ("A moralidade \u00e9 apenas uma fic\u00e7\u00e3o usada pelo rebanho de seres humanos inferiores para conter os poucos homens superiores.", "La moralidad es solo una ficci\u00f3n usada por el reba\u00f1o de seres humanos inferiores para contener a los pocos hombres superiores."),
    # 78
    ("A coragem \u00e9 a melhor matadora \u2014 a coragem que ataca, pois em todo ataque h\u00e1 o som do triunfo.", "El coraje es el mejor asesino \u2014 el coraje que ataca, pues en todo ataque hay el sonido del triunfo."),
    # 79
    ("O vision\u00e1rio mente para si mesmo, o mentiroso apenas para os outros.", "El visionario miente a s\u00ed mismo, el mentiroso solo a los dem\u00e1s."),
    # 80
    ("A verdade \u00e9 misteriosa, elusiva, sempre a ser conquistada. A liberdade \u00e9 perigosa, t\u00e3o dif\u00edcil de conviver quanto estimulante. Devemos marchar em dire\u00e7\u00e3o a esses dois objetivos, dolorosa mas resolutamente.", "La verdad es misteriosa, elusiva, siempre por conquistar. La libertad es peligrosa, tan dif\u00edcil de convivir como estimulante. Debemos marchar hacia estos dos objetivos, dolorosa pero resueltamente."),
    # 81
    ("Todos os homens t\u00eam a felicidade como objetivo: n\u00e3o h\u00e1 exce\u00e7\u00e3o. Por mais diferentes que sejam os meios que empregam, miram o mesmo fim.", "Todos los hombres tienen la felicidad como objetivo: no hay excepci\u00f3n. Por m\u00e1s diferentes que sean los medios que emplean, apuntan al mismo fin."),
    # 82
    ("A felicidade n\u00e3o est\u00e1 fora de n\u00f3s nem dentro de n\u00f3s. Est\u00e1 em Deus, tanto fora quanto dentro de n\u00f3s.", "La felicidad no est\u00e1 fuera de nosotros ni dentro de nosotros. Est\u00e1 en Dios, tanto fuera como dentro de nosotros."),
    # 83
    ("Conhecimento de Deus sem conhecimento da mis\u00e9ria do homem leva ao orgulho. Conhecimento da mis\u00e9ria do homem sem conhecimento de Deus leva ao desespero. Conhecimento de Jesus Cristo \u00e9 o caminho do meio.", "Conocimiento de Dios sin conocimiento de la miseria del hombre lleva al orgullo. Conocimiento de la miseria del hombre sin conocimiento de Dios lleva a la desesperaci\u00f3n. Conocimiento de Jesucristo es el camino del medio."),
    # 84
    ("Quanto mais areia escapou da ampulheta da nossa vida, mais claramente devemos ver atrav\u00e9s dela.", "Cuanta m\u00e1s arena ha escapado del reloj de arena de nuestra vida, m\u00e1s claramente debemos ver a trav\u00e9s de \u00e9l."),
    # 85
    ("Sem liberdade, n\u00e3o h\u00e1 arte; a arte s\u00f3 vive das restri\u00e7\u00f5es que imp\u00f5e a si mesma, e morre de todas as outras.", "Sin libertad, no hay arte; el arte solo vive de las restricciones que se impone a s\u00ed mismo, y muere de todas las dem\u00e1s."),
    # 86
    ("Por que um homem e n\u00e3o outro? Era estranho. Voc\u00ea se v\u00ea envolvida com um sujeito para a vida inteira s\u00f3 porque ele foi o que voc\u00ea conheceu quando tinha dezenove anos.", "\u00bfPor qu\u00e9 un hombre y no otro? Era extra\u00f1o. Te ves involucrada con un tipo para toda la vida solo porque fue el que conociste cuando ten\u00edas diecinueve a\u00f1os."),
    # 87
    ("A moralidade \u00e9 o melhor de todos os dispositivos para conduzir a humanidade pelo nariz.", "La moralidad es el mejor de todos los dispositivos para llevar a la humanidad por la nariz."),
    # 88
    ("Temos que ter cuidado para que, ao expulsar o diabo, n\u00e3o expulsemos a melhor parte de n\u00f3s mesmos.", "Tenemos que tener cuidado de que, al expulsar al diablo, no expulsemos la mejor parte de nosotros mismos."),
    # 89
    ("Cansa\u00e7o, que busca alcan\u00e7ar o \u00faltimo com um salto, com um salto mortal; um pobre cansa\u00e7o ignorante, sem vontade sequer de querer mais: isso criou todos os deuses e transmundos.", "Cansancio, que busca alcanzar lo \u00faltimo con un salto, con un salto mortal; un pobre cansancio ignorante, sin voluntad siquiera de querer m\u00e1s: eso cre\u00f3 todos los dioses y trasmundos."),
    # 90
    ("Para que a arte exista, para que qualquer tipo de atividade ou percep\u00e7\u00e3o est\u00e9tica exista, uma certa precondi\u00e7\u00e3o fisiol\u00f3gica \u00e9 indispens\u00e1vel: a embriaguez.", "Para que el arte exista, para que cualquier tipo de actividad o percepci\u00f3n est\u00e9tica exista, una cierta precondici\u00f3n fisiol\u00f3gica es indispensable: la embriaguez."),
    # 91
    ("A lux\u00faria e a for\u00e7a s\u00e3o a fonte de todas as nossas a\u00e7\u00f5es; a lux\u00faria causa a\u00e7\u00f5es volunt\u00e1rias, a for\u00e7a as involunt\u00e1rias.", "La lujuria y la fuerza son la fuente de todas nuestras acciones; la lujuria causa acciones voluntarias, la fuerza las involuntarias."),
    # 92
    ("Um idiota \u00e9 um idiota. Dois idiotas s\u00e3o dois idiotas. Dez mil idiotas s\u00e3o um partido pol\u00edtico.", "Un idiota es un idiota. Dos idiotas son dos idiotas. Diez mil idiotas son un partido pol\u00edtico."),
    # 93
    ("Ele realmente queria que este quarto quente, t\u00e3o confortavelmente mobiliado com m\u00f3veis antigos da fam\u00edlia, fosse transformado numa caverna, onde sem d\u00favida seria livre para rastejar em todas as dire\u00e7\u00f5es, mas ao pre\u00e7o de rapidamente esquecer seu passado humano?", "\u00bfRealmente quer\u00eda que esta habitaci\u00f3n c\u00e1lida, tan c\u00f3modamente amueblada con antiguos muebles familiares, fuera transformada en una cueva, donde sin duda ser\u00eda libre de arrastrarse en todas direcciones, pero al precio de olvidar r\u00e1pidamente su pasado humano?"),
    # 94
    ("H\u00e1 dois tipos de pobres: os que s\u00e3o pobres juntos e os que s\u00e3o pobres sozinhos. Os primeiros s\u00e3o os verdadeiros pobres, os outros s\u00e3o ricos sem sorte.", "Hay dos tipos de pobres: los que son pobres juntos y los que son pobres solos. Los primeros son los verdaderos pobres, los otros son ricos sin suerte."),
    # 95
    ("A admira\u00e7\u00e3o por uma qualidade ou arte pode ser t\u00e3o forte que nos impede de nos esfor\u00e7armos para possu\u00ed-la.", "La admiraci\u00f3n por una cualidad o arte puede ser tan fuerte que nos impide esforzarnos por poseerla."),
    # 96
    ("O mal que existe no mundo sempre vem da ignor\u00e2ncia, e as boas inten\u00e7\u00f5es podem causar tanto dano quanto a malev\u00f3lencia, se lhes falta compreens\u00e3o.", "El mal que existe en el mundo siempre viene de la ignorancia, y las buenas intenciones pueden causar tanto da\u00f1o como la malevolencia, si les falta comprensi\u00f3n."),
    # 97
    ("Se voc\u00ea est\u00e1 solit\u00e1rio quando est\u00e1 sozinho, est\u00e1 em m\u00e1 companhia.", "Si est\u00e1s solitario cuando est\u00e1s solo, est\u00e1s en mala compa\u00f1\u00eda."),
    # 98
    ("Livros s\u00e3o um narc\u00f3tico.", "Los libros son un narc\u00f3tico."),
    # 99 - German quote - keep original + translate
    ("Um sempre est\u00e1 errado: mas com dois come\u00e7a a verdade. Um n\u00e3o pode provar a si mesmo: mas dois j\u00e1 n\u00e3o podem ser refutados.", "Uno siempre est\u00e1 equivocado: pero con dos comienza la verdad. Uno no puede probarse a s\u00ed mismo: pero a dos ya no se los puede refutar."),
]

for i, key in enumerate(batch):
    if i < len(tl):
        tr[key] = {"pt": tl[i][0], "es": tl[i][1]}

with open('c:/Users/lalli/Flutter/coach_phrase_app/translations_exist.json', 'w', encoding='utf-8') as f:
    json.dump(tr, f, ensure_ascii=False, indent=2)

print(f'Existentialism total: {len(tr)} translations')
