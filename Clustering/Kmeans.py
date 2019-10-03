from MixedDistance import *
import numpy as np
import random
import copy

# data = np.random.rand(5000, 10)

data, types, info, order_info = readFile()
data = copy.deepcopy(data)

# for x in temp_data:
#     data.append(x[:len(x)-1])
#     print(x[:len(x)-1])

DisMat = getDissimilaryMatrix(data,types,info,order_info)

k = int(input("Enter k: "))
clusters = random.sample([data[i] for i in range(len(data))], k=k)
cluster_id = [None for i in range(len(data))]

while True:
    clusters_p = copy.deepcopy(clusters)
    for i in range(len(data)):
        for c in range(len(clusters)):
            distance = DisMat[max(i,c)][min(i,c)]
            if cluster_id[i] is None:
                cluster_id[i] = (c, distance)
            elif distance < cluster_id[i][1]:
                cluster_id[i] = (c, distance)
    temp = [[0.0 for j in range(len(data[0]))] for i in range(k)]
    count = [0 for i in range(k)]
    for i in range(len(data)):
        count[cluster_id[i][0]] += 1
        for j in range(len(data[i])):
            temp[cluster_id[i][0]][j] += data[i][j]
    for i in range(k):
        for j in range(len(temp[i])):
            temp[i][j] /= count[i]
        clusters[i] = np.array(temp[i])

    cost = 0.0
    for i in range(len(data)):
        distance = np.linalg.norm(data[i] - clusters[cluster_id[i][0]], ord=2)
        cost += distance
    cost /= len(data)
    print(cost)

    eq = True
    for i in range(len(clusters)):
        for j in range(len(clusters[i])):
            if clusters_p[i][j] != clusters[i][j]:
                eq = False
    if eq:
        break


final_clusters = {}
for x in cluster_id:
    final_clusters[x[0]] = []

for obj in range(0,len(data)):
    leader = cluster_id[obj][0]
    final_clusters[leader].append(obj)

for leader in final_clusters.keys():
    print("Cluster Leader: ",leader)
    members = final_clusters[leader]
    for member in members:
        print(member,end=" ")
    print("")

print("Converged")



