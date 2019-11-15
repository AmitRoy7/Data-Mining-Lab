from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [0.05,0.10,0.15,0.20,0.25]
Apriori = [369.635480,137.401388,67.480012,38.258281000000,27.309194000000]
FP_growth = [12.675318,8.425148,5.716512,4.873855000000,4.115335000000]

plt.plot(x, Apriori, color='r', label='Apriori')
plt.plot(x, FP_growth, color='b', label='FP-Growth')

plt.ylabel('Running Time (second)')
plt.xlabel('min sup %')


plt.suptitle('Comparison between Apriori and FP-growth Algorithm')
plt.title('Dataset Name: retail.dat')
plt.legend(loc='upper right')

plt.yscale('log',basey = 2)

###tobechanged
plt.savefig('retail.pdf')
plt.savefig('retail.png')

# plt.yticks(Apriori+FP_growth,Apriori+FP_growth)
plt.xticks(x,x)



plt.show()