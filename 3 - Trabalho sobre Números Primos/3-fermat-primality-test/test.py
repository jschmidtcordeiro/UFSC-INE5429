#!/usr/bin/env python3
"""
Experimento de Geração de Números Primos com o Teste de Primalidade de Fermat

Este script realiza um experimento para gerar números primos de diferentes tamanhos
(40 a 4096 bits) e mede o tempo necessário para encontrar cada primo.
"""

import random
import time
import sys
from typing import Tuple, List, Dict
import os
import json
from datetime import datetime

# Importa as funções do código principal
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from main import fermat_primality_test, power_mod, gcd


def generate_random_bits(bits: int) -> int:
    """
    Gera um número aleatório com o número especificado de bits.
    
    Args:
        bits: Número de bits do número a ser gerado
        
    Returns:
        Um número aleatório com o número especificado de bits
    """
    # Gera um número entre 2^(bits-1) e 2^bits - 1
    return random.randint(2 ** (bits - 1), 2 ** bits - 1)


def generate_random_odd(bits: int) -> int:
    """
    Gera um número ímpar aleatório com o número especificado de bits.
    
    Args:
        bits: Número de bits do número a ser gerado
        
    Returns:
        Um número ímpar aleatório com o número especificado de bits
    """
    num = generate_random_bits(bits)
    # Garante que o número é ímpar
    if num % 2 == 0:
        num += 1
    return num


def find_prime(bits: int, timeout_seconds: float = 300, k: int = 10) -> Tuple[int, int, float]:
    """
    Encontra um número primo com o número especificado de bits usando o Teste de Fermat,
    com um limite de tempo para evitar que o programa fique preso.
    
    Args:
        bits: Número de bits do primo a ser encontrado
        timeout_seconds: Tempo máximo em segundos para tentar
        k: Número de iterações para o teste de Fermat
        
    Returns:
        Tupla contendo (número primo, número de tentativas, tempo em ms)
    """
    start_time = time.time()
    end_time = start_time + timeout_seconds
    attempts = 0
    
    # Geramos um número ímpar aleatório inicial
    num = generate_random_odd(bits)
    
    print(f"Buscando primo de {bits} bits...", end="", flush=True)
    
    while time.time() < end_time:
        attempts += 1
        
        if attempts % 10 == 0:
            print(".", end="", flush=True)
        
        # Teste de Fermat
        is_probable_prime, _ = fermat_primality_test(num, k)
        
        if is_probable_prime:
            elapsed_ms = (time.time() - start_time) * 1000
            print(f" Encontrado após {attempts} tentativas!")
            return num, attempts, elapsed_ms
        
        # Se não for primo, tente o próximo número ímpar
        num += 2
    
    # Se chegamos aqui, não encontramos um primo dentro do tempo limite
    elapsed_ms = (time.time() - start_time) * 1000
    print(f" Tempo esgotado após {attempts} tentativas.")
    return 0, attempts, elapsed_ms


