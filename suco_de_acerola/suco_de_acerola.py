# Suco de Acerola
# Cada acerola rende 50 ml de suco, dividido igualmente entre os N amigos.
# A resposta é em litros, com duas casas decimais.

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
    n, f = linha.split()
    n = int(n)
    f = int(f)
    if n == 0 and f == 0:
        break
    litros = f * 50 / n / 1000
    print(f"{litros:.2f}")
