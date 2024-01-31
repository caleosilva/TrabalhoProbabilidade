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