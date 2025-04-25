# Introdução

O que sera feito nesse trabalho?

Solucoes escolhidas para serem desenvolvidas.

# Numeros aleatorios

## Xorshift

### Descrição

O algoritmo Xorshift é uma classe de geradores de números pseudoaleatórios (PRNGs) desenvolvida pelo matemático George Marsaglia e publicada em 2003 no Journal of Statistical Software. O Xorshift pertence à família dos registradores de deslocamento com retroalimentação linear (LFSRs), mas foi projetado para permitir implementações particularmente eficientes em software.

O princípio fundamental do Xorshift é a geração de números pseudoaleatórios através de uma sequência de operações bit a bit simples: o XOR (ou exclusivo) de um número com uma versão deslocada de si mesmo. Este processo é repetido algumas vezes em cada ciclo de geração.

A fórmula básica do algoritmo pode ser expressa da seguinte forma:
1. Inicia-se com um valor de estado inicial não-nulo x
2. Aplica-se x ⊕= x << a (desloca x à esquerda por a bits e faz XOR com o valor original)
3. Aplica-se x ⊕= x >> b (desloca x à direita por b bits e faz XOR com o valor resultante)
4. Aplica-se x ⊕= x << c (desloca x à esquerda por c bits e faz XOR com o valor resultante)
5. O resultado é o novo valor de x, que também se torna o estado para a próxima iteração

Os parâmetros a, b e c devem ser escolhidos cuidadosamente para garantir que o algoritmo atinja seu período máximo (2ⁿ-1, onde n é o tamanho do estado em bits). Existem versões de 32 bits, 64 bits e 128 bits, cada uma com períodos diferentes.

Uma característica notável do Xorshift é sua extrema eficiência em implementações de software modernas, exigindo apenas algumas operações de bits por número gerado. Isso o torna um dos PRNGs mais rápidos disponíveis, requerendo código mínimo e pouco estado interno.

Apesar de sua simplicidade, as versões básicas do Xorshift não passam em todos os testes estatísticos de aleatoriedade sem refinamentos adicionais. Para melhorar a qualidade estatística, variantes como Xorshift*, Xorshift+ e Xoroshiro foram desenvolvidas, adicionando operações não-lineares (como multiplicação ou adição) ao resultado final.

Na prática, o algoritmo Xorshift oferece um excelente equilíbrio entre velocidade, simplicidade de implementação e qualidade estatística suficiente para muitas aplicações, embora não seja adequado para uso criptográfico devido à sua natureza determinística e previsível quando o estado interno é conhecido.


### Implementação

### Experimento