def run_experiment() -> Dict:
    """
    Executa o experimento completo para todos os tamanhos de bits especificados.
    
    Returns:
        Um dicionário com os resultados do experimento
    """
    # Tamanhos em bits para testar
    bit_sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    
    # Configurações de timeout por tamanho
    timeouts = {
        40: 60,     # 1 minuto
        56: 60,     # 1 minuto
        80: 60,     # 1 minuto
        128: 120,   # 2 minutos
        168: 180,   # 3 minutos
        224: 240,   # 4 minutos
        256: 300,   # 5 minutos
        512: 600,   # 10 minutos
        1024: 900,  # 15 minutos
        2048: 1200, # 20 minutos
        4096: 1800, # 30 minutos
    }
    
    # Parâmetros do teste de Fermat
    k_small = 10    # Para tamanhos até 256 bits
    k_large = 5     # Para tamanhos maiores
    
    results = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "algorithm": "Fermat Primality Test",
        "results": []
    }
    
    print("\nIniciando experimento de geração de números primos usando o Teste de Fermat")
    print("=" * 80)
    print(f"{'Tamanho (bits)':<15} {'Tentativas':<12} {'Tempo (ms)':<15} {'Status'}")
    print("-" * 80)
    
    for bits in bit_sizes:
        # Ajusta parâmetros com base no tamanho
        timeout = timeouts.get(bits, 300)  # Default de 5 minutos se não especificado
        k = k_small if bits <= 256 else k_large
        
        try:
            prime, attempts, elapsed_ms = find_prime(bits, timeout, k)
            
            status = "Sucesso" if prime > 0 else "Timeout"
            
            print(f"{bits:<15} {attempts:<12} {elapsed_ms:.2f} ms      {status}")
            
            result_entry = {
                "bits": bits,
                "prime": prime,
                "attempts": attempts,
                "time_ms": round(elapsed_ms, 2),
                "status": status
            }
            results["results"].append(result_entry)
            
            # Salvar resultado parcial para não perder tudo se houver falhas
            with open("prime_generation_results.json", "w") as f:
                json.dump(results, f, indent=2)
                
        except Exception as e:
            print(f"{bits:<15} {'Erro':<15} {'-':<12} {'-':<15} {str(e)}")
            results["results"].append({
                "bits": bits,
                "prime": 0,
                "attempts": 0,
                "time_ms": 0,
                "status": f"Erro: {str(e)}"
            })
    
    return results


def format_results_as_table(results: Dict) -> str:
    """
    Formata os resultados como uma tabela Markdown.
    
    Args:
        results: Os resultados do experimento
        
    Returns:
        Uma string contendo a tabela em formato Markdown
    """
    table = "| Algoritmo | Tamanho do Número | Tentativas | Tempo para gerar |\n"
    table += "|-----------|------------------|------------|-------------------|\n"
    
    for result in results["results"]:
        algorithm = results["algorithm"]
        bits = f"{result['bits']} bits"
        
        if result["status"] == "Sucesso":
            attempts_str = str(result["attempts"])
            time_str = f"{result['time_ms']} ms"
        else:
            attempts_str = str(result["attempts"])
            if result["status"] == "Timeout":
                time_str = f"{result['time_ms']} ms (timeout)"
            else:
                time_str = f"{result['time_ms']} ms (erro)"
        
        table += f"| {algorithm} | {bits} | {attempts_str} | {time_str} |\n"
    
    return table


