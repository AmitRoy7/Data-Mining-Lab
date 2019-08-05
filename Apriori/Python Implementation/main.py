from DatasetClass import Dataset
from Apriori import *
global transactions
transactions = []

if __name__ == '__main__':

    while True:

        print("\n\t\t\tAPRIORI - frequenty itemset finding algorithm")
        print("\t\t=============================================================")

        datasets = ["Data Mining Book Example.txt", "FP-Growth Paper.dat", "mushroom.dat",
                    "retail.dat", "chess.dat", "kosarak.dat", "pumsb.dat", "pumsb_star.dat",
                    "connect.dat", "T10I4D100K.dat", "T40I10D100K.dat", "accidents.dat"]

        print("\n\n\t\t SELECT DATASET :\n")
        for i in range(len(datasets)):
            print("\t\t %d. %s" % ((i + 1), datasets[i]))

        print("\t\t 0. Exit")

        while True:
            print("\n\n\t\tEnter Choice: ", end="")
            choice = int(input())
            if choice == 0:
                exit(0)
            elif choice >= 1 and choice <= len(datasets):
                choice -= 1
                break
            print("Invalid Choice")

        datasetName = datasets[choice]
        myDataset = Dataset(datasetName)
        transactions, candidates = myDataset.loadDataset()
        # for x in transactions:
        #     print(x)
        # print(candidates)
        myDataset.datasetDetails()
        print("\n\t\tEnter Minimum Frequency Percentage%: ", end="")
        minSup = float(input())
        myDataset.upadateSupportThreshold(minSup)
        runApriori(myDataset)

