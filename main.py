from API import get_data_from_google_sheets_api
from module import calcular_estatisticas, editar_renda_familiar


def main():
    data = get_data_from_google_sheets_api()
    
    # print(data)

    # Dicionários vazios para armazenar listas de valores para cada chave
    idade = [] #---------------------------------------------------------------------------
    sexo = []
    semestre = [] #---------------------------------------------------------------------------
    renda_familiar = [] #---------------------------------------------------------------------------
    trabalha = []
    mora = []
    tempo_estudo_diario = [] #---------------------------------------------------------------------------
    periodo = []
    infra_sala = []
    infra_biblioteca = []
    infra_geral = []
    internet = []
    laboratorio = []
    qualidade_ensino = []
    atendimento_secretaria = []
    relacao_prof_aluno = []
    metodos_avaliacao = []
    dedicacao_semanal = []
    participacao_intensa = []
    participacao_setenta = []

    # Adicionando informações nos dicionarios acima
    for resposta in data:
        idade.append(resposta['Idade'])
        sexo.append(resposta['Sexo'])
        semestre.append(resposta['Semestre'])
        
        renda_familiar.append(editar_renda_familiar(resposta['RendaFamiliar']))
        
        
        
        trabalha.append(resposta['Trabalha'])
        mora.append(resposta['Mora'])
        tempo_estudo_diario.append(resposta['TempoEstudoDiario'])
        periodo.append(resposta['Periodo'])
        infra_sala.append(resposta['InfraSala'])
        infra_biblioteca.append(resposta['InfraBiblioteca'])
        infra_geral.append(resposta['InfraGeral'])
        internet.append(resposta['Internet'])
        laboratorio.append(resposta['Laboratorio'])
        qualidade_ensino.append(resposta['QualidadeEnsino'])
        atendimento_secretaria.append(resposta['AtendimentoSecretaria'])
        relacao_prof_aluno.append(resposta['RelacaoProfAluno'])
        metodos_avaliacao.append(resposta['MetodosAvaliacao'])
        dedicacao_semanal.append(resposta['DedicacaoSemanal'])
        participacao_intensa.append(resposta['ParticipacaoIntensa'])
        participacao_setenta.append(resposta['ParticipacaoSetenta'])

    # Lista com cada informação:
    # print("Idade:", idade)
    # estatisticasIdade = calcular_estatisticas(idade)
    print("Estatisticas da Idade: ", calcular_estatisticas(idade), '\n\n')
    
    print("Estatisticas do Semestre: ", calcular_estatisticas(semestre), '\n\n')
    
    print("Estatisticas da renda familiar: ", calcular_estatisticas(renda_familiar), '\n\n')
    
    print("Estatisticas do tempo de estudo diario: ", calcular_estatisticas(tempo_estudo_diario), '\n\n')


if __name__ == "__main__":
    main()
