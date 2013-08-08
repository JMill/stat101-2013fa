import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

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
            weightsFreqDict[weight] += 1
        else:
            weightsFreqDict[weight] = 1
        i += 1

weightsArrRev = weightsArr[:]
weightsArrRev.reverse()

freqStep = []
for weight in weightsArrRev:
    freqStep.append(weightsFreqDict[weight])
    weightsFreqDict[weight] -= 1
freqStep.reverse()

x = weightsArr
y = freqStep


# set figure to be not so tall. I think default size is 8x6
fig = plt.figure()
fig.set_size_inches(8,4.5)

# turn off/on black frame
ax = plt.axes(frameon=True)
# remove y-axis labels and ticks
ax.axes.get_yaxis().set_visible(False)
# disable ticks at top of plot
ax.get_xaxis().tick_bottom()


plt.plot(x, y, 'o')

# set y-axis limits
#plt.ylim([0,20])

# removes whitespace at top of plot (like a crop). Number represents fraction of the figure dimensions. 
# See http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.subplots_adjust
plt.subplots_adjust(top = 0.4)


plt.xlabel("Weight in pounds")

#plt.yaxis('off')

# Pad margins so that markers don't get clipped by the axes
plt.margins(0.05)

figfilename = "s01l02-img-weights-histo1.png"
figfile = open(figfilename, "wb")
plt.savefig(figfile, bbox_inches='tight') # bbox reduces whitespace
figfile.close()
