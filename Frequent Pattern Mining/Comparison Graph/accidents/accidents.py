from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [50,55,60,65,70,75]
Apriori = [286.629637000000,218.987451000000,70.963750000000,30.541581,16.646713000000,15.723102000000]
FP_growth = [12.361593000000,12.350644000000,12.218966,11.185202000000,10.645799000000,10.645799000000]

plt.plot(x, Apriori, color='r', label='Apriori')
plt.plot(x, FP_growth, color='b', label='FP-Growth')

plt.ylabel('Running Time (second)')
plt.xlabel('min sup %')


plt.suptitle('Comparison between Apriori and FP-growth Algorithm')
plt.title('Dataset Name: accidents.dat')
plt.legend(loc='upper right')

plt.yscale('log',basey=2)

###tobechanged
plt.savefig('accidents.pdf')
plt.savefig('accidents.png')

# plt.yticks(Apriori+FP_growth,Apriori+FP_growth)
plt.xticks(x,x)



plt.show()