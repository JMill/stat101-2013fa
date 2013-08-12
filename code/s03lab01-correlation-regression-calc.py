from scipy import stats

x = [ 5.05, 6.75, 3.21, 2.66 ]
y = [ 1.65, 26.5, -5.93, 7.96 ]

m, b, r, p, std_err = stats.linregress( x, y )

print 'slope', m
print 'y-intercept', b
print 'correlation coefficient', r
print 'R squared', r*r
print 'p-value', p
print 'standard error', std_err
