from typing import List
from AutomataState import EstadoDeAutomato


class Automato:
    def __init__(self, estados: List[EstadoDeAutomato], simbolosTerminais: List[str], estadosIniciais: List[int], estadosDeAceitacao: List[int]) -> None:
        self.estados: List[EstadoDeAutomato] = estados
        self.simbolosTerminais: List[str] = simbolosTerminais
        self.estadosIniciais = estadosIniciais
        self.estadosDeAceitacao = estadosDeAceitacao
        pass

    def adicionaTransicao(self, estadoOrigem: str, estadoDestino: str, transicao: str) -> None:
        self.estados[int(estadoOrigem)].adicionaTransicao(
            estadoDestino, transicao)
        return

    def testaSequenciaPorTodosEstados(self, sequencia) -> bool:
        # TODO: Corrigir para funcionar com Lambda
        if sequencia == '-':
            return False
        for estadoInicial in self.estadosIniciais:
            eSequenciaValida = self.testaSequencia(sequencia, 0, estadoInicial)
            if eSequenciaValida is True:
                return True

    def testaSequencia(self, sequencia: str, indexDaSequencia: int, estado: int) -> bool:
        if len(sequencia) == indexDaSequencia:
            if str(estado) in self.estadosDeAceitacao:
                return True
            else:
                return False

        estadoDoAutomato: EstadoDeAutomato = self.estados[estado]
        simboloAtual = sequencia[indexDaSequencia]
        resultados = list()
        if simboloAtual in estadoDoAutomato.transicoes.keys():
            for proximoEstado in estadoDoAutomato.transicoes[simboloAtual]:
                resultados.append(self.testaSequencia(
                    sequencia=sequencia, indexDaSequencia=indexDaSequencia+1, estado=proximoEstado))
        return True in resultados