| Algoritmo        | Tamanho do Número | Tempo para gerar (ms) |
|------------------|-------------------|----------------------|
| Xorshift32       | 40 bits           | 0.0011 ms            |
| Xorshift32       | 56 bits           | 0.0009 ms            |
| Xorshift32       | 80 bits           | 0.0013 ms            |
| Xorshift32       | 128 bits          | 0.0016 ms            |
| Xorshift32       | 168 bits          | 0.0024 ms            |
| Xorshift32       | 224 bits          | 0.0027 ms            |
| Xorshift32       | 256 bits          | 0.0031 ms            |
| Xorshift32       | 512 bits          | 0.0059 ms            |
| Xorshift32       | 1024 bits         | 0.0124 ms            |
| Xorshift32       | 2048 bits         | 0.0250 ms            |
| Xorshift32       | 4096 bits         | 0.0547 ms            |
| Xorshift64       | 40 bits           | 0.0005 ms            |
| Xorshift64       | 56 bits           | 0.0005 ms            |
| Xorshift64       | 80 bits           | 0.0008 ms            |
| Xorshift64       | 128 bits          | 0.0008 ms            |
| Xorshift64       | 168 bits          | 0.0011 ms            |
| Xorshift64       | 224 bits          | 0.0015 ms            |
| Xorshift64       | 256 bits          | 0.0015 ms            |
| Xorshift64       | 512 bits          | 0.0029 ms            |
| Xorshift64       | 1024 bits         | 0.0058 ms            |
| Xorshift64       | 2048 bits         | 0.0115 ms            |
| Xorshift64       | 4096 bits         | 0.0261 ms            |
| Xorshift128      | 40 bits           | 0.0011 ms            |
| Xorshift128      | 56 bits           | 0.0012 ms            |
| Xorshift128      | 80 bits           | 0.0016 ms            |
| Xorshift128      | 128 bits          | 0.0019 ms            |
| Xorshift128      | 168 bits          | 0.0028 ms            |
| Xorshift128      | 224 bits          | 0.0033 ms            |
| Xorshift128      | 256 bits          | 0.0040 ms            |
| Xorshift128      | 512 bits          | 0.0074 ms            |
| Xorshift128      | 1024 bits         | 0.0156 ms            |
| Xorshift128      | 2048 bits         | 0.0304 ms            |
| Xorshift128      | 4096 bits         | 0.0678 ms            |
| Xorshift128Plus  | 40 bits           | 0.0006 ms            |
| Xorshift128Plus  | 56 bits           | 0.0006 ms            |
| Xorshift128Plus  | 80 bits           | 0.0010 ms            |
| Xorshift128Plus  | 128 bits          | 0.0011 ms            |
| Xorshift128Plus  | 168 bits          | 0.0014 ms            |
| Xorshift128Plus  | 224 bits          | 0.0018 ms            |
| Xorshift128Plus  | 256 bits          | 0.0017 ms            |
| Xorshift128Plus  | 512 bits          | 0.0035 ms            |
| Xorshift128Plus  | 1024 bits         | 0.0062 ms            |
| Xorshift128Plus  | 2048 bits         | 0.0130 ms            |
| Xorshift128Plus  | 4096 bits         | 0.0290 ms            |

*Cada medição representa a média de 1000 execuções.*

## Blum Blum Shub

### Descrição

O algoritmo Blum Blum Shub (BBS) é um gerador de números pseudoaleatórios criptograficamente seguro proposto em 1986 por Lenore Blum, Manuel Blum e Michael Shub. Diferentemente de algoritmos como o Xorshift, o BBS foi projetado com foco primário em segurança criptográfica, sendo fundamentado em problemas matemáticos considerados computacionalmente difíceis.

A base matemática do BBS está na teoria dos resíduos quadráticos e na dificuldade do problema de fatoração de inteiros. O algoritmo funciona da seguinte forma:

1. Escolhem-se dois números primos grandes p e q, cada um congruente a 3 módulo 4 (ou seja, p ≡ q ≡ 3 (mod 4))
2. Calcula-se n = p × q, que é chamado de módulo de Blum
3. Seleciona-se um valor inicial (semente) s, tal que s seja co-primo com n (ou seja, mdc(s,n) = 1)
4. Gera-se a sequência de estados internos através da recorrência: x₁ = s² mod n, x₂ = x₁² mod n, x₃ = x₂² mod n, ...
5. Para cada estado xᵢ, extrai-se um ou mais bits de saída, tipicamente o bit menos significativo de cada xᵢ

A segurança do BBS deriva da dificuldade computacional de calcular raízes quadradas modulares sem conhecer os fatores de n. Sem o conhecimento de p e q, prever os próximos números na sequência é equivalente a resolver o problema de resíduo quadrático, que é considerado computacionalmente intratável para valores suficientemente grandes de n.

Principais características do BBS:
- É criptograficamente seguro sob a suposição de que o problema da fatoração de inteiros é difícil
- Possui uma prova matemática formal de segurança
- É significativamente mais lento que PRNGs não criptográficos como Xorshift
- Requer operações aritméticas de precisão arbitrária para módulos grandes
- Possui período potencialmente muito longo, dependendo da escolha de p, q e s

