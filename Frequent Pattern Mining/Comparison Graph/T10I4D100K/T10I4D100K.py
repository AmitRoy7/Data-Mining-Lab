from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [0.5,0.60,0.75,0.80,1]
Apriori = [27.888561,22.540296000000,20.185786,17.769763000000,14.489263]
FP_growth = [9.700328000000,8.643774000000,8.607398000000,8.095570000000,6.745633000000]

plt.plot(x, Apriori, color='r', label='Apriori')
plt.plot(x, FP_growth, color='b', label='FP-Growth')

plt.ylabel('Running Time (second)')
plt.xlabel('min sup %')


plt.suptitle('Comparison between Apriori and FP-growth Algorithm')
plt.title('Dataset Name: T10I4D100K.dat')
plt.legend(loc='upper right')

plt.yscale('log',basey = 2)

###tobechanged
plt.savefig('T10I4D100K.pdf')
plt.savefig('T10I4D100K.png')

# plt.yticks(Apriori+FP_growth,Apriori+FP_growth)
plt.xticks(x,x)



plt.show()