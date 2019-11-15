from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [50,55,60,65,70,75]
Apriori = [140980,139868,139336,138860,138860,138860]
FP_growth = [1375620,1359060,1353864,1347132,1344888,1344036]

plt.plot(x, Apriori, color='r', label='Apriori')
plt.plot(x, FP_growth, color='b', label='FP-Growth')

plt.ylabel('Memory Usage (VM + RSS)')
plt.xlabel('min sup %')


plt.suptitle('Comparison between Apriori and FP-growth Algorithm')
plt.title('Dataset Name: accidents.dat')
plt.legend(loc='upper right')

plt.yscale('log',basey = 2)

###tobechanged
plt.savefig('accidents_mem.pdf')
plt.savefig('accidents_mem.png')

# plt.yticks(Apriori+FP_growth,Apriori+FP_growth)
plt.xticks(x,x)



plt.show()