O BBS é principalmente utilizado em aplicações criptográficas onde a previsibilidade representa um risco de segurança, embora sua lentidão relativa o torne menos adequado para aplicações que demandam alta performance ou grandes volumes de números aleatórios.

### Implementação

### Experimento

Tempo médio para geração de números pseudoaleatórios de diferentes tamanhos usando o algoritmo Blum Blum Shub.

| Algoritmo      | Tamanho do Número   | Tempo para gerar (ms)   |
|----------------|---------------------|-------------------------|
| Blum Blum Shub | 40 bits             | 0.1566 ms               |
| Blum Blum Shub | 56 bits             | 0.2212 ms               |
| Blum Blum Shub | 80 bits             | 0.3244 ms               |
| Blum Blum Shub | 128 bits            | 0.5477 ms               |
| Blum Blum Shub | 168 bits            | 0.6986 ms               |
| Blum Blum Shub | 224 bits            | 0.9175 ms               |
| Blum Blum Shub | 256 bits            | 1.0078 ms               |
| Blum Blum Shub | 512 bits            | 2.0929 ms               |
| Blum Blum Shub | 1024 bits           | 4.1772 ms               |
| Blum Blum Shub | 2048 bits           | 8.6273 ms               |
| Blum Blum Shub | 4096 bits           | 17.3932 ms              |

*Cada medição representa a média de 10 execuções.*

## Análise

Foi interessante perceber a grande diferença, que era esperada, entre o resultado de geração de números pseudo-aleatórios ao utilizar os algoritmos de Xorshift e de Blum Blum Shub. Em média, o algoritmo Blum Blum Shub é aproximadamente 244 vezes mais lento que o Xorshift128 (o mais lento entre os Xorshifts). Entendemos que essa lentidão é decorrente da diferença de custo computacional das operações realizadas em cada um dos algoritmos, as operações do Xorshift são muito mais simples que as do Blum Blum Shub.

Também podemos avaliar essa diferença entre os algoritmos ao analisar a complexidade de cada um. O Xorshift possui uma complexidade temporal de O(1), pois independentemente do tamanho do número gerado, ele realiza apenas um número fixo de operações bit a bit (XOR e deslocamentos). Essas operações são extremamente eficientes em hardware moderno.

Por outro lado, o Blum Blum Shub possui uma complexidade temporal de O(k log n), onde k é o número de bits a serem gerados e n é o módulo utilizado no algoritmo. Cada bit gerado requer uma operação de quadrado modular, que é computacionalmente cara, especialmente para números grandes. Além disso, o BBS depende de operações aritméticas de precisão arbitrária, que são intrinsecamente mais lentas que as operações bit a bit utilizadas pelo Xorshift.

Esta diferença de complexidade explica claramente a discrepância de desempenho observada nos experimentos, onde o BBS se torna progressivamente mais lento à medida que o tamanho dos números aumenta.

# Numeros primos

## Teste de Primalidade de Fermat

### Descrição

O Teste de Primalidade de Fermat é um método probabilístico para determinar se um número é provavelmente primo. Baseado no Pequeno Teorema de Fermat, este teste foi desenvolvido no século XVII e é um dos testes de primalidade mais antigos e fundamentais.

O Pequeno Teorema de Fermat, que é a base matemática do teste, estabelece que:

Se p é um número primo e a é um inteiro não divisível por p, então:

a^(p-1) ≡ 1 (mod p)

Ou seja, quando elevamos qualquer número a à potência p-1 e dividimos o resultado por p, o resto será sempre 1, desde que a e p sejam coprimos (não compartilhem fatores comuns além de 1).

O teste funciona da seguinte forma:

1. Para verificar se um número n é primo, escolhemos aleatoriamente um valor de a tal que 1 < a < n-1.
2. Calculamos a^(n-1) mod n.
3. Se o resultado não for 1, então n é definitivamente composto (não primo).
4. Se o resultado for 1, então n é provavelmente primo, e a é chamado de "testemunha de Fermat" para a provável primalidade de n.

