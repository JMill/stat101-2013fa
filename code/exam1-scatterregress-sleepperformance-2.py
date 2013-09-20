import pylab
from scipy import stats

# our data
nosleep = [ 49, 38, 38, 24, 38, 35, 50, 34, 42 ]
mistakes = [ 6, 8, 13, 5, 7, 6, 5, 8, 12 ]

# calculate the regression equation
m, b, r, p, std_err = stats.linregress( nosleep, mistakes )
fit = pylab.polyfit( nosleep, mistakes, 1 )
fit_fn = pylab.poly1d( fit )

# plot scatter and regression line
pylab.plot( nosleep, mistakes, 'o', nosleep, fit_fn ( nosleep) )

# add the (written) equation to the plot
equation = "y' = %.3f x %+.3f" % ( m, b )
#pylab.figtext( 0.5, 0.4, equation )

# adjust the graph's details
pylab.xlabel("Hours without sleep")
pylab.ylabel("Numer of Mistakes")
pylab.xlim([20,50])
pylab.ylim([0,14]) 
pylab.show()