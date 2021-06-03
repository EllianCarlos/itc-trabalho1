from typing import Dict, List


#
#   Define o estado de um autômato, ex:
#
#       __
#     /    \
#     \ qx /
#      ----
#       
#
#
#

class EstadoDeAutomato:

    # Inicia a classe
    def __init__(self, number) -> None:
        # Identificador do estado
        self.identificador: str = str(number)

        # Inicializa dicionário com a lista de transições
        self.transicoes: Dict[str, List[int]] = {}
        # sempre coloca uma transição para si mesmo na cadeia nula:
        self.transicoes["-"].append(int(self))
        pass


    # Adiciona uma transição no estado
    def adicionaTransicao(self, estadoDestino: str, transicao: str) -> None:
        if transicao in self.transicoes.keys():
            self.transicoes[transicao].append(int(estadoDestino))
        else:
            self.transicoes[transicao] = list()
            self.transicoes[transicao].append(int(estadoDestino))
        return