Para aumentar a confiança no resultado, o teste pode ser repetido com diferentes valores de a. Cada teste bem-sucedido aumenta a probabilidade de que n seja realmente primo, embora nunca forneça uma prova definitiva de primalidade.

Uma característica importante deste teste é que ele nunca produz falsos negativos - se o teste indica que um número é composto, então ele é definitivamente composto. No entanto, existem números compostos especiais, chamados "pseudoprimos de Fermat", que podem enganar o teste para bases específicas. Ainda mais problemáticos são os números de Carmichael, que são números compostos que passam no teste de Fermat para todas as bases a que são coprimas com n.

Apesar desta limitação, o Teste de Fermat é valorizado por sua simplicidade e eficiência computacional, especialmente para verificações iniciais rápidas. Ele frequentemente é usado como um pré-teste antes de aplicar métodos mais robustos como Miller-Rabin ou outros testes determinísticos mais complexos.

O algoritmo do teste pode ser descrito da seguinte forma:

**Entradas**: n (número a ser testado), k (número de iterações do teste)
**Saída**: "composto" ou "provavelmente primo"

1. Repita k vezes:
   a. Escolha um número aleatório a no intervalo [2, n-2]
   b. Se mdc(a, n) ≠ 1, retorne "composto"
   c. Se a^(n-1) mod n ≠ 1, retorne "composto"
2. Se após k iterações nenhum valor de a demonstrou que n é composto, retorne "provavelmente primo"

A complexidade computacional do teste é O(k log²n log log n), onde k é o número de testes realizados e n é o valor a ser verificado. Esta eficiência torna o teste de Fermat particularmente útil para números muito grandes, apesar de suas limitações inerentes.

### Implementação

### Experimento 1 - Tentativas limitadas por tentativas


Data/Hora: 2025-04-25 09:52:30

#### Resultados

| Algoritmo | Tamanho do Número | Tentativas | Tempo para gerar |
|-----------|------------------|------------|-------------------|
| Fermat Primality Test | 40 bits | 4 | 0.56 ms |
| Fermat Primality Test | 56 bits | 1 | 0.17 ms |
| Fermat Primality Test | 80 bits | 8 | 0.43 ms |
| Fermat Primality Test | 128 bits | 57 | 2.81 ms |
| Fermat Primality Test | 168 bits | 13 | 1.96 ms |
| Fermat Primality Test | 224 bits | 10 | 4.48 ms |
| Fermat Primality Test | 256 bits | 154 | 31.63 ms |
| Fermat Primality Test | 512 bits | 23 | 40.07 ms |
| Fermat Primality Test | 1024 bits | 374 | 2206.93 ms |
| Fermat Primality Test | 2048 bits | 100 | 3741.89 ms (falha) |
| Fermat Primality Test | 4096 bits | 100 | 29044.89 ms (falha) |


#### Observações

- Taxa de sucesso: 9/11 (81.8%)
- Tempo médio: 254.34 ms
- Tempo mínimo: 0.17 ms
- Tempo máximo: 2206.93 ms
- Tentativas médias: 71.56
- Tentativas mínimas: 1
- Tentativas máximas: 374

#### Relação entre tamanho e esforço

- À medida que o tamanho em bits aumenta, nota-se:
  - Para 40 bits: 4 tentativas, 0.56 ms
  - Para 1024 bits: 374 tentativas, 2206.93 ms
  - Aumento de tentativas: 93.50x
  - Aumento de tempo: 3940.95x

### Experimento 2 - Tentativas limitadas por tempo

Data/Hora: 2025-04-25 11:28:49

#### Resultados

