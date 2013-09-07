from scipy import stats

x = [ 60, 43, 56, 46, 57 ]
y = [ 138, 119, 134, 128, 132 ]

m, b, r, p, std_err = stats.linregress( x, y )

print 'correlation coefficient', r