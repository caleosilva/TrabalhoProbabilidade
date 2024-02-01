import numpy as np
import statistics
import matplotlib.pyplot as plt


def calcular_estatisticas(lista):
    estatisticas = {}

    # Mínimo
    estatisticas['min'] = np.min(lista)
    # Máximo
    estatisticas['max'] = np.max(lista)
    # Média
    estatisticas['media'] = np.mean(lista)
    # Moda
    estatisticas['moda'] = statistics.mode(lista)
    # Mediana
    estatisticas['mediana'] = np.median(lista)
    # Amplitude
    estatisticas['amplitude'] = np.ptp(lista)
    # Desvio Padrão
    estatisticas['desvio_padrao'] = np.std(lista)
    # Variância
    estatisticas['variancia'] = np.var(lista)
    # Coeficiente de Variação
    estatisticas['coeficiente_variacao'] = (
        np.std(lista) / np.mean(lista)) * 100

    return estatisticas


def editar_renda_familiar(renda):
    if (renda == "Até 1 salário mínimo"):
        return 1
    elif (renda == "De 1 a 3 salários mínimos"):
        return 2
    elif (renda == "De 3 a 5 salários mínimos"):
        return 4
    elif (renda == "De 5 a 7 salários mínimos"):
        return 6
    elif (renda == "Mais de 7 salários mínimos"):
        return 8
    else:
        return 0


def rendaFamiliar_trabalho(renda_familiar, trabalha):
    # Separando as rendas familiares por grupo de 'Trabalha?' (Sim / Não)
    renda_trabalha_sim = [renda_familiar[i]
                          for i in range(len(renda_familiar)) if trabalha[i] == 'Sim']
    renda_trabalha_nao = [renda_familiar[i]
                          for i in range(len(renda_familiar)) if trabalha[i] == 'Não']

    # Configuração do histograma
    plt.figure(figsize=(8, 6))
    plt.hist([renda_trabalha_sim, renda_trabalha_nao], bins=range(min(
        renda_familiar), max(renda_familiar) + 1, 1), label=['Trabalha', 'Não Trabalha'])
    plt.title('Relação da renda familiar com o fato de trabalhar ou não')
    plt.xlabel('Renda Familiar')
    plt.ylabel('Frequência')
    plt.legend()
    plt.grid(True)
    plt.show()


def moraSozinho_trabalha(mora, trabalha):
    # Contagem de pessoas que moram em cada categoria e trabalham ou não
    moradia_trabalha_sim = {categoria: sum(1 for i in range(len(
        mora)) if mora[i] == categoria and trabalha[i] == 'Sim') for categoria in set(mora)}
    moradia_trabalha_nao = {categoria: sum(1 for i in range(len(
        mora)) if mora[i] == categoria and trabalha[i] == 'Não') for categoria in set(mora)}
    categorias = list(set(mora))

    # Configuração do gráfico de barras empilhadas
    plt.figure(figsize=(10, 6))
    plt.bar(categorias, [moradia_trabalha_sim[categoria]
            for categoria in categorias], label='Trabalha: Sim')
    plt.bar(categorias, [moradia_trabalha_nao[categoria] for categoria in categorias], bottom=[
            moradia_trabalha_sim[categoria] for categoria in categorias], label='Trabalha: Não')
    plt.xlabel('Com quem mora')
    plt.ylabel('Número de Pessoas')
    plt.title('Relação entre Moradia e Trabalho')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def tempoEstudoDiario_periodo(tempo_estudo_diario, periodo):
    # Criando dicionários para contar a frequência de tempo de estudo para cada período
    diurno_counts = {}
    noturno_counts = {}

    for tempo, periodo_estudo in zip(tempo_estudo_diario, periodo):
        if periodo_estudo == 'Diurno':
            diurno_counts[tempo] = diurno_counts.get(tempo, 0) + 1
        else:
            noturno_counts[tempo] = noturno_counts.get(tempo, 0) + 1

    # Configuração do gráfico de barras agrupadas
    plt.figure(figsize=(10, 6))
    bar_width = 0.35
    index = range(1, max(max(diurno_counts.keys()),
                  max(noturno_counts.keys())) + 1)

    plt.bar(index, [diurno_counts.get(i, 0)
            for i in index], bar_width, label='Diurno')
    plt.bar([i + bar_width for i in index], [noturno_counts.get(i, 0)
            for i in index], bar_width, label='Noturno')

    plt.xlabel('Tempo de Estudo Diário')
    plt.ylabel('Frequência')
    plt.title('Tempo de Estudo Diário por Período de Estudo')
    plt.xticks([i + bar_width/2 for i in index], index)
    plt.legend()
    plt.tight_layout()
    plt.show()


