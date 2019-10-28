from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [2,3,4,5,6]
KMeans = [0.2230395887,
0.5140235168,
0.2864282119,
0.3471647396,
0.2662120893]
KMediods = [0.6435145374,
0.5221559826,
0.4667371149,
0.3591643836,
0.3351381688
]
plt_title = "Dataset Name: Iris"

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
