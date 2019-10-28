from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [13,14,15,16,17]
KMeans = [44.93315682,
21.94561627,
28.74738045,
17.06936745,
25.13210186]
KMediods = [37.71232733,
31.22423571,
32.36411168,
23.20451135,
23.47529594]
plt_title = "Dataset Name: R15"

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
