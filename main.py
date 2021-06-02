from InputReader import recebeEstadosDeAceitacao, recebeEstadosIniciais, recebeEstados, recebeSimbolosTerminais, recebeSequenciasDeTeste, recebeTransicoes
from Automata import Automato


if __name__ == "__main__":
    estados = recebeEstados()
    simbolosTerminais = recebeSimbolosTerminais()
    estadosIniciais = recebeEstadosIniciais()
    estadosDeAceitacao = recebeEstadosDeAceitacao()
    Automato = Automato(estados, simbolosTerminais,
                        estadosIniciais, estadosDeAceitacao)
    recebeTransicoes(Automato)
    sequenciasDeTeste = recebeSequenciasDeTeste()
    for sequencia in sequenciasDeTeste:
        if Automato.testaSequenciaPorTodosEstadosIniciais(sequencia):
            print("aceita")
        else:
            print("rejeita")
