"""
Implementação do algoritmo Xorshift PRNG
Baseado no trabalho original de George Marsaglia (2003)

Inclui implementações para versões de 32 bits, 64 bits e 128 bits.
"""

class Xorshift32:
    """
    Implementação do Xorshift de 32 bits com período de 2^32-1.
    """
    def __init__(self, seed=123456789):
        """
        Inicializa o gerador com uma semente não-nula.
        
        Args:
            seed (int): Valor de semente. Deve ser não-zero.
        """
        if seed == 0:
            seed = 123456789  # Evita estado zero
        self.state = seed & 0xFFFFFFFF  # Garante valor de 32 bits
    
    def next(self):
        """
        Gera o próximo número pseudoaleatório.
        
        Returns:
            int: Um número pseudoaleatório de 32 bits.
        """
        # Copia o estado atual para a variável x
        x = self.state
        # Aplica o primeiro deslocamento: desloca x 13 bits à esquerda, 
        # faz XOR com o valor original e mantém apenas os 32 bits inferiores
        x ^= (x << 13) & 0xFFFFFFFF
        # Aplica o segundo deslocamento: desloca x 17 bits à direita,
        # faz XOR com o resultado anterior e mantém apenas os 32 bits inferiores
        x ^= (x >> 17) & 0xFFFFFFFF
        # Aplica o terceiro deslocamento: desloca x 5 bits à esquerda,
        # faz XOR com o resultado anterior e mantém apenas os 32 bits inferiores
        x ^= (x << 5) & 0xFFFFFFFF
        # Atualiza o estado interno do gerador com o novo valor
        # garantindo que apenas os 32 bits inferiores sejam mantidos
        self.state = x & 0xFFFFFFFF
        
        # Retorna o novo estado como o número pseudoaleatório gerado
        return self.state
    
    def random(self):
        """
        Retorna um número de ponto flutuante no intervalo [0.0, 1.0).
        
        Returns:
            float: Um número entre 0.0 e 1.0.
        """
        return self.next() / 0x100000000


class Xorshift64:
    """
    Implementação do Xorshift de 64 bits com período de 2^64-1.
    """
    def __init__(self, seed=88172645463325252):
        """
        Inicializa o gerador com uma semente não-nula.
        
        Args:
            seed (int): Valor de semente. Deve ser não-zero.
        """
        if seed == 0:
            seed = 88172645463325252  # Evita estado zero
        self.state = seed & 0xFFFFFFFFFFFFFFFF  # Garante valor de 64 bits
    
    def next(self):
        """
        Gera o próximo número pseudoaleatório.
        
        Returns:
            int: Um número pseudoaleatório de 64 bits.
        """
        # Copia o estado atual para a variável x
        x = self.state
        # Aplica XOR entre x e (x deslocado 13 bits à esquerda), mantendo apenas 64 bits
        x ^= (x << 13) & 0xFFFFFFFFFFFFFFFF
        # Aplica XOR entre x e (x deslocado 7 bits à direita), mantendo apenas 64 bits
        x ^= (x >> 7) & 0xFFFFFFFFFFFFFFFF
        # Aplica XOR entre x e (x deslocado 17 bits à esquerda), mantendo apenas 64 bits
        x ^= (x << 17) & 0xFFFFFFFFFFFFFFFF
        # Atualiza o estado interno com o novo valor, garantindo que tenha apenas 64 bits
        self.state = x & 0xFFFFFFFFFFFFFFFF
        # Retorna o novo estado como o número pseudoaleatório gerado
        return self.state
    
    def random(self):
        """
        Retorna um número de ponto flutuante no intervalo [0.0, 1.0).
        
        Returns:
            float: Um número entre 0.0 e 1.0.
        """
        return self.next() / 0x10000000000000000


class Xorshift128:
    """
    Implementação do Xorshift de 128 bits com período de 2^128-1.
    """
    def __init__(self, seed=None):
        """
        Inicializa o gerador com uma semente ou valores padrão.
        
        Args:
            seed (list, optional): Lista de 4 valores inteiros para inicializar o estado.
        """
        if seed is None:
            # Valores iniciais não-nulos por padrão
            self.state = [123456789, 362436069, 521288629, 88675123]
        else:
            # Verifica se todos os valores são zero
            if all(s == 0 for s in seed):
                self.state = [123456789, 362436069, 521288629, 88675123]
            else:
                self.state = [s & 0xFFFFFFFF for s in seed[:4]]
    
    def next(self):
        """
        Gera o próximo número pseudoaleatório.
        
        Returns:
            int: Um número pseudoaleatório de 32 bits.
        """
        # Armazena o último valor do estado (índice 3) em t
        t = self.state[3]
        # Armazena o primeiro valor do estado (índice 0) em s
        s = self.state[0]
        
        # Desloca os valores do estado: o valor do índice 2 vai para o índice 3
        self.state[3] = self.state[2]
        # Desloca os valores do estado: o valor do índice 1 vai para o índice 2
        self.state[2] = self.state[1]
        # Desloca os valores do estado: o valor do índice 0 (s) vai para o índice 1
        self.state[1] = s
        
        # Aplica a primeira transformação XOR: desloca t 11 bits à esquerda e faz XOR com t
        # A máscara 0xFFFFFFFF garante que o resultado tenha 32 bits
        t ^= (t << 11) & 0xFFFFFFFF
        # Aplica a segunda transformação XOR: desloca t 8 bits à direita e faz XOR com t
        t ^= (t >> 8) & 0xFFFFFFFF
        # Aplica a terceira transformação XOR: faz XOR entre t e o resultado de (s XOR (s deslocado 19 bits à direita))
        t ^= (s ^ (s >> 19)) & 0xFFFFFFFF
        
        # Atualiza o primeiro valor do estado (índice 0) com o novo valor de t
        # A máscara 0xFFFFFFFF garante que o resultado tenha 32 bits
        self.state[0] = t & 0xFFFFFFFF
        # Retorna o valor gerado, garantindo que tenha 32 bits
        return t & 0xFFFFFFFF
    
    def random(self):
        """
        Retorna um número de ponto flutuante no intervalo [0.0, 1.0).
        
        Returns:
            float: Um número entre 0.0 e 1.0.
        """
        return self.next() / 0x100000000


