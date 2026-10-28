# Esquerda, Volver!

## Descrição
Um recruta começa com a face voltada para o **Norte**. O sargento dá uma série
de comandos e, a cada um, o recruta gira um quarto de volta:
- **E** ("Esquerda, Volver!"): gira para a esquerda.
- **D** ("Direita, Volver!"): gira para a direita.

Descubra para qual direção o recruta fica olhando no final.

## Entrada
Vários casos de teste. A primeira linha de cada caso tem um inteiro **N**
(1 ≤ N ≤ 1000), o número de comandos. A segunda linha tem N caracteres
(`E` ou `D`). A entrada termina com **N = 0**.

## Saída
Para cada caso, uma linha com a direção final: `N` (Norte), `L` (Leste),
`S` (Sul) ou `O` (Oeste).

## Raciocínio
- As direções em sentido horário são: N → L → S → O → N.
- Guardamos a posição atual numa lista `["N", "L", "S", "O"]`.
- `D` soma 1 e `E` subtrai 1 da posição; o `% 4` faz a volta completa.

## Como executar
Dentro desta pasta, em qualquer terminal (PowerShell, CMD ou Bash):
```
python esquerda_volver.py
```
O programa lê sozinho o `entrada.txt` desta pasta. O resultado deve ser
igual ao `saida.txt`.

Também funciona passando a entrada pelo terminal:
- CMD ou Bash: `python esquerda_volver.py < entrada.txt`
- PowerShell: `Get-Content entrada.txt | python esquerda_volver.py`
