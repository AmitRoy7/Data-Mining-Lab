from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [12,13,14,15,16,17]
KMeans = [0.2194053291,
0.135275224,
0.1766778352,
0.1812493327,
0.1801980307,
0.1951307147]
KMediods = [0.2176434994,
0.212643363,
0.2117644767,
0.2209404023,
0.2188655115,
0.2221062299
]
plt_title = "Dataset Name: Libras Movement"

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
