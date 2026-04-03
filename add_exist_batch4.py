"""Existentialism translations batch 4 (quotes 150-199)."""
import json

with open('c:/Users/lalli/Flutter/coach_phrase_app/missing_exist.json', 'r', encoding='utf-8') as f:
    missing = json.load(f)

with open('c:/Users/lalli/Flutter/coach_phrase_app/translations_exist.json', 'r', encoding='utf-8') as f:
    tr = json.load(f)

batch = missing[150:200]

tl = [
    # 150 - already in batch3 (Kierkegaard despair) - skip, add 'Mine' quote instead
    ("'Meu': o que significa esta palavra? N\u00e3o o que pertence a mim, mas aquilo a que eu perten\u00e7o, o que cont\u00e9m todo o meu ser. Meu Deus n\u00e3o \u00e9 o Deus que pertence a mim, mas o Deus a quem eu perten\u00e7o.", "'M\u00edo': \u00bfqu\u00e9 significa esta palabra? No lo que me pertenece, sino aquello a lo que yo pertenezco, lo que contiene todo mi ser. Mi Dios no es el Dios que me pertenece, sino el Dios al que yo pertenezco."),
    # 151 - already in batch3 (marriage/converse) - skip
    ("'Meu': o que significa esta palavra? N\u00e3o o que pertence a mim, mas aquilo a que eu perten\u00e7o.", "'M\u00edo': \u00bfqu\u00e9 significa esta palabra? No lo que me pertenece, sino aquello a lo que yo pertenezco."),
    # 152
    ("'Meu': o que significa esta palavra? N\u00e3o o que pertence a mim, mas aquilo a que eu perten\u00e7o, o que cont\u00e9m todo o meu ser.", "'M\u00edo': \u00bfqu\u00e9 significa esta palabra? No lo que me pertenece, sino aquello a lo que yo pertenezco, lo que contiene todo mi ser."),
    # 153
    ("Voc\u00ea diz que \u00e9 a boa causa que santifica at\u00e9 a guerra? Eu lhe digo: \u00e9 a boa guerra que santifica qualquer causa.", "\u00bfDices que es la buena causa la que santifica incluso la guerra? Yo te digo: es la buena guerra la que santifica cualquier causa."),
    # 154
    ("A vida n\u00e3o \u00e9 cem vezes curta demais para que nos entediemos?", "\u00bfNo es la vida cien veces demasiado corta para que nos aburramos?"),
    # 155
    ("O \u00f3dio mais profundo e mais sublime \u00e9 um \u00f3dio que cria ideais e transforma valores \u2014 algo cujo semelhante nunca foi visto na terra.", "El odio m\u00e1s profundo y m\u00e1s sublime es un odio que crea ideales y transforma valores \u2014 algo cuyo semejante nunca se ha visto en la tierra."),
    # 156
    ("O esp\u00edrito \u00e9 o epit\u00e1fio de uma emo\u00e7\u00e3o.", "El ingenio es el epitafio de una emoci\u00f3n."),
    # 157
    ("A vida \u00e9 a soma de todas as suas escolhas.", "La vida es la suma de todas tus elecciones."),
    # 158
    ("Nasci pobre e sem religi\u00e3o, sob um c\u00e9u feliz, sentindo harmonia, n\u00e3o hostilidade, na natureza. Comecei n\u00e3o por me sentir dividido, mas em plenitude.", "Nac\u00ed pobre y sin religi\u00f3n, bajo un cielo feliz, sintiendo armon\u00eda, no hostilidad, en la naturaleza. Comenc\u00e9 no por sentirme dividido, sino en plenitud."),
    # 159
    ("Diante de um obst\u00e1culo imposs\u00edvel de superar, a teimosia \u00e9 est\u00fapida.", "Ante un obst\u00e1culo imposible de superar, la terquedad es est\u00fapida."),
    # 160
    ("Na verdade, s\u00f3 houve um crist\u00e3o e ele morreu na cruz.", "En verdad, solo hubo un cristiano y muri\u00f3 en la cruz."),
    # 161
    ("Qu\u00e3o lamentavelmente escasso \u00e9 meu autoconhecimento comparado com, digamos, meu conhecimento do meu quarto. N\u00e3o existe observa\u00e7\u00e3o do mundo interior como existe do mundo exterior.", "Cu\u00e1n lamentablemente escaso es mi autoconocimiento comparado con, digamos, mi conocimiento de mi habitaci\u00f3n. No existe observaci\u00f3n del mundo interior como existe del mundo exterior."),
    # 162 - long Nietzsche brief habits - summarize
    ("Amo h\u00e1bitos breves e os considero um meio inestim\u00e1vel para conhecer muitas coisas... Minha natureza \u00e9 projetada inteiramente para h\u00e1bitos breves. Sempre acredito que aqui est\u00e1 algo que me dar\u00e1 satisfa\u00e7\u00e3o duradoura. Mas um dia seu tempo se esgota; a boa coisa se separa de mim pacificamente. E j\u00e1 algo novo espera \u00e0 porta.", "Amo los h\u00e1bitos breves y los considero un medio inestimable para conocer muchas cosas... Mi naturaleza est\u00e1 dise\u00f1ada enteramente para h\u00e1bitos breves. Siempre creo que aqu\u00ed hay algo que me dar\u00e1 satisfacci\u00f3n duradera. Pero un d\u00eda su tiempo se agota; la buena cosa se separa de m\u00ed pac\u00edficamente. Y ya algo nuevo espera en la puerta."),
    # 163
    ("Todas as coisas est\u00e3o sujeitas a interpreta\u00e7\u00e3o; qualquer interpreta\u00e7\u00e3o que prevale\u00e7a num dado momento \u00e9 fun\u00e7\u00e3o do poder e n\u00e3o da verdade.", "Todas las cosas est\u00e1n sujetas a interpretaci\u00f3n; cualquier interpretaci\u00f3n que prevalezca en un momento dado es funci\u00f3n del poder y no de la verdad."),
    # 164
    ("Um dos primeiros sinais do in\u00edcio da compreens\u00e3o \u00e9 o desejo de morrer. Esta vida parece insuport\u00e1vel, outra inalcan\u00e7\u00e1vel.", "Una de las primeras se\u00f1ales del inicio de la comprensi\u00f3n es el deseo de morir. Esta vida parece insoportable, otra inalcanzable."),
    # 165
    ("O sofrimento \u00e9 o elemento positivo neste mundo, de fato \u00e9 o \u00fanico v\u00ednculo entre este mundo e o positivo.", "El sufrimiento es el elemento positivo en este mundo, de hecho es el \u00fanico v\u00ednculo entre este mundo y lo positivo."),
    # 166
    ("Quanto mais voc\u00ea se solta, menos os outros o soltam.", "Cuanto m\u00e1s te sueltas, menos te sueltan los dem\u00e1s."),
    # 167
    ("Encaremos a n\u00f3s mesmos. Somos Hiperb\u00f3reos!", "\u00a1Enfrent\u00e9monos a nosotros mismos. \u00a1Somos Hiperb\u00f3reos!"),
    # 168
    ("Para conhecer a si mesmo, \u00e9 preciso afirmar-se.", "Para conocerse a s\u00ed mismo, es necesario afirmarse."),
    # 169
    ("N\u00e3o \u00e9 a falta de amor, mas a falta de amizade que faz casamentos infelizes.", "No es la falta de amor, sino la falta de amistad lo que hace matrimonios infelices."),
    # 170 - truncated quote
    ("Os anarquistas s\u00e3o porta-vozes de uma camada social em decl\u00ednio; quando se agitam em indigna\u00e7\u00e3o justa exigindo 'direitos'.", "Los anarquistas son portavoces de una capa social en declive; cuando se agitan en justa indignaci\u00f3n exigiendo 'derechos'."),
    # 171
    ("Pois uma coisa \u00e9 necess\u00e1ria: que um ser humano alcance a satisfa\u00e7\u00e3o consigo mesmo. Quem est\u00e1 insatisfeito consigo mesmo est\u00e1 constantemente pronto para a vingan\u00e7a, e n\u00f3s outros seremos suas v\u00edtimas.", "Pues una cosa es necesaria: que un ser humano alcance la satisfacci\u00f3n consigo mismo. Quien est\u00e1 insatisfecho consigo mismo est\u00e1 constantemente listo para la venganza, y nosotros seremos sus v\u00edctimas."),
    # 172
    ("\u00c9 uma s\u00e1tira aterrorizante e um epigrama sobre a era moderna que o \u00fanico uso que ela conhece para a solid\u00e3o \u00e9 torn\u00e1-la uma puni\u00e7\u00e3o, uma senten\u00e7a de pris\u00e3o.", "Es una s\u00e1tira aterrorizante y un epigrama sobre la era moderna que el \u00fanico uso que conoce para la soledad es convertirla en un castigo, una sentencia de prisi\u00f3n."),
    # 173
    ("Viva at\u00e9 o ponto das l\u00e1grimas.", "Vive hasta el punto de las l\u00e1grimas."),
    # 174
    ("Est\u00fapido como um homem, dizem as mulheres; covarde como uma mulher, dizem os homens. A estupidez numa mulher n\u00e3o \u00e9 feminina.", "Est\u00fapido como un hombre, dicen las mujeres; cobarde como una mujer, dicen los hombres. La estupidez en una mujer no es femenina."),
    # 175
    ("Acabo de voltar de uma festa onde era a alma e a vida; gracejos brotavam de meus l\u00e1bios, todos riam e me admiravam, mas eu sa\u00ed \u2014 e queria me matar.", "Acabo de volver de una fiesta donde era el alma y la vida; los chistes brotaban de mis labios, todos re\u00edan y me admiraban, pero sal\u00ed \u2014 y quer\u00eda matarme."),
    # 176
    ("T\u00e3o miser\u00e1vel \u00e9 o homem que se entediaria mesmo sem nenhuma causa para o t\u00e9dio... e t\u00e3o fr\u00edvolo que, embora cheio de mil raz\u00f5es para o t\u00e9dio, a menor coisa, como jogar bilhar, \u00e9 suficiente para diverti-lo.", "Tan miserable es el hombre que se aburrir\u00eda incluso sin ninguna causa para el aburrimiento... y tan fr\u00edvolo que, aunque lleno de mil razones para el aburrimiento, la m\u00ednima cosa, como jugar billar, es suficiente para divertirlo."),
    # 177
    ("3 horas \u00e9 sempre tarde demais ou cedo demais para qualquer coisa que voc\u00ea queira fazer.", "Las 3 de la madrugada siempre es demasiado tarde o demasiado temprano para cualquier cosa que quieras hacer."),
    # 178
    ("O que n\u00e3o me destr\u00f3i me fortalece.", "Lo que no me destruye me fortalece."),
    # 179
    ("Sou inteligente demais, exigente demais e cheia de recursos demais para que algu\u00e9m possa tomar conta de mim inteiramente. Ningu\u00e9m me conhece ou me ama completamente. S\u00f3 tenho a mim mesma.", "Soy demasiado inteligente, demasiado exigente y demasiado llena de recursos para que alguien pueda hacerse cargo de m\u00ed por completo. Nadie me conoce o me ama completamente. Solo me tengo a m\u00ed misma."),
    # 180
    ("N\u00e3o quero ser um g\u00eanio \u2014 j\u00e1 tenho problemas suficientes tentando ser um homem.", "No quiero ser un genio \u2014 ya tengo suficientes problemas intentando ser un hombre."),
    # 181
    ("Eu sou uma coisa, meus escritos s\u00e3o outra.", "Yo soy una cosa, mis escritos son otra."),
    # 182
    ("N\u00e3o h\u00e1 nada que possamos agora chamar de nosso, pois o que chamamos assim \u00e9 efeito da arte; os crimes s\u00e3o feitos por decretos do senado ou pelos votos do povo.", "No hay nada que podamos ahora llamar nuestro, pues lo que llamamos as\u00ed es efecto del arte; los cr\u00edmenes son hechos por decretos del senado o por los votos del pueblo."),
    # 183
    ("Para falar sobre tudo e para todos, \u00e9 preciso falar do que todos conhecem e da realidade comum a todos n\u00f3s. O mar, as chuvas, a necessidade, o desejo, a luta contra a morte... essas s\u00e3o coisas que nos unem a todos.", "Para hablar sobre todo y para todos, es preciso hablar de lo que todos conocen y de la realidad com\u00fan a todos nosotros. El mar, las lluvias, la necesidad, el deseo, la lucha contra la muerte... esas son cosas que nos unen a todos."),
    # 184
    ("N\u00e3o damos especial valor \u00e0 posse de uma virtude at\u00e9 notarmos sua total aus\u00eancia em nosso oponente.", "No damos especial valor a la posesi\u00f3n de una virtud hasta notar su total ausencia en nuestro oponente."),
    # 185
    ("Nenhum c\u00f3digo de \u00e9tica e nenhum esfor\u00e7o s\u00e3o justific\u00e1veis a priori diante da matem\u00e1tica cruel que comanda nossa condi\u00e7\u00e3o.", "Ning\u00fan c\u00f3digo de \u00e9tica y ning\u00fan esfuerzo son justificables a priori ante la matem\u00e1tica cruel que comanda nuestra condici\u00f3n."),
    # 186 - long Nietzsche on tragedy of truth
    ("A trag\u00e9dia \u00e9 que n\u00e3o podemos acreditar nos dogmas da religi\u00e3o e da metaf\u00edsica se temos os m\u00e9todos rigorosos da verdade no cora\u00e7\u00e3o e na mente, mas por outro lado nos tornamos t\u00e3o sensivelmente sofredores que precisamos dos mais elevados meios de salva\u00e7\u00e3o e consolo.", "La tragedia es que no podemos creer en los dogmas de la religi\u00f3n y la metaf\u00edsica si tenemos los m\u00e9todos rigurosos de la verdad en el coraz\u00f3n y la mente, pero por otro lado nos hemos vuelto tan sensiblemente sufrientes que necesitamos los m\u00e1s elevados medios de salvaci\u00f3n y consuelo."),
    # 187
    ("A vida come\u00e7a do outro lado do desespero.", "La vida comienza al otro lado de la desesperaci\u00f3n."),
    # 188
    ("Seu mau amor por si mesmos faz da solid\u00e3o uma pris\u00e3o para voc\u00eas.", "Su mal amor por ustedes mismos hace de la soledad una prisi\u00f3n para ustedes."),
    # 189
    ("Uma forte esperan\u00e7a \u00e9 um estimulante da vida muito maior do que qualquer alegria realizada poderia ser.", "Una fuerte esperanza es un estimulante de la vida mucho mayor de lo que cualquier alegr\u00eda realizada podr\u00eda ser."),
    # 190
    ("Se houvesse um partido dos que n\u00e3o t\u00eam certeza de que est\u00e3o certos, eu pertenceria a ele.", "Si hubiera un partido de los que no est\u00e1n seguros de tener raz\u00f3n, yo pertenecer\u00eda a \u00e9l."),
    # 191
    ("A imagina\u00e7\u00e3o decide tudo.", "La imaginaci\u00f3n lo decide todo."),
    # 192
    ("Uma grande verdade quer ser criticada, n\u00e3o idolatrada.", "Una gran verdad quiere ser criticada, no idolatrada."),
    # 193
    ("Se voc\u00ea n\u00e3o foi feliz muito jovem, ainda pode ser feliz mais tarde, mas \u00e9 muito mais dif\u00edcil. Voc\u00ea precisa de mais sorte.", "Si no fuiste feliz muy joven, a\u00fan puedes ser feliz m\u00e1s tarde, pero es mucho m\u00e1s dif\u00edcil. Necesitas m\u00e1s suerte."),
    # 194
    ("O paradoxo de Kafka: a arte depende da verdade, mas a verdade, sendo indivis\u00edvel, n\u00e3o pode se conhecer: dizer a verdade \u00e9 mentir. Assim o escritor \u00e9 a verdade, mas quando fala, mente.", "La paradoja de Kafka: el arte depende de la verdad, pero la verdad, siendo indivisible, no puede conocerse: decir la verdad es mentir. As\u00ed el escritor es la verdad, pero cuando habla, miente."),
    # 195
    ("\u00c9 a doen\u00e7a natural do homem acreditar que possui a verdade.", "Es la enfermedad natural del hombre creer que posee la verdad."),
    # 196
    ("Este \u00e9 o s\u00e9culo do medo.", "Este es el siglo del miedo."),
    # 197 - long Camus on culture - summarize
    ("N\u00e3o \u00e9 verdade que a cultura possa ser, mesmo temporariamente, suspensa para dar lugar a uma nova cultura. O testemunho ininterrupto do homem sobre seu sofrimento e sua nobreza n\u00e3o pode ser suspenso. Sim, quando a tirania moderna nos mostra que o artista \u00e9 um inimigo p\u00fablico, ela tem raz\u00e3o. Minha conclus\u00e3o: no meio do som e da f\u00faria da nossa hist\u00f3ria, \u201cAlegremo-nos.\u201d", "No es verdad que la cultura pueda ser, ni siquiera temporalmente, suspendida para dar lugar a una nueva cultura. El testimonio ininterrumpido del hombre sobre su sufrimiento y su nobleza no puede suspenderse. S\u00ed, cuando la tiran\u00eda moderna nos muestra que el artista es un enemigo p\u00fablico, tiene raz\u00f3n. Mi conclusi\u00f3n: en medio del sonido y la furia de nuestra historia, \u00abAlegr\u00e9monos.\u00bb"),
    # 198 - long Beauvoir on philosophy
    ("O que me atraiu na filosofia foi que ia direto ao essencial. Eu percebia o significado geral das coisas e n\u00e3o suas singularidades; preferia compreender a ver. A filosofia ia direto ao cora\u00e7\u00e3o da verdade e me revelava uma ordem, uma raz\u00e3o, uma necessidade em tudo.", "Lo que me atra\u00eda de la filosof\u00eda era que iba directo a lo esencial. Yo percib\u00eda el significado general de las cosas y no sus singularidades; prefer\u00eda comprender a ver. La filosof\u00eda iba directo al coraz\u00f3n de la verdad y me revelaba un orden, una raz\u00f3n, una necesidad en todo."),
    # 199
    ("O amor n\u00e3o conhece limite para sua resist\u00eancia, nem fim para sua confian\u00e7a, nem esmaecimento de sua esperan\u00e7a; pode sobreviver a qualquer coisa. O amor ainda permanece de p\u00e9 quando tudo o mais caiu.", "El amor no conoce l\u00edmite para su resistencia, ni fin para su confianza, ni desvanecimiento de su esperanza; puede sobrevivir a cualquier cosa. El amor a\u00fan permanece en pie cuando todo lo dem\u00e1s ha ca\u00eddo."),
]

for i, key in enumerate(batch):
    if i < len(tl):
        tr[key] = {"pt": tl[i][0], "es": tl[i][1]}

with open('c:/Users/lalli/Flutter/coach_phrase_app/translations_exist.json', 'w', encoding='utf-8') as f:
    json.dump(tr, f, ensure_ascii=False, indent=2)

print(f'Existentialism total: {len(tr)} translations')
