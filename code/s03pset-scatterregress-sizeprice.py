import pylab
from scipy import stats

# our data
size = [ 26, 27, 41, 29, 33, 34, 36, 45, 22 ]
price = [ 235, 273, 387, 253, 295, 335, 395, 475, 203 ]

# calculate the regression equation
m, b, r, p, std_err = stats.linregress( size, price )
fit = pylab.polyfit( size, price, 1 )
fit_fn = pylab.poly1d( fit )

# plot scatter and regression line
pylab.plot( size, price, 'o', size, fit_fn ( size) )

# add the (written) equation to the plot
equation = "y' = %.3f x %+.3f" % ( m, b )
pylab.figtext( 0.5, 0.4, equation )

# adjust the graph's details
pylab.xlabel("Size")
pylab.ylabel("Price")
pylab.xlim([20,50])
pylab.ylim([200,500]) 
pylab.show()