| Algoritmo | Tamanho do Número | Tentativas | Tempo para gerar |
|-----------|------------------|------------|-------------------|
| Fermat Primality Test | 40 bits | 3 | 0.83 ms |
| Fermat Primality Test | 56 bits | 46 | 0.74 ms |
| Fermat Primality Test | 80 bits | 37 | 0.92 ms |
| Fermat Primality Test | 128 bits | 5 | 0.73 ms |
| Fermat Primality Test | 168 bits | 57 | 8.89 ms |
| Fermat Primality Test | 224 bits | 63 | 10.11 ms |
| Fermat Primality Test | 256 bits | 35 | 11.42 ms |
| Fermat Primality Test | 512 bits | 145 | 166.37 ms |
| Fermat Primality Test | 1024 bits | 128 | 792.42 ms |
| Fermat Primality Test | 2048 bits | 145 | 5343.09 ms |
| Fermat Primality Test | 4096 bits | 768 | 211568.14 ms |


#### Observações

- Taxa de sucesso: 11/11 (100.0%)
- Tempo médio: 19809.42 ms
- Tempo mínimo: 0.73 ms
- Tempo máximo: 211568.14 ms
- Tentativas médias: 130.18
- Tentativas mínimas: 3
- Tentativas máximas: 768

#### Relação entre tamanho e esforço

- À medida que o tamanho em bits aumenta, nota-se:
  - Para 40 bits: 3 tentativas, 0.83 ms
  - Para 4096 bits: 768 tentativas, 211568.14 ms
  - Aumento de tentativas: 256.00x
  - Aumento de tempo: 254901.37x

## Miller-Rabin

### Descrição

O Teste de Primalidade de Miller-Rabin é um algoritmo probabilístico amplamente utilizado para determinar se um número é provavelmente primo. Desenvolvido por Gary Miller e Michael Rabin na década de 1970, este teste é uma evolução do Teste de Fermat, oferecendo maior confiabilidade e menor probabilidade de falsos positivos.

A base matemática do teste Miller-Rabin está na teoria dos números e em propriedades específicas de números primos. Especificamente, o teste explora o fato de que, para números primos p, a equação x² ≡ 1 (mod p) tem exatamente duas soluções: x ≡ 1 (mod p) e x ≡ -1 (mod p). Para números compostos, podem existir outras soluções, conhecidas como "raízes quadradas não-triviais de 1".

O algoritmo funciona da seguinte forma:

1. Para um número ímpar n > 3 a ser testado, expressamos n-1 como 2^s * d, onde d é ímpar.
2. Escolhemos uma base a aleatória tal que 2 ≤ a ≤ n-2.
3. Calculamos x₀ = a^d mod n.
4. Se x₀ = 1 ou x₀ = n-1, então a é uma testemunha da provável primalidade de n.
5. Caso contrário, calculamos a sequência x₁ = x₀² mod n, x₂ = x₁² mod n, ..., x_{s-1} = x_{s-2}² mod n.
6. Se em algum momento encontrarmos x_i = n-1, então a é uma testemunha da provável primalidade.
7. Se chegarmos ao fim da sequência sem encontrar n-1, então a é uma testemunha da composição de n, provando definitivamente que n é composto.

O teste é repetido k vezes com diferentes bases a aleatórias. Se todas as bases testadas forem testemunhas da provável primalidade, declaramos n como "provavelmente primo". A probabilidade de um número composto ser incorretamente classificado como primo é no máximo 4^(-k), o que significa que cada iteração adicional reduz a probabilidade de erro por um fator de 4.

Uma característica fundamental do Miller-Rabin é que, diferentemente do Teste de Fermat, não existem números compostos que passem no teste para todas as bases possíveis. Para um número composto n, pelo menos 3/4 de todas as possíveis bases 2 ≤ a ≤ n-2 revelarão que n é composto. Esta propriedade elimina o problema dos números de Carmichael que afeta o teste de Fermat.

