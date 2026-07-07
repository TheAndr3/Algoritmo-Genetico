import random
from individuo import Individuo

class AlgoritmoGenetico:
    def __init__(self, tam_populacao=100, geracoes=200, taxa_cruzamento=0.80, taxa_mutacao=0.01, taxa_elitismo=0.10):
        self.tam_populacao = tam_populacao
        self.geracoes = geracoes
        self.taxa_cruzamento = taxa_cruzamento
        self.taxa_mutacao = taxa_mutacao
        self.taxa_elitismo = taxa_elitismo
        
        self.num_elites = int(self.tam_populacao * self.taxa_elitismo)
        self.populacao = []

    def inicializar_populacao(self):
        """Cria a população inicial com indivíduos aleatórios."""
        self.populacao = [Individuo() for _ in range(self.tam_populacao)]

    def selecao_roleta(self, quantidade):
        """Seleciona 'quantidade' de indivíduos usando o método da Roleta com deslocamento (Shift)."""
        # Avalia o fitness de todos os indivíduos da população
        fitnesses = [ind.evaluate() for ind in self.populacao]
        
        # Como o fitness pode ser negativo, aplicamos um deslocamento (shift)
        # para garantir que todas as fatias da roleta sejam estritamente positivas (> 0).
        min_fit = min(fitnesses)
        shifted_fitnesses = [f - min_fit + 1e-6 for f in fitnesses]
        soma_fitness = sum(shifted_fitnesses)
        
        selecionados = []
        for _ in range(quantidade):
            limite = random.uniform(0, soma_fitness)
            soma_acumulada = 0
            for ind, fit_deslocado in zip(self.populacao, shifted_fitnesses):
                soma_acumulada += fit_deslocado
                if soma_acumulada >= limite:
                    selecionados.append(ind)
                    break
        return selecionados

    def cruzamento_um_ponto(self, pai1, pai2):
        """Realiza o cruzamento de um ponto com probabilidade dada por taxa_cruzamento."""
        if random.random() < self.taxa_cruzamento:
            # Ponto de corte entre 1 e L-1 (onde L = 22)
            ponto = random.randint(1, 21)
            
            filho1_crom = pai1.cromossomo[:ponto] + pai2.cromossomo[ponto:]
            filho2_crom = pai2.cromossomo[:ponto] + pai1.cromossomo[ponto:]
            
            return Individuo(filho1_crom), Individuo(filho2_crom)
        else:
            # Retorna clones se não houver cruzamento
            return Individuo(pai1.cromossomo), Individuo(pai2.cromossomo)

    def mutacao(self, individuo):
        """Aplica mutação simples (bit-flip) com probabilidade de taxa_mutacao em cada gene."""
        crom_mutado = []
        for bit in individuo.cromossomo:
            if random.random() < self.taxa_mutacao:
                # Faz o bit-flip (se for 1 vira 0, se for 0 vira 1)
                crom_mutado.append(1 - bit)
            else:
                crom_mutado.append(bit)
        return Individuo(crom_mutado)

    def executar(self):
        """Executa o loop do Algoritmo Genético por 'geracoes' iterações."""
        self.inicializar_populacao()
        
        # Histórico para salvar o melhor fitness de cada geração
        historico_melhor_fitness = []
        
        for g in range(self.geracoes):
            # Ordena a população atual pelo fitness em ordem decrescente
            self.populacao.sort(key=lambda ind: ind.evaluate(), reverse=True)
            
            melhor_da_geracao = self.populacao[0]
            historico_melhor_fitness.append(melhor_da_geracao.evaluate())
            
            # Elitismo: Copia os melhores indivíduos diretamente para a nova população
            proxima_populacao = []
            for i in range(self.num_elites):
                # Preserva o indivíduo criando um clone para evitar efeitos colaterais
                proxima_populacao.append(Individuo(self.populacao[i].cromossomo))
            
            # Preenche o restante da população
            vagas_restantes = self.tam_populacao - self.num_elites
            
            # Como geramos 2 filhos por cruzamento, dividimos por 2
            for _ in range(vagas_restantes // 2):
                # Seleciona dois pais via roleta (sobre a população atual inteira)
                pais = self.selecao_roleta(2)
                pai1, pai2 = pais[0], pais[1]
                
                # Crossover
                filho1, filho2 = self.cruzamento_um_ponto(pai1, pai2)
                
                # Mutação
                filho1 = self.mutacao(filho1)
                filho2 = self.mutacao(filho2)
                
                proxima_populacao.extend([filho1, filho2])
            
            # Se sobrar alguma vaga ímpar (não deve ocorrer com tam=100 e elitismo=10%), preenchemos com mais um
            if len(proxima_populacao) < self.tam_populacao:
                pais = self.selecao_roleta(1)
                filho = self.mutacao(pais[0])
                proxima_populacao.append(filho)
                
            self.populacao = proxima_populacao
            
        # Avalia a última população após o fim das gerações
        self.populacao.sort(key=lambda ind: ind.evaluate(), reverse=True)
        melhor_final = self.populacao[0]
        
        return historico_melhor_fitness, melhor_final
