from scipy import stats

nonMemberPrice = [ 58, 42, 46, 32, 25, 75, 35, 63 ]
memberPrice = [ 32, 22, 20, 16, 19, 58, 34, 48 ]

m, b, r, p, std_err = stats.linregress( nonMemberPrice, memberPrice )

print 'correlation coefficient', r