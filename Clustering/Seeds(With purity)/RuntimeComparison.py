from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [3,
4,
5,
6,
7]
KMeans = [0.1094629765,
0.06522631645,
0.05115699768,
0.09515500069,
0.09860754013]
KMediods = [ 0.5242869854,
1.214434862,
1.275073051,
1.224798679,
1.615141869,
]

plt.plot(x, KMeans, color='r', label='K-Means')
plt.plot(x, KMediods, color='b', label='K-Medoids')

plt.ylabel('Running Time(seconds)')
plt.xlabel('k')


plt.suptitle('Comparison between K-Means and K-Medoids Algorithm')
plt.title('Dataset Name: Seeds')
plt.legend(loc='upper left')

plt.yscale('log',basey = 2)

###tobechanged
plt.savefig('runtime.pdf')
plt.savefig('runtime.png')

# plt.yticks(KMeans+KMediods,KMeans+KMediods)
plt.xticks(x,x)



plt.show()