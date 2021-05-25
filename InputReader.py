from Automata import Automata
from typing import List
from AutomataState import AutomataState


def getStates() -> List[AutomataState]:
    maxNumberOfStates = 10
    minNumberOfStates = 1
    numberOfStates = input('')
    assert (int(numberOfStates) >= minNumberOfStates and
            int(numberOfStates) <= maxNumberOfStates)
    states = []
    for i in range(int(numberOfStates)):
        state = AutomataState(i)
        states.append(state)
    return states


def getTerminalSymbols() -> List[str]:
    maxNumberOfTerminalSymbols = 10
    readInput = input('').split(' ')
    numberOfTerminalSymbols = readInput[0]
    assert (int(numberOfTerminalSymbols) <= maxNumberOfTerminalSymbols)
    terminalSymbols = readInput[1:]
    return terminalSymbols


def getInitialStates() -> List[str]:
    maxNumberOfInitialStates = 10
    readInput = input('').split(' ')
    numberOfInitialStates = readInput[0]
    assert (int(numberOfInitialStates) <= maxNumberOfInitialStates)
    initialStates = readInput[1:]
    if numberOfInitialStates == '1':
        initialStates.append(0)
    return initialStates


def getAcceptanceStates() -> List[str]:
    maxNumberOfAcceptanceStates = 10
    minNumberOfAcceptanceStates = 0
    readInput = input('').split(' ')
    numberOfAcceptanceStates = readInput[0]
    assert (int(numberOfAcceptanceStates) >= minNumberOfAcceptanceStates and
            int(numberOfAcceptanceStates) <= maxNumberOfAcceptanceStates)
    acceptanceStates = readInput[1:]
    return acceptanceStates


def getTransitions(automata: Automata) -> None:
    maxNumberOfTransitions = 50
    numberOfTransitions = input('')
    assert (int(numberOfTransitions) <= maxNumberOfTransitions)
    for _ in range(int(numberOfTransitions)):
        readInput = input('').split(' ')
        transition = readInput[1]
        firstState = readInput[0]
        secondState = readInput[2]
        automata.addTransition(firstState, secondState, transition)


def getTestCases() -> List[str]:
    numberOfCases = int(input(''))
    testCases = []
    for _ in range(numberOfCases):
        case = input('')
        testCases.append(case)
    return testCases
