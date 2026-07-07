# Glossário de Domínio

- **Indivíduo / Cromossomo:** Representa uma solução candidata para o problema. É codificado como uma sequência de **22 bits**.
- **Fitness / Avaliação:** Valor da função objetivo para o cromossomo. Definido como $f(x) = x \cdot \sin(10\pi x) + 1$. Pode assumir valores negativos.
- **Fitness Deslocado (Shifted Fitness):** Como a roleta não suporta números negativos, o fitness deslocado é usado apenas durante o sorteio. Soma-se o módulo do menor fitness da geração a todos os indivíduos para que o mínimo seja $\ge 0$.
- **Decodificação:** Processo matemático de conversão do valor binário (cromossomo) para o seu equivalente real no intervalo de $[-1, 2]$.
- **População:** Conjunto de Indivíduos (fixado em 100) que evoluem a cada geração.
- **Geração:** Uma iteração completa do Algoritmo Genético, que gera uma nova população a partir da atual.
- **Seleção por Roleta:** Método probabilístico para escolha de pais, onde fatias são baseadas no *Fitness Deslocado*. Os pais são sorteados de *toda a população*.
- **Elitismo:** Cópia direta dos 10 melhores indivíduos da geração atual para a próxima. A geração seguinte terá então 10 "elites" e 90 "filhos" recém-criados.
- **Cruzamento de Um Ponto:** Operação genética onde um ponto de corte é escolhido aleatoriamente e o material genético de dois pais é trocado.
- **Mutação Simples:** Inversão (bit-flip) com dada probabilidade em cada bit (gene) do cromossomo de um indivíduo recém gerado.
