# Xorshift

### Referência 1: Marsaglia, G. (2003)
- Parágrafo 1: Informação sobre o desenvolvedor (George Marsaglia) e a publicação original em 2003
- Parágrafos 3-4: A fórmula básica do algoritmo e os passos de implementação
- Parágrafo 5: Conceito do período máximo (2ⁿ-1)
- Parágrafo 6: Eficiência do algoritmo em implementações de software

### Referência 2: Brent, R. P. (2004)
- Parágrafo 1: Classificação do Xorshift como parte da família LFSR
- Parágrafo 5: Informações complementares sobre a escolha cuidadosa dos parâmetros a, b e c

### Referência 3: Panneton, F., & L'Ecuyer, P. (2005)
- Parágrafo 7: Discussão sobre as falhas nos testes estatísticos de aleatoriedade
- Parágrafo 8: Menção à inadequação para uso criptográfico

### Referência 4: Vigna, S. (2016)
- Parágrafo 7: Informações sobre a variante Xorshift* e a adição de operações não-lineares
- Parágrafo 8: Análise do equilíbrio entre velocidade e qualidade estatística

### Referência 5: Blackman, D., & Vigna, S. (2018)
- Parágrafo 7: Informações sobre as variantes mais recentes Xorshift+ e Xoroshiro
- Parágrafo 8: Discussões sobre aplicações práticas das versões mais modernas do algoritmo

## Blum Blum Shub

### Referência 1: Blum, L., Blum, M., & Shub, M. (1986)
- Parágrafo 1: Informação histórica sobre a criação do algoritmo em 1986
- Parágrafo 2-3: Descrição dos passos fundamentais do algoritmo (pontos 1-5)
- Parágrafo 4: Característica de segurança criptográfica e prova matemática formal

### Referência 2: Sidorenko, A., & Schoenmakers, B. (2005)
- Parágrafo 4: Análise da segurança baseada no problema de resíduo quadrático
- Parágrafo 5: Característica de segurança criptográfica sob a suposição do problema de fatoração

### Referência 3: Vassilev, A., & Staples, R. (2016)
- Parágrafo 5: Características sobre a eficiência computacional (lentidão relativa)
- Parágrafo 6: Discussão sobre aplicações práticas em segurança

### Referência 4: Koblitz, N. & Menezes, A. (2015)
- Parágrafo 4: Relação com problemas computacionais intratáveis
- Parágrafo 6: Limitações práticas em aplicações de alta performance

### Referência 5: Menezes, A. J., Vanstone, S. A., & Oorschot, P. C. V. (1996)
- Parágrafo 2: Base matemática em resíduos quadráticos
- Parágrafo 5: Características técnicas sobre operações aritméticas de precisão arbitrária
- Parágrafo 5: Informações sobre o período do gerador

## Teste de Primalidade de Fermat

### Referência 1: Pomerance, C., Selfridge, J. L., & Wagstaff, S. S. (1980)
- Parágrafo 6: Informação sobre a raridade dos pseudoprimos (1,091,987,405 primos versus 21,853 pseudoprimos base dois)
- Parágrafo 7: Conceito de "industrial grade primes" mencionado por Cohen

### Referência 2: Cohen, H. (1993)
- Parágrafo 3-5: Formalização matemática do teste baseada no Pequeno Teorema de Fermat
- Parágrafo 12-14: Descrição do algoritmo e sua implementação

### Referência 3: Ribenboim, P. (1995)
- Parágrafo 6: Referências históricas, incluindo o pseudoprimo par de Lehmer
- Parágrafo 8: Informações sobre a evolução dos testes de primalidade

### Referência 4: Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009)
- Parágrafo 12-14: Análise da complexidade computacional O(k log²n log log n)
- Parágrafo 15: Aplicações práticas do teste em sistemas modernos

### Referência 5: Alford, W. R., Granville, A., & Pomerance, C. (1994)
- Parágrafo 8-9: Discussão sobre números de Carmichael e a prova de que existem infinitos deles
- Parágrafo 10: Impacto dessas limitações na confiabilidade do teste

### Referência 6: Pinch, R. G. E. (1993)
- Parágrafo 9: Lista dos números de Carmichael menores que 100.000
- Parágrafo 10: Referência aos trabalhos catalográficos sobre pseudoprimos e números de Carmichael

## Miller-Rabin

### Referência 1: Rabin, M. O. (1980)
- Parágrafo 1: Informação histórica sobre o desenvolvimento do algoritmo por Michael Rabin na década de 1970
- Parágrafo 8: Análise probabilística do erro (4^(-k)) e garantias estatísticas do algoritmo
- Parágrafo 11: Aplicações em criptografia moderna

### Referência 2: Miller, G. L. (1976)
- Parágrafo 1: Informação histórica sobre o desenvolvimento inicial por Gary Miller
- Parágrafo 2-3: Base matemática relacionada às propriedades das raízes quadradas módulo um número primo
- Parágrafo 5-7: Descrição das etapas fundamentais do algoritmo

### Referência 3: Crandall, R., & Pomerance, C. (2005)
- Parágrafo 9: Análise da proporção de bases que revelam composição (pelo menos 3/4)
- Parágrafo 10: Informações sobre variantes determinísticas do teste para números de até certo tamanho
- Parágrafo 11: Análise da complexidade computacional O(k log³ n)

### Referência 4: Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996)
- Parágrafo 10: Detalhes sobre conjuntos específicos de bases para versões determinísticas
- Parágrafo 11: Aplicações em sistemas criptográficos como RSA e DSA
- Parágrafo 15: Análise comparativa com outros testes de primalidade

### Referência 5: Yan, S. Y. (2009)
- Parágrafo 8: Explicação detalhada sobre a garantia de erro (4^(-k))
- Parágrafo 9: Comparação com o teste de Fermat e limitações dos números de Carmichael
- Parágrafo 14: Aspectos da implementação prática do algoritmo

### Referência 6: Shoup, V. (2009)
- Parágrafo 2-3: Formalização matemática das propriedades de números primos relacionadas às raízes quadradas de 1
- Parágrafo 12-14: Detalhes do pseudocódigo e sua implementação
- Parágrafo 15: Análise do equilíbrio entre eficiência computacional e confiabilidade estatística
