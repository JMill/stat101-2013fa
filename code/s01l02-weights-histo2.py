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

lowestValue = 80
bins = [lowestValue]
for i in range(8):
    bins.append(lowestValue + i*20)

plt.hist(weights, bins, label='weights')
plt.title("Student Weights")
plt.xlabel("Weight in pounds")
plt.ylabel("Number of students")

figfilename = "s01l02-img-weights-histo2.png"
figfile = open(figfilename, "wb")
plt.savefig(figfile)
figfile.close()