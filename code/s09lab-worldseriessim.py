import random 
import pylab

def playSeries( numGames, teamProb):
    """Assumes numGames an odd integer,
         teamProb a floaat between 0 and 1
       Returns True if better team wins series"""
    numWon = 0
    for game in range(numGames):
        if random.random() <= teamProb:
            numWon += 1
    return ( numWon > numGames//2 )
    
def simSeries( numSeries ):
    prob = 0.5
    fracWon = []
    probs = []
    while prob <= 1.0:
        seriesWon = 0.0
        for i in range( numSeries ):
            if playSeries( 7, prob ):
                seriesWon += 1
        fracWon.append( seriesWon/numSeries )
        probs.append( prob )
        prob += 0.01
    pylab.plot( probs, fracWon, linewidth = 5 )
    pylab.xlabel( 'Probability of Winning a Game' )
    pylab.ylabel( 'Probability of Winning a Series' )
    pylab.title( str( numSeries ) + ' Seven-Games Series' )
    pylab.show()

simSeries(400)