def generate_report(results: Dict) -> None:
    """
    Gera um relatório completo do experimento.
    
    Args:
        results: Os resultados do experimento
    """
    # Cria o relatório
    report = "# Experimento de Geração de Números Primos com o Teste de Fermat\n\n"
    report += f"Data/Hora: {results['timestamp']}\n\n"
    
    # Adiciona a tabela
    report += "## Resultados\n\n"
    report += format_results_as_table(results)
    report += "\n\n"
    
    # Análise e observações
    report += "## Observações\n\n"
    
    # Analisa taxa de sucesso
    successful = sum(1 for r in results["results"] if r["status"] == "Sucesso")
    total = len(results["results"])
    success_rate = (successful / total) * 100 if total > 0 else 0
    
    report += f"- Taxa de sucesso: {successful}/{total} ({success_rate:.1f}%)\n"
    
    # Analisa tempos e tentativas
    if successful > 0:
        times = [r["time_ms"] for r in results["results"] if r["status"] == "Sucesso"]
        attempts = [r["attempts"] for r in results["results"] if r["status"] == "Sucesso"]
        
        avg_time = sum(times) / len(times)
        max_time = max(times)
        min_time = min(times)
        
        avg_attempts = sum(attempts) / len(attempts)
        max_attempts = max(attempts)
        min_attempts = min(attempts)
        
        report += f"- Tempo médio: {avg_time:.2f} ms\n"
        report += f"- Tempo mínimo: {min_time:.2f} ms\n"
        report += f"- Tempo máximo: {max_time:.2f} ms\n"
        report += f"- Tentativas médias: {avg_attempts:.2f}\n"
        report += f"- Tentativas mínimas: {min_attempts}\n"
        report += f"- Tentativas máximas: {max_attempts}\n\n"
        
        # Análise da relação entre tamanho de bits e número de tentativas
        sizes = [r["bits"] for r in results["results"] if r["status"] == "Sucesso"]
        if len(sizes) > 1:
            report += "### Relação entre tamanho e esforço\n\n"
            report += "- À medida que o tamanho em bits aumenta, nota-se:\n"
            
            # Ordenar resultados por tamanho de bits para comparação
            sorted_results = sorted([r for r in results["results"] if r["status"] == "Sucesso"], 
                                    key=lambda x: x["bits"])
            
            if len(sorted_results) >= 2:
                smallest = sorted_results[0]
                largest = sorted_results[-1]
                report += f"  - Para {smallest['bits']} bits: {smallest['attempts']} tentativas, {smallest['time_ms']:.2f} ms\n"
                report += f"  - Para {largest['bits']} bits: {largest['attempts']} tentativas, {largest['time_ms']:.2f} ms\n"
                
                attempt_increase = largest['attempts'] / smallest['attempts'] if smallest['attempts'] > 0 else 0
                time_increase = largest['time_ms'] / smallest['time_ms'] if smallest['time_ms'] > 0 else 0
                
                report += f"  - Aumento de tentativas: {attempt_increase:.2f}x\n"
                report += f"  - Aumento de tempo: {time_increase:.2f}x\n\n"
    
    # Análise dos timeouts
    timeout_bits = [r["bits"] for r in results["results"] if r["status"] == "Timeout"]
    if timeout_bits:
        report += "### Timeouts\n\n"
        report += f"- Não foi possível encontrar números primos dentro do tempo limite para os seguintes tamanhos: {', '.join(str(b) for b in timeout_bits)} bits.\n"
        report += "- O limite de tempo foi configurado de forma progressiva, aumentando conforme o tamanho do número.\n"
        report += "- Para números maiores, o tempo necessário cresce exponencialmente, tornando impraticável a geração em hardware convencional.\n\n"
    
    # Analisa desempenho por tamanho
    report += "### Dificuldades encontradas\n\n"
    report += "- À medida que o tamanho do número aumenta, o tempo necessário para a geração de primos cresce exponencialmente.\n"
    report += "- O número de tentativas também aumenta com o tamanho do número, seguindo a distribuição esperada de números primos.\n"
    report += "- A teoria dos números sugere que a probabilidade de um número aleatório ser primo é aproximadamente 1/ln(n), diminuindo conforme n aumenta.\n"
    report += "- Para números acima de 1024 bits, o processo se torna significativamente mais lento e pode exigir recursos computacionais consideráveis.\n"
    report += "- O teste de Fermat pode aceitar números compostos como primos (falsos positivos), especialmente para números de Carmichael.\n"
    report += "- Para tamanhos maiores, seria recomendável usar o teste de Miller-Rabin ou outros testes mais robustos em conjunto com o teste de Fermat.\n"
    
    # Salva o relatório
    with open("prime_generation_report.md", "w") as f:
        f.write(report)
    
    print("\nRelatório gerado com sucesso: prime_generation_report.md")


if __name__ == "__main__":
    print("Experimento de Geração de Números Primos com o Teste de Primalidade de Fermat")
    print("=" * 80)
    print("\nEste experimento tentará gerar números primos de diferentes tamanhos (40 a 4096 bits)")
    print("e medirá o tempo necessário para cada geração.")
    print("\nAtenção: Para tamanhos maiores (>1024 bits), o processo pode levar muito tempo.")
    print("Os resultados serão salvos em arquivo para que você possa interromper o processo se necessário.")
    
    input("\nPressione Enter para iniciar o experimento...")
    
    # Executa o experimento
    results = run_experiment()
    
    # Gera o relatório
    generate_report(results)
    
    print("\nExperimento concluído!")
    print(f"Os resultados completos foram salvos em 'prime_generation_results.json'")
