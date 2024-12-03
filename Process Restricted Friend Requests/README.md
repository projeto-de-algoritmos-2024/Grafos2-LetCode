# [2076. Processar solicitações de amizade restritas](https://leetcode.com/problems/process-restricted-friend-requests/description/) 

Você recebe um inteiro `n` indicando o número de pessoas em uma rede. Cada pessoa é rotulada de `0` a `n - 1`.

Você também recebe uma matriz de inteiros 2D indexada em 0, `restrictions`, onde `restrictions[i] = [xi, yi]` significa que a pessoa `xi` e a pessoa `yi` **não podem** se tornar amigas, seja diretamente ou indiretamente por meio de outras pessoas.

Inicialmente, ninguém é amigo de ninguém. Você recebe uma lista de solicitações de amizade como um array de inteiros 2D indexado em 0, `requests`, onde `requests[j] = [uj, vj]` é uma solicitação de amizade entre a pessoa `uj` e a pessoa `vj`.

Uma solicitação de amizade é bem-sucedida se `uj` e `vj` podem se tornar amigos. Cada solicitação de amizade é processada na ordem dada (ou seja, `requests[j]` ocorre antes de `requests[j + 1]`), e, quando uma solicitação é bem-sucedida, `uj` e `vj` se tornam amigos diretos para todas as futuras solicitações de amizade.

Retorne um array booleano `result`, onde `result[j]` indica `true` se a solicitação de amizade foi bem-sucedida ou `false` caso contrário.

**Observação**: Se `uj` e `vj` já forem amigos diretos, a solicitação de amizade ainda será bem-sucedida.


## Exemplos

### Exemplo 1:

**Entrada**: 
- `n = 3`
- `restrições = [[0, 1]]`
- `solicitações = [[0, 2], [2, 1]]`

**Saída**: 
- `[verdadeiro, falso]`

**Explicação**:
- **Solicitação 0**: A pessoa 0 e a pessoa 2 podem ser amigas, então elas se tornam amigas diretas.
- **Solicitação 1**: A pessoa 2 e a pessoa 1 não podem ser amigas, pois a pessoa 0 e a pessoa 1 seriam amigas indiretas (`1--2--0`).

### Exemplo 2:

**Entrada**:
- `n = 3`
- `restrições = [[0, 1]]`
- `solicitações = [[1, 2], [0, 2]]`

**Saída**:
- `[verdadeiro, falso]`

**Explicação**:
- **Solicitação 0**: A pessoa 1 e a pessoa 2 podem ser amigas, então elas se tornam amigas diretas.
- **Solicitação 1**: A pessoa 0 e a pessoa 2 não podem ser amigas, pois a pessoa 0 e a pessoa 1 seriam amigas indiretas (`0--2--1`).

### Exemplo 3:

**Entrada**:
- `n = 5`
- `restrições = [[0, 1], [1, 2], [2, 3]]`
- `solicitações = [[0, 4], [1, 2], [3, 1], [3, 4]]`

**Saída**:
- `[verdadeiro, falso, verdadeiro, falso]`

**Explicação**:
- **Solicitação 0**: A pessoa 0 e a pessoa 4 podem ser amigas, então elas se tornam amigas diretas.
- **Solicitação 1**: A pessoa 1 e a pessoa 2 não podem ser amigas, pois estão diretamente restritas.
- **Solicitação 2**: A pessoa 3 e a pessoa 1 podem ser amigas, então elas se tornam amigas diretas.
- **Solicitação 3**: A pessoa 3 e a pessoa 4 não podem ser amigas, pois a pessoa 0 e a pessoa 1 seriam amigas indiretas (`0--4--3--1`).

## Restrições

- `2 <= n <= 1000`
- `0 <= restrictions.length <= 1000`
- `restrictions[i].length == 2`
- `0 <= xi, yi <= n - 1`
- `xi != yi`
- `1 <= requests.length <= 1000`
- `requests[j].length == 2`
- `0 <= uj, vj <= n - 1`
- `uj != vj`
****