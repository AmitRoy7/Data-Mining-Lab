from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [5,6,7,8,9]
KMeans = [0.2109776303,
0.2380100242,
0.3108097082,
0.1718447559,
0.2232864618]
KMediods = [0.3264569579,
0.2286534629,
0.2101546722,
0.2173557937,
0.2248496158
]
plt_title = "Dataset Name: Glass"

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
