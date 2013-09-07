import pylab

price = [ 23, 18, 19, 21, 20, 25, 22, 17, 22 ]
demand = [ 17, 48, 41, 38, 33, 17, 35, 52, 24 ]

pylab.plot(price,demand, 'bo')
pylab.xlabel("Price (dollars)")
pylab.ylabel("Demand (hundreds)")
pylab.xlim([15,30])
pylab.ylim([0,60]) 
pylab.show()