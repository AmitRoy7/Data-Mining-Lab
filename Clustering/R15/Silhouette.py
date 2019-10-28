from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [13,14,15,16,17]
KMeans = [0.1826356701,
0.5171934676,
0.436096949,
0.5842438966,
0.4495541247]
KMediods = [0.3376819301,
0.3875919533,
0.3574381159,
0.5018354502,
0.369095206
]
plt_title = "Dataset Name: R15"

n_groups = len(x)
fig,ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.8

X = KMeans
Y = KMediods
measure_name = 'Silhouette Coefficeint'
file_name = 'silhouette.png'

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
