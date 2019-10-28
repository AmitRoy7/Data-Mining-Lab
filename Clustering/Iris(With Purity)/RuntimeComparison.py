from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [2,3,4,5,6]
KMeans = [0.01469635963,
0.01397228241,
0.01247024536,
0.01060509682,
0.02069878578]
KMediods = [0.1775770187,
0.2719025612,
0.3838717937,
0.4701457024,
0.8767814636
]

plt.plot(x, KMeans, color='r', label='K-Means')
plt.plot(x, KMediods, color='b', label='K-Medoids')

plt.ylabel('Running Time(seconds)')
plt.xlabel('k')


plt.suptitle('Comparison between K-Means and K-Medoids Algorithm')
plt.title('Dataset Name: Iris')
plt.legend(loc='upper left')

plt.yscale('log',basey = 2)

###tobechanged
plt.savefig('runtime.pdf')
plt.savefig('runtime.png')

# plt.yticks(KMeans+KMediods,KMeans+KMediods)
plt.xticks(x,x)



plt.show()