class Xorshift128Plus:
    """
    Implementação do Xorshift128+ - uma variante que utiliza adição para
    melhorar a qualidade estatística (período 2^128-1).
    """
    def __init__(self, seed=None):
        """
        Inicializa o gerador com uma semente ou valores padrão.
        
        Args:
            seed (list, optional): Lista de 2 valores inteiros de 64 bits para inicializar o estado.
        """
        if seed is None:
            # Valores iniciais não-nulos por padrão
            self.state = [1234567890123456789, 9876543210987654321]
        else:
            # Verifica se todos os valores são zero
            if all(s == 0 for s in seed):
                self.state = [1234567890123456789, 9876543210987654321]
            else:
                self.state = [s & 0xFFFFFFFFFFFFFFFF for s in seed[:2]]
    
    def next(self):
        """
        Gera o próximo número pseudoaleatório.
        
        Returns:
            int: Um número pseudoaleatório de 64 bits.
        """
        # Armazena os dois valores do estado atual em variáveis temporárias
        s0 = self.state[0]  # Primeiro valor do estado (64 bits)
        s1 = self.state[1]  # Segundo valor do estado (64 bits)
        
        # Atualiza o primeiro valor do estado com o valor de s1
        # Isso faz parte da rotação do estado para a próxima iteração
        self.state[0] = s1
        
        # Aplica a primeira transformação XOR em s1:
        # Desloca s1 23 bits à esquerda, faz XOR com s1 original
        # A máscara 0xFFFFFFFFFFFFFFFF garante que o resultado tenha 64 bits
        s1 ^= (s1 << 23) & 0xFFFFFFFFFFFFFFFF
        
        # Calcula o novo valor para o segundo elemento do estado:
        # Combina s1 transformado com s0 original e mais duas operações de deslocamento e XOR
        # - s1 ^ s0: XOR entre s1 transformado e s0 original
        # - ^ (s1 >> 18): XOR com s1 deslocado 18 bits à direita
        # - ^ (s0 >> 5): XOR com s0 deslocado 5 bits à direita
        # A máscara final garante que o resultado tenha 64 bits
        self.state[1] = (s1 ^ s0 ^ (s1 >> 18) ^ (s0 >> 5)) & 0xFFFFFFFFFFFFFFFF
        
        # Retorna a soma dos dois valores do estado como o número pseudoaleatório
        # Esta adição é o que diferencia o Xorshift128+ do Xorshift128 padrão,
        # melhorando a qualidade estatística dos números gerados
        # A máscara garante que o resultado tenha 64 bits
        return (self.state[0] + self.state[1]) & 0xFFFFFFFFFFFFFFFF
    
    def random(self):
        """
        Retorna um número de ponto flutuante no intervalo [0.0, 1.0).
        
        Returns:
            float: Um número entre 0.0 e 1.0.
        """
        return self.next() / 0x10000000000000000


# Exemplo de uso
if __name__ == "__main__":
    # Demonstração do Xorshift32
    rng32 = Xorshift32(seed=42)
    print("Xorshift32 (primeiros 5 valores):")
    for _ in range(5):
        print(f"  Inteiro: {rng32.next()}, Ponto flutuante: {rng32.random():.8f}")
    
    # Demonstração do Xorshift64
    rng64 = Xorshift64(seed=42)
    print("\nXorshift64 (primeiros 5 valores):")
    for _ in range(5):
        print(f"  Inteiro: {rng64.next()}, Ponto flutuante: {rng64.random():.8f}")
    
    # Demonstração do Xorshift128
    rng128 = Xorshift128(seed=[42, 43, 44, 45])
    print("\nXorshift128 (primeiros 5 valores):")
    for _ in range(5):
        print(f"  Inteiro: {rng128.next()}, Ponto flutuante: {rng128.random():.8f}")
    
    # Demonstração do Xorshift128Plus
    rng128plus = Xorshift128Plus(seed=[42, 43])
    print("\nXorshift128Plus (primeiros 5 valores):")
    for _ in range(5):
        print(f"  Inteiro: {rng128plus.next()}, Ponto flutuante: {rng128plus.random():.8f}")
