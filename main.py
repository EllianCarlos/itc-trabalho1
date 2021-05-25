from InputReader import getAcceptanceStates, getInitialStates, getStates, getTerminalSymbols, getTestCases, getTransitions
from Automata import Automata


if __name__ == "__main__":
    states = getStates()
    terminalSymbols = getTerminalSymbols()
    initialStates = getInitialStates()
    acceptanceStates = getAcceptanceStates()
    automata = Automata(states, terminalSymbols,
                        initialStates, acceptanceStates)
    getTransitions(automata)
    testSequences = getTestCases()
    for sequence in testSequences:
        if automata.testSequence(sequence):
            print("aceita")
        else:
            print("rejeita")
