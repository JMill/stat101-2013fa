from scipy import stats
import pylab

x = [ 5.05, 6.75, 3.21, 2.66 ]
y = [ 1.65, 26.5, -5.93, 7.96 ]

m, b, r, p, std_err = stats.linregress( x, y )

fit = pylab.polyfit( x, y, 1 )
fit_fn = pylab.poly1d( fit )

pylab.plot( x, y, 'o', x, fit_fn( x ) )

equation = "y' = %.3f * x + %.3f" % ( m, b )
pylab.figtext( 0.5, 0.4, equation )

label = "R^2 value is %.3f" % ( r*r )
pylab.figtext( 0.5, 0.2, label )

pylab.show()