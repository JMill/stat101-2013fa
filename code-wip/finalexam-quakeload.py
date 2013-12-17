'''
Reads a comma-separated values (csv) text file, 
removes the label header, and generates the 
average quake magnitude.
'''
import csv

with open("finalquake.csv", 'rU') as textfile:
    text = csv.reader(textfile, dialect=csv.excel_tab) #open csv file

    magSum = 0.0
    numQuakes = 0
    quakes = []
    for line in text:
        quakes.append(' '.join(line)) #convert lists to strings
        
    quakes = quakes[1:] #remove header
    for line in quakes:
        numQuakes = numQuakes + 1 #track the number of quakes
        line = ' '.join(line) #remove whitespace
        myList = line.split(',') #seperate columns
        magSum = magSum + float(myList[3].replace(' ', '')) #prep for avg
    print 'average quake magnitude is', magSum/numQuakes
