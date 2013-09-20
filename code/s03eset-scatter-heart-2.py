import pylab

age = [ 16, 26, 32, 37, 42, 53, 48, 21 ]
heart = [ 220, 194, 193, 178, 172, 160, 174, 214 ]

pylab.plot(heart,age, 'bo')
pylab.xlabel("Age")
pylab.ylabel("Peak Heart Rate")
pylab.ylim([0,60])
pylab.xlim([150,230]) 
pylab.show()