from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [40,41,42,44,45]
Apriori = [127.244867 ,93.378363000000,60.831316,24.871440000000,11.100331]
FP_growth = [19.113025000000,19.104602000000,18.476802,16.354517000000,4.388295]

plt.plot(x, Apriori, color='r', label='Apriori')
plt.plot(x, FP_growth, color='b', label='FP-Growth')

plt.ylabel('Running Time (second)')
plt.xlabel('min sup %')


plt.suptitle('Comparison between Apriori and FP-growth Algorithm')
plt.title('Dataset Name: pumsb_star.dat')
plt.legend(loc='upper right')

plt.yscale('log',basey = 2)

###tobechanged
plt.savefig('pumsb_star.pdf')
plt.savefig('pumsb_star.png')

# plt.yticks(Apriori+FP_growth,Apriori+FP_growth)
plt.xticks(x,x)



plt.show()