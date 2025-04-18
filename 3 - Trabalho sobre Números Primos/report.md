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

# Numeros primos

## Teste de Primalidade de Fermat

### Descrição

### Implementação

### Experimento

## Miller-Rabin

### Descrição

### Implementação

### Experimento

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


