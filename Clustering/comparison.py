from matplotlib import pyplot as plt
import numpy as np
datasets_name = [
"Iris",
"Wine",
"Breast Cancer",
"Wisconsin",
"Original",
"Prognostic",
"Cylinder Bands",
"Car",
"Mushroom",
"Wine Quality"
]

attributes = [
4,
13,
9,
10,
10,
10,
39,
6,
21,
11
]

tuples = [
150,
178,
286,
540,
699,
699,
699,
1599,
1728,
8124
]

decision_tree_accuracy = [
94.66,
91.015,
66.079,
60.185,
94.991,
93.278,
93.991,
56.786,
80.957,
99.323
]

decision_tree_precision = [
100.00,
90.700,
83.120,
91.893,
96.129,
94.991,
94.496,
69.356,
92.000,
99.462
]

decision_tree_recall = [
100.00,
87.591,
72.713,
60.225,
96.318,
94.746,
96.294,
63.750,
91.812,
99.143
]

decision_tree_fscore = [
100.00,
88.902,
77.568,
72.692,
96.223,
94.868,
95.386,
66.383,
86.125,
99.302
]

decision_tree_running_time = [
0.195506,
1.576283,
0.266840,
35.515057,
3.653997,
4.114888,
4.572104,
201.686458,
0.355417,
1.8576
]

naive_bayes_accuracy = [
95.333,
96.665,
71.693,
96.143783,
95.99,
96.281516,
73.0896,
85.301788,
95.347063,
54.274818
]

naive_bayes_precision = [
100,
95,
84.109,
95.205447,
95.195,
95.19828,
43.661,
95.785124,
90.449182,
64.898025

]

naive_bayes_recall = [
100,
100,
77.583,
98.891164,
98.668,
99.10101,
88.189,
91.665833,
99.886686,
66.912366
]

naive_bayes_fscore = [
100,
97.391,
80.623,
96.992528,
96.874,
97.104764,
52.275,
93.663633,
94.933085,
65.764534
]

naive_bayes_running_time = [
0.009613,
0.028092,
0.008924,
0.048827,
0.044584,
0.047749,
0.089919,
0.042838,
0.372548,
0.297652

]

n_groups = len(datasets_name)
fig,ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.4
opacity = 0.8

X = attributes
Y = tuples
measure_name = 'Count'
file_name = 'dataset_description.png'


# X = decision_tree_precision
# Y = naive_bayes_precision
# measure_name = 'Precision (%)'
# file_name = 'precision_comparison.png'
#
#
# X = decision_tree_recall
# Y = naive_bayes_recall
# measure_name = 'Recall (%)'
# file_name = 'recall_comparison.png'
#
#
# X = decision_tree_fscore
# Y = naive_bayes_fscore
# measure_name = 'F-Score (%)'
# file_name = 'fscore_comparison.png'

rects1 = plt.bar(index, X,bar_width,
alpha=opacity,
color='b',
label='Attributes')

rects2 = plt.bar(index+bar_width, Y,bar_width,
alpha=opacity,
color='r',
label='Tuples')

plt.xlabel('Datasets')
plt.ylabel(measure_name)
plt.title('Dataset Description')

plt.xticks(index+bar_width,tuple(datasets_name),rotation='vertical')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.yscale('log',basey=2)

plt.tight_layout()
plt.savefig(file_name,dpi=600)
#here

plt.show()