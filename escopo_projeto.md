Aqui está o conteúdo do documento estruturado e formatado em Markdown, pronto para uso:

---

# EPC 6 - Inteligência Artificial Não Simbólica

* **Universidade:** Universidade Estadual de Feira de Santana (UEFS)
* **Curso:** Engenharia de Computação
* **Professor:** Matheus Giovanni Pires
* **Data de Entrega:** 05/07/2026

---

## 1. Introdução à Otimização e Algoritmos Genéticos

Otimização é a procura pelo melhor desempenho em direção a um ou alguns pontos ótimos, ou seja, é a busca da melhor solução para um dado problema.

Os **Algoritmos Genéticos (AGs)** são algoritmos que realizam essa busca baseados no mecanismo da seleção natural e da genética natural. Consistem em tentar várias soluções e utilizar a informação obtida neste processo de forma a encontrar soluções cada vez melhores.

### Estrutura de um Algoritmo Genético Simples

```pascal
algoritmo genético
    t ← 0
    inicializar P(t)
    avaliar P(t)
    enquanto (condição verdadeira) faça
        t ← t + 1
        gerar P(t) de P(t - 1)
        alterar P(t)
        avaliar P(t)
    fim enquanto
fim

```

---

## 2. Descrição do Problema

Um exemplo simples de otimização é a melhoria da imagem das televisões com antena acoplada. Através do ajuste manual da antena, várias soluções são testadas, guiadas pela qualidade de imagem obtida na TV, até a obtenção de uma resposta ótima, ou seja, uma boa imagem.

Considere um sinal de TV definido pela seguinte equação matemática:

$$f(x) = x \cdot \operatorname{sen}(10\pi x) + 1$$

O objetivo é construir um algoritmo genético que encontre um $x \in [-1, 2]$ que maximize a função $f$, isto é, encontrar um $x_0$ tal que:

$$f(x_0) \ge f(x), \quad \forall x \in [-1, 2]$$

> **Nota sobre o Máximo Global:** Neste problema, o máximo global encontra-se no ponto cujo valor de $x$ é igual a **1,85055**. Neste ponto, a função assume o valor **2,85027**.

---

## 3. Parâmetros para a Implementação

### Codificação e Mapeamento

* **Representação:** Os cromossomos devem ser codificados como sequências de dígitos binários com tamanho fixo de **22 bits**.
* **Precisão:** A precisão requerida através da representação cromossômica é de 6 casas decimais para o intervalo $[-1, 2]$.
* **Conversão Binário para Real:** Utilize a expressão abaixo para converter a representação na base 10 para o valor real correspondente:

$$x = \min + (\max - \min) \cdot \frac{b_{10}}{2^L - 1}$$

* Onde:
* $\min = -1$ (limite inferior da variável $x$)
* $\max = 2$ (limite superior da variável $x$)
* $b_{10} =$ codificação do número na base 10
* $L = 22$ (quantidade de bits)



### Configurações Globais do AG

* **Tamanho da População:** 100 indivíduos, gerados inicialmente de forma aleatória.
* **Critério de Parada / Número de Gerações:** Máximo de 200 gerações.
* **Função de Fitness:** A própria função objetivo do problema:

$$\text{fitness}(\text{cromossomo}_i) = f(x_i) = x_i \cdot \operatorname{sen}(10\pi x_i) + 1$$


* **Método de Seleção:** Seleção por Roleta combinada com Elitismo.
* **Operadores Genéticos:** Cruzamento de um ponto e Mutação simples.

---

## 4. Experimentos e Simulações

Após configurar os parâmetros, realize as seguintes simulações e gere os relatórios pedidos:

### Simulação 1: Variação da Taxa de Cruzamento

* **Configuração:** Execute o AG variando a taxa de cruzamento em **70%**, **80%** e **90%**.
* **Fixos:** Taxa de mutação em **1%** e taxa de elitismo em **10%**.
* **Saída:** Gere um único gráfico ilustrando o comportamento do melhor indivíduo ao longo das gerações para as três diferentes taxas de cruzamento.

### Simulação 2: Variação da Taxa de Mutação

* **Configuração:** Execute o AG variando a taxa de mutação em **1%**, **5%** e **10%**.
* **Fixos:** Taxa de elitismo em **10%** e a **melhor taxa de cruzamento** obtida no experimento anterior.
* **Saída:** Gere um único gráfico ilustrando o comportamento do melhor indivíduo ao longo das gerações para as três diferentes taxas de mutação.

---

## 5. Observações Importantes

1. **Individualidade:** O EPC deve ser realizado individualmente.
2. **Organização:** Os resultados devem ser entregues em sequência, respeitando a numeração do EPC.
3. **Restrição de Código:** **Não é permitido o uso de bibliotecas prontas** para a implementação do algoritmo genético (toda a lógica de população, seleção, cruzamento e mutação deve ser desenvolvida do zero).
4. **Política de Atraso:** * A entrega após a data e horário definidos implicará em um desconto de **2 pontos**.
* Após 24 horas de atraso, será descontado mais **1 ponto** na nota.
* O EPC **não será mais recebido** após 48h de atraso.