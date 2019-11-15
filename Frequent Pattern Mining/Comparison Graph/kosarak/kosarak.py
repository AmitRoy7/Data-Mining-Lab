from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [0.25,0.30,0.5,0.6,0.75]
Apriori = [167.375497,117.729638000000,50.247591,37.097422000000,24.935911]
FP_growth = [85.003965,54.974787000000,27.932876,24.395974000000,19.161934]

plt.plot(x, Apriori, color='r', label='Apriori')
plt.plot(x, FP_growth, color='b', label='FP-Growth')

plt.ylabel('Running Time (second)')
plt.xlabel('min sup %')


plt.suptitle('Comparison between Apriori and FP-growth Algorithm')
plt.title('Dataset Name: kosarak.dat')
plt.legend(loc='upper right')

plt.yscale('log',basey = 2)

###tobechanged
plt.savefig('kosarak.pdf')
plt.savefig('kosarak.png')

# plt.yticks(Apriori+FP_growth,Apriori+FP_growth)
plt.xticks(x,x)



plt.show()