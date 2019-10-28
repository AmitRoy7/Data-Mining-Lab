from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [12,
13,
14,
15,
16,
17]
KMeans = [1.510924578,
2.114582062,
1.937050343,
3.113382101,
2.151068449,
2.316946745]
KMediods = [11.42324233,
11.96720314,
11.24094725,
13.73017359,
16.63861585,
17.38047123
]

plt.plot(x, KMeans, color='r', label='K-Means')
plt.plot(x, KMediods, color='b', label='K-Mediods')

plt.ylabel('Running Time(seconds)')
plt.xlabel('k')


plt.suptitle('Comparison between K-Means and K-Mediods Algorithm')
plt.title('Dataset Name: Libras Movement')
plt.legend(loc='upper left')

plt.yscale('log',basey = 2)

###tobechanged
plt.savefig('runtime.pdf')
plt.savefig('runtime.png')

# plt.yticks(KMeans+KMediods,KMeans+KMediods)
plt.xticks(x,x)



plt.show()