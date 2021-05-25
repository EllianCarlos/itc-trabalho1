from typing import Dict


class AutomataState:
    def __init__(self, number) -> None:
        self.number: str = str(number)
        self.transitions: Dict[str, int] = {}
        pass

    def addTransition(self, stateDestination: str, transition: str) -> None:
        self.transitions[transition] = int(stateDestination)
        return
