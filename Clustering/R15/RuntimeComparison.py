from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [13,14,15,16,17]
KMeans = [0.1108675003,
0.249724865,
0.1324393749,
0.1310503483,
0.1312339306]
KMediods = [63.34089518,
78.44403696,
72.34407902,
80.51552749,
91.86335468]

plt.plot(x, KMeans, color='r', label='K-Means')
plt.plot(x, KMediods, color='b', label='K-Medoids')

plt.ylabel('Running Time(seconds)')
plt.xlabel('k')


plt.suptitle('Comparison between K-Means and K-Medoids Algorithm')
plt.title('Dataset Name: R15')
plt.legend(loc='center left')

plt.yscale('log',basey = 2)

###tobechanged
plt.savefig('runtime.pdf')
plt.savefig('runtime.png')

# plt.yticks(KMeans+KMediods,KMeans+KMediods)
plt.xticks(x,x)



plt.show()