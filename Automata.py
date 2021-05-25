from typing import List
from AutomataState import AutomataState


class Automata:
    def __init__(self, states: List[AutomataState], terminalSymbols: List[str], initialStates: List[int], acceptanceStates: List[int]) -> None:
        self.states: List[AutomataState] = states
        self.terminalSymbols: List[str] = terminalSymbols
        self.initialStates = initialStates
        self.acceptanceStates = acceptanceStates
        pass

    def addTransition(self, stateSource: str, stateDestination: str, transition: str) -> None:
        self.states[int(stateSource)].addTransition(stateDestination, transition)
        return

    def printAllValues(self):
        for i in self.states:
            print(i.transitions.values());

    def nextStateFromTransition(self, automataState: str) -> AutomataState:
        return;


    def testSequence(self, sequence) -> bool:
        # Funciona apenas para AFD
        state = self.initialStates[0]
        for symbol in sequence:
            if symbol == '-':
                return False
            state = self.states[state].transitions[symbol]
        return str(state) in self.acceptanceStates
