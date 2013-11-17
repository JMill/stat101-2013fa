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

def findSeriesLength( teamProb ):
    numSeries = 200
    maxLen = 2500
    step = 10
    
    def fracWon( teamProb, numSeries, seriesLen ):
        won = 0.0
        for series in range( numSeries ):
            if playSeries( seriesLen, teamProb ):
                won += 1
        return won/numSeries
        
    winFrac = []
    for seriesLen in range( 1, maxLen, step ):
        winFrac.append( fracWon( teamProb, numSeries, seriesLen ))
    pylab.plot( step*( pylab.arange( len(winFrac)) + 1) - 1, winFrac, linewidth = 5 )
    pylab.xlabel( 'Maximum Length of Series' )
    pylab.ylabel( 'Probability of Winning Series' )
    pylab.title( str( round(teamProb, 4)) + 
        ' Probability of Better Team Winning a Game')
    pylab.axhline(0.95) #draw horizontal line at y = 0.95
    pylab.show()

YanksProb = 0.636
PhilsProb = 0.574
findSeriesLength( YanksProb/(YanksProb + PhilsProb))