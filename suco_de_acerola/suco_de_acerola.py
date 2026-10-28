# Suco de Acerola
# Cada acerola rende 50 ml de suco, dividido igualmente entre os N amigos.
# A resposta é em litros, com duas casas decimais.

linha = input().split()
n = int(linha[0])
f = int(linha[1])
while n != 0 or f != 0:
    litros = f * 50 / n / 1000
    print(f"{litros:.2f}")
    linha = input().split()
    n = int(linha[0])
    f = int(linha[1])
