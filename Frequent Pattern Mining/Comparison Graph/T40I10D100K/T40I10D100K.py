from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [4,5,6]
Apriori = [58.012575,38.564493,24.673382]
FP_growth = []

plt.plot(x, Apriori, color='r', label='Apriori')
plt.plot(x, FP_growth, color='b', label='FP-Growth')

plt.ylabel('Running Time (second)')
plt.xlabel('min sup %')


plt.suptitle('Comparison between Apriori and FP-growth Algorithm')
plt.title('Dataset Name: T40I10D100K.dat')
plt.legend(loc='upper left')

###tobechanged
plt.savefig('T40I10D100K.pdf')
plt.savefig('T40I10D100K.png')

# plt.yticks(Apriori+FP_growth,Apriori+FP_growth)
plt.xticks(x,x)



plt.show()