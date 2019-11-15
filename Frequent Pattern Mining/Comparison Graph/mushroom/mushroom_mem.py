from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [20,22,25,27,30]
Apriori = [31140,23716,21788,21260,20768]
FP_growth = [43744,39516,37932,37404,36096]

plt.plot(x, Apriori, color='r', label='Apriori')
plt.plot(x, FP_growth, color='b', label='FP-Growth')

plt.ylabel('Memory Usage (VM + RSS)')
plt.xlabel('min sup %')


plt.suptitle('Comparison between Apriori and FP-growth Algorithm')
plt.title('Dataset Name: mushroom.dat')
plt.legend(loc='upper right')

# plt.yscale('log',basey = 2)

###tobechanged
plt.savefig('mushroom_mem.pdf')
plt.savefig('mushroom_mem.png')

# plt.yticks(Apriori+FP_growth,Apriori+FP_growth)
plt.xticks(x,x)



plt.show()