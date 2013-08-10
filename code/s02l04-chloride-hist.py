import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# chloride data source: 
# http://hydro16.geology.um.maine.edu/blohg/attachments/Gsa2013/_build/html/content/Basic_Plotting.html

data = [64, 67, 72, 72, 77, 81, 86, 90, 94, 94, 95, 98, 100, 102, 106, 110, \
110, 110, 117, 120, 123, 130, 136, 140, 140, 140, 141, 160, 173, 176, 280]
data.sort()

plt.title("Chloride concentrations around landfill")
plt.xlabel("Chloride concentration (ppm)")
plt.ylabel("Frequency")

plt.hist(data, 9)

#boxplot(data,0)
figfilename = "s02l04-img-chloride-hist.png"
figfile = open(figfilename, "wb")
plt.savefig(figfile)
figfile.close()
