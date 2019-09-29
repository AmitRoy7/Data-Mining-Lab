from matplotlib import pyplot as plt
import numpy as np
datasets_name = [
"Iris",
"Wine",
"Breast Cancer",
"Cylinder-Bands",
"Diagnostic",
"Original",
"Prognostic",
"Wine Quality"
"Car",
"Mushroom"
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
33.33,
33.147,
72.389,
42.221,
69.099,
69.242,
69.233,
39.335,
85.417,
95.273
]

naive_bayes_precision = [
100.00,
100.00,
83.609,
100.000,
99.782,
99.782,
99.782,
90.751,
95.867,
90.322
]

naive_bayes_recall = [
33.33,
33.147,
78.469,
100.000,
68.007,
68.109,
68.132,
42.928,
91.710,
99.859
]

naive_bayes_fscore = [
50.00,
49.786,
80.957,
59.374,
80.885,
80.957,
80.964,
58.275,
93.742,
94.851
]

naive_bayes_running_time = [
0.009072,
0.103515,
0.034045,
0.170198,
0.070497,
0.070609,
0.071878,
0.653502,
0.072443,
0.616981
]

n_groups = len(datasets_name)
fig,ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.4
opacity = 0.8

X = decision_tree_accuracy
Y = naive_bayes_accuracy

rects1 = plt.bar(index, X,bar_width,
alpha=opacity,
color='b',
label='Decision Tree')

rects2 = plt.bar(index+bar_width, Y,bar_width,
alpha=opacity,
color='r',
label='Naive Bayes')

plt.xlabel('Datasets')
#change from here
plt.ylabel('Accuracy (%)')
plt.title('Performance Measure of Decision Tree and Naiive Bayes')
#to here

plt.xticks(index+bar_width,tuple(datasets_name),rotation='vertical')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


plt.tight_layout()

#change file name
plt.savefig('accuracy_comparison.png',dpi=600)
#here

plt.show()