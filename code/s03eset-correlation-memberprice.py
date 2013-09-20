from scipy import stats

nonMemberPrice = [ 60, 42, 46, 30, 25, 75, 35, 68 ]
memberPrice = [ 50, 22, 20, 20, 19, 58, 34, 60 ]

m, b, r, p, std_err = stats.linregress( nonMemberPrice, memberPrice )

print 'correlation coefficient', r