from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [90,92,93,94,95]
Apriori = [500.158217,155.815078,93.532932000000,52.637221000000,27.998194]
FP_growth = [1.705981000000,1.658458000000,1.618286000000,1.596667000000,1.538772]

# for y in range(0,len(Apriori)):
#     Apriori[y] = Apriori[y] * 1000;
# for y in range(0,len(FP_growth)):
#     FP_growth[y] = FP_growth[y] * 1000;

plt.plot(x, Apriori, color='r', label='Apriori')
plt.plot(x, FP_growth, color='b', label='FP-Growth')

plt.ylabel('Running Time (second)')
plt.xlabel('min sup %')


plt.suptitle('Comparison between Apriori and FP-growth Algorithm')
plt.title('Dataset Name: connect.dat')
plt.legend(loc='upper right')

plt.yscale('log',basey = 2)

###tobechanged
plt.savefig('connect.pdf')
plt.savefig('connect.png')

# plt.yticks(Apriori+FP_growth,Apriori+FP_growth)
plt.xticks(x,x)



plt.show()