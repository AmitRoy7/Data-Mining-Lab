from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [20,22,25,27,30]
Apriori = [63.888738,9.942417000000,3.737537,2.873665000000,2.278852]
FP_growth = [0.365368000,0.26565900000,0.161234000,0.160174000000,0.127769000]

plt.plot(x, Apriori, color='r', label='Apriori')
plt.plot(x, FP_growth, color='b', label='FP-Growth')

plt.ylabel('Running Time (second)')
plt.xlabel('min sup %')


plt.suptitle('Comparison between Apriori and FP-growth Algorithm')
plt.title('Dataset Name: mushroom.dat')
plt.legend(loc='upper right')

plt.yscale('log',basey = 2)

###tobechanged
plt.savefig('mushroom.pdf')
plt.savefig('mushroom.png')

# plt.yticks(Apriori+FP_growth,Apriori+FP_growth)
plt.xticks(x,x)



plt.show()