from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [13,14,15,16,17]
KMeans = [0.655,
0.7866666667,
0.7533333333,
0.8366666667,
0.7783333333]
KMediods = [0.7333333333,
0.6266666667,
0.7266666667,
0.775,
0.7883333333
]
plt_title = "Dataset Name: R15"

n_groups = len(x)
fig,ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.8

X = KMeans
Y = KMediods
measure_name = 'Purity'
file_name = 'purity_comparison.png'

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
plt.legend(loc='upper left')

# plt.yscale('log',basey=2)

# plt.tight_layout()
plt.savefig(file_name,dpi=600)


plt.show()
