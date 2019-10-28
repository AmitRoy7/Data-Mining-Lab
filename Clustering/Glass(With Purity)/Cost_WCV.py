from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [5,6,7,8,9]
KMeans = [18.25305448,
14.35612801,
14.50182337,
13.40140952,
13.7248931]
KMediods = [12.47902327,
11.9321226,
11.40575257,
10.89504322,
10.41809687
]
plt_title = "Dataset Name: Glass"

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
