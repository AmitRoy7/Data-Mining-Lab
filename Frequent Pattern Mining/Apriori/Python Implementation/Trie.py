freq = {}


class Trie(object):
    def __init__(self):
        self.endmark = False
        self.mp = {}
        self.cnt = 0

    def init(self):
        self.mp.clear()




def insertTrie(curr,st):
    # print(st)
    for it in st:
        if curr.mp.get(it)==None:
            # print(it)
            curr.mp[it] = Trie()
        curr = curr.mp[it]
    curr.endmark = True

def updateFrequency(transaction,curr):
    if curr.endmark == True:
        return

    for it in curr.mp.keys():
        item = it
        global transactions
        if item not in transaction:
            continue
        curr.mp[it].cnt += 1
        updateFrequency(transaction,curr.mp[it])


def mapUpdate(curr,st):
    if curr.endmark == True:
        freq[st] = curr.cnt
        # print(st + ":" + str(freq[st]))
        return

    if st!="":
        st += " "
    for it in curr.mp.keys():
        mapUpdate(curr.mp[it],st+it)


def myDelete(cur):
    for it in cur.mp.keys():
        myDelete(cur.mp[it])
    cur.init()
    del(cur)
    return







