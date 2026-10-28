# Fechem as portas!
# Cada porta é trocada uma vez para cada divisor do seu número.
# Só fica aberta a porta com quantidade ímpar de divisores,
# ou seja, os quadrados perfeitos (1, 4, 9, 16, ...).

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


linhas = ler_linhas()
for linha in linhas:
    n = int(linha)
    if n == 0:
        break
    abertas = []
    i = 1
    while i * i <= n:
        abertas.append(str(i * i))
        i = i + 1
    print(" ".join(abertas))
