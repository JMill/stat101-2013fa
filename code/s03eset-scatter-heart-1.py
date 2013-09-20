import pylab

age = [ 16, 26, 32, 37, 42, 53, 48, 21 ]
heart = [ 220, 194, 193, 178, 172, 160, 174, 214 ]

pylab.plot(age,heart, 'bo')
pylab.xlabel("Age")
pylab.ylabel("Peak Heart Rate")
pylab.xlim([0,60])
pylab.ylim([150,230]) 
pylab.show()