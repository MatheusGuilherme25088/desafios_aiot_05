# Help!
# Calcula o placar de um time na maratona de programação:
# S = quantidade de problemas resolvidos
# P = tempo total (tempo do acerto + 20 minutos por erro antes do acerto)

n = int(input())
while n != 0:
    erros = {}       # erros de cada problema antes do acerto
    resolvidos = {}  # tempo do acerto de cada problema
    for i in range(n):
        problema, tempo, julgamento = input().split()
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
    n = int(input())
