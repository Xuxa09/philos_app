"""Add all remaining classical translations."""
import json

with open('c:/Users/lalli/Flutter/coach_phrase_app/missing_classical.json', 'r', encoding='utf-8') as f:
    missing = json.load(f)

with open('c:/Users/lalli/Flutter/coach_phrase_app/translations_classical.json', 'r', encoding='utf-8') as f:
    tr = json.load(f)

tl = [
    # 1 - long Aristotle On the Soul (already has translation key from batch2, this is the exact dart key)
    ("O conhecimento da alma contribui grandemente para o avan\u00e7o da verdade. Nosso objetivo \u00e9 apreender sua natureza essencial e suas propriedades. Alcan\u00e7ar qualquer conhecimento sobre a alma \u00e9 uma das coisas mais dif\u00edceis do mundo.", "El conocimiento del alma contribuye grandemente al avance de la verdad. Nuestro objetivo es aprehender su naturaleza esencial y sus propiedades. Alcanzar cualquier conocimiento sobre el alma es una de las cosas m\u00e1s dif\u00edciles del mundo."),
    # 2
    ("Nenhum mal pode acontecer a um homem bom, nem na vida nem ap\u00f3s a morte.", "Ning\u00fan mal puede sucederle a un hombre bueno, ni en vida ni despu\u00e9s de la muerte."),
    # 3
    ("Fugir dos problemas \u00e9 uma forma de covardia e, embora seja verdade que o suicida enfrenta a morte, ele o faz n\u00e3o por algum objeto nobre, mas para escapar de algum mal.", "Huir de los problemas es una forma de cobard\u00eda y, aunque es verdad que el suicida afronta la muerte, lo hace no por alg\u00fan objeto noble, sino para escapar de alg\u00fan mal."),
    # 4
    ("As pessoas comuns n\u00e3o parecem perceber que aqueles que realmente se dedicam da maneira correta \u00e0 filosofia est\u00e3o direta e por conta pr\u00f3pria se preparando para morrer e para a morte.", "Las personas comunes no parecen darse cuenta de que aquellos que realmente se dedican de la manera correcta a la filosof\u00eda est\u00e1n directa y por cuenta propia prepar\u00e1ndose para morir y para la muerte."),
    # 5
    ("A morte n\u00e3o \u00e9 o pior que pode acontecer aos homens.", "La muerte no es lo peor que puede sucederles a los hombres."),
    # 6
    ("Ningu\u00e9m sabe se a morte, que as pessoas temem como o maior mal, n\u00e3o \u00e9 o maior bem.", "Nadie sabe si la muerte, que la gente teme como el mayor mal, no es el mayor bien."),
    # 7
    ("A democracia... \u00e9 uma forma encantadora de governo, cheia de variedade e desordem; e dispensando uma esp\u00e9cie de igualdade a iguais e desiguais.", "La democracia... es una forma encantadora de gobierno, llena de variedad y desorden; y dispensando una especie de igualdad a iguales y desiguales."),
    # 8
    ("Se a liberdade e a igualdade s\u00e3o encontradas principalmente na democracia, ser\u00e3o melhor alcan\u00e7adas quando todas as pessoas igualmente participarem do governo ao m\u00e1ximo.", "Si la libertad y la igualdad se encuentran principalmente en la democracia, se alcanzar\u00e1n mejor cuando todas las personas por igual participen del gobierno al m\u00e1ximo."),
    # 9
    ("Ent\u00e3o n\u00e3o apenas o costume, mas tamb\u00e9m a natureza afirma que cometer injusti\u00e7a \u00e9 mais vergonhoso do que sofr\u00ea-la, e que justi\u00e7a \u00e9 igualdade.", "Entonces no solo la costumbre, sino tambi\u00e9n la naturaleza afirma que cometer injusticia es m\u00e1s vergonzoso que sufrirla, y que justicia es igualdad."),
    # 10
    ("Bons h\u00e1bitos formados na juventude fazem toda a diferen\u00e7a.", "Buenos h\u00e1bitos formados en la juventud hacen toda la diferencia."),
    # 11
    ("A m\u00fasica \u00e9 uma lei moral. D\u00e1 alma ao universo, asas \u00e0 mente, voo \u00e0 imagina\u00e7\u00e3o, e encanto e alegria \u00e0 vida e a tudo.", "La m\u00fasica es una ley moral. Da alma al universo, alas a la mente, vuelo a la imaginaci\u00f3n, y encanto y alegr\u00eda a la vida y a todo."),
    # 12
    ("A m\u00fasica \u00e9 o movimento do som para alcan\u00e7ar a alma para a educa\u00e7\u00e3o de sua virtude.", "La m\u00fasica es el movimiento del sonido para alcanzar el alma para la educaci\u00f3n de su virtud."),
    # 13
    ("Aqueles que t\u00eam a virtude sempre na boca e a negligenciam na pr\u00e1tica s\u00e3o como uma harpa que emite um som agrad\u00e1vel aos outros, enquanto ela mesma \u00e9 insens\u00edvel \u00e0 m\u00fasica.", "Aquellos que tienen la virtud siempre en la boca y la descuidan en la pr\u00e1ctica son como un arpa que emite un sonido agradable a los dem\u00e1s, mientras ella misma es insensible a la m\u00fasica."),
    # 14
    ("Pois a introdu\u00e7\u00e3o de um novo tipo de m\u00fasica deve ser evitada como algo que p\u00f5e em perigo todo o estado, j\u00e1 que os estilos musicais nunca s\u00e3o perturbados sem afetar as mais importantes institui\u00e7\u00f5es pol\u00edticas.", "Pues la introducci\u00f3n de un nuevo tipo de m\u00fasica debe evitarse como algo que pone en peligro todo el estado, ya que los estilos musicales nunca se perturban sin afectar las m\u00e1s importantes instituciones pol\u00edticas."),
    # 15
    ("A educa\u00e7\u00e3o \u00e9 a melhor provis\u00e3o para a velhice.", "La educaci\u00f3n es la mejor provisi\u00f3n para la vejez."),
    # 16
    ("A timidez \u00e9 um ornamento para a juventude, mas uma censura para a velhice.", "La timidez es un ornamento para la juventud, pero un reproche para la vejez."),
    # 17
    ("Diferentes homens buscam a felicidade de diferentes maneiras e por diferentes meios, e assim criam para si diferentes modos de vida e formas de governo.", "Diferentes hombres buscan la felicidad de diferentes maneras y por diferentes medios, y as\u00ed crean para s\u00ed diferentes modos de vida y formas de gobierno."),
    # 18
    ("Os pol\u00edticos tamb\u00e9m n\u00e3o t\u00eam lazer, porque est\u00e3o sempre mirando algo al\u00e9m da vida pol\u00edtica em si \u2014 poder e gl\u00f3ria, ou felicidade.", "Los pol\u00edticos tampoco tienen ocio, porque siempre est\u00e1n apuntando a algo m\u00e1s all\u00e1 de la vida pol\u00edtica en s\u00ed \u2014 poder y gloria, o felicidad."),
    # 19
    ("N\u00e3o h\u00e1 grande g\u00eanio sem algum toque de loucura.", "No hay gran genio sin alg\u00fan toque de locura."),
    # 20
    ("O homem \u00e9 o mais inteligente dos animais \u2014 e o mais tolo.", "El hombre es el m\u00e1s inteligente de los animales \u2014 y el m\u00e1s tonto."),
    # 21
    ("Muito aprendizado n\u00e3o ensina compreens\u00e3o.", "Mucho aprendizaje no ense\u00f1a comprensi\u00f3n."),
    # 22
    ("A ignor\u00e2ncia de todas as coisas n\u00e3o \u00e9 um mal terr\u00edvel nem excessivo, nem o maior de todos; mas grande esperteza e muito aprendizado, se acompanhados de m\u00e1 cria\u00e7\u00e3o, s\u00e3o um infort\u00fanio muito maior.", "La ignorancia de todas las cosas no es un mal terrible ni excesivo, ni el mayor de todos; pero gran astucia y mucho aprendizaje, si van acompa\u00f1ados de mala crianza, son un infortunio mucho mayor."),
    # 23
    ("O aprendizado e o conhecimento que temos \u00e9, no m\u00e1ximo, pouco comparado com aquilo de que somos ignorantes.", "El aprendizaje y el conocimiento que tenemos es, como mucho, poco comparado con aquello de lo que somos ignorantes."),
    # 24
    ("N\u00e3o aprendemos, e o que chamamos de aprendizado \u00e9 apenas um processo de recorda\u00e7\u00e3o.", "No aprendemos, y lo que llamamos aprendizaje es solo un proceso de recuerdo."),
    # 25
    ("Gostaria de envelhecer aprendendo muitas coisas.", "Me gustar\u00eda envejecer aprendiendo muchas cosas."),
    # 26
    ("A ignor\u00e2ncia total n\u00e3o \u00e9 um mal t\u00e3o terr\u00edvel ou extremo, e est\u00e1 longe de ser o maior de todos; muita esperteza e muito aprendizado, acompanhados de m\u00e1 cria\u00e7\u00e3o, s\u00e3o muito mais fatais.", "La ignorancia total no es un mal tan terrible o extremo, y est\u00e1 lejos de ser el mayor de todos; mucha astucia y mucho aprendizaje, acompa\u00f1ados de mala crianza, son mucho m\u00e1s fatales."),
    # 27
    ("E qual, S\u00f3crates, \u00e9 o alimento da alma? Certamente, eu disse, o conhecimento \u00e9 o alimento da alma.", "Y cu\u00e1l, S\u00f3crates, es el alimento del alma? Ciertamente, dije, el conocimiento es el alimento del alma."),
    # 28
    ("Qualquer um pode ficar com raiva \u2014 isso \u00e9 f\u00e1cil, mas ficar com raiva da pessoa certa, no grau certo, no momento certo, pelo motivo certo e da maneira certa \u2014 isso n\u00e3o est\u00e1 ao alcance de todos e n\u00e3o \u00e9 f\u00e1cil.", "Cualquiera puede enojarse \u2014 eso es f\u00e1cil, pero enojarse con la persona correcta, en el grado correcto, en el momento correcto, por el motivo correcto y de la manera correcta \u2014 eso no est\u00e1 al alcance de todos y no es f\u00e1cil."),
    # 29
    ("Vivemos em atos, n\u00e3o em anos; em pensamentos, n\u00e3o em respira\u00e7\u00f5es; em sentimentos, n\u00e3o em n\u00fameros num mostrador. Devemos contar o tempo pelos batimentos do cora\u00e7\u00e3o. Mais vive quem mais pensa, sente o mais nobre, age o melhor.", "Vivimos en actos, no en a\u00f1os; en pensamientos, no en respiraciones; en sentimientos, no en cifras en un dial. Debemos contar el tiempo por los latidos del coraz\u00f3n. M\u00e1s vive quien m\u00e1s piensa, siente lo m\u00e1s noble, act\u00faa lo mejor."),
    # 30
    ("Empregue seu tempo em se aprimorar pelos escritos de outros homens, para que venha facilmente pelo que outros trabalharam arduamente.", "Emplea tu tiempo en mejorarte por los escritos de otros hombres, para que obtengas f\u00e1cilmente lo que otros han trabajado arduamente."),
    # 31
    ("Nada pode ser mais absurdo do que a pr\u00e1tica que prevalece em nosso pa\u00eds de homens e mulheres n\u00e3o seguirem as mesmas ocupa\u00e7\u00f5es com toda a for\u00e7a e com uma s\u00f3 mente.", "Nada puede ser m\u00e1s absurdo que la pr\u00e1ctica que prevalece en nuestro pa\u00eds de hombres y mujeres no siguiendo las mismas ocupaciones con toda su fuerza y con una sola mente."),
    # 32
    ("No seu melhor, o homem \u00e9 o mais nobre de todos os animais; separado da lei e da justi\u00e7a, \u00e9 o pior.", "En su mejor momento, el hombre es el m\u00e1s noble de todos los animales; separado de la ley y la justicia, es el peor."),
    # 33
    ("O homem ideal suporta os acidentes da vida com dignidade e gra\u00e7a, fazendo o melhor das circunst\u00e2ncias.", "El hombre ideal soporta los accidentes de la vida con dignidad y gracia, haciendo lo mejor de las circunstancias."),
    # 34
    ("Uma boa decis\u00e3o \u00e9 baseada em conhecimento e n\u00e3o em n\u00fameros.", "Una buena decisi\u00f3n se basa en el conocimiento y no en los n\u00fameros."),
    # 35
    ("Case-se de qualquer maneira. Se conseguir uma boa esposa, ser\u00e1 feliz; se conseguir uma m\u00e1, se tornar\u00e1 fil\u00f3sofo.", "C\u00e1sate de cualquier manera. Si consigues una buena esposa, ser\u00e1s feliz; si consigues una mala, te convertir\u00e1s en fil\u00f3sofo."),
    # 36
    ("A persuas\u00e3o \u00e9 alcan\u00e7ada pelo car\u00e1ter pessoal do orador quando o discurso \u00e9 falado de tal forma que nos faz consider\u00e1-lo cred\u00edvel.", "La persuasi\u00f3n se logra por el car\u00e1cter personal del orador cuando el discurso es pronunciado de tal forma que nos hace considerarlo cre\u00edble."),
    # 37
    ("O ci\u00fame \u00e9 razo\u00e1vel e pertence aos homens razo\u00e1veis, enquanto a inveja \u00e9 baixa e pertence aos baixos.", "Los celos son razonables y pertenecen a los hombres razonables, mientras que la envidia es baja y pertenece a los bajos."),
    # 38
    ("Duas e tr\u00eas vezes, como dizem, bom \u00e9 repetir e revisar o que \u00e9 bom.", "Dos y tres veces, como dicen, bueno es repetir y revisar lo que es bueno."),
    # 39
    ("Como quest\u00e3o de autopreserva\u00e7\u00e3o, um homem precisa de bons amigos ou de inimigos ardentes, pois os primeiros o instruem e os \u00faltimos o chamam \u00e0 responsabilidade.", "Como cuesti\u00f3n de autopreservaci\u00f3n, un hombre necesita buenos amigos o enemigos ardientes, pues los primeros lo instruyen y los \u00faltimos lo llaman a la responsabilidad."),
    # 40
    ("O que mais gosto de beber \u00e9 vinho que pertence a outros.", "Lo que m\u00e1s me gusta beber es vino que pertenece a otros."),
    # 41
    ("N\u00e3o haver\u00e1 fim para os problemas dos estados, ou da pr\u00f3pria humanidade, at\u00e9 que os fil\u00f3sofos se tornem reis neste mundo, ou at\u00e9 que aqueles que chamamos de reis se tornem verdadeiramente fil\u00f3sofos.", "No habr\u00e1 fin para los problemas de los estados, o de la propia humanidad, hasta que los fil\u00f3sofos se conviertan en reyes en este mundo, o hasta que aquellos que llamamos reyes se conviertan verdaderamente en fil\u00f3sofos."),
    # 42
    ("O valor \u00faltimo da vida depende da consci\u00eancia e do poder de contempla\u00e7\u00e3o, e n\u00e3o da mera sobreviv\u00eancia.", "El valor \u00faltimo de la vida depende de la conciencia y del poder de contemplaci\u00f3n, y no de la mera supervivencia."),
    # 43
    ("O que est\u00e1 em nosso poder fazer, est\u00e1 em nosso poder n\u00e3o fazer.", "Lo que est\u00e1 en nuestro poder hacer, est\u00e1 en nuestro poder no hacer."),
    # 44
    ("Eu s\u00f3 gostaria que as pessoas comuns tivessem uma capacidade ilimitada de fazer mal; ent\u00e3o poderiam ter um poder ilimitado de fazer o bem.", "Solo desear\u00eda que las personas comunes tuvieran una capacidad ilimitada de hacer mal; entonces podr\u00edan tener un poder ilimitado de hacer el bien."),
    # 45
    ("Numa democracia os pobres ter\u00e3o mais poder que os ricos, porque s\u00e3o mais numerosos, e a vontade da maioria \u00e9 suprema.", "En una democracia los pobres tendr\u00e1n m\u00e1s poder que los ricos, porque son m\u00e1s numerosos, y la voluntad de la mayor\u00eda es suprema."),
    # 46
    ("\u00c9 justo que sejamos gratos n\u00e3o apenas \u00e0queles com cujas opini\u00f5es concordamos, mas tamb\u00e9m \u00e0queles que expressaram opini\u00f5es mais superficiais; pois estes tamb\u00e9m contribu\u00edram algo, desenvolvendo diante de n\u00f3s os poderes do pensamento.", "Es justo que seamos agradecidos no solo con aquellos con cuyas opiniones estamos de acuerdo, sino tambi\u00e9n con aquellos que expresaron opiniones m\u00e1s superficiales; pues estos tambi\u00e9n contribuyeron algo, desarrollando ante nosotros los poderes del pensamiento."),
    # 47
    ("Quem se deleita na solid\u00e3o \u00e9 uma fera selvagem ou um deus.", "Quien se deleita en la soledad es una bestia salvaje o un dios."),
    # 48
    ("O fim da vida \u00e9 ser semelhante a Deus, e a alma que segue Deus ser\u00e1 semelhante a Ele.", "El fin de la vida es ser semejante a Dios, y el alma que sigue a Dios ser\u00e1 semejante a \u00c9l."),
    # 49
    ("A culpa \u00e9 de quem escolhe: Deus \u00e9 inocente.", "La culpa es de quien elige: Dios es inocente."),
    # 50
    ("Aquele que \u00e9 incapaz de viver em sociedade, ou que n\u00e3o tem necessidade porque \u00e9 suficiente para si mesmo, deve ser ou uma fera ou um deus.", "Aquel que es incapaz de vivir en sociedad, o que no tiene necesidad porque es suficiente para s\u00ed mismo, debe ser o una bestia o un dios."),
    # 51
    ("O comportamento humano flui de tr\u00eas fontes principais: desejo, emo\u00e7\u00e3o e conhecimento.", "El comportamiento humano fluye de tres fuentes principales: deseo, emoci\u00f3n y conocimiento."),
    # 52
    ("A opini\u00e3o \u00e9 o meio-termo entre o conhecimento e a ignor\u00e2ncia.", "La opini\u00f3n es el t\u00e9rmino medio entre el conocimiento y la ignorancia."),
    # 53
    ("Conhecimento sem justi\u00e7a deveria ser chamado de ast\u00facia, n\u00e3o de sabedoria.", "Conocimiento sin justicia deber\u00eda llamarse astucia, no sabidur\u00eda."),
    # 54
    ("O conhecimento adquirido sob compuls\u00e3o n\u00e3o se fixa na mente.", "El conocimiento adquirido bajo compulsi\u00f3n no se fija en la mente."),
    # 55
    ("O conhecimento \u00e9 opini\u00e3o verdadeira.", "El conocimiento es opini\u00f3n verdadera."),
    # 56
    ("Alcan\u00e7ar qualquer conhecimento seguro sobre a alma \u00e9 uma das coisas mais dif\u00edceis do mundo.", "Alcanzar cualquier conocimiento seguro sobre el alma es una de las cosas m\u00e1s dif\u00edciles del mundo."),
    # 57
    ("A coragem \u00e9 um meio-termo em rela\u00e7\u00e3o ao medo e \u00e0 confian\u00e7a.", "El coraje es un t\u00e9rmino medio con respecto al miedo y la confianza."),
    # 58
    ("Ganhei isto da filosofia: fa\u00e7o sem ser ordenado o que outros fazem apenas por medo da lei.", "He ganado esto de la filosof\u00eda: hago sin que me lo ordenen lo que otros hacen solo por miedo a la ley."),
    # 59
    ("Onde h\u00e1 rever\u00eancia h\u00e1 medo, mas n\u00e3o h\u00e1 rever\u00eancia em todo lugar onde h\u00e1 medo, porque o medo presumivelmente tem uma extens\u00e3o mais ampla do que a rever\u00eancia.", "Donde hay reverencia hay miedo, pero no hay reverencia en todo lugar donde hay miedo, porque el miedo presumiblemente tiene una extensi\u00f3n m\u00e1s amplia que la reverencia."),
    # 60
    ("Os homens s\u00e3o mais influenciados pelo medo do que pela rever\u00eancia.", "Los hombres son m\u00e1s influenciados por el miedo que por la reverencia."),
    # 61
    ("A generalidade dos homens \u00e9 naturalmente apta a ser influenciada pelo medo em vez da rever\u00eancia, e a se abster do mal por causa da puni\u00e7\u00e3o que traz, e n\u00e3o por causa de sua pr\u00f3pria torpeza.", "La generalidad de los hombres es naturalmente apta para ser influenciada por el miedo en vez de la reverencia, y para abstenerse del mal por causa del castigo que trae, y no por causa de su propia torpeza."),
    # 62
    ("A injusti\u00e7a \u00e9 censurada porque os censores t\u00eam medo de sofrer, e n\u00e3o por medo de cometer injusti\u00e7a.", "La injusticia es censurada porque los censores tienen miedo de sufrir, y no por miedo de cometer injusticia."),
    # 63
    ("Certamente d\u00e3o nomes muito estranhos \u00e0s doen\u00e7as.", "Ciertamente dan nombres muy extra\u00f1os a las enfermedades."),
    # 64
    ("Plat\u00e3o me \u00e9 caro, mas mais cara ainda \u00e9 a verdade.", "Plat\u00f3n me es querido, pero m\u00e1s querida a\u00fan es la verdad."),
    # 65
    ("A piedade nos exige honrar a verdade acima de nossos amigos.", "La piedad nos exige honrar la verdad por encima de nuestros amigos."),
    # 66
    ("A verdade \u00e9 o in\u00edcio de todo bem para os deuses, e de todo bem para o homem.", "La verdad es el inicio de todo bien para los dioses, y de todo bien para el hombre."),
    # 67
    ("O menor desvio inicial da verdade se multiplica depois mil vezes.", "La menor desviaci\u00f3n inicial de la verdad se multiplica despu\u00e9s mil veces."),
    # 68
    ("Voc\u00ea nunca far\u00e1 nada neste mundo sem coragem. \u00c9 a maior qualidade da mente depois da honra.", "Nunca har\u00e1s nada en este mundo sin coraje. Es la mayor cualidad de la mente despu\u00e9s del honor."),
    # 69
    ("\u00c9 homem de coragem aquele que n\u00e3o foge, mas permanece em seu posto e luta contra o inimigo.", "Es hombre de coraje aquel que no huye, sino que permanece en su puesto y lucha contra el enemigo."),
    # 70
    ("A melhor maneira de viver com honra neste mundo \u00e9 ser o que fingimos ser.", "La mejor manera de vivir con honor en este mundo es ser lo que pretendemos ser."),
    # 71
    ("Melhor pouco bem feito do que muito feito imperfeitamente.", "Mejor poco bien hecho que mucho hecho imperfectamente."),
    # 72
    ("A primeira e maior vit\u00f3ria \u00e9 conquistar a si mesmo; ser conquistado por si mesmo \u00e9 a coisa mais vergonhosa e vil.", "La primera y mayor victoria es conquistarse a s\u00ed mismo; ser conquistado por s\u00ed mismo es lo m\u00e1s vergonzoso y vil."),
    # 73
    ("O sofrimento se torna belo quando algu\u00e9m suporta grandes calamidades com alegria, n\u00e3o por insensibilidade, mas por grandeza de esp\u00edrito.", "El sufrimiento se vuelve bello cuando alguien soporta grandes calamidades con alegr\u00eda, no por insensibilidad, sino por grandeza de esp\u00edritu."),
    # 74
    ("A aten\u00e7\u00e3o \u00e0 sa\u00fade \u00e9 o maior empecilho da vida.", "La atenci\u00f3n a la salud es el mayor impedimento de la vida."),
    # 75
    ("Estamos duplamente armados se lutamos com f\u00e9.", "Estamos doblemente armados si luchamos con fe."),
    # 76
    ("Quanto ao casamento ou celibato, que o homem tome o caminho que quiser, com certeza se arrepender\u00e1.", "En cuanto al matrimonio o el celibato, que el hombre tome el camino que quiera, con seguridad se arrepentir\u00e1."),
    # 77
    ("A beleza \u00e9 uma tirania de curta dura\u00e7\u00e3o.", "La belleza es una tiran\u00eda de corta duraci\u00f3n."),
    # 78
    ("A beleza pessoal \u00e9 uma recomenda\u00e7\u00e3o maior do que qualquer carta de refer\u00eancia.", "La belleza personal es una recomendaci\u00f3n mayor que cualquier carta de referencia."),
    # 79
    ("A beleza \u00e9 a isca que com deleite atrai o homem a expandir sua esp\u00e9cie.", "La belleza es el cebo que con deleite atrae al hombre a expandir su especie."),
    # 80
    ("Seja lento para cair na amizade; mas quando estiver nela, continue firme e constante.", "S\u00e9 lento para caer en la amistad; pero cuando est\u00e9s en ella, contin\u00faa firme y constante."),
    # 81
    ("A ret\u00f3rica pode ser definida como a faculdade de observar em qualquer caso dado os meios dispon\u00edveis de persuas\u00e3o. Esta n\u00e3o \u00e9 fun\u00e7\u00e3o de nenhuma outra arte.", "La ret\u00f3rica puede definirse como la facultad de observar en cualquier caso dado los medios disponibles de persuasi\u00f3n. Esta no es funci\u00f3n de ninguna otra arte."),
    # 82
    ("\u00c9 Homero quem principalmente ensinou os outros poetas a arte de contar mentiras habilmente.", "Es Homero quien principalmente ha ense\u00f1ado a los otros poetas el arte de contar mentiras h\u00e1bilmente."),
    # 83
    ("A arte de ser escravo \u00e9 governar seu mestre.", "El arte de ser esclavo es gobernar a tu amo."),
    # 84
    ("Homero ensinou a todos os outros poetas a arte de contar mentiras habilmente.", "Homero ha ense\u00f1ado a todos los dem\u00e1s poetas el arte de contar mentiras h\u00e1bilmente."),
    # 85
    ("Uma das penalidades de se recusar a participar da pol\u00edtica \u00e9 acabar sendo governado por seus inferiores.", "Una de las penalidades de negarse a participar en pol\u00edtica es terminar siendo gobernado por tus inferiores."),
    # 86
    ("A democracia \u00e9 quando os indigentes, e n\u00e3o os homens de propriedade, s\u00e3o os governantes.", "La democracia es cuando los indigentes, y no los hombres de propiedad, son los gobernantes."),
    # 87
    ("A amizade \u00e9 essencialmente uma parceria.", "La amistad es esencialmente una asociaci\u00f3n."),
    # 88
    ("Quem tem muitos amigos n\u00e3o tem nenhum.", "Quien tiene muchos amigos no tiene ninguno."),
    # 89
    ("A amizade perfeita \u00e9 a amizade de homens que s\u00e3o bons e semelhantes em excel\u00eancia; pois estes desejam o bem igualmente um ao outro enquanto bons, e s\u00e3o bons em si mesmos.", "La amistad perfecta es la amistad de hombres que son buenos y semejantes en excelencia; pues estos desean el bien igualmente el uno al otro en cuanto buenos, y son buenos en s\u00ed mismos."),
    # 90
    ("Qualidade n\u00e3o \u00e9 um ato, \u00e9 um h\u00e1bito.", "La calidad no es un acto, es un h\u00e1bito."),
    # 91
    ("As m\u00e3es s\u00e3o mais apegadas que os pais a seus filhos porque t\u00eam mais certeza de que s\u00e3o seus.", "Las madres son m\u00e1s apegadas que los padres a sus hijos porque tienen m\u00e1s certeza de que son suyos."),
    # 92
    ("A democracia passa ao despotismo.", "La democracia pasa al despotismo."),
    # 93
    ("A puni\u00e7\u00e3o que sofrem os s\u00e1bios que se recusam a participar do governo \u00e9 viver sob o governo de homens piores.", "El castigo que sufren los sabios que se niegan a participar del gobierno es vivir bajo el gobierno de hombres peores."),
    # 94
    ("As ra\u00edzes da educa\u00e7\u00e3o s\u00e3o amargas, mas o fruto \u00e9 doce.", "Las ra\u00edces de la educaci\u00f3n son amargas, pero el fruto es dulce."),
    # 95
    ("Se um homem negligencia a educa\u00e7\u00e3o, caminha manco at\u00e9 o fim da vida.", "Si un hombre descuida la educaci\u00f3n, camina cojo hasta el final de la vida."),
    # 96
    ("A educa\u00e7\u00e3o \u00e9 um ornamento na prosperidade e um ref\u00fagio na adversidade.", "La educaci\u00f3n es un ornamento en la prosperidad y un refugio en la adversidad."),
    # 97
    ("A dire\u00e7\u00e3o em que a educa\u00e7\u00e3o inicia um homem determinar\u00e1 seu futuro na vida.", "La direcci\u00f3n en que la educaci\u00f3n inicia a un hombre determinar\u00e1 su futuro en la vida."),
    # 98
    ("A parte mais importante da educa\u00e7\u00e3o \u00e9 o treinamento adequado na inf\u00e2ncia.", "La parte m\u00e1s importante de la educaci\u00f3n es el entrenamiento adecuado en la infancia."),
    # 99
    ("Seja como deseja parecer.", "S\u00e9 como deseas parecer."),
    # 100
    ("A verdadeira sabedoria chega a cada um de n\u00f3s quando percebemos qu\u00e3o pouco entendemos sobre a vida, sobre n\u00f3s mesmos e sobre o mundo ao nosso redor.", "La verdadera sabidur\u00eda llega a cada uno de nosotros cuando nos damos cuenta de cu\u00e1n poco entendemos sobre la vida, sobre nosotros mismos y sobre el mundo que nos rodea."),
    # 101
    ("A sabedoria come\u00e7a no espanto.", "La sabidur\u00eda comienza en el asombro."),
    # 102
    ("H\u00e1 tr\u00eas classes de homens: amantes da sabedoria, amantes da honra e amantes do ganho.", "Hay tres clases de hombres: amantes de la sabidur\u00eda, amantes del honor y amantes de la ganancia."),
    # 103
    ("Decidi que n\u00e3o foi a sabedoria que permitiu aos poetas escrever sua poesia, mas uma esp\u00e9cie de instinto ou inspira\u00e7\u00e3o, como aquela que se encontra em videntes e profetas.", "Decid\u00ed que no fue la sabidur\u00eda lo que permiti\u00f3 a los poetas escribir su poes\u00eda, sino una especie de instinto o inspiraci\u00f3n, como la que se encuentra en videntes y profetas."),
    # 104
    ("Reis s\u00e1bios geralmente t\u00eam conselheiros s\u00e1bios, e ele pr\u00f3prio deve ser um homem s\u00e1bio que \u00e9 capaz de distinguir um.", "Los reyes sabios generalmente tienen consejeros sabios, y \u00e9l mismo debe ser un hombre sabio que es capaz de distinguir a uno."),
    # 105
    ("A ast\u00facia... \u00e9 apenas a r\u00e9plica inferior da sabedoria.", "La astucia... es solo la r\u00e9plica inferior de la sabidur\u00eda."),
    # 106
    ("A virtude da justi\u00e7a consiste na modera\u00e7\u00e3o, regulada pela sabedoria.", "La virtud de la justicia consiste en la moderaci\u00f3n, regulada por la sabidur\u00eda."),
    # 107
    ("A excel\u00eancia, ent\u00e3o, \u00e9 um estado relacionado \u00e0 escolha, situado num meio-termo relativo a n\u00f3s, determinado pela raz\u00e3o e da maneira como o homem de sabedoria pr\u00e1tica o determinaria.", "La excelencia, entonces, es un estado relacionado con la elecci\u00f3n, situado en un t\u00e9rmino medio relativo a nosotros, determinado por la raz\u00f3n y de la manera como el hombre de sabidur\u00eda pr\u00e1ctica lo determinar\u00eda."),
    # 108
    ("Cuidado com a esterilidade de uma vida ocupada.", "Cuidado con la esterilidad de una vida ocupada."),
    # 109
    ("A vida deve ser vivida como um jogo.", "La vida debe vivirse como un juego."),
    # 110
    ("Um homem n\u00e3o pode praticar muitas artes com sucesso.", "Un hombre no puede practicar muchas artes con \u00e9xito."),
    # 111
    ("Da\u00ed a poesia ser algo mais filos\u00f3fico e de maior import\u00e2ncia do que a hist\u00f3ria, j\u00e1 que suas afirma\u00e7\u00f5es s\u00e3o antes da natureza de universais, enquanto as da hist\u00f3ria s\u00e3o singulares.", "De ah\u00ed que la poes\u00eda sea algo m\u00e1s filos\u00f3fico y de mayor importancia que la historia, ya que sus afirmaciones son m\u00e1s bien de la naturaleza de universales, mientras que las de la historia son singulares."),
    # 112
    ("Um her\u00f3i nasce entre cem, um homem s\u00e1bio se encontra entre mil, mas um realizado pode n\u00e3o ser encontrado nem entre cem mil.", "Un h\u00e9roe nace entre cien, un hombre sabio se encuentra entre mil, pero uno realizado puede no encontrarse ni entre cien mil."),
    # 113
    ("As almas de todos os homens s\u00e3o imortais, mas as almas dos justos s\u00e3o imortais e divinas.", "Las almas de todos los hombres son inmortales, pero las almas de los justos son inmortales y divinas."),
    # 114
    ("Os homens maus est\u00e3o cheios de arrependimento.", "Los hombres malos est\u00e1n llenos de arrepentimiento."),
    # 115
    ("\u00c9 impr\u00f3prio para jovens proferir m\u00e1ximas.", "Es impropio para los j\u00f3venes proferir m\u00e1ximas."),
    # 116
    ("A maioria dos homens est\u00e1 a um dedo de dist\u00e2ncia da loucura.", "La mayor\u00eda de los hombres est\u00e1 a un dedo de distancia de la locura."),
    # 117
    ("Aqueles que se destacam em virtude t\u00eam o melhor direito de todos a se rebelar, mas s\u00e3o de todos os homens os menos inclinados a faz\u00ea-lo.", "Aquellos que se destacan en virtud tienen el mejor derecho de todos a rebelarse, pero son de todos los hombres los menos inclinados a hacerlo."),
    # 118
    ("A mudan\u00e7a em todas as coisas \u00e9 doce.", "El cambio en todas las cosas es dulce."),
    # 119
    ("O excesso geralmente causa rea\u00e7\u00e3o e produz mudan\u00e7a na dire\u00e7\u00e3o oposta, seja nas esta\u00e7\u00f5es, nos indiv\u00edduos ou nos governos.", "El exceso generalmente causa reacci\u00f3n y produce cambio en la direcci\u00f3n opuesta, sea en las estaciones, en los individuos o en los gobiernos."),
    # 120
    ("Somente a mudan\u00e7a \u00e9 imut\u00e1vel.", "Solo el cambio es inmutable."),
    # 121
    ("A justi\u00e7a na vida e na conduta do Estado s\u00f3 \u00e9 poss\u00edvel quando primeiro reside nos cora\u00e7\u00f5es e almas dos cidad\u00e3os.", "La justicia en la vida y en la conducta del Estado solo es posible cuando primero reside en los corazones y almas de los ciudadanos."),
    # 122
    ("\u00c9 correto dar a cada homem o que lhe \u00e9 devido.", "Es correcto dar a cada hombre lo que le es debido."),
    # 123
    ("A corrente do casamento \u00e9 t\u00e3o pesada que s\u00e3o necess\u00e1rios dois para carreg\u00e1-la \u2014 e \u00e0s vezes tr\u00eas.", "La cadena del matrimonio es tan pesada que se necesitan dos para cargarla \u2014 y a veces tres."),
    # 124
    ("N\u00e3o sou ateniense ou grego, mas cidad\u00e3o do mundo.", "No soy ateniense o griego, sino ciudadano del mundo."),
]

for i, key in enumerate(missing):
    if i < len(tl):
        tr[key] = {"pt": tl[i][0], "es": tl[i][1]}

with open('c:/Users/lalli/Flutter/coach_phrase_app/translations_classical.json', 'w', encoding='utf-8') as f:
    json.dump(tr, f, ensure_ascii=False, indent=2)

print(f'Classical translations total: {len(tr)}')
