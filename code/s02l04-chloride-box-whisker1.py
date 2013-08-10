import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# data description:
# chloride concentrations measured in monitoring wells around a demolition debris landfill.
# data source: 
# http://hydro16.geology.um.maine.edu/blohg/attachments/Gsa2013/_build/html/content/Basic_Plotting.html

data = [64, 67, 72, 72, 77, 81, 86, 90, 94, 94, 95, 98, \
	100, 102, 106, 110, 110, 110, 117, 120, 123, 130,   \
	136, 140, 140, 140, 141, 160, 173, 176, 280]

data.sort()


import math
import functools

def percentile(N, percent, key=lambda x:x):
    """
    Find the percentile of a list of values.

    @parameter N - is a list of values. Note N MUST BE already sorted.
    @parameter percent - a float value from 0.0 to 1.0.
    @parameter key - optional key function to compute value from each element of N.

    @return - the percentile of the values
    """
    if not N:
        return None
    k = (len(N)-1) * percent
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return key(N[int(k)])
    d0 = key(N[int(f)]) * (c-k)
    d1 = key(N[int(c)]) * (k-f)
    return d0+d1

# median is 50th percentile.
median = functools.partial(percentile, percent=0.5)





### @export "min"
lowest = min(data)
print lowest

### @export "max"
highest = max(data)
print highest

### @export "range"
range = highest - lowest
print range

### @export "upper quartile"
print percentile(data, percent=0.75)

### @export "median"
print percentile(data, percent=0.5)

### @export "lower quartile"
print percentile(data, percent=0.25)


### @export "hidden"

plt.title("Chloride concentrations around landfill")
plt.ylabel("Chloride concentration (ppm)")
plt.boxplot(data,0)

figfilename = "s02l04-img-chloride-box.png"
figfile = open(figfilename, "wb")
plt.savefig(figfile)
figfile.close()
