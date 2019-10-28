from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [5,
6,
7,
8,
9]
KMeans = [0.4672897196,
0.5327102804,
0.5514018692,
0.5794392523,
0.6168224299]
KMediods = [0.5420560748,
0.6588785047,
0.6635514019,
0.6728971963,
0.691588785
]
plt_title = "Dataset Name: Glass"

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
