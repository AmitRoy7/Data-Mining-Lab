from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [3,4,5,6,7]
KMeans = [0.3891639937,
0.3293147201,
0.2566762988,
0.2521570627,
0.2241169827]
KMediods = [0.453366338,
0.380369821,
0.3184077598,
0.2760045103,
0.28157436
]
plt_title = "Dataset Name: Seeds"

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
