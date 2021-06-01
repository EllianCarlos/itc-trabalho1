from typing import Dict, List


class EstadoDeAutomato:
    def __init__(self, number) -> None:
        self.identificador: str = str(number)
        self.transicoes: Dict[str, List[int]] = {}
        pass

    def adicionaTransicao(self, estadoDestino: str, transicao: str) -> None:
        if transicao in self.transicoes.keys():
            self.transicoes[transicao].append(int(estadoDestino))
        else:
            self.transicoes[transicao] = list()
            self.transicoes[transicao].append(int(estadoDestino))
        return
