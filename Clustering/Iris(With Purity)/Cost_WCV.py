from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [2,3,4,5,6]
KMeans = [21.38044919,
19.62317805,
10.80320585,
11.54946749,
12.8826887]
KMediods = [16.16378296,
12.12682439,
10.67378766,
9.923787665,
9.223752354
]
plt_title = "Dataset Name: Iris"

n_groups = len(x)
fig,ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.8

X = KMeans
Y = KMediods
measure_name = 'Cost/Within Cluster Variation'
file_name = 'cost_wcv.png'

rects1 = plt.bar(index, X,bar_width,
alpha=opacity,
color='b',
label='K-Means')

rects2 = plt.bar(index+bar_width, Y,bar_width,
alpha=opacity,
color='r',
label='K-Medoids')

plt.xlabel('k')
plt.ylabel(measure_name)
plt.suptitle('Comparison between K-Means and K-Medoids Algorithm\n')
plt.title(plt_title)

plt.xticks(index+bar_width,tuple(x))
# plt.yticks(index+bar_width,tuple(x))
plt.legend(loc='upper right')

# plt.yscale('log',basey=2)

# plt.tight_layout()
plt.savefig(file_name,dpi=600)


plt.show()
