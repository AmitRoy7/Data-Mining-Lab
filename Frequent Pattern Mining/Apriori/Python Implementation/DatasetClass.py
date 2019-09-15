import math
PRINT_FLAG = True
class Dataset:
    def __init__(self,file):
        super(Dataset,self).__init__()
        self.datasetName = file
        self.minFreq = 0
        self.minSup = 0
        self.transactions = []
        self.freq = {}
        self.candidates = []
        self.totalLength = 0
        self.numOfTransaction = 0
        self.distinctItems = 0
        self.avgLength = 0
        self.densityPercentage = 0
        self.datasetType = ""
        self.afterJoin = []
        self.afterPrune = []
        self.actualFrequent = []

    def loadDataset(self):
        print("\n\t\tReading Dataset...")
        fin = open("Dataset/" + self.datasetName,'r')
        ch = fin.read()
        ch = ch.split("\n")

        for temp in ch:
            temp = temp.strip()
            temp = temp.replace(","," ")

            if temp == "":
                continue

            temp = temp.split(" ")
            itemset = []

            for item in temp:
                item = item.strip()
                if item != "":
                    itemset.append(item)

            itemset = sorted(itemset)

            self.totalLength += len(itemset)
            self.transactions.append(itemset)

            for item in itemset:
                item = item.strip()
                if item == "":
                    continue
                if item not in self.freq:
                    self.candidates.append(item)
                    self.freq[item] = 0
                self.freq[item] += 1

        self.candidates = sorted(self.candidates)

        self.numOfTransaction = len(self.transactions)
        self.distinctItems = len(self.freq.keys())
        self.avgLength = self.totalLength/self.numOfTransaction
        self.densityPercentage = (self.avgLength/self.distinctItems) * 100
        if self.densityPercentage>=10.0:
            self.datasetType = "Dense Dataset"
        else:
            self.datasetType = "Sparse Dataset"
        fin.close()
        return self.transactions,self.candidates

    def upadateSupportThreshold(self,minSup):
        self.minSup = minSup
        self.minFreq = math.ceil((self.minSup*self.numOfTransaction)/100);
        print("\n\t\tMinimum Support Threshold: %d"%self.minFreq)


    def datasetDetails(self):
        print("\n\t\t\t\t\tDataset Description")
        print("\t\t=============================================================")
        print("\n\t\tDataset Name: %s"%(self.datasetName))
        print("\t\tNo. of Transactions: %d"%(self.numOfTransaction))
        print("\t\tDistinct Items: %d"%(self.distinctItems))
        print("\t\tAvg. Length: %0.2lf"%(self.avgLength))
        print("\t\tDensity Percentage: %0.2lf %%"%(self.densityPercentage))
        print("\t\tDataset Type: %s"%(self.datasetType))

