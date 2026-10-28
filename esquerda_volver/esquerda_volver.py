# Esquerda, Volver!
# As direções ficam numa lista no sentido horário.
# "D" anda uma posição para frente e "E" anda uma para trás.

direcoes = ["N", "L", "S", "O"]

n = int(input())
while n != 0:
    comandos = input().strip()
    posicao = 0  # começa olhando para o Norte
    for c in comandos:
        if c == "D":
            posicao = (posicao + 1) % 4
        else:
            posicao = (posicao - 1) % 4
    print(direcoes[posicao])
    n = int(input())
