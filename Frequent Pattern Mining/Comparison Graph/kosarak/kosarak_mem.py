from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [0.25,0.30,0.5,0.6,0.75]
Apriori = [221888,199052,187096,186436,185960]
FP_growth = [1748724,1696284,1641968,1641968,1637080]

plt.plot(x, Apriori, color='r', label='Apriori')
plt.plot(x, FP_growth, color='b', label='FP-Growth')

plt.ylabel('Memory Usage (VM + RSS)')
plt.xlabel('min sup %')


plt.suptitle('Comparison between Apriori and FP-growth Algorithm')
plt.title('Dataset Name: kosarak.dat')
plt.legend(loc='upper right')

plt.yscale('log',basey = 2)

###tobechanged
plt.savefig('kosarak_mem.pdf')
plt.savefig('kosarak_mem.png')

# plt.yticks(Apriori+FP_growth,Apriori+FP_growth)
plt.xticks(x,x)



plt.show()