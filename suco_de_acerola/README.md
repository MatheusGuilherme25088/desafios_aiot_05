# Suco de Acerola

## Descrição
Um grupo de **N** amigos foi a uma fazenda e colheu **F** acerolas para fazer
suco. Cada acerola rende **50 ml** de suco, e o suco é dividido igualmente
entre os amigos. Quantos litros de suco cada amigo vai beber?

## Entrada
Vários casos de teste. Cada caso é uma linha com dois inteiros **N** e **F**
(1 ≤ N ≤ 1000, 1 ≤ F ≤ 1000). A entrada termina com a linha `0 0`.

## Saída
Para cada caso, uma linha com a quantidade de suco (em litros) de cada amigo,
com **duas casas decimais**.

## Raciocínio
- Total de suco em ml: `F × 50`.
- Cada amigo recebe: `F × 50 / N` ml.
- Em litros: dividir por 1000.
- Exemplo: 5 amigos e 431 acerolas → 431 × 50 / 5 / 1000 = **4.31** litros.

## Como executar
Dentro desta pasta, em qualquer terminal (PowerShell, CMD ou Bash):
```
python suco_de_acerola.py
```
O programa lê sozinho o `entrada.txt` desta pasta. O resultado deve ser
igual ao `saida.txt`.

Também funciona passando a entrada pelo terminal:
- CMD ou Bash: `python suco_de_acerola.py < entrada.txt`
- PowerShell: `Get-Content entrada.txt | python suco_de_acerola.py`
