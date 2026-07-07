import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from ag import AlgoritmoGenetico

# Caminho do diretório de artefatos para salvar as imagens caso exista
ARTIFACT_DIR = r"C:\Users\Usuário\.gemini\antigravity\brain\153d5e71-8a90-4e7b-985e-0f81a3b4a3d3"

def salvar_grafico(fig, nome_arquivo):
    """Salva a figura no diretório de trabalho e no diretório de artefatos, se ele existir."""
    # Salva no diretório atual
    fig.savefig(nome_arquivo, dpi=300, bbox_inches='tight')
    print(f"Gráfico salvo no diretório atual como: {nome_arquivo}")
    
    # Salva no diretório de artefatos
    if os.path.exists(ARTIFACT_DIR):
        caminho_artefato = os.path.join(ARTIFACT_DIR, nome_arquivo)
        fig.savefig(caminho_artefato, dpi=300, bbox_inches='tight')
        print(f"Gráfico copiado para os artefatos em: {caminho_artefato}")

def executar_simulacao_1():
    print("==================================================")
    print("INICIANDO SIMULAÇÃO 1: VARIAÇÃO DA TAXA DE CRUZAMENTO")
    print("Configurações fixas: Mutação = 1%, Elitismo = 10%, População = 100, Gerações = 200")
    print("==================================================")
    
    taxas_cruzamento = [0.70, 0.80, 0.90]
    historicos = {}
    melhores_individuos = {}
    
    for tc in taxas_cruzamento:
        print(f"\nRodando AG com taxa de cruzamento de {int(tc*100)}%...")
        ag = AlgoritmoGenetico(
            tam_populacao=100,
            geracoes=200,
            taxa_cruzamento=tc,
            taxa_mutacao=0.01,
            taxa_elitismo=0.10
        )
        historico, melhor = ag.executar()
        historicos[tc] = historico
        melhores_individuos[tc] = melhor
        print(f"Resultado final para Cruzamento={int(tc*100)}%: Melhor x={melhor.get_x():.6f}, Fitness={melhor.evaluate():.6f}")

    # Plotando os resultados da Simulação 1
    fig, ax = plt.subplots(figsize=(10, 6))
    for tc in taxas_cruzamento:
        ax.plot(historicos[tc], label=f"Cruzamento {int(tc*100)}% (Final: {melhores_individuos[tc].evaluate():.5f})")
    
    ax.axhline(y=2.85027, color='r', linestyle='--', alpha=0.7, label="Máximo Global Conhecido (2.85027)")
    ax.set_title("Simulação 1: Evolução do Melhor Indivíduo por Taxa de Cruzamento")
    ax.set_xlabel("Geração")
    ax.set_ylabel("Fitness (Valor da Função)")
    ax.legend()
    ax.grid(True, linestyle=':', alpha=0.6)
    
    salvar_grafico(fig, "simulacao1_cruzamento.png")
    plt.close(fig)
    
    # Determina a melhor taxa de cruzamento (aquela que obteve o maior fitness final)
    melhor_tc = max(taxas_cruzamento, key=lambda tc: melhores_individuos[tc].evaluate())
    print(f"\n--> Melhor taxa de cruzamento identificada: {int(melhor_tc*100)}% (Fitness: {melhores_individuos[melhor_tc].evaluate():.6f})")
    return melhor_tc

def executar_simulacao_2(melhor_tc):
    print("\n==================================================")
    print("INICIANDO SIMULAÇÃO 2: VARIAÇÃO DA TAXA DE MUTAÇÃO")
    print(f"Configurações fixas: Cruzamento = {int(melhor_tc*100)}%, Elitismo = 10%, População = 100, Gerações = 200")
    print("==================================================")
    
    taxas_mutacao = [0.01, 0.05, 0.10]
    historicos = {}
    melhores_individuos = {}
    
    for tm in taxas_mutacao:
        print(f"\nRodando AG com taxa de mutação de {int(tm*100)}%...")
        ag = AlgoritmoGenetico(
            tam_populacao=100,
            geracoes=200,
            taxa_cruzamento=melhor_tc,
            taxa_mutacao=tm,
            taxa_elitismo=0.10
        )
        historico, melhor = ag.executar()
        historicos[tm] = historico
        melhores_individuos[tm] = melhor
        print(f"Resultado final para Mutação={int(tm*100)}%: Melhor x={melhor.get_x():.6f}, Fitness={melhor.evaluate():.6f}")

    # Plotando os resultados da Simulação 2
    fig, ax = plt.subplots(figsize=(10, 6))
    for tm in taxas_mutacao:
        ax.plot(historicos[tm], label=f"Mutação {int(tm*100)}% (Final: {melhores_individuos[tm].evaluate():.5f})")
    
    ax.axhline(y=2.85027, color='r', linestyle='--', alpha=0.7, label="Máximo Global Conhecido (2.85027)")
    ax.set_title(f"Simulação 2: Evolução do Melhor Indivíduo por Taxa de Mutação (Cruzamento={int(melhor_tc*100)}%)")
    ax.set_xlabel("Geração")
    ax.set_ylabel("Fitness (Valor da Função)")
    ax.legend()
    ax.grid(True, linestyle=':', alpha=0.6)
    
    salvar_grafico(fig, "simulacao2_mutacao.png")
    plt.close(fig)

if __name__ == "__main__":
    melhor_cruzamento = executar_simulacao_1()
    executar_simulacao_2(melhor_cruzamento)
    print("\nSimulações concluídas com sucesso!")
