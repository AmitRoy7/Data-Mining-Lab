from matplotlib import pyplot as plt
import numpy as np


###tobechanged
x = [85,86,87,88,90]
Apriori = [175.237482,119.091542000000,81.167116,54.783790000000,54.783790000000]
FP_growth = [3.616744000000,3.479913000000,3.465913000000,3.398241000000,3.108630]

plt.plot(x, Apriori, color='r', label='Apriori')
plt.plot(x, FP_growth, color='b', label='FP-Growth')

plt.ylabel('Running Time (second)')
plt.xlabel('min sup %')


plt.suptitle('Comparison between Apriori and FP-growth Algorithms')
plt.title('Dataset Name: pumsb.dat')
plt.legend(loc='upper right')

plt.yscale('log',basey = 2)


###tobechanged
plt.savefig('pumsb.pdf')
plt.savefig('pumsb.png')

# plt.yticks(Apriori+FP_growth,Apriori+FP_growth)
plt.xticks(x,x)



plt.show()