from Automata import *
from AutomataState import *
from typing import List

#
#   Define as funções responsáveis por ler o arquivo e gerar as estruturas necessárias
#
#



# Le o arquivo de entrada e retorna uma lista com
# os estados do automato
def recebeEstados() -> List[EstadoDeAutomato]:

    # Define número máximo e mínimo de estados 
    numeroMaximoDeEstados = 10
    numeroMinimoDeEstados = 1


    # Verifica se está no intervalo de máximo e mínimo aceito
    # de estados
    numeroDeEstados = int(input(''))
    assert (numeroDeEstados >= numeroMinimoDeEstados and
            numeroDeEstados <= numeroMaximoDeEstados)

    # Inicializa estados
    estados = []
    for i in range(numeroDeEstados):
        # Cria novo estado
        estado = EstadoDeAutomato(i)
        # Adiciona na lista de estados
        estados.append(estado)
    return estados


## Lê a lista de símbolos terminais, retorna uma lista destes símbolos
def recebeSimbolosTerminais() -> List[str]:
    numeroMaximoDeSimbolosTerminais = 10

    # divide a entrada pelos espaços
    entradaDoPrograma = input('').split(' ')

    # Primeiro símbolo = número de estados terminais
    numeroDeSimbolosTerminais = int(entradaDoPrograma[0])

    # Verifica se número está no range
    assert (numeroDeSimbolosTerminais <= numeroMaximoDeSimbolosTerminais)
    simbolosTerminais = entradaDoPrograma[1:]
    return simbolosTerminais


def recebeEstadosIniciais() -> List[str]:
    numeroMaximoDeEstadosIniciais = 10
    entradaDoPrograma = input('').split(' ')
    numeroDeEstadosIniciais = int(entradaDoPrograma[0])
    assert (numeroDeEstadosIniciais <= numeroMaximoDeEstadosIniciais)
    estadosInicias = entradaDoPrograma[1:]
    if numeroDeEstadosIniciais == 1:
        estadosInicias.append(0)
    return estadosInicias


def recebeEstadosDeAceitacao() -> List[str]:
    numeroMaximoDeEstadosDeAceitacao = 10
    numeroMinimoDeEstadosDeAceitacao = 0
    entradaDoPrograma = input('').split(' ')
    numeroDeEstadosDeAceitacao = int(entradaDoPrograma[0])
    assert (numeroDeEstadosDeAceitacao >= numeroMinimoDeEstadosDeAceitacao and
            numeroDeEstadosDeAceitacao <= numeroMaximoDeEstadosDeAceitacao)
    estadosDeAceitacao = entradaDoPrograma[1:]
    return estadosDeAceitacao


def recebeTransicoes(automata: Automato) -> None:
    numeroMaximoDeTransacoes = 50
    numeroDeTransacoes = int(input(''))
    assert (numeroDeTransacoes <= numeroMaximoDeTransacoes)
    for _ in range(numeroDeTransacoes):
        entradaDoPrograma = input('').split(' ')
        simboloDaTransicao = entradaDoPrograma[1]
        estadoOrigem = entradaDoPrograma[0]
        estadoDestino = entradaDoPrograma[2]
        automata.adicionaTransicao(estadoOrigem, estadoDestino, simboloDaTransicao)


def recebeSequenciasDeTeste() -> List[str]:
    numeroDeSequencias = int(input(''))
    sequenciasDeTeste = []
    for _ in range(numeroDeSequencias):
        sequencia = input('')
        sequenciasDeTeste.append(sequencia)
    return sequenciasDeTeste