Além disso, existem versões determinísticas do teste Miller-Rabin para números de até um certo tamanho, usando um conjunto específico e limitado de bases. Por exemplo, para números de 64 bits, testar apenas as bases {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37} é suficiente para determinar com certeza absoluta se o número é primo.

A complexidade computacional do teste Miller-Rabin é O(k log³ n), onde k é o número de iterações e n é o número sendo testado. Esta eficiência, combinada com sua forte garantia probabilística, torna o Miller-Rabin o teste de primalidade mais utilizado em aplicações criptográficas modernas, incluindo geração de chaves para RSA, DSA e outros sistemas criptográficos.

O pseudocódigo do algoritmo pode ser descrito como:

```
Função Miller-Rabin(n, k):
    Se n = 2 ou n = 3, retorne "primo"
    Se n ≤ 1 ou n é par, retorne "composto"
    
    Escreva n-1 como 2^s * d, onde d é ímpar
    
    Para i de 1 até k:
        a ← número aleatório entre 2 e n-2
        x ← a^d mod n
        
        Se x = 1 ou x = n-1, continue com próxima iteração
        
        Para r de 1 até s-1:
            x ← x² mod n
            Se x = n-1, continue com próxima iteração de i
            Se x = 1, retorne "composto"
        
        Retorne "composto"
    
    Retorne "provavelmente primo"
```

A principal vantagem do Miller-Rabin sobre outros testes de primalidade é seu equilíbrio entre eficiência computacional e confiabilidade estatística, tornando-o ideal para sistemas criptográficos que dependem da geração rápida de números primos grandes.

### Implementação

### Experimento

Data/Hora: 2025-04-25 10:47:04

#### Resultados

| Algoritmo | Tamanho do Número | Tentativas | Tempo para gerar |
|-----------|-------------------|------------|-------------------|
| Miller-Rabin | 40 bits | 1 | 0.03 ms |
| Miller-Rabin | 56 bits | 70 | 0.56 ms |
| Miller-Rabin | 80 bits | 4 | 0.56 ms |
| Miller-Rabin | 128 bits | 15 | 1.67 ms |
| Miller-Rabin | 168 bits | 129 | 8.60 ms |
| Miller-Rabin | 224 bits | 150 | 19.00 ms |
| Miller-Rabin | 256 bits | 46 | 11.76 ms |
| Miller-Rabin | 512 bits | 128 | 158.37 ms |
| Miller-Rabin | 1024 bits | 844 | 4530.48 ms |
| Miller-Rabin | 2048 bits | 297 | 11650.23 ms |
| Miller-Rabin | 4096 bits | 2356 | 633614.98 ms |


#### Observações

- Taxa de sucesso: 11/11 (100.0%)
- Tempo médio: 59090.57 ms
- Tempo mínimo: 0.03 ms
- Tempo máximo: 633614.98 ms
- Tentativas médias: 367.27
- Tentativas mínimas: 1
- Tentativas máximas: 2356

#### Relação entre tamanho e esforço

- À medida que o tamanho em bits aumenta, nota-se:
  - Para 40 bits: 1 tentativas, 0.03 ms
  - Para 4096 bits: 2356 tentativas, 633614.98 ms
  - Aumento de tentativas: 2356.00x
  - Aumento de tempo: 19981758.38x

## Análise

Ao comparar o Teste de Primalidade de Fermat e o Teste de Miller-Rabin, podemos observar características importantes em termos de eficiência, precisão e aplicabilidade prática.

Foi decidido implementar o teste de Fermat como complemento ao Miller-Rabin devido à relação evolutiva entre eles. O teste de Fermat constitui a base histórica e conceitual para o teste de Miller-Rabin, permitindo uma análise comparativa que evidencia por que o segundo tornou-se o padrão em aplicações criptográficas modernas.

A diferença fundamental entre os dois algoritmos está na forma como lidam com casos especiais. O teste de Fermat sofre de uma limitação crítica: os números de Carmichael (como 561, 1105, 1729), que são números compostos que passam no teste para todas as bases coprimas, resultando em falsos positivos. Este problema impossibilita seu uso isolado em aplicações de segurança.

