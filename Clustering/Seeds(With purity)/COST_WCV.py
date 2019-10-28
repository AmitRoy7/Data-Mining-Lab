from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [3,4,5,6,7]
KMeans = [26.54713578,
18.97369081,
24.65746639,
16.21849819,
16.1768276]
KMediods = [20.45407492,
18.58982332,
16.81869792,
16.08739767,
15.33522922
]
plt_title = "Dataset Name: Seeds"

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
