import random
import math
import time
from sympy import isprime, gcd

class BlumBlumShub:
    def __init__(self, bits_length=256, seed=None):
        """
        Inicializa o gerador Blum Blum Shub.
        
        Args:
            bits_length: Comprimento dos primos p e q em bits (padrão: 256)
            seed: Semente inicial (opcional)
        """
        # Gerar primos p e q congruentes a 3 mod 4
        self.p = self._generate_prime(bits_length)
        self.q = self._generate_prime(bits_length)
        while self.p == self.q:
            self.q = self._generate_prime(bits_length)
        
        # Calcular n = p * q (módulo de Blum)
        self.n = self.p * self.q
        
        # Escolher semente
        if seed is None:
            # Gerar uma semente aleatória co-prima com n
            seed = random.randint(2, self.n - 1)
            while gcd(seed, self.n) != 1:
                seed = random.randint(2, self.n - 1)
        else:
            # Verificar se a semente fornecida é adequada
            if seed < 2 or seed >= self.n or gcd(seed, self.n) != 1:
                raise ValueError("A semente deve ser um inteiro co-primo com n e estar no intervalo [2, n-1]")
                
        # Calcular o estado inicial
        self.state = (seed * seed) % self.n  # x₁ = s² mod n
        
    def _generate_prime(self, bits_length):
        """
        Gera um número primo p tal que p ≡ 3 (mod 4) com o comprimento especificado.
        """
        while True:
            # Gerar um número aleatório com o comprimento especificado
            # Garantir que o bit mais significativo seja 1 (para garantir o comprimento)
            # E que o bit menos significativo também seja 1 (para ser ímpar)
            p = random.getrandbits(bits_length) | (1 << (bits_length - 1)) | 1
            
            # Verificar se p ≡ 3 (mod 4) e se é primo
            if p % 4 == 3 and isprime(p):
                return p
    
    def next_bit(self):
        """
        Gera o próximo bit pseudoaleatório.
        
        Returns:
            0 ou 1: o bit menos significativo do próximo estado.
        """
        self.state = (self.state * self.state) % self.n
        return self.state & 1  # Retorna o bit menos significativo
    
    def next_bits(self, num_bits):
        """
        Gera uma sequência de bits pseudoaleatórios.
        
        Args:
            num_bits: Número de bits a serem gerados.
            
        Returns:
            Um inteiro representando os bits gerados.
        """
        result = 0
        for _ in range(num_bits):
            result = (result << 1) | self.next_bit()
        return result
    
    def next_int(self, a, b):
        """
        Gera um número inteiro aleatório no intervalo [a, b].
        
        Args:
            a: Limite inferior.
            b: Limite superior.
            
        Returns:
            Um inteiro no intervalo [a, b].
        """
        # Calcular quantos bits são necessários
        range_size = b - a + 1
        bits_needed = math.ceil(math.log2(range_size))
        
        # Gerar bits e converter para o intervalo desejado
        while True:
            result = self.next_bits(bits_needed)
            if result < range_size:
                return a + result

# Exemplo de uso
if __name__ == "__main__":
    print("Demonstração do algoritmo Blum Blum Shub (BBS)")
    print("----------------------------------------------")
    
    # Criar uma instância do gerador
    # Usando tamanho de primo menor para demonstração rápida
    print("Inicializando o gerador BBS...")
    bbs = BlumBlumShub(bits_length=128)
    print(f"Módulo n tem {bbs.n.bit_length()} bits")
    
    # Exemplo 1: Gerar bits individuais
    print("\nGerando bits individuais (primeiros 20):")
    bits = []
    for _ in range(20):
        bit = bbs.next_bit()
        bits.append(bit)
    print(' '.join(map(str, bits)))
    
    # Exemplo 2: Gerar sequências de bits (números binários)
    print("\nGerando sequências de bits:")
    for size in [8, 16, 32]:
        number = bbs.next_bits(size)
        binary = bin(number)[2:].zfill(size)
        print(f"  {size} bits: {number} (binário: {binary})")
    
    # Exemplo 3: Gerar números aleatórios em diferentes intervalos
    print("\nGerando números em intervalos específicos:")
    intervals = [(1, 6), (1, 100), (1000, 9999)]
    for a, b in intervals:
        numbers = [bbs.next_int(a, b) for _ in range(5)]
        print(f"  Intervalo [{a}, {b}]: {numbers}")
