# Help!

## Descrição
Na maratona de programação, o time envia soluções e cada envio recebe o
julgamento `correct` (certo) ou `incorrect` (errado). Ajude a montar o placar
do time calculando:
- **S**: quantos problemas diferentes foram resolvidos (`correct`);
- **P**: a soma, para cada problema resolvido, do tempo do primeiro `correct`
  mais **20 minutos** de penalidade para cada `incorrect` recebido nesse
  problema.

Problemas que nunca foram resolvidos não somam penalidade.

## Entrada
Vários casos de teste. Cada caso começa com um inteiro **N** (1 ≤ N ≤ 300),
o número de envios. Cada uma das N linhas seguintes tem:
- a letra do problema (`A` a `Z`);
- o tempo **T** em minutos (0 ≤ T ≤ 300);
- o julgamento: `correct` ou `incorrect`.

Os envios estão em ordem crescente de tempo. A entrada termina com **N = 0**.

## Saída
Para cada caso, uma linha com os inteiros **S** e **P** separados por espaço.

## Raciocínio
- Um dicionário guarda quantos erros cada problema teve.
- Outro dicionário guarda o tempo em que cada problema foi resolvido.
- No final: S = quantidade de problemas resolvidos e
  P = soma de (tempo do acerto + 20 × erros) dos resolvidos.
- Exemplo: A certo em 100, B com 1 erro e certo em 111, C certo em 200
  → S = 3 e P = 100 + (111 + 20) + 200 = **431**.

## Como executar
Dentro desta pasta, em qualquer terminal (PowerShell, CMD ou Bash):
```
python help.py
```
O programa lê sozinho o `entrada.txt` desta pasta. O resultado deve ser
igual ao `saida.txt`.

Também funciona passando a entrada pelo terminal:
- CMD ou Bash: `python help.py < entrada.txt`
- PowerShell: `Get-Content entrada.txt | python help.py`
