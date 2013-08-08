import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

maleWeights = [140, 145, 160, 190, 155, 165, 150, 190, 195, 138, 160, 155, 153,\
145, 170, 175, 175, 170, 180, 135, 170, 157, 130, 185, 190, 155, 170, 155, 215,\
150, 145, 155, 155, 150, 155, 150, 180, 160, 135, 160, 130, 155, 150, 148, 155,\
150, 140, 180, 190, 145, 150, 164, 140, 142, 136, 123, 155]
	
femaleWeights = [140, 120, 130, 138, 121, 125, 116, 145, 150, 112, 125, 130,\
120, 130, 131, 120, 118, 125, 135, 125, 118, 122, 115, 102, 115, 150, 110, 116,\
108, 95, 125, 133, 110, 150, 108]

weights = maleWeights + femaleWeights
weightsArr = weights[:]
weightsArr.sort()
weightsFreqDict = {}

i = 0
for weight in weightsArr:
    if i > len(weightsArr):
        pass
    else:
        if weight in weightsFreqDict:
            weightsFreqDict[weight] += 1.
        else:
            weightsFreqDict[weight] = 1.
        i += 1.

weightsArrRev = weightsArr[:]
weightsArrRev.reverse()

freqStep = []
for weight in weightsArrRev:
    freqStep.append(weightsFreqDict[weight])
    weightsFreqDict[weight] -= 1.
freqStep.reverse()

freqStepNormed = []

for item in freqStep:
	freqStepNormed.append(item/len(freqStep))


x = weightsArr
y = freqStepNormed


lowestValue = 80
bins = [lowestValue]
for i in range(8):
    bins.append(lowestValue + i*20)

value = 0
i = 0
for item in y:
	value = value + item
	i+=1

# For some reason each value in y is about 2.7 times larger 
# than it should be, so this corrections/normalizes each 
# value before weighting the histogram.

yadj = []
for item in y:
	yadj.append(item/value)

#yadj = []
#for x in range(len(y)):
#	yadj.append(1./len(y))
#print yadj

plt.hist(x, bins, weights=yadj, label='weights')
plt.title("Student Weights")
plt.xlabel("Weight in pounds")
plt.ylabel("Number of students")


figfilename = "s01l02-weights-histo3.png"
figfile = open(figfilename, "wb")
plt.savefig(figfile)
figfile.close()