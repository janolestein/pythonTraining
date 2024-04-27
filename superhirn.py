import art as art
import random as random
import os as os
import itertools as itertools

gameIsOver = 0
gameIsWon = False
colorOptions = [1, 2, 3, 4, 5, 6, 7, 8]
secretPick = []
gameState = ""
allSolutions = set(itertools.product(colorOptions, repeat=5))


def drawGameState():
    os.system("clear")
    print(gameState)


def makePseudoRandomGuess():
    randomPick = []
    global allSolutions
    randomPick = allSolutions.pop()
    return randomPick


def removeImpossibleGuesses(guess):
    global allSolutions
    correctPositionsOfGuess, correctColorsOfGuess = determineCorrectPicks(
        guess, secretPick
    )
    tempAllSolutions = allSolutions.copy()
    for elem in tempAllSolutions:
        correctPositionsOfElem, correctColorsOfElem = determineCorrectPicks(elem, guess)
        if (
            correctPositionsOfGuess != correctPositionsOfElem
            or correctColorsOfGuess != correctColorsOfElem
        ):
            allSolutions.remove(elem)
    print("Size of Set: " + str(len(allSolutions)))


def determineCorrectPicks(actualPick, pickToCheckAgainst):
    correctPositions: int = 0
    correctColor = 0
    incorectGuesses = []
    incorecctAnswers = []

    for guess, answer in zip(actualPick, pickToCheckAgainst):
        if guess == answer:
            correctPositions += 1
        else:
            incorectGuesses.append(guess)
            incorecctAnswers.append(answer)

    for elem in incorectGuesses:
        if elem in incorecctAnswers:
            incorecctAnswers.remove(elem)
            correctColor += 1

    return correctPositions, correctColor


def checkInputAgainstSecretPick(inputList):
    global secretPick
    global gameIsWon

    correctPositions, correctColor = determineCorrectPicks(inputList, secretPick)

    if correctPositions == len(secretPick):
        gameIsWon = True

    return correctPositions, correctColor


def selectSecretPick():
    for _ in range(5):
        secretPick.append(colorOptions[random.randint(0, len(colorOptions) - 1)])

    global gameState
    gameState += (
        "\n###########################\n"
        + "Secret Pick:\n"
        + str(secretPick)
        + "\n##########################\n"
    )


def gameLoop(letCpuPlay):
    userInput = ""
    global gameIsOver
    global gameIsWon
    global gameState
    while gameIsOver < 10:
        if letCpuPlay == True:
            inputList = makePseudoRandomGuess()
            removeImpossibleGuesses(inputList)
        else:
            userInput = input(
                "Please make a guess (five numbers, seperated with a comma):"
            )
            # TODO: validate input
            inputList = list(map(int, userInput.split(",")))
            if len(inputList) != 5:
                print("Please Enter 5 Numbers")
                continue
        correctPositions, correctColor = checkInputAgainstSecretPick(inputList)
        if gameIsWon == True:
            break

        gameState += (
            "\n###########################\n"
            + str(inputList)
            + "\nYou have "
            + str(correctPositions)
            + " correct Guesses\n"
            + "and you have "
            + str(correctColor)
            + " correct Color(s)"
            + "\n##########################\n"
        )
        drawGameState()
        gameIsOver += 1

    if gameIsWon == True:
        art.tprint("You Win!")
    else:
        art.tprint("You Lose...")


def startNewGame(letCpuPlay=False):
    print("New Game started")
    selectSecretPick()
    drawGameState()
    gameLoop(letCpuPlay)


def main():
    art.tprint("Superhirn")
    print("To start a new game press n")
    print("To let the Cpu play press c")
    print("To quit press q")
    userInput = ""
    userInput = input("Please Enter a selection:")
    if userInput == "n":
        print("New Game selected")
        startNewGame()
    elif userInput == "c":
        print("New Cpu Game selected")
        startNewGame(letCpuPlay=True)
    elif userInput == "q":
        print("quiting...")
        return
    else:
        print("No Valid input, quiting program")


main()
