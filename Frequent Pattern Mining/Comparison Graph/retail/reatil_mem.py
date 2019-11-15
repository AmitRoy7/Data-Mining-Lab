from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [0.05,0.10,0.15,0.20,0.25]
Apriori = [2737348,852744,394696,262688,234032]
FP_growth = [239080,240856,241120,241516,241516]

plt.plot(x, Apriori, color='r', label='Apriori')
plt.plot(x, FP_growth, color='b', label='FP-Growth')

plt.ylabel('Memory Usage (VM + RSS)')
plt.xlabel('min sup %')


plt.suptitle('Comparison between Apriori and FP-growth Algorithm')
plt.title('Dataset Name: retail.dat')
plt.legend(loc='upper right')

plt.yscale('log',basey = 2)

###tobechanged
plt.savefig('retail_mem.pdf')
plt.savefig('retail_mem.png')

# plt.yticks(Apriori+FP_growth,Apriori+FP_growth)
plt.xticks(x,x)



plt.show()