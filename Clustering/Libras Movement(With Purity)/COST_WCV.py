from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [12,13,14,15,16,17]
KMeans = [38.87159145,
38.14287314,
36.9906348,
36.34479246,
36.57809723,
35.47324925]
KMediods = [37.95913761,
37.04036243,
36.14860491,
35.2969309,
34.51477046,
33.7950439
]
plt_title = "Dataset Name: Libras Movement"

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
label='K-Mediods')

plt.xlabel('k')
plt.ylabel(measure_name)
plt.suptitle('Comparison between K-Means and K-Mediods Algorithm\n')
plt.title(plt_title)

plt.xticks(index+bar_width,tuple(x))
# plt.yticks(index+bar_width,tuple(x))
plt.legend(loc='upper right')

# plt.yscale('log',basey=2)

# plt.tight_layout()
plt.savefig(file_name,dpi=600)


plt.show()
