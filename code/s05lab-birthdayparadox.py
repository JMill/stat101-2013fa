import random

NTRIALS = 10000
NPEOPLE = 30

matches = 0

matches = 0
for trial in range(NTRIALS):
    taken = {}
    
    for person in range(NPEOPLE):
        day = random.randint(0,365)
        if day in taken:
            matches += 1
            break
        taken[day] = 1
        
print 'The fraction of trials that have matching birthdays is', float(matches)/NTRIALS

