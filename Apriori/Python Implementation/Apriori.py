from datetime import datetime
from Trie import *
from copy import deepcopy
PRINT_FLAG = False

afterJoin = []
afterPrune = []
actualFrequent = []

def printSpace(x):
    # print(x,end="")
    for xx in range(x):
        print(" ",end="")


def runApriori(dataset):

    afterJoin.clear()
    afterPrune.clear()
    actualFrequent.clear()

    stTime = datetime.now()

    print("\n\n\t\t=========================================================")
    print("\t\t|Level-i| After Joining | After Pruning |Actual Frequent|")
    print("\t\t=========================================================")

    transactions = deepcopy(dataset.transactions)
    candidates = deepcopy(dataset.candidates)
    frequency = deepcopy(dataset.freq)
    minFreq = deepcopy(dataset.minFreq)

    i = 1

    cur_candidates = []
    prev_candidates = []

    totAfterJoin = 0
    totAfterPrune = 0
    totFreqPattern = 0

    while True:

        if i == 1:
            cur_candidates = deepcopy(candidates)
            afterJoin.append(len(cur_candidates))
            afterPrune.append(len(cur_candidates))
            candidates.clear()

        else:
            cur_candidates = aprioriGen(prev_candidates, i - 1)
            # for x in cur_candidates:
            #      print(x)
            candidates.clear()
            freq.clear()

            root = Trie()

            for it in cur_candidates:
                newCandidate = str(it).split(" ")
                insertTrie(root,newCandidate)


            for transaction in transactions:
                cur = root
                updateFrequency(transaction, cur)

            cur = root
            mapUpdate(cur, "")

            myDelete(root)
            frequency = deepcopy(freq)

            # for x in frequency:
            #     print(x + " " + str(frequency[x]))

        for it in cur_candidates:
            if frequency[it] >= minFreq:
                candidates.append(it)

        if afterJoin[i-1] > 0:

            actualFrequent.append(len(candidates))
            print("\t\t| L-%d\t|\t\t%d\t\t|\t\t%d\t\t|\t\t%d\t\t|"
            % (i, afterJoin[i - 1], afterPrune[i - 1],actualFrequent[i - 1]))
            totAfterJoin += afterJoin[i - 1]
            totAfterPrune += afterPrune[i - 1]
            totFreqPattern += actualFrequent[i - 1]
            print("\t\t=========================================================")

        if len(candidates) > 0:

            # print(len(candidates))

            # global PRINT_FLAG
            # if PRINT_FLAG==True:
            #     print("\n\n\t\t Frequent %d itemsets: " % (i))
            #     for it in candidates:
            #         print("\t\t %s : %d" % (it, frequency[it]))

            prev_candidates = deepcopy(candidates)
            i += 1
        else:
            break



    print("\t\t| Total |",end="")
    printSpace (15-len(str(totAfterJoin))-6)
    print(totAfterJoin,end="")
    printSpace(6)
    print("|",end="")

    printSpace(15 - len(str(totAfterPrune))-6)
    print(totAfterPrune, end="")
    printSpace(6)
    print("|", end="")

    printSpace(15 - len(str(totAfterPrune))-6)
    print(totFreqPattern, end="")
    printSpace(6)
    print("|")

    print("\t\t=========================================================")

    endTime = datetime.now()

    execution_time = endTime - stTime

    print("\n\n\t\tExecution Time: ", end="")
    print(execution_time)
    print("\n\n")

    return


def aprioriGen(st, sz):
    flag = False
    st2 = []
    cntJoinStep = 0

    for i in range(len(st)):
        for j in range(i + 1, len(st)):

            # print(st[i] + " " + st[j])

            v1 = str(st[i]).split(" ")
            v2 = str(st[j]).split(" ")

            flag = True

            for k in range(0, sz - 1):
                if v1[k] != v2[k]:
                    flag = False
                    break

            if flag == False:
                break

            v1.append(v2[sz - 1])
            cntJoinStep += 1



            # prune_step

            for k in range(0, len(v1)):

                temp = ""
                first = True

                for l in range(0, len(v1)):

                    if k == l:
                        continue

                    if first:
                        first = False
                    else:
                        temp += " "

                    temp += v1[l]

                # checking whether it has an infrequent subset
                # if yes then it is not a candidate
                # apriori  property

                if temp not in st:  # use binary search here
                    flag = False
                    break

                if flag == False:
                    break

            if flag:
                tmp = ""
                for k in range(len(v1)):
                    if k > 0:
                        tmp += " "
                    tmp += v1[k]
                st2.append(tmp)

    afterJoin.append(cntJoinStep)
    afterPrune.append(len(st2))
    st2 = sorted(st2)
    # print(cntJoinStep1)
    # for x in st2:
    #     print("XX"+x+"XX")
    return st2