Miller-Rabin, por outro lado, refina o teste ao adicionar verificações para raízes quadradas não-triviais de 1, eliminando o problema dos números de Carmichael. Para qualquer número composto n, pelo menos 3/4 de todas as possíveis bases revelarão sua composição, garantindo uma probabilidade de erro que decresce exponencialmente com o número de iterações (4^(-k)).

Analisando os experimentos realizados, observamos padrões importantes. Ambos os algoritmos apresentam aumento significativo no tempo de execução conforme o tamanho do número cresce. Para números de 4096 bits, o Miller-Rabin apresentou um aumento de aproximadamente 20 milhões de vezes no tempo em relação a números de 40 bits, enquanto o Fermat apresentou um aumento de cerca de 255 mil vezes.

Em termos de complexidade, o teste de Fermat tem complexidade O(k × log²n log log n), onde k é o número de iterações e n o número testado. Já o Miller-Rabin apresenta complexidade O(k × log³n). A complexidade adicional do Miller-Rabin justifica-se pela verificação mais rigorosa que realiza, executando múltiplas verificações de quadrados modulares ao longo do processo.

Quanto ao número de tentativas, o Miller-Rabin geralmente necessitou mais tentativas para encontrar números primos (média de 367.27 tentativas contra 130.18 do Fermat no segundo experimento). Para 4096 bits, Miller-Rabin necessitou 2356 tentativas contra 768 do Fermat.

Um aspecto importante observado em ambos os algoritmos é a variabilidade do tempo de execução mesmo para números do mesmo tamanho. Isso ocorre porque o tempo depende não apenas do tamanho do número, mas também de suas propriedades matemáticas específicas. A natureza probabilística dos testes significa que alguns números são confirmados como primos mais rapidamente que outros. Além disso, a aleatoriedade na escolha das bases testemunhas influencia significativamente o desempenho. Esta variabilidade reforça a necessidade de múltiplas execuções para obter resultados estatisticamente significativos, como foi feito nos experimentos.

Embora o teste de Fermat seja computacionalmente mais eficiente para números muito grandes (como demonstrado no tempo médio de 19809.42 ms contra 59090.57 ms do Miller-Rabin), sua suscetibilidade a falsos positivos o torna inadequado para aplicações criptográficas críticas, onde a certeza da primalidade é essencial.

Miller-Rabin, apesar do maior custo computacional, oferece garantias probabilísticas muito mais robustas, tornando-o preferível para geração de chaves em criptografia assimétrica (RSA, DSA), sistemas de assinatura digital e protocolos que dependem da dificuldade da fatoração de números compostos.

Por fim, observamos que ambos os algoritmos conseguiram gerar com sucesso números primos de até 4096 bits, tamanho suficiente para aplicações criptográficas modernas, embora com tempos significativamente diferentes.

Esta análise comparativa demonstra que, apesar da eficiência computacional do teste de Fermat, o teste de Miller-Rabin representa um avanço fundamental na verificação de primalidade, equilibrando de forma mais adequada eficiência e confiabilidade para aplicações de segurança computacional.

# Conclusão

# Referências

## Xorshift

1. Marsaglia, G. (2003). "Xorshift RNGs". *Journal of Statistical Software*, 8(14), 1-6. https://doi.org/10.18637/jss.v008.i14

2. Brent, R. P. (2004). "Note on Marsaglia's Xorshift Random Number Generators". *Journal of Statistical Software*, 11(5). https://doi.org/10.18637/jss.v011.i05

3. Panneton, F., & L'Ecuyer, P. (2005). "On the xorshift random number generators". *ACM Transactions on Modeling and Computer Simulation*, 15(4), 346-361. https://doi.org/10.1145/1113316.1113319

