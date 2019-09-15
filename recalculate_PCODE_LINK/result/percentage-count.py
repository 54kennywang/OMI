from matplotlib import pyplot as plt
import numpy as np

Instability, Deprivation, Dependency, Ethniccon = np.loadtxt('UHN_2016_weightAverage_q_within_1SD_noPcode.csv', delimiter = ',', unpack = True)
bins = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
fig = plt.figure()

# ax1 = plt.subplot2grid((1, 1), (0, 0))
# ax1.hist(Instability, bins, histtype = 'bar', rwidth = 0.8, label = 'Instability') # histogram is for distribution
# ax1.set_xticks(bins)


# ax2 = plt.subplot2grid((1, 1), (0, 0))
# ax2.hist(Deprivation, bins, histtype = 'bar', rwidth = 0.8, label = 'Deprivation') # histogram is for distribution
# ax2.set_xticks(bins)


# ax3 = plt.subplot2grid((1, 1), (0, 0))
# ax3.hist(Dependency, bins, histtype = 'bar', rwidth = 0.8, label = 'Dependency') # histogram is for distribution
# ax3.set_xticks(bins)


ax4 = plt.subplot2grid((1, 1), (0, 0))
ax4.hist(Ethniccon, bins, histtype = 'bar', rwidth = 0.8, label = 'Ethniccon') # histogram is for distribution
ax4.set_xticks(bins)


plt.xlabel('Range')
plt.ylabel('Count')
plt.title('Ethniccon in 1SD')
plt.legend()
fig.savefig('UHN_Ethniccon_1SD.png')
plt.show()