def dedicacao_participacao(dedicacao_semanal, participacao_setenta):
    # Contagem de respostas para cada variável
    dedicacao_counts = {'Sim': dedicacao_semanal.count(
        'Sim'), 'Não': dedicacao_semanal.count('Não')}
    participacao_counts = {'Sim': participacao_setenta.count(
        'Sim'), 'Não': participacao_setenta.count('Não')}

    # Configuração do gráfico de barras agrupadas
    labels = ['Sim', 'Não']
    dedicacao_values = [dedicacao_counts[label] for label in labels]
    participacao_values = [participacao_counts[label] for label in labels]

    x = range(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x, dedicacao_values, width, label='Dedicação Semanal')
    rects2 = ax.bar([i + width for i in x], participacao_values,
                    width, label='Participação em Aulas')

    ax.set_ylabel('Frequência')
    ax.set_title('Comparação de Dedicação Semanal e Participação em Aulas')
    ax.set_xticks([i + width/2 for i in x])
    ax.set_xticklabels(labels)
    ax.legend()

    plt.tight_layout()
    plt.show()


def infraestrutura_qualidadeEnsino(infra_geral, qualidade_ensino):
    # Contagem das respostas
    contagem_combinacoes = {}
    for infra, qualidade in zip(infra_geral, qualidade_ensino):
        comb = (infra, qualidade)
        if comb in contagem_combinacoes:
            contagem_combinacoes[comb] += 1
        else:
            contagem_combinacoes[comb] = 1

    # Categorias únicas
    categorias_infra = sorted(set(infra_geral))
    categorias_qualidade = sorted(set(qualidade_ensino))

    # Preparando dados para o gráfico de barras empilhadas
    dados = []
    for infra in categorias_infra:
        valores = [contagem_combinacoes.get((infra, qualidade), 0) for qualidade in categorias_qualidade]
        dados.append(valores)

    # Convertendo para array numpy e calculando as alturas das barras empilhadas
    dados = np.array(dados)
    alturas_barras = np.cumsum(dados, axis=0)

    # Plotagem do gráfico
    fig, ax = plt.subplots()
    cores = ['tab:blue', 'tab:orange', 'tab:green']
    for i in range(len(categorias_qualidade)):
        if i == 0:
            ax.bar(categorias_infra, dados[i], color=cores[i], label=categorias_qualidade[i])
        else:
            ax.bar(categorias_infra, dados[i], bottom=alturas_barras[i-1], color=cores[i], label=categorias_qualidade[i])

    # Adicionando legenda
    ax.legend(title="Qualidade de Ensino", bbox_to_anchor=(1, 1), loc='upper left')

    # Adicionando rótulos
    ax.set_xlabel('Estrutura Geral da Universidade')
    ax.set_ylabel('Frequência')

    # Adicionando título
    plt.title('Análise da Estrutura Geral da Universidade em relação à Qualidade de Ensino')

    # Exibindo o gráfico
    plt.show()


def infraestrutura_participacaoIntensa(infra_geral, participacao_intensa):
    # Contagem das respostas
    contagem_combinacoes = {}
    for infra, participacao in zip(infra_geral, participacao_intensa):
        comb = (infra, participacao)
        if comb in contagem_combinacoes:
            contagem_combinacoes[comb] += 1
        else:
            contagem_combinacoes[comb] = 1

    # Categorias únicas
    categorias_infra = sorted(set(infra_geral))
    categorias_participacao = sorted(set(participacao_intensa))

    # Preparando dados para o gráfico
    num_categorias_infra = len(categorias_infra)
    largura_barra = 0.35
    posicao_barras = np.arange(num_categorias_infra)

    # Plotagem do gráfico
    fig, ax = plt.subplots()
    for i, participacao in enumerate(categorias_participacao):
        dados = [contagem_combinacoes.get((infra, participacao), 0) for infra in categorias_infra]
        ax.bar(posicao_barras + i * largura_barra, dados, largura_barra, label=participacao)

    # Adicionando legendas
    ax.set_xticks(posicao_barras + largura_barra / 2)
    ax.set_xticklabels(categorias_infra)
    ax.legend(title="Participação Intensa")

    # Adicionando rótulos
    ax.set_xlabel('Avaliação da Estrutura Geral da Universidade')
    ax.set_ylabel('Frequência')

    # Adicionando título
    plt.title('Análise da Estrutura Geral da Universidade em relação à Participação Intensa nos Trabalhos')

    # Exibindo o gráfico
    plt.show()
