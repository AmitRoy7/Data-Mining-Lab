from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [70,72,75,77,80]
Apriori = [66.970493,38.942090000000,18.484947,10.941887000000,5.586742]
FP_growth = [0.465268000,0.328541000000,0.263759000,0.184821000000,0.165147000]

plt.plot(x, Apriori, color='r', label='Apriori')
plt.plot(x, FP_growth, color='b', label='FP-Growth')

plt.ylabel('Running Time (second)')
plt.xlabel('min sup %')


plt.suptitle('Comparison between Apriori and FP-growth Algorithm')
plt.title('Dataset Name: chess.dat')
plt.legend(loc='upper right')

plt.yscale('log',basey=2)

###tobechanged
plt.savefig('chess.pdf')
plt.savefig('chess.png')

# plt.yticks(Apriori+FP_growth,Apriori+FP_growth)
plt.xticks(x,x)



plt.show()