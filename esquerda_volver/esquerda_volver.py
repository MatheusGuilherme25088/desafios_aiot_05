# Esquerda, Volver!
# As direções ficam numa lista no sentido horário.
# "D" anda uma posição para frente e "E" anda uma para trás.

import os
import sys


def ler_linhas():
    # Se a entrada vier por "<" ou "|", lê do terminal (stdin).
    # Se rodar só "python arquivo.py", lê o entrada.txt da mesma pasta.
    texto = ""
    if not sys.stdin.isatty():
        texto = sys.stdin.read()
    if texto.strip() == "":
        pasta = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(pasta, "entrada.txt"), encoding="utf-8-sig") as arquivo:
            texto = arquivo.read()
    # Remove o caractere invisível (BOM) que o PowerShell coloca no começo
    texto = texto.replace(chr(0xFEFF), "")
    return [linha.strip() for linha in texto.splitlines() if linha.strip()]


direcoes = ["N", "L", "S", "O"]

linhas = ler_linhas()
i = 0
while i < len(linhas):
    n = int(linhas[i])
    if n == 0:
        break
    comandos = linhas[i + 1]
    posicao = 0  # começa olhando para o Norte
    for c in comandos[:n]:
        if c == "D":
            posicao = (posicao + 1) % 4
        else:
            posicao = (posicao - 1) % 4
    print(direcoes[posicao])
    i = i + 2
