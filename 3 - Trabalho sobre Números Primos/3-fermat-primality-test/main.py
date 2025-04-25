#!/usr/bin/env python3
"""
Implementação do Teste de Primalidade de Fermat

Este algoritmo implementa o Teste de Primalidade de Fermat, um teste probabilístico
que verifica se um número é provavelmente primo baseado no Pequeno Teorema de Fermat.
"""

import random
import time
from typing import Tuple


def gcd(a: int, b: int) -> int:
    """
    Calcula o Máximo Divisor Comum (MDC) entre dois números usando o algoritmo de Euclides.
    
    Args:
        a: Primeiro número
        b: Segundo número
        
    Returns:
        O MDC entre a e b
    """
    while b:
        a, b = b, a % b
    return a


def power_mod(base: int, exponent: int, modulus: int) -> int:
    """
    Calcula (base^exponent) % modulus de forma eficiente usando exponenciação modular rápida.
    
    Args:
        base: A base
        exponent: O expoente
        modulus: O módulo
        
    Returns:
        (base^exponent) % modulus
    """
    result = 1
    base = base % modulus
    
    while exponent > 0:
        # Se o bit menos significativo é 1, multiplique pelo atual resultado
        if exponent & 1:
            result = (result * base) % modulus
            
        # Expoente é reduzido pela metade
        exponent >>= 1
        
        # Base é elevada ao quadrado
        base = (base * base) % modulus
        
    return result


def fermat_primality_test(n: int, k: int = 5) -> Tuple[bool, list]:
    """
    Executa o teste de primalidade de Fermat em um número dado.
    
    Args:
        n: O número a ser testado
        k: Número de iterações (maior k = maior confiabilidade)
        
    Returns:
        (Resultado, Testemunhas):
            - Resultado: True se n for provavelmente primo, False se for definitivamente composto
            - Testemunhas: Lista contendo as testemunhas de Fermat (se composto) ou as bases testadas (se primo)
    """
    # Casos especiais
    if n <= 1:
        return False, []
    if n <= 3:
        return True, []
    if n % 2 == 0:
        return False, [2]  # 2 é uma testemunha para números pares > 2
    
    witnesses = []
    
    # Executar k testes
    for _ in range(k):
        # Escolher base aleatória entre 2 e n-2
        a = random.randint(2, n-2)
        
        # Verificar se a e n são coprimos
        if gcd(a, n) != 1:
            return False, [a]  # Encontramos um fator de n
        
        # Verificar a congruência de Fermat
        if power_mod(a, n-1, n) != 1:
            return False, [a]  # a é uma testemunha de Fermat para a composição de n
        
        witnesses.append(a)
    
    # Se chegamos aqui, n passou em todos os k testes
    return True, witnesses


if __name__ == "__main__":
    print("Teste de Primalidade de Fermat")
    print("==============================")
    print("\nEste programa implementa o Teste de Primalidade de Fermat.")
    print("Para realizar experimentos completos, execute o arquivo test.py.")
    
    try:
        while True:
            try:
                n = int(input("\nDigite um número para testar (ou 0 para sair): "))
                if n == 0:
                    break
                    
                if n < 2:
                    print("Por favor, digite um número inteiro maior que 1.")
                    continue
                    
                k = int(input("Digite o número de iterações (recomendado ≥ 5): "))
                if k < 1:
                    print("O número de iterações deve ser pelo menos 1.")
                    continue
                
                start_time = time.time()
                is_probable_prime, witnesses = fermat_primality_test(n, k)
                end_time = time.time()
                execution_time = (end_time - start_time) * 1000
                
                print("\n" + "="*50)
                if is_probable_prime:
                    print(f"{n} é provavelmente primo.")
                    print(f"Bases testadas: {witnesses}")
                    print("\nNOTA: Este é um teste probabilístico e não uma prova definitiva.")
                else:
                    print(f"{n} é definitivamente composto (não primo).")
                    print(f"Testemunha de Fermat: {witnesses[0]}")
                    
                    if gcd(witnesses[0], n) != 1:
                        factor = gcd(witnesses[0], n)
                        print(f"Fator encontrado: {factor} (n = {factor} × {n//factor})")
                
                print(f"Tempo de execução: {execution_time:.6f} ms")
                print("="*50)
                
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")
    
    except KeyboardInterrupt:
        print("\n\nOperação interrompida pelo usuário.")
        
    print("\nObrigado por usar o programa de Teste de Primalidade de Fermat!")
