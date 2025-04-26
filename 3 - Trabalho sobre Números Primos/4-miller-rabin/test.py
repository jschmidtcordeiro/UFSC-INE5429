#!/usr/bin/env python3
"""
Experimento de Geração de Números Primos usando o Teste de Miller-Rabin

Este script realiza experimentos de geração de números primos de diferentes tamanhos
usando o algoritmo de Miller-Rabin. Ele gera uma tabela com o tempo necessário 
para encontrar um número primo para cada tamanho especificado.

Autor: João Pedro Schmidt Cordeiro
Data: Abril 2024
"""

import sys
import time
import random
from typing import Dict, Tuple, List
from datetime import datetime

# Importa as funções do arquivo principal
from main import is_prime_miller_rabin, generate_probable_prime


def find_prime_with_timeout(bits: int, timeout_seconds: float = 300) -> Tuple[int, float, int, bool]:
    """
    Tenta encontrar um número primo com o número especificado de bits,
    com um limite de tempo para evitar que o programa fique preso.
    
    Args:
        bits: Número de bits do primo a ser gerado
        timeout_seconds: Tempo máximo em segundos para tentar
        
    Returns:
        Uma tupla (primo, tempo_em_ms, tentativas, sucesso)
    """
    print(f"Testando geração de primo de {bits} bits...", end="", flush=True)
    
    start_time = time.time()
    end_time = start_time + timeout_seconds
    attempts = 0
    prime = None
    
    while time.time() < end_time:
        attempts += 1
        if attempts % 10 == 0:
            print(".", end="", flush=True)
        
        # Gera um número ímpar aleatório com o número exato de bits
        n = random.getrandbits(bits)
        n |= (1 << (bits - 1)) | 1  # Garante MSB=1 e número ímpar
        
        if is_prime_miller_rabin(n):
            prime = n
            break
    
    duration = (time.time() - start_time) * 1000  # Converte para milissegundos
    success = prime is not None
    
    if success:
        print(f" Encontrado em {attempts} tentativas e {duration:.2f} ms")
    else:
        print(f" Falha após {attempts} tentativas e {timeout_seconds*1000:.2f} ms")
    
    return prime, duration, attempts, success


def format_number_compact(n: int) -> str:
    """
    Formata um número grande de forma compacta, mostrando apenas o início e o fim.
    
    Args:
        n: O número a ser formatado
        
    Returns:
        Uma string com o número formatado
    """
    if n is None:
        return "N/A"
    
    str_n = str(n)
    if len(str_n) <= 20:
        return str_n
    
    return f"{str_n[:10]}...{str_n[-10:]}"


def run_prime_experiment() -> Dict:
    """
    Executa o experimento de geração de números primos.
    
    Returns:
        Um dicionário com os resultados do experimento
    """
    bit_sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    results = {
        "algorithm": "Miller-Rabin",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "results": []
    }
    
    print(f"Experimento iniciado em: {results['timestamp']}")
    print("=" * 80)
    
    # Tempo limite aumenta com o tamanho do número
    for bits in bit_sizes:
        # Define um timeout adequado baseado no tamanho
        if bits <= 128:
            timeout = 60  # 1 minuto para números pequenos
        elif bits <= 512:
            timeout = 300  # 5 minutos para números médios
        elif bits <= 1024:
            timeout = 600  # 10 minutos para números grandes
        else:
            timeout = 1200  # 20 minutos para números muito grandes
        
        prime, duration, attempts, success = find_prime_with_timeout(bits, timeout)
        
        result_entry = {
            "bits": bits,
            "prime": prime,
            "time_ms": duration,
            "attempts": attempts,
            "status": "Sucesso" if success else "Falha"
        }
        
        results["results"].append(result_entry)
    
    print("=" * 80)
    print(f"Experimento concluído em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
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
    table += "|-----------|-------------------|------------|-------------------|\n"
    
    for result in results["results"]:
        algorithm = results["algorithm"]
        bits = f"{result['bits']} bits"
        
        if result["status"] == "Sucesso":
            attempts_str = str(result["attempts"])
            time_str = f"{result['time_ms']:.2f} ms"
        else:
            attempts_str = str(result["attempts"])
            time_str = "Timeout"
        
        table += f"| {algorithm} | {bits} | {attempts_str} | {time_str} |\n"
    
    return table


def generate_report(results: Dict) -> None:
    """
    Gera um relatório completo do experimento.
    
    Args:
        results: Os resultados do experimento
    """
    # Cria o relatório
    report = "# Experimento de Geração de Números Primos com o Teste de Miller-Rabin\n\n"
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
    
    # Analisa desempenho por tamanho
    report += "### Dificuldades encontradas\n\n"
    
    failed_bits = [r["bits"] for r in results["results"] if r["status"] == "Falha"]
    if failed_bits:
        report += f"- Não foi possível gerar números primos para os seguintes tamanhos: {', '.join(str(b) for b in failed_bits)} bits\n"
    
    # Salva o relatório
    filename = "miller_rabin_report.md"
    with open(filename, "w") as f:
        f.write(report)
    
    print(f"\nRelatório completo gerado com sucesso: {filename}")


def print_experiment_results(results: Dict):
    """
    Imprime os resultados do experimento em formato de tabela.
    
    Args:
        results: Dicionário com os resultados do experimento
    """
    print("\n\nData/Hora: " + results["timestamp"])
    print("\n#### Resultados\n")
    print(format_results_as_table(results))
    
    successful_results = [r for r in results["results"] if r["status"] == "Sucesso"]
    
    if successful_results:
        print("\n#### Observações\n")
        print(f"- Taxa de sucesso: {len(successful_results)}/{len(results['results'])} ({len(successful_results)/len(results['results'])*100:.1f}%)")
        
        times = [r["time_ms"] for r in successful_results]
        print(f"- Tempo médio: {sum(times)/len(times):.2f} ms")
        print(f"- Tempo mínimo: {min(times):.2f} ms")
        print(f"- Tempo máximo: {max(times):.2f} ms")
        
        attempts = [r["attempts"] for r in successful_results]
        print(f"- Tentativas médias: {sum(attempts)/len(attempts):.2f}")
        print(f"- Tentativas mínimas: {min(attempts)}")
        print(f"- Tentativas máximas: {max(attempts)}")


if __name__ == "__main__":
    try:
        # Executa o experimento
        results = run_prime_experiment()
        
        # Imprime os resultados
        print_experiment_results(results)
        
        # Gera relatório em markdown
        generate_report(results)
        
    except KeyboardInterrupt:
        print("\n\nExperimento interrompido pelo usuário.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nErro durante o experimento: {e}")
        sys.exit(1)
