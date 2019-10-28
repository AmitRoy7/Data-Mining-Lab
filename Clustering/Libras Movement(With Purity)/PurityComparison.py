from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [12,13,14,15,16,17]
KMeans = [0.3638888889,
0.3805555556,
0.3833333333,
0.4666666667,
0.425,
0.4694444444]
KMediods = [0.4222222222,
0.4361111111,
0.4472222222,
0.475,
0.4916666667,
0.4944444444
]
plt_title = "Dataset Name: Libras Movement"

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
label='K-Mediods')

plt.xlabel('k')
plt.ylabel(measure_name)
plt.suptitle('Comparison between K-Means and K-Mediods Algorithm\n')
plt.title(plt_title)

plt.xticks(index+bar_width,tuple(x))
# plt.yticks(index+bar_width,tuple(x))
plt.legend(loc='upper left')

# plt.yscale('log',basey=2)

# plt.tight_layout()
plt.savefig(file_name,dpi=600)


plt.show()
