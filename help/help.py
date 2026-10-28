# Help!
# Calcula o placar de um time na maratona de programação:
# S = quantidade de problemas resolvidos
# P = tempo total (tempo do acerto + 20 minutos por erro antes do acerto)

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
i = 0
while i < len(linhas):
    n = int(linhas[i])
    if n == 0:
        break
    erros = {}       # erros de cada problema antes do acerto
    resolvidos = {}  # tempo do acerto de cada problema
    for linha in linhas[i + 1:i + 1 + n]:
        problema, tempo, julgamento = linha.split()
        tempo = int(tempo)
        if problema in resolvidos:
            continue  # já resolvido, ignora envios depois do acerto
        if julgamento == "correct":
            resolvidos[problema] = tempo
        else:
            erros[problema] = erros.get(problema, 0) + 1

    s = len(resolvidos)
    p = 0
    for problema in resolvidos:
        p = p + resolvidos[problema] + 20 * erros.get(problema, 0)
    print(s, p)
    i = i + 1 + n
