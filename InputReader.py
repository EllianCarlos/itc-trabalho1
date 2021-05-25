from Automata import Automata
from typing import List
from AutomataState import AutomataState


def getStates() -> List[AutomataState]:
    maxNumberOfStates = 10
    minNumberOfStates = 1
    numberOfStates = int(input(''))
    assert (numberOfStates >= minNumberOfStates and
            numberOfStates <= maxNumberOfStates)
    states = []
    for i in range(numberOfStates):
        state = AutomataState(i)
        states.append(state)
    return states


def getTerminalSymbols() -> List[str]:
    maxNumberOfTerminalSymbols = 10
    readInput = input('').split(' ')
    numberOfTerminalSymbols = int(readInput[0])
    assert (numberOfTerminalSymbols <= maxNumberOfTerminalSymbols)
    terminalSymbols = readInput[1:]
    return terminalSymbols


def getInitialStates() -> List[str]:
    maxNumberOfInitialStates = 10
    readInput = input('').split(' ')
    numberOfInitialStates = int(readInput[0])
    assert (numberOfInitialStates <= maxNumberOfInitialStates)
    initialStates = readInput[1:]
    if numberOfInitialStates == 1:
        initialStates.append(0)
    return initialStates


def getAcceptanceStates() -> List[str]:
    maxNumberOfAcceptanceStates = 10
    minNumberOfAcceptanceStates = 0
    readInput = input('').split(' ')
    numberOfAcceptanceStates = int(readInput[0])
    assert (numberOfAcceptanceStates >= minNumberOfAcceptanceStates and
            numberOfAcceptanceStates <= maxNumberOfAcceptanceStates)
    acceptanceStates = readInput[1:]
    return acceptanceStates


def getTransitions(automata: Automata) -> None:
    maxNumberOfTransitions = 50
    numberOfTransitions = int(input(''))
    assert (numberOfTransitions <= maxNumberOfTransitions)
    for _ in range(numberOfTransitions):
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
