"""
Experimento para avaliação de desempenho de geradores de números pseudoaleatórios.

Este script avalia o tempo necessário para gerar números pseudoaleatórios de diferentes
tamanhos (40-4096 bits) usando diferentes implementações do algoritmo Xorshift.

O experimento gera múltiplos números para cada tamanho e calcula o tempo médio.
"""

import time
import sys
from main import Xorshift32, Xorshift64, Xorshift128, Xorshift128Plus

# Tamanhos de bits a serem testados
BIT_SIZES = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

# Número de amostras para calcular o tempo médio
NUM_SAMPLES = 1000


def generate_random_bits(generator, num_bits):
    """
    Gera um número pseudoaleatório com o número especificado de bits.
    
    Args:
        generator: Objeto gerador Xorshift
        num_bits: Número de bits desejado
    
    Returns:
        int: Número pseudoaleatório com o tamanho especificado
    """
    result = 0
    bits_generated = 0
    
    # Determina o número de bits por chamada com base no tipo de gerador
    if isinstance(generator, Xorshift32):
        bits_per_call = 32
    elif isinstance(generator, Xorshift64) or isinstance(generator, Xorshift128Plus):
        bits_per_call = 64
    elif isinstance(generator, Xorshift128):
        bits_per_call = 32
    else:
        raise ValueError("Gerador não reconhecido")
    
    # Gera bits até atingir o tamanho desejado
    while bits_generated < num_bits:
        # Gera um novo número
        new_bits = generator.next()
        
        # Adiciona os novos bits ao resultado (shifts e OR)
        result = (result << bits_per_call) | new_bits
        bits_generated += bits_per_call
    
    # Ajusta para o tamanho exato solicitado (remove bits extras)
    if bits_generated > num_bits:
        extra_bits = bits_generated - num_bits
        result = result >> extra_bits
        
    # Garante que o número tenha exatamente o número de bits solicitado
    # Seta o bit mais significativo para 1
    result |= (1 << (num_bits - 1))
    
    return result


def measure_generation_time(generator_class, bit_size, seed=42):
    """
    Mede o tempo médio para gerar números pseudoaleatórios de determinado tamanho.
    
    Args:
        generator_class: Classe do gerador a ser usada
        bit_size: Tamanho do número em bits
        seed: Semente para inicializar o gerador
    
    Returns:
        float: Tempo médio em milissegundos
    """
    # Inicializa o gerador apropriadamente dependendo da classe
    if generator_class == Xorshift32 or generator_class == Xorshift64:
        generator = generator_class(seed=seed)
    elif generator_class == Xorshift128:
        generator = generator_class(seed=[seed, seed+1, seed+2, seed+3])
    elif generator_class == Xorshift128Plus:
        generator = generator_class(seed=[seed, seed+1])
    
    # Mede o tempo total para gerar NUM_SAMPLES números
    start_time = time.time()
    
    for _ in range(NUM_SAMPLES):
        generate_random_bits(generator, bit_size)
    
    end_time = time.time()
    
    # Calcula o tempo médio em milissegundos
    avg_time_ms = ((end_time - start_time) / NUM_SAMPLES) * 1000
    
    return avg_time_ms


def run_experiment():
    """
    Executa o experimento completo e exibe os resultados em formato de tabela.
    """
    generators = [
        ("Xorshift32", Xorshift32),
        ("Xorshift64", Xorshift64),
        ("Xorshift128", Xorshift128),
        ("Xorshift128Plus", Xorshift128Plus)
    ]
    
    # Imprime o cabeçalho da tabela
    print("\n" + "=" * 80)
    print(f"{'Algoritmo':<20} | {'Tamanho do Número':<20} | {'Tempo para gerar (ms)':<20}")
    print("-" * 80)
    
    # Executa o experimento para cada combinação de gerador e tamanho
    for gen_name, gen_class in generators:
        for bit_size in BIT_SIZES:
            # Mede o tempo de geração
            time_ms = measure_generation_time(gen_class, bit_size)
            
            # Formata e imprime o resultado
            print(f"{gen_name:<20} | {bit_size} bits{' ':<14} | {time_ms:.4f} ms")
        
        # Linha separadora entre geradores
        print("-" * 80)
    
    print("=" * 80)
    print(f"Experimento concluído. Cada medição representa a média de {NUM_SAMPLES} execuções.")


def verify_random_number_quality(show_numbers=False):
    """
    Verifica a qualidade dos números gerados por cada algoritmo.
    Esta função é útil para validar se os números gerados têm o tamanho especificado.
    
    Args:
        show_numbers: Se True, exibe os números gerados para inspeção visual
    """
    print("\nVerificação da qualidade dos números gerados:")
    print("-" * 80)
    
    generators = [
        ("Xorshift32", Xorshift32(seed=42)),
        ("Xorshift64", Xorshift64(seed=42)),
        ("Xorshift128", Xorshift128(seed=[42, 43, 44, 45])),
        ("Xorshift128Plus", Xorshift128Plus(seed=[42, 43]))
    ]
    
    # Seleciona alguns tamanhos para testar
    test_sizes = [40, 128, 256, 1024]
    
    for gen_name, generator in generators:
        print(f"\nGerador: {gen_name}")
        
        for bit_size in test_sizes:
            number = generate_random_bits(generator, bit_size)
            
            # Verifica se o número tem o tamanho correto (em bits)
            binary = bin(number)[2:]  # Remove o prefixo '0b'
            actual_bits = len(binary)
            
            print(f"  Tamanho solicitado: {bit_size} bits")
            print(f"  Tamanho real: {actual_bits} bits")
            
            if show_numbers:
                # Limita a exibição para evitar números muito grandes
                if bit_size <= 128:
                    print(f"  Número binário: {binary}")
                else:
                    print(f"  Número binário: {binary[:64]}...{binary[-64:]} (parte inicial e final)")
            
            print("-" * 40)


if __name__ == "__main__":
    # Verifica se o usuário quer executar o experimento com verificação de qualidade
    verify_quality = len(sys.argv) > 1 and sys.argv[1] == "--verify"
    
    if verify_quality:
        verify_random_number_quality(show_numbers=True)
    else:
        print("\nIniciando experimento de geração de números pseudoaleatórios...")
        print(f"Gerando {NUM_SAMPLES} amostras para cada combinação algoritmo-tamanho")
        run_experiment()
        print("\nDica: Execute com a flag --verify para testar a qualidade dos números gerados.")
