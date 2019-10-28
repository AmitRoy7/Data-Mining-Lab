from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [2,
3,
4,
5,
6]
KMeans = [0.1123621464,
0.04260444641,
0.0799446106,
0.09431314468,
0.1173949242]
KMediods = [0.8413333893,
1.449322701,
1.161122322,
1.677128553,
2.689814806,
]

plt.plot(x, KMeans, color='r', label='K-Means')
plt.plot(x, KMediods, color='b', label='K-Medoids')

plt.ylabel('Running Time(seconds)')
plt.xlabel('k')


plt.suptitle('Comparison between K-Means and K-Medoids Algorithm')
plt.title('Dataset Name: Breast Cancer')
plt.legend(loc='upper left')

plt.yscale('log',basey = 2)

###tobechanged
plt.savefig('runtime.pdf')
plt.savefig('runtime.png')

# plt.yticks(KMeans+KMediods,KMeans+KMediods)
plt.xticks(x,x)



plt.show()