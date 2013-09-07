import random

def rollDie():
    """returns a random integer between 1 and 6"""
    return random.choice( [ 1, 2, 3, 4, 5, 6 ] )
    
print rollDie()