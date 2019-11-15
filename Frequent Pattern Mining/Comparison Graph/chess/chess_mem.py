from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [80,82,85,87,90]
Apriori = [21432,20604,19952,19256,19124]
FP_growth = [40732,39544,38620,38032,37900]

plt.plot(x, Apriori, color='r', label='Apriori')
plt.plot(x, FP_growth, color='b', label='FP-Growth')

plt.ylabel('Memory Usage (VM + RSS)')
plt.xlabel('min sup %')


plt.suptitle('Comparison between Apriori and FP-growth Algorithm')
plt.title('Dataset Name: chess.dat')
plt.legend(loc='upper right')

# plt.yscale('log',basey = 2)

###tobechanged
plt.savefig('chess_mem.pdf')
plt.savefig('chess_mem.png')

# plt.yticks(Apriori+FP_growth,Apriori+FP_growth)
plt.xticks(x,x)



plt.show()