import random

targetWord='s'
characters="abcdefghijklmnopqrstuvwxyz"
targetLength = len(targetWord)

def monkeyGuess(characters, targetLength):
    randomGuess = ""
    for character in range(targetLength):
        randomGuess = randomGuess + random.choice(characters)
    return randomGuess
    
def monkeyExperiment():
    guess = ""
    numGuesses = 0
    while guess != targetWord:
        guess = monkeyGuess(characters, targetLength)
        numGuesses = numGuesses + 1
    return numGuesses

def monkeySim(trials):
    high = 0
    guessSum = 0.
    low = 9999999
    for trial in range(trials):
        numGuesses = monkeyExperiment()
        if numGuesses > high:
            high = numGuesses
        if numGuesses < low:
            low = numGuesses
        guessSum += numGuesses
    return low, high, guessSum

trials = 1 #can change this
low, high, guessSum = monkeySim(trials)
average = guessSum / trials
print "Fewest number of guesses: " + str(low)
print "Greatest number of guesses: " + str(high)
print "Mean number of guesses: " + str(average)