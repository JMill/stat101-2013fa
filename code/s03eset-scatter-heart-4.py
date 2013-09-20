import pylab

age = [ 16, 26, 32, 37, 42, 53, 48, 21 ]
heart = [ 230, 104, 163, 170, 127, 155, 170, 230 ]

pylab.plot(age,heart, 'bo')
pylab.xlabel("Age")
pylab.ylabel("Peak Heart Rate")
pylab.xlim([0,60])
#pylab.ylim([150,230]) 
pylab.show()