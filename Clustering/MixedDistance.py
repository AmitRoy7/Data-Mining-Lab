from time import time
import re
import numpy as np
import math

from copy import deepcopy


def readFile():

    datasets = ["Iris(With Purity)","Glass(With Purity)","breast-cancer(With Purity)","Libras Movement(With Purity)","Seeds(With purity)","R15(With Purity)",
                "Thyroid","Wine","Yeast","Breast","Wdbc","leaves"
                ,"Aggregation","Compound","Pathbased","Spiral","Jain","Flame","Sample"]
                # "iris","breast-cancer","book","S1","S2","S3","S4","A1","A2","A3"
                # ,"Birch1","Birch2","Birch3"]

    for i in range(len(datasets)):
        print(i+1,":", datasets[i])
    print()
    dataset = int(input("Enter dataset number: ")) - 1

    print("Reading dataset: ",datasets[dataset])

    types = []
    for l in open(datasets[dataset] + "/types.info").readlines():
        types.append(l.replace("\n", ""))


    info = [None for i in range(len(types))]


    data = []
    has_class = False
    class_map = {}
    row = 0
    for l in open(datasets[dataset] + "/dataset.data").readlines():
        l = l.replace("\n", "")
        l = re.sub("\s+", ",", l.strip())
        l = l.split(",")
        d_tuple = []
        for i in range(len(types)):
            if types[i] == "Numeric":


                d_tuple.append(float(l[i]))
                if info[i] is None:
                    info[i] = (float(l[i]), float(l[i]))
                info[i] = (max(info[i][0], float(l[i])), info[i][1])
                info[i] = (info[i][0], min(info[i][1], float(l[i])))
            if types[i] == "Nominal":
                d_tuple.append(l[i])
            if types[i] == "Binary":
                d_tuple.append(l[i])
            if types[i] == "Ordinal":
                d_tuple.append(l[i])
            if types[i] == "Class":

                has_class = True
                class_map[row] = l[i]
                row += 1

            if types[i] == "R":
                continue


        data.append(d_tuple)

    print("Total Tuples, N: ",len(data))
    d = len(data[0])
    print("Dimension Per Tuple, D:",d)



    info_temp = []
    for x in info:
        if x is None:
            continue
        info_temp.append(x)
    info = deepcopy(info_temp)

    types_temp = []

    for x in types:
        if x=="R" or x=="Class":
            continue
        types_temp.append(x)

    types = deepcopy(types_temp)

    # print(info)

    order_info = []
    for l in open(datasets[dataset] + "/order.info").readlines():
        l = l.replace(" ", "").replace("\n", "")
        l = l.split(",")
        if l[0]=='R':
            continue
        order_info.append(l)

    return data,types,info,order_info,has_class,class_map,d,datasets[dataset]


def dis(row1, row2, types, info, order_info):
    up, down = 0, 0
    for i in range(len(types)):



        if types[i] == "Numeric":
            down += 1
            up += math.fabs(row1[i]-row2[i])/(info[i][0]-info[i][1])
        if types[i] == "Nominal":
            down += 1
            if row1[i] != row2[i]:
                up += 1
        if types[i] == "Binary":
            if row1[i] == order_info[i][1] and row2[i]==order_info[i][1]:
                continue
            down += 1
            if row1[i] != row2[i]:
                up += 1
        if types[i] == "Ordinal":
            r1, r2 = None, None

            for o in range(len(order_info[i])):

                if order_info[i][o] == row1[i]:
                    r1 = o
                if order_info[i][o] == row2[i]:
                    r2 = o

            distance = math.fabs(r1 - r2)/(len(order_info[i])-1)
            down += 1
            up += distance
    return up/down


def getDissimilaryMatrix(data, types, info, order_info):

    DisMat = {}

    n = len(data)
    for i in range(0, n):
        DisMat[i] = {}
        for j in range(0, i + 1):
            row1 = data[i]
            row2 = data[j]
            distance = dis(row1, row2, types, info, order_info)
            DisMat[i][j] = distance

    # for i in range(0,n):
    #     for j in range(0,i+1):
    #         print("%0.2lf "%DisMat[i][j],end="")
    #     print("")
    return DisMat


def calculate_silhouette_coefficient(data,clusters, object, types, info, order_info):
    a = 0
    b = math.inf

    for x in clusters.keys():
        cluster = clusters[x]

        if object in cluster:
            for sample_object in cluster:
                if sample_object == object:
                    continue
                a += dis(data[sample_object], data[object], types, info, order_info)
            a /= (len(cluster) - 1)
        else:
            temp = 0
            for sample_object in cluster:
                temp += dis(data[sample_object], data[object], types, info, order_info)
            temp /= (len(cluster))
            b = min(temp, b)

    return (b - a) / (max(a, b))


def calculate_purity(clusters,n,class_map):
    tot = 0
    for idx in clusters.keys():
        cluster = clusters[idx]
        cnt = {}
        for tuple_idx in cluster:
            tuple_class = class_map[tuple_idx]
            if tuple_class not in cnt.keys():
                cnt[tuple_class] = 0
            cnt[tuple_class] += 1

        res = 0
        for x in cnt.keys():
            res = max(res,cnt[x])

        tot += res
    return (tot/n)


if __name__ == '__main__':

    data, types, info, order_info = readFile()

    # st = time()
    DisMat = getDissimilaryMatrix(data,types,info,order_info)
    # en = time()

    # print((en-st))


