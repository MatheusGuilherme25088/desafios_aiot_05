# Fechem as portas!
# Cada porta é trocada uma vez para cada divisor do seu número.
# Só fica aberta a porta com quantidade ímpar de divisores,
# ou seja, os quadrados perfeitos (1, 4, 9, 16, ...).

n = int(input())
while n != 0:
    abertas = []
    i = 1
    while i * i <= n:
        abertas.append(str(i * i))
        i = i + 1
    print(" ".join(abertas))
    n = int(input())
