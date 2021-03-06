import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x = range(1,12)
y = [1, 2, 4, 3, 4, 6, 5, 5, 3, 4, 1]


# set figure to be not so tall. I think default size is 8x6
fig = plt.figure()
fig.set_size_inches(8,4.5)

# turn off/on black frame
ax = plt.axes(frameon=False)
# remove axis labels and ticks
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)

# removes whitespace at top of plot (like a crop). Number represents fraction of the figure dimensions. 
# See http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.subplots_adjust
plt.subplots_adjust(top = 0.4)

plt.xlim([0,12])
plt.ylim([0,10])

plt.bar(x, y)

plt.title("Wide Spread")
figfilename = "s02l01-img-hist-wide.png"
figfile = open(figfilename, "wb")
plt.savefig(figfile, bbox_inches='tight' )
figfile.close()