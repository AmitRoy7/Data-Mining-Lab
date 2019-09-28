# import math
# from sklearn.datasets import *
#
# X = load_diabetes().data
# Y = load_diabetes().target
#
# print(X)
#
# print(math.log(1,2.0))

import re

path = "/home/amit-roy/Dropbox/Own 4-2/2.Lab/CSE-4255: Introducing Data mining and warehousnig Lab/Classification/Decision Tree Amt/"

datasets = ["Book Example","Mushroom","Iris","Breast Cancer","Breast Cancer Wisconsin (Diagnostic)","Breast Cancer Wisconsin (Original)","Breast Cancer Wisconsin (Prognostic)",
            "Abalone","Car","Play Tennis"]


print("\n\t\t\tDecision Tree - Classification Algorithm")
print("\t\t=============================================================\n\n")

for idx in range(len(datasets)):
    print("\t\t%d. %s"%(idx+1,datasets[idx]))
print("\t\t0. Exit")

while True:
    print("\n\n\t\tEnter Choice: ", end="")
    choice = int(input())
    if choice == 0:
        exit(0)
    elif choice >= 1 and choice <= len(datasets):
        choice -= 1
        break
    print("Invalid Choice")

datasetpath = path+datasets[choice]+"/dataset.data"
labelinfopath = path+datasets[choice]+"/labelinfo.data"

dataset = open(datasetpath,"r")
labelinfo = open(labelinfopath,"r")

attribute_name = []
feature_matrix = []
class_matrix = []

labelinfo = labelinfo.readlines()
dataset = dataset.readlines()

class_idx = 0
missing_attribute = 0

for idx in range(len(labelinfo)):
    label = labelinfo[idx]
    label = label.replace("\n","")

    if label.startswith("class"):
        class_idx = idx
        continue
    elif label.startswith("Missing Attribute Values"):
        label = label.replace("Missing Attribute Values ","")
        if label == "?":
            missing_attribute = 1
        else:
            missing_attribute = 0
        continue
    elif label != "":
        label = re.sub(" +"," ",label)
        label = label.split(" ")

        # print(label)


        attribute = label[0]
        for idx in range(1,len(label)-1):
            attribute += " "
            attribute += label[idx]
        type = int(label[len(label)-1])

        # 0 means nominal/categorical/discrete
        # 1 means numerical/continuous
        # 2 means serial/TID/codeno
        # 3 means class type

        # if type != 2:
        attribute_name.append((attribute,type))

# print("Has Missing Attributes: " , missing_attribute)
print("Class Label Idx: ", class_idx)
# for x in attribute_name:
#     print(x)


# for idx in range(len(dataset)):
#     print(dataset[idx])
#     if idx > 100:
#         break

for idx in range(len(dataset)):
    tuple = dataset[idx]
    tuple = tuple.replace("\n","")
    tuple = tuple.split(",")

    print(tuple)

    class_name = tuple[class_idx]
    class_matrix.append(class_name)
    tuple.remove(class_name)
    feature_matrix.append(tuple)

for idx in range(len(feature_matrix)):
    print(feature_matrix[idx],class_matrix[idx])
    if(idx>100):
        break







