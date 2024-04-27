import random as random
def makeRandomGuess(colorOptions):
    randomPick = []
    for _ in range(5):
        randomPick.append(colorOptions[random.randint(0, len(colorOptions) - 1)])

    return randomPick
