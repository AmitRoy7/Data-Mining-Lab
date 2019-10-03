from time import time

import numpy as np
import math

def readFile():

    datasets = ["iris","breast-cancer","book"]

    for i in range(len(datasets)):
        print(i+1,":", datasets[i])
    print()
    dataset = int(input("Enter dataset number: ")) - 1

    print("Reading dataset: ",datasets[dataset])

    types = []
    for l in open(datasets[dataset] + "/types.info").readlines():
        types.append(l.replace("\n", ""))
    print(types)

    info = [None for i in range(len(types))]

    data = []
    for l in open(datasets[dataset] + "/dataset.data").readlines():
        l = l.replace("\n", "")
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
        data.append(d_tuple)

    order_info = []
    for l in open(datasets[dataset] + "/order.info").readlines():
        l = l.replace(" ", "").replace("\n", "")
        l = l.split(",")
        order_info.append(l)

    return data,types,info,order_info


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

if __name__ == '__main__':

    data, types, info, order_info = readFile()

    # st = time()
    DisMat = getDissimilaryMatrix(data,types,info,order_info)
    # en = time()

    # print((en-st))


