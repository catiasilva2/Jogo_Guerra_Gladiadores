# Constantes
raio_de_ataque = 2
x_arena = 5
y_arena = 5
jogadas_max = 10

# Estatísticas
contador = 0
vitimas = 0
sobreviventes = 0

import random


# Gerar posição do gladiador
def gera_coordenada():
    coordenada = random.uniform(1, 5)
    return coordenada


# Gerar modo de ataque do gladiador
def modo_ataque():
    modo = random.choice([True, False])
    return modo


# Calcular distância
def calcula_distancia(xA, yA, xB, yB):
    return ((xA - xB) ** 2 + (yA - yB) ** 2) ** 0.5


# Enquanto ainda há jogadas...
while contador < jogadas_max:

    # Colocar gladiador numa posição aleatória da arena
    xA = gera_coordenada()
    yA = gera_coordenada()
    print("\nO gladiador está em posição!")

    # Pedir ao utilizador que indique as posições do adversário
    print("Onde colocar o adversário?")
    xB = float(input("X = "))
    yB = float(input("Y = "))

    # Jogo
    if (xB < 0 or xB > x_arena) or (yB < 0 or yB > y_arena):
        print("Coordenada inválida")
    else:
        # Determinar distância entre gladiador e adversário
        dist = calcula_distancia(xA, yA, xB, yB)

        # Verificar se o adversário está no raio de ataque do gladiador
        if dist <= raio_de_ataque and modo_ataque() == False:
            print("O gladiador foi morto!")
            contador += 1
            sobreviventes += 1
            break
        if dist <= raio_de_ataque and modo_ataque() == True:
            print("O gladiador eliminou o adversário...")
            contador += 1
            vitimas += 1
        elif dist > 2:
            print("O adversário escapou!")
            contador += 1
            sobreviventes += 1

# No final, imprimir as estatísticas pedidas!
print("\nFim do jogo!")
print("Vítimas: " + str(vitimas))
print("Sobreviventes: " + str(sobreviventes))
print("Tentativas necessárias para eliminar o gladiador: " + str(contador))