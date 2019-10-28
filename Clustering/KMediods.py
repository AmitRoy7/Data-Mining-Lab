from MixedDistance import *
import matplotlib.pyplot as plt
import matplotlib.markers
import numpy as np
import time


PLOT_FLAG = 0

#S = set of representative objects/tuple
#U = set of non-representive objects/tuple
#Dp = distance to the closest object for a arbitary point p
#Ep = distance to the 2nd closest object for a arbitary point p

K_VECTOR = []
COST_VECTOR = []
RUNTIME_VECTOR = []
PURITY_VECTOR = []
SILHOUTTE_VECTOR = []

def getCost(Dj):
    cost = 0.0
    for x in Dj:
        cost += x
    return cost

def updateDpAndEp(n,Dp,Ep,S,U,DisMat):
    for i in range(0,n):
        mn1,mn2 = math.inf,math.inf
        for j in S:
            distance = DisMat[max(i,j)][min(i,j)]
            if distance < mn1:
                mn2 = mn1
                mn1 = distance
            elif distance<mn2:
                mn2 = distance
        Dp[i],Ep[i] = mn1,mn2
    return

def BUILD(n,k,data,DisMat):

    S = []
    U = list(range(0, len(data)))

    Dp = [math.inf] * n
    Ep = [math.inf] * n

    init_dist = []
    for i in range(0, n):
        tot = 0
        for j in range(0, i+1):
            mx = max(i, j)
            mn = min(i, j)
            # print(mn,mx)
            tot += DisMat[mx][mn]
        init_dist.append(tot)
    first_mediod = np.argmin(init_dist)
    # print(init_dist)
    # print(first_mediod)
    S.append(first_mediod)
    U.remove(first_mediod)
    updateDpAndEp(n, Dp, Ep, S, U, DisMat)

    while len(S)<k:

        mx,newMediod = - math.inf, -1

        for i in U:

            gi = 0

            for j in U:
                if i == j:
                    continue
                Dj = Dp[j]
                distance = DisMat[max(i,j)][min(i,j)]

                cji = 0
                if Dj > distance:
                    cji = max(Dj - distance,cji)
                gi += cji

            if gi >= mx:
                mx,newMediod = gi,i

        S.append(newMediod)
        U.remove(newMediod)
        updateDpAndEp(n, Dp, Ep, S, U, DisMat)

    return S,U,Dp,Ep


def SWAP(n,Dp,Ep,S,U,DisMat):

    # print("Initial Representative: ")
    # print(S)
    # print("Within Cluster Variation:", getCost(Dp))

    while True:

        mn,ii,hh = math.inf,-1,-1

        for i in S:
            for h in U:

                Tih = 0

                for j in U:
                    if j == h:
                        continue

                    disji = DisMat[max(i,j)][min(i,j)]
                    disjh = DisMat[max(j,h)][min(j,h)]
                    Dj = Dp[j]
                    Kjih = 0

                    if disji > Dj:

                        Kjih = min(disjh - Dj,0)

                    elif disji == Dj:

                        Kjih = min(disjh,Ep[j]) - Dp[j]

                    Tih += Kjih

                if Tih < mn:
                    mn,ii,hh = Tih,i,h

        Tih = mn

        # print("Within Cluster Variation:", getCost(Dp))

        if Tih < 0:
            S.remove(ii)
            U.append(ii)
            U.remove(hh)
            S.append(hh)
            updateDpAndEp(n, Dp, Ep, S, U, DisMat)
        else:
            cost = getCost(Dp)
            print("Within Cluster Variation:", cost)
            COST_VECTOR.append(cost)
            break

    return S,U,Dp,Ep

def assignCluster(n,data,S,DisMat,Dp):
    clusters = {}
    for j in S:
        clusters[j] = []

    for i in range(0,n):
        for j in S:
            distance = DisMat[max(i,j)][min(i,j)]
            closest = Dp[i]

            if distance == closest:
                clusters[j].append(i)
                break
    return clusters




if __name__ == '__main__':

    print("\n\n\t\t K-Mediods Clustering Algorithm\n\n")

    data, types, info, order_info,has_class,class_map,d,dataset = readFile()
    if d < 3:
        PLOT_FLAG = 1
    else:
        PLOT_FLAG = 0
    DisMat = getDissimilaryMatrix(data,types,info,order_info)
    n = len(data)
    # while True:
    #     k = int(input("Enter k: "))
    #     if k>n:
    #         print("K should be less than n")
    #     else:
    #         break

    print("Enter l: ", end="")
    l = int(input())
    print("Enter r: ", end="")
    r = int(input())
    for k in range(l,r+1):

        K_VECTOR.append(k)

        st = time.time()

        DisMat = getDissimilaryMatrix(data, types, info, order_info)
        S,U,Dp,Ep = BUILD(n,k,data,DisMat)
        S, U, Dp, Ep = SWAP(n,Dp,Ep,S,U,DisMat)
        clusters = assignCluster(n,data,S,DisMat,Dp)
        if has_class:
            purity = calculate_purity(clusters,n,class_map)
            PURITY_VECTOR.append(purity)

            print("Purity:",purity)

        silhouette_coeff = 0
        for obj in range(n):
            silhouette_coeff += calculate_silhouette_coefficient(data, clusters, obj, types, info, order_info)
        silhouette_coeff /= n
        print("Silhoutte Coefficient:",silhouette_coeff)
        SILHOUTTE_VECTOR.append(silhouette_coeff)


        en = time.time()
        print("Runtime:",en-st)
        RUNTIME_VECTOR.append((en-st))

        for representative in clusters.keys():
            ### print("Cluster Representative: ", data[representative])
            # print("Cluster Representative: ",representative)
            members = clusters[representative]
            # for member in members:

            #     print(member, end=" ")
            # print("")

            cluster_member = []

            if PLOT_FLAG == 1:

                for member in members:
                    cluster_member.append(data[member])

                cluster_member = np.array(cluster_member)
                x, y = cluster_member.T
                plt.scatter(x, y)

        if PLOT_FLAG == 1:

            cluster_leader = []
            for x in S:
                temp = data[x]
                xx = temp[0]
                yy = temp[1]
                plt.scatter(xx,yy,marker="*")


            plt.suptitle("K-mediods algorithm Visualization")
            plt.title("Dataset Name: "+dataset)
            plt.show()
            print("Converged")


    print("K: ")
    for k in K_VECTOR:
        print(k)

    print("Runtime: ")
    for runtime in RUNTIME_VECTOR:
        print(runtime)

    print("Purity: ")
    for purity in PURITY_VECTOR:
        print(purity)

    print("Silhouette Coefficient: ")
    for coeff in SILHOUTTE_VECTOR:
        print(coeff)


    print("COST:(WCV)")
    for wcv in COST_VECTOR:
        print(wcv)



