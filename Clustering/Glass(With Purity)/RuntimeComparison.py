from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [5,
6,
7,
8,
9]
KMeans = [0.08393597603,
0.04468250275,
0.07472062111,
0.06846475601,
0.1846382618]
KMediods = [1.007563114,
1.571109056,
2.072346687,
2.3126719,
3.353453398,
]

plt.plot(x, KMeans, color='r', label='K-Means')
plt.plot(x, KMediods, color='b', label='K-Medoids')

plt.ylabel('Running Time(seconds)')
plt.xlabel('k')


plt.suptitle('Comparison between K-Means and K-Medoids Algorithm\n')
plt.title('Dataset Name: Glass')
plt.legend(loc='upper left')

plt.yscale('log',basey = 2)

###tobechanged
plt.savefig('runtime.pdf')
plt.savefig('runtime.png')

# plt.yticks(KMeans+KMediods,KMeans+KMediods)
plt.xticks(x,x)



plt.show()