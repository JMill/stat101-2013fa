import random

targetWord='hi'
characters="abcdefghijklmnopqrstuvwxyz"
targetLength = len(targetWord)
guess = ""
numGuesses = 0

def monkeyGuess(characters, targetLength):
    """
    Generates a random permutation of specified length, composed of
    the specified letters.
    
    Returns: a random string, such as "jadf" if 4 characters were specified,
    or "nusil" if 5 characters were specified.
    """
    randomGuess = ""
    for character in range(targetLength):
        randomGuess = randomGuess + random.choice(characters)
    return randomGuess
        
while guess != targetWord:
    guess = monkeyGuess(characters, targetLength)
    numGuesses = numGuesses + 1
    
print "The monkeys discovered '%s'" % (guess )
print "after " + str(numGuesses) + " random guesses."
