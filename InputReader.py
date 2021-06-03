from Automata import *
from AutomataState import *
from typing import List


def recebeEstados() -> List[EstadoDeAutomato]:
    numeroMaximoDeEstados = 10
    numeroMinimoDeEstados = 1
    numeroDeEstados = int(input(''))
    assert (numeroDeEstados >= numeroMinimoDeEstados and
            numeroDeEstados <= numeroMaximoDeEstados)
    estados = []
    for i in range(numeroDeEstados):
        estado = EstadoDeAutomato(i)
        estados.append(estado)
    return estados


def recebeSimbolosTerminais() -> List[str]:
    numeroMaximoDeSimbolosTerminais = 10
    entradaDoPrograma = input('').split(' ')
    numeroDeSimbolosTerminais = int(entradaDoPrograma[0])
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
