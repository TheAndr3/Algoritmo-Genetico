import random
import math

class Individuo:
    def __init__(self, cromossomo=None):
        if cromossomo is None:
            # Inicializa de forma aleatória com 22 bits
            self.cromossomo = [random.randint(0, 1) for _ in range(22)]
        else:
            self.cromossomo = list(cromossomo)
        
        self._x = None
        self._fitness = None

    def get_x(self):
        """Converte a representação binária (cromossomo) para o valor real no intervalo [-1, 2]."""
        if self._x is not None:
            return self._x
            
        # Converte a sequência de bits (lista de 0s e 1s) em um inteiro na base 10 (b_10)
        b_10 = int("".join(map(str, self.cromossomo)), 2)
        
        # Parâmetros definidos no escopo
        val_min = -1.0
        val_max = 2.0
        L = 22
        
        # Expressão matemática para decodificação
        self._x = val_min + (val_max - val_min) * (b_10 / (2**L - 1))
        return self._x

    def evaluate(self):
        """Calcula e retorna o fitness do indivíduo: f(x) = x * sen(10 * pi * x) + 1."""
        if self._fitness is not None:
            return self._fitness
            
        x = self.get_x()
        self._fitness = x * math.sin(10 * math.pi * x) + 1
        return self._fitness

    def __repr__(self):
        return f"Individuo(x={self.get_x():.6f}, fitness={self.evaluate():.6f})"
