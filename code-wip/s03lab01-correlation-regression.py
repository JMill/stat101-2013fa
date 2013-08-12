### @export 'statsmodule'
from scipy import stats

### @export 'independent variable'
x = [5.05, 6.75, 3.21, 2.66]

### @export 'dependent variable'
y = [1.65, 26.5, -5.93, 7.96]

### @export 'unpack linregress'
m, b, r, p, std_err = stats.linregress(x,y)

### @export 'slope'
m

### @export 'y-intercept'
b

### @export 'correlation coefficient'
r

### @export 'R squared'
r*r

### @export 'p-value'
p

### @export 'standard error'
std_err