4. Vigna, S. (2016). "An experimental exploration of Marsaglia's xorshift generators, scrambled". *ACM Transactions on Mathematical Software*, 42(4), 30. https://doi.org/10.1145/2845077

5. Blackman, D., & Vigna, S. (2018). "Scrambled Linear Pseudorandom Number Generators". *arXiv preprint* arXiv:1805.01407.

## Blum Blum Shub

1. Blum, L., Blum, M., & Shub, M. (1986). "A Simple Unpredictable Pseudo-Random Number Generator". *SIAM Journal on Computing*, 15(2), 364–383. https://doi.org/10.1137/0215025

2. Sidorenko, A., & Schoenmakers, B. (2005). "Concrete Security of the Blum-Blum-Shub Pseudorandom Generator". *Cryptography and Coding*, 355-375.

3. Vassilev, A., & Staples, R. (2016). "Entropy as a Service: Unlocking Cryptography's Full Potential". *Computer*, 49(9), 98-102. https://doi.org/10.1109/MC.2016.275

4. Koblitz, N. & Menezes, A. (2015). "A riddle wrapped in an enigma". *IEEE Security & Privacy*, 13(6), 34-42. https://doi.org/10.1109/MSP.2015.132

5. Menezes, A. J., Vanstone, S. A., & Oorschot, P. C. V. (1996). "Handbook of Applied Cryptography". CRC Press. (Chapter 5: Pseudorandom Bits and Sequences)

## Teste de Primalidade de Fermat

1. Pomerance, C., Selfridge, J. L., & Wagstaff, S. S. (1980). "The Pseudoprimes to 25·10^9". *Mathematics of Computation*, 35(151), 1003-1026. https://doi.org/10.1090/S0025-5718-1980-0572872-7

2. Cohen, H. (1993). "A Course in Computational Algebraic Number Theory". Springer-Verlag. (Chapter 8: Primality Testing)

3. Ribenboim, P. (1995). "The New Book of Prime Number Records". Springer-Verlag. (Capítulo 2: Testes de Primalidade)

4. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). "Introduction to Algorithms" (3ª ed.). MIT Press. (Seção 31.8: Testes de Primalidade)

5. Alford, W. R., Granville, A., & Pomerance, C. (1994). "There are Infinitely Many Carmichael Numbers". *Annals of Mathematics*, 140(3), 703-722. https://doi.org/10.2307/2118576

6. Pinch, R. G. E. (1993). "The Carmichael Numbers up to 10^16". *Mathematics of Computation*, 61(203), 381-391. https://doi.org/10.1090/S0025-5718-1993-1137272-X

## Miller-Rabin

1. Rabin, M. O. (1980). "Probabilistic algorithm for testing primality". *Journal of Number Theory*, 12(1), 128-138. https://doi.org/10.1016/0022-314X(80)90084-0

2. Miller, G. L. (1976). "Riemann's Hypothesis and Tests for Primality". *Journal of Computer and System Sciences*, 13(3), 300-317. https://doi.org/10.1016/S0022-0000(76)80043-8

3. Crandall, R., & Pomerance, C. (2005). "Prime Numbers: A Computational Perspective" (2nd ed.). Springer. (Chapter 3: Recognizing Primes and Composites)

4. Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). "Handbook of Applied Cryptography". CRC Press. (Chapter 4: Primality Testing)

5. Yan, S. Y. (2009). "Primality Testing and Integer Factorization in Public-Key Cryptography" (3rd ed.). Springer. (Chapter 5: Probabilistic Primality Tests)

6. Shoup, V. (2009). "A Computational Introduction to Number Theory and Algebra" (2nd ed.). Cambridge University Press. (Section 11.5: The Miller-Rabin test)

# Anexos

## Codigo do Xorshift

```python

```

## Codigo do Blum Blum Shub

```python

```


## Codigo do Miller-Rabin

```python

```

## Codigo do Teste de Primalidade de Fermat

```python

```


