#!/usr/bin/env python3
"""
Implementação do Teste de Primalidade de Miller-Rabin

Este módulo implementa o algoritmo de teste de primalidade Miller-Rabin,
um algoritmo probabilístico eficiente para determinar se um número é provavelmente primo.

Autor: João Pedro Schmidt Cordeiro
Data: Abril 2024
"""

import random
import time
from typing import Tuple, List


def decompose(n: int) -> Tuple[int, int]:
    """
    Decompõe n-1 como (2^s) * d, onde d é ímpar.
    
    Args:
        n: O número a ser decomposto (n-1)
    
    Returns:
        Uma tupla (s, d) onde s e d satisfazem n-1 = (2^s) * d e d é ímpar
    """
    n_minus_1 = n - 1
    s = 0
    d = n_minus_1
    
    # Enquanto d for par, divide por 2 e incrementa s
    while d % 2 == 0:
        d //= 2
        s += 1
    
    return s, d


def miller_rabin_round(n: int, a: int) -> bool:
    """
    Executa uma rodada do teste de Miller-Rabin com a base 'a'.
    
    Args:
        n: O número a ser testado para primalidade
        a: A base para o teste (2 <= a <= n-2)
    
    Returns:
        True se n passa no teste para a base a, False caso contrário
    """
    if n == a:
        return True
    
    if n % a == 0:
        return False
    
    # Decompõe n-1 como 2^s * d
    s, d = decompose(n)
    
    # Calcula x = a^d mod n
    x = pow(a, d, n)
    
    # Se x == 1 ou x == n-1, n passa no teste para essa base
    if x == 1 or x == n - 1:
        return True
    
    # Calcula x = x^2 mod n para s-1 iterações
    for _ in range(s - 1):
        x = pow(x, 2, n)
        # Se x == n-1, n passa no teste para essa base
        if x == n - 1:
            return True
        # Se x == 1, encontramos uma raiz quadrada não-trivial de 1, então n é composto
        if x == 1:
            return False
    
    # Se chegamos aqui, n é composto para esta base
    return False


def is_prime_miller_rabin(n: int, k: int = 40) -> bool:
    """
    Determina se n é provavelmente primo usando o teste de Miller-Rabin.
    
    Args:
        n: O número a ser testado
        k: O número de rodadas/bases a serem testadas (padrão: 40)
           Quanto maior o valor de k, menor a probabilidade de erro
    
    Returns:
        True se n é provavelmente primo, False se n é definitivamente composto
    """
    # Casos triviais
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    # Para números pequenos, podemos usar um conjunto fixo de bases
    # que garantem determinismo até certo limite
    # Recomendação de Menezes, van Oorschot e Vanstone (1996)
    if n < 1_373_653:
        # Para n < 1,373,653, é suficiente testar as bases 2, 3
        bases_deterministic = [2, 3]
    elif n < 9_080_191:
        # Para n < 9,080,191, é suficiente testar as bases 31, 73
        bases_deterministic = [31, 73]
    elif n < 25_326_001:
        # Para n < 25,326,001, é suficiente testar as bases 2, 3, 5
        bases_deterministic = [2, 3, 5]
    elif n < 3_215_031_751:
        # Para n < 3,215,031,751, é suficiente testar as bases 2, 3, 5, 7
        bases_deterministic = [2, 3, 5, 7]
    elif n < 4_759_123_141:
        # Para n < 4,759,123,141, é suficiente testar as bases 2, 7, 61
        bases_deterministic = [2, 7, 61]
    elif n < 1_122_004_669_633:
        # Para n < 1,122,004,669,633, é suficiente testar as bases 2, 13, 23, 1662803
        bases_deterministic = [2, 13, 23, 1662803]
    elif n < 2_152_302_898_747:
        # Para n < 2,152,302,898,747, é suficiente testar as bases 2, 3, 5, 7, 11
        bases_deterministic = [2, 3, 5, 7, 11]
    elif n < 3_474_749_660_383:
        # Para n < 3,474,749,660,383, é suficiente testar as bases 2, 3, 5, 7, 11, 13
        bases_deterministic = [2, 3, 5, 7, 11, 13]
    elif n < 341_550_071_728_321:
        # Para n < 341,550,071,728,321, é suficiente testar as bases 2, 3, 5, 7, 11, 13, 17
        bases_deterministic = [2, 3, 5, 7, 11, 13, 17]
    elif n < 2**64:
        # Para n < 2^64, é suficiente testar as bases 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37
        # Conforme provado por Pomerance, Selfridge e Wagstaff e ampliado por Jaeschke
        bases_deterministic = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    else:
        # Para números maiores, usamos bases aleatórias
        for _ in range(k):
            a = random.randint(2, n - 2)
            if not miller_rabin_round(n, a):
                return False
        return True
    
    # Teste com as bases determinísticas selecionadas
    for a in bases_deterministic:
        if a >= n:
            break
        if not miller_rabin_round(n, a):
            return False
    
    # Se todas as k bases passaram no teste, n é provavelmente primo
    return True


def generate_probable_prime(bits: int, k: int = 40) -> int:
    """
    Gera um número provavelmente primo com o número especificado de bits.
    
    Args:
        bits: Número de bits do primo a ser gerado
        k: Número de rodadas no teste de Miller-Rabin (padrão: 40)
    
    Returns:
        Um número provavelmente primo com o número especificado de bits
    """
    while True:
        # Gera um número aleatório com o número especificado de bits
        # Garante que o número é ímpar e tem exatamente o número de bits solicitado
        n = random.getrandbits(bits)
        n |= (1 << (bits - 1)) | 1  # Garante que o bit mais significativo é 1 e que é ímpar
        
        if is_prime_miller_rabin(n, k):
            return n
