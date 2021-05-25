from typing import Dict


class AutomataState:
    def __init__(self, number, transitions: Dict[str, str] = {}) -> None:
        self.number: str = str(number)
        self.transitions: Dict[str, str] = transitions
        pass

    def addTransition(self, stateDestination: str, transition: str) -> None:
        self.transitions[transition] = stateDestination
        return
