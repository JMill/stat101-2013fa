from scipy import stats

x = [ 52, 60, 54, 53, 55, 56 ]
y = [ 308, 338, 308, 298, 298, 308 ]

m, b, r, p, std_err = stats.linregress( x, y )

print "y' = %.3fx + %.3f" % ( m, b )
# The above line uses a float formatter, %f (the 'f' refers to 'float').
# The code '%.3f' tells Python to round the variable to 3 decimal spaces.
# Read more here: http://mkaz.com/solog/python/python-string-format.html