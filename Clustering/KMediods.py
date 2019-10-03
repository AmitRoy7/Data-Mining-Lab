from MixedDistance import *
import numpy as np

#S = set of representative objects/tuple
#U = set of non-representive objects/tuple
#Dp = distance to the closest object for a arbitary point p
#Ep = distance to the 2nd closest object for a arbitary point p

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

        if Tih < 0:
            S.remove(ii)
            U.append(ii)
            U.remove(hh)
            S.append(hh)
            updateDpAndEp(n, Dp, Ep, S, U, DisMat)
        else:
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

    data, types, info, order_info = readFile()
    DisMat = getDissimilaryMatrix(data,types,info,order_info)
    n = len(data)
    while True:
        k = int(input("Enter k: "))
        if k>n:
            print("K should be less than n")
        else:
            break

    S,U,Dp,Ep = BUILD(n,k,data,DisMat)
    S, U, Dp, Ep = SWAP(n,Dp,Ep,S,U,DisMat)
    clusters = assignCluster(n,data,S,DisMat,Dp)

    print(Dp)

    for representative in clusters.keys():
        print("Cluster Representative: ",representative+1)
        members = clusters[representative]
        for member in members:
            print(member+1,end=" ")
        print("")

