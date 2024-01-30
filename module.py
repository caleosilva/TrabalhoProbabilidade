import numpy as np
import statistics

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
    estatisticas['coeficiente_variacao'] = (np.std(lista) / np.mean(lista)) * 100

    return estatisticas