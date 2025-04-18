# Trabalho Individual sobre Números Primos

Números inteiros maiores que um são ditos primos se seus únicos divisores são 1 e o próprio número. Em segurança computacional utilizamos números primos em várias algoritmos e protocolos. Para isso, é necessário manter-se uma tabela de números primos (uma lista pré computada) ou, gerar tais números quando necessário.

Não é simples a geração de números primos para uso em sistemas de segurança computacional. Normalmente, estamos interessados em números grandes, da ordem de grandeza de centenas de dígitos. No Brasil, por exemplo, para assinar documentos eletrônicos, você vai precisar ter chaves criptográficas geradas a partir de números primos de 2048 bits.

Uma forma de se gerar números primos é primeiro gerar um número aleatório ímpar (grande) e depois testá-lo para saber se é primo. Caso não seja, gera-se outro número aleatório até que seja primo.

Portanto, temos duas tarefas para fazer:

1. gerar números aleatórios;
2. testar se esse número gerado é primo.

Neste trabalho individual, vamos explorar técnicas para se gerar números pseudo-aleatórios e para se verificar a primalidade desses números.

**Atenção**: se julgar necessário, os professores podem convidar os alunos para apresentar o trabalho e a nota será dada com base no documento entregue e apresentação.

## 1) Quanto ao Entregável

Você deve entregar no Moodle um ÚNICO arquivo PDF com os seguinte requisitos:

1. Uma seção para Números Aleatórios com descrição e resultados obtidos;
2. Uma seção para Números Primos com descrição e resultados obtidos;
3. Os códigos devem estar no PDF (incluído no PDF) e devidamente documentados (comentados).Alternativamente, pode-se colar no PDF um link para o git com commit feito em data anterior ao deadline da entrega.
4. **Obrigatório: referências e citações a cada um dos algoritmos (livros, links, etc).Obs.: Trabalho sem citações e referências bibliográficas apropriadas não será corrigido.**

LEMBRE-SE: Entregue um único documento PDF, contendo o relatório desse trabalho individual ( incluindo os códigos dos programas, tabelas, saídas, … )

## 2) Gerar Números Pseudo-aleatórios

### Passo 1 - descrição e implementação

Você deve **escolher dois (2)** dos seguintes algoritmos geradores de números pseudo-aleatórios, **descrevê-los** **e implementá-los**. Na descrição do algoritmo, você vai explicar em texto o funcionamento do algoritmo, seguido de referências bibliográficas utilizadas.

- Blum Blum Shub
- Complementary-multiply-with-carry
- Inversive congruential generator
- ISAAC (cipher)
- Lagged Fibonacci generator
- Linear congruential generator
- Linear feedback shift register
- Maximal periodic reciprocals
- Mersenne twister
- Multiply-with-carry
- Naor-Reingold Pseudorandom Function
- Park–Miller random number generator
- Well Equidistributed Long-period Linear
- Xorshift

### Passo 2 - experimento

Você deve executar cada um dos algoritmos escolhidos para:

- Gerar números pseudo-aleatórios grandes. Entende-se como grande, números de até 4096 bits. Experimente gerar números da seguintes ordens de grandeza: 40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096 bits binários;
    - Caso não seja possível gerar números aleatórios de um determinado tamanho usando um dos algoritmos, você deve justificar;
    - O código implementado deve estar documentado. Dá-se preferência para documentar no próprio corpo do programa, na forma de comentários;
- Monte uma tabela explicitando o algoritmo, o tamanho do número e o tempo necessário para gerá-lo;
    - **Ideia**: gerar uma quantidade específica de números para cada tamanho e calcular o tempo médio de geração;
    - Exemplo de tabela:

| **Algoritmo** | **Tamanho do Número** | **Tempo para gerar** |
| --- | --- | --- |
| Blum blum Shib | 40 bits | 10 ms |
| ... | 56 bits | ... |
| ... | ... | ... |

### Passo 3 - análise

Compare os dois algoritmos escolhidos:

    - discuta o tempo de geração obtido em cada um deles e
    - faça uma análise de complexidade dos algoritmos para justificar o tempo.

## 3) Verificação de Primalidade

Miller-Rabin é um método clássico usado para se verificar se um número é ou não primo.

Neste trabalho individual você deve implementar o Miller-Rabin e algum outro método (da lista abaixo, ou ainda outro qualquer).

Sugestões de métodos de teste de primalidade em adição ao Miller-Rabin.

- Teste de Primalidade de Fermat
- Solovay-Strassem
- Frobenius

### Passo 1 descrição e implementação

**Descreva e implemente** os dois algoritmos. Justifique a escolha do segundo método. Na descrição do algoritmo, você vai explicar em texto o funcionamento do algoritmo, seguido de referências bibliográficas utilizadas.

- O código implementado deve estar documentado. Dá-se preferência para documentar no próprio corpo do programa, na forma de comentários;

### Passo 2 - experimento

Gere uma tabela com números primos de 40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048 e 4096 bits.

- Use como entrada os números aleatórios gerados no passo anterior. Se necessário, gere mais números ou use a estratégia de incrementar o número ímpar gerado.
- Escreva sobre as dificuldades encontradas e o tempo necessário em seu computador para gerar esses números;
- Provavelmente, você vai ter dificuldade em gerar números dessas ordens de grandeza. Procure gerar o máximo possível;
- Exemplo de tabela:

| **Algoritmo** | **Tamanho do Número** | **Número primo gerado** | **Tempo para gerar** |
| --- | --- | --- | --- |
| Miller Rabin | 40 bits | ... |  |
| ... | 56 bits | ... | ... |
| ... | ... | ... | ... |

### Passo 3 - análise

Compare os dois algoritmos:

- discuta o tempo de geração obtido e
- faça uma análise de complexidade dos algoritmos.
- **Ideia de análise**: será que os dois algoritmos implementados retornam a mesma resposta para a mesma entrada aleatória? Ou será que existem erros (um responde que é primo enquanto o outro responde que é composto)? Existem números pseudo-primos que falham alguns testes conhecidos, experimente rodar seus algoritmos com eles!