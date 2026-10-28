# Fechem as portas!

## Descrição
Uma mansão tem **N** quartos, numerados de 1 a N, todos com a porta fechada.
N descendentes entram na mansão, um de cada vez. O descendente de número **i**
troca o estado (abre se estiver fechada, fecha se estiver aberta) de todas as
portas cujo número é múltiplo de **i**.

Depois que todos passarem, quais portas ficam abertas?

## Entrada
Vários casos de teste. Cada caso é uma linha com um inteiro **N**.
A entrada termina com **N = 0**.

## Saída
Para cada caso, uma linha com os números das portas abertas, em ordem
crescente e separados por espaço.

## Raciocínio
- A porta **k** é trocada uma vez para cada divisor de k.
- Ela termina aberta só se for trocada um número **ímpar** de vezes.
- Os divisores aparecem em pares (ex.: 12 → 1×12, 2×6, 3×4), menos nos
  **quadrados perfeitos**, em que um divisor se repete (ex.: 16 → 4×4).
- Logo, as portas abertas são 1, 4, 9, 16, 25, ... até N.

## Como executar
Dentro desta pasta, em qualquer terminal (PowerShell, CMD ou Bash):
```
python fechem_as_portas.py
```
O programa lê sozinho o `entrada.txt` desta pasta. O resultado deve ser
igual ao `saida.txt`.

Também funciona passando a entrada pelo terminal:
- CMD ou Bash: `python fechem_as_portas.py < entrada.txt`
- PowerShell: `Get-Content entrada.txt | python fechem_as_portas.py`
