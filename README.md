# Jogo de Guerra: Gladiadores

Na Roma Antiga, os Gladiadores lutavam entre si na arena, para entretimento do Imperador e do público. O espetáculo, violento e sangrento, era até à morte. Hoje, vamos escrever um pequeno jogo em Python, que nos permita simular um jogo de gladiadores com o computador!

Um gladiador (computador) está escondido numa arena de 5 por 5 metros. A cada jogada, é colocado numa posição aleatória (x,y) na arena.

O utilizador deve então também colocar o seu jogador (adversário) na arena. O gladiador tem uma zona de ataque de raio r, como mostra a figura, e o jogo respeita as seguintes regras:

Arena de Gladiadores

Se o adversário estiver longe do gladiador, escapa com vida!
Se o adversário estiver na zona de ataque do gladiador e se o gladiador estiver em modo de ataque, então o gladiador decapitará o seu adversário instantaneamente. Estar “em modo de ataque” deverá ser um comportamento aleatório;
Se o adversário estiver na zona de ataque do gladiador e o gladiador não estiver em modo de ataque, então o gladiador é morto.
Podemos assumir o seguinte:

São permitidas no máximo 10 jogadas;
O raio de ataque do gladiador é de 2 metros;
A cada jogada, o programa deverá indicar se o adversário escapou ou não com vida;
No final de todas as jogadas, deve ser impresso o número total de vítimas e sobreviventes. No entanto, se o gladiador for morto numa jogada, o programa deverá parar e indicar o número de vítimas e sobreviventes até ao momento e o número de jogadas que foram necessárias para o aniquilar!


Source: As Raparigas do Código - Workshop Python
