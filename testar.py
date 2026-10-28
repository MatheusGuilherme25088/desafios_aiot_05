# Roda todos os desafios com o entrada.txt e compara com o saida.txt.
# Como usar (dentro da pasta desafios):  python testar.py

import os
import subprocess
import sys

desafios = ["fechem_as_portas", "esquerda_volver", "suco_de_acerola", "help"]
raiz = os.path.dirname(os.path.abspath(__file__))
tudo_certo = True

for nome in desafios:
    pasta = os.path.join(raiz, nome)
    with open(os.path.join(pasta, "entrada.txt"), encoding="utf-8") as arquivo:
        entrada = arquivo.read()
    with open(os.path.join(pasta, "saida.txt"), encoding="utf-8") as arquivo:
        esperado = arquivo.read().split("\n")

    resultado = subprocess.run(
        [sys.executable, os.path.join(pasta, nome + ".py")],
        input=entrada, capture_output=True, text=True,
    )
    obtido = resultado.stdout.split("\n")

    esperado = [linha.strip() for linha in esperado if linha.strip()]
    obtido = [linha.strip() for linha in obtido if linha.strip()]

    if obtido == esperado:
        print(f"[OK]   {nome}")
    else:
        tudo_certo = False
        print(f"[ERRO] {nome}")
        print("  esperado:", esperado)
        print("  obtido:  ", obtido)
        if resultado.stderr:
            print(resultado.stderr)

print()
print("Todos os desafios passaram!" if tudo_certo else "Algum desafio falhou.")
