import time
import pandas as pd
import matplotlib.pyplot as plt
from main import BlumBlumShub
from tabulate import tabulate

def run_experiment(bit_sizes, num_runs=10):
    """
    Executa o experimento de geração de números aleatórios para diferentes tamanhos de bits.
    
    Args:
        bit_sizes: Lista com os tamanhos de bits a serem testados
        num_runs: Número de execuções para calcular a média do tempo (padrão: 10)
        
    Returns:
        DataFrame com os resultados
    """
    print("Iniciando experimento...")
    print(f"Gerando números aleatórios de diferentes tamanhos ({num_runs} execuções para cada tamanho)")
    
    # Inicializar o gerador BBS (apenas uma vez para todos os testes)
    # Usamos um tamanho menor (512 bits) para a configuração inicial para economizar tempo
    # Em um ambiente de produção real, um valor maior seria recomendado
    print("Inicializando o gerador Blum Blum Shub...")
    bbs = BlumBlumShub(bits_length=512)
    print("Gerador inicializado.")
    
    results = []
    
    for size in bit_sizes:
        print(f"Testando tamanho: {size} bits")
        times = []
        
        try:
            # Aquecer o gerador para minimizar efeitos de cache/JIT
            bbs.next_bits(size)
            
            # Executar o teste várias vezes para obter uma média confiável
            for _ in range(num_runs):
                start_time = time.time()
                bbs.next_bits(size)
                elapsed_time = (time.time() - start_time) * 1000  # Converter para milissegundos
                times.append(elapsed_time)
            
            # Calcular a média dos tempos
            avg_time = sum(times) / len(times)
            results.append({
                "Algoritmo": "Blum Blum Shub",
                "Tamanho do Número": f"{size} bits",
                "Tempo para gerar (ms)": f"{avg_time:.4f} ms"
            })
            print(f"Média de tempo: {avg_time:.4f} ms")
            
        except Exception as e:
            # Registrar se houver algum erro na geração
            print(f"Erro ao gerar número de {size} bits: {str(e)}")
            results.append({
                "Algoritmo": "Blum Blum Shub",
                "Tamanho do Número": f"{size} bits",
                "Tempo para gerar (ms)": f"ERRO: {str(e)}"
            })
    
    # Criar DataFrame com os resultados
    df = pd.DataFrame(results)
    return df

def plot_results(results_df):
    """
    Cria um gráfico dos resultados do experimento.
    
    Args:
        results_df: DataFrame com os resultados
    """
    # Extrair os tamanhos de bits e tempos
    sizes = [int(size.split()[0]) for size in results_df["Tamanho do Número"]]
    times = [float(time.split()[0]) for time in results_df["Tempo para gerar (ms)"]]
    
    # Criar o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker='o', linestyle='-')
    plt.xscale('log2')
    plt.yscale('log')
    plt.grid(True, which="both", ls="--", alpha=0.7)
    
    plt.xlabel('Tamanho do Número (bits)')
    plt.ylabel('Tempo para gerar (ms)')
    plt.title('Desempenho do Blum Blum Shub por Tamanho de Número')
    
    # Adicionar anotações de dados
    for i, (size, time) in enumerate(zip(sizes, times)):
        plt.annotate(f"{time:.2f} ms", 
                    (size, time),
                    textcoords="offset points", 
                    xytext=(0, 10), 
                    ha='center')
    
    plt.tight_layout()
    plt.savefig('bbs_performance.png')
    print("Gráfico salvo como 'bbs_performance.png'")

if __name__ == "__main__":
    # Definir tamanhos a serem testados (em bits)
    bit_sizes = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    
    # Executar o experimento
    results = run_experiment(bit_sizes)
    
    # Exibir tabela de resultados
    print("\nResultados do Experimento:")
    print(tabulate(results, headers="keys", tablefmt="pipe", showindex=False))
    
    # Também salvar os resultados em um arquivo Markdown
    with open("resultados_bbs.md", "w") as f:
        f.write("# Resultados do Experimento: Blum Blum Shub\n\n")
        f.write("Tempo médio para geração de números pseudoaleatórios de diferentes tamanhos usando o algoritmo Blum Blum Shub.\n\n")
        f.write(tabulate(results, headers="keys", tablefmt="pipe", showindex=False))
        f.write("\n\n*Cada medição representa a média de 10 execuções.*\n")
    
    print("\nResultados salvos em 'resultados_bbs.md'")
    
    # Gerar gráfico (requer matplotlib)
    try:
        plot_results(results)
    except ImportError:
        print("Matplotlib não está instalado. Gráfico não gerado.")
    except Exception as e:
        print(f"Erro ao gerar gráfico: {str(e)}")
    
    # Instruções para adicionar os resultados ao relatório
    print("\nDica: Para adicionar esses resultados ao seu relatório, copie a tabela acima")
    print("ou importe o arquivo 'resultados_bbs.md' gerado.")
