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

    def testaSequenciaPorTodosEstadosIniciais(self, sequencia) -> bool:
        if sequencia == '-':
            # Não faz nada
            assert(True)
        for estadoInicial in self.estadosIniciais:
            eSequenciaValida = self.testaSequencia(sequencia, 0, estadoInicial)
            if eSequenciaValida is True:
                return True
        return False

    def testaSequencia(self, sequencia: str, indexDaSequencia: int, estado: int) -> bool:

        print("Testando sequência...")

        # Se está no útlimo estado, verifica se é estado de aceitação e retorna
        print("tamanho da sequencia: ",len(sequencia))
        print("índice atual:", indexDaSequencia)
        ## TODO: VERIFICAR SE O ÍNDICE ESTÁ CORRETO
        if len(sequencia) == indexDaSequencia:
            if str(estado) in self.estadosDeAceitacao:
                return True
            else:
                return False

        # Define estado atual como próximo estado
        estadoDoAutomato: EstadoDeAutomato = self.estados[estado]
        print("Estado atual: ", estadoDoAutomato.identificador)
        print("Transições: ", estadoDoAutomato.transicoes)

        # Define símbolo atual como próximo símbolo da sequencia
        simboloAtual = sequencia[indexDaSequencia]
        print("Símbolo atual: ", sequencia[indexDaSequencia])


        resultadosDaRecursao = list()

        # Verifica se o símbolo atual está na lista de transições 
        if simboloAtual in estadoDoAutomato.transicoes.keys():
            print("Símbolo atual está nas transicoes, vai para próximo")
            # Se sim, avança para o(s) próximos estados e repete
            for proximoEstado in estadoDoAutomato.transicoes[simboloAtual]:
                resultadosDaRecursao.append(
                    self.testaSequencia(
                        sequencia=sequencia, indexDaSequencia=indexDaSequencia+1, estado=proximoEstado
                    )
                )
        return True in resultadosDaRecursao
