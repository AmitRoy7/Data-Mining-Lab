import re
from copy import deepcopy
from matplotlib import pyplot as plt
import time
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import KFold

from sklearn.metrics import roc_curve
from sklearn.metrics import auc

import math
import os
import termtables as tt
import numpy as np


# def draw_auc(y_true, y_score):
#     fpr, tpr, thresholds = roc_curve(y_true, y_score)
#     roc_auc = auc(y_true, y_score)
#
#     # Plot ROC curve
#     plt.plot(fpr, tpr, label='ROC curve (area = %0.3f)' % roc_auc)
#     plt.plot([0, 1], [0, 1], 'k--')  # random predictions curve
#     plt.xlim([0.0, 1.0])
#     plt.ylim([0.0, 1.0])
#     plt.xlabel('False Positive Rate or (1 - Specifity)')
#     plt.ylabel('True Positive Rate or (Sensitivity)')
#     plt.title('Receiver Operating Characteristic')
#     plt.legend(loc="lower right")


def getImpClass(class_matrix):
    cntMp = {}
    mx = 10000000000000000000000
    res = ""
    for tuple in class_matrix:
        attVal = tuple
        if attVal not in cntMp:
            cntMp[attVal] = 0
        cntMp[attVal] += 1

        if cntMp[attVal] < mx:
            mx = cntMp[attVal]
            res = attVal
    return res


def getMostCommonAttVal(class_matrix, idx):
    cntMp = {}
    mx = 0
    res = ""
    for tuple in class_matrix:
        attVal = tuple[idx]
        if attVal not in cntMp:
            cntMp[attVal] = 0
        cntMp[attVal] += 1

        if cntMp[attVal] > mx:
            mx = cntMp[attVal]
            res = attVal
    return res


def readFile():
    path = os.getcwd()
    path += "/"

    datasets = ["Sample Input", "Book Example", "Iris", "Wine",
                "Breast Cancer", "Breast Cancer Wisconsin (Diagnostic)",
                "Breast Cancer Wisconsin (Original)", "Breast Cancer Wisconsin (Prognostic)", "Cylinder Bands",
                "Car", "Mushroom", "Wine Quality"]
    # "Abalone", "Play Tennis","Poker Hand Testing"]

    print("\n\t\t\t\t\tNaive Bayes - Classification Algorithm")
    print("\t\t=============================================================\n\n")
    print("\t\t\t\tSelect Dataset\n\n")

    for idx in range(len(datasets)):
        print("\t\t%d. %s" % (idx + 1, datasets[idx]))
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

    datasetpath = path + datasets[choice] + "/dataset.data"
    labelinfopath = path + datasets[choice] + "/labelinfo.data"

    dataset = open(datasetpath, "r")
    labelinfo = open(labelinfopath, "r")

    attribute_name = []
    feature_matrix = []
    class_matrix = []

    labelinfo = labelinfo.readlines()
    dataset = dataset.readlines()

    class_idx = 0
    missing_attribute = 0

    continuous_attribute = {}

    for idx in range(len(labelinfo)):
        label = labelinfo[idx]
        label = label.replace("\n", "")

        if label.startswith("class"):
            class_idx = idx
            continue
        elif label.startswith("Missing Attribute Values"):
            label = label.replace("Missing Attribute Values ", "")
            if label == "?":
                missing_attribute = 1
            else:
                missing_attribute = 0
            continue
        elif label != "":
            label = re.sub(" +", " ", label)
            label = label.split(" ")

            attribute = label[0]
            for idx2 in range(1, len(label) - 1):
                attribute += " "
                attribute += label[idx2]
            type = int(label[len(label) - 1])

            # 0 means nominal/categorical/discrete
            # 1 means numerical/continuous
            # 2 means serial/TID/codeno

            # if type != 2:

            if type == 1:
                continuous_attribute[idx] = 1

            attribute_name.append((attribute, type))

    for idx in range(len(dataset)):
        tuple = dataset[idx]
        tuple = tuple.replace("\n", "")
        tuple = tuple.replace(";", ",")
        tuple = tuple.split(",")
        dataset[idx] = tuple

    for idx in range(len(dataset)):
        tuple = dataset[idx]
        # print(tuple)
        for x in range(len(tuple)):
            if x in continuous_attribute:
                if tuple[x] == '?':
                    tuple[x] = getMostCommonAttVal(deepcopy(dataset), x)

                try:
                    tuple[x] = float(tuple[x])
                except:
                    print(x, tuple)
                    exit(0)

        class_name = tuple[class_idx]
        class_matrix.append(class_name)
        tuple.pop(class_idx)
        feature_matrix.append(tuple)

    classCnt = {}
    totClass = len(class_matrix)
    for _class in class_matrix:
        if _class not in classCnt:
            classCnt[_class] = 0
        classCnt[_class] += 1

    print("\n\n\t\tDataset Name: ", datasets[choice])
    print("\t\tTotal Tuples: ", len(feature_matrix))
    print("\t\tTotal Attributes: ", len(attribute_name), "\n\n")
    print("\t\t\t\t\t\tClass Distribution")
    print("\t\t==============================================")

    class_distribution = []

    for _class in classCnt:
        class_distribution.append([_class, classCnt[_class], round(classCnt[_class] / totClass, 4)])
    class_distribution = sorted(class_distribution)

    string = tt.to_string(
        class_distribution,
        header=["Class", "Cnt", "Proportion"],
        style=tt.styles.ascii_thin_double,
        # alignment="ll",
        # padding=(1, 10),
    )
    string = string.split("\n")
    for x in string:
        print("\t\t\t", x)

    return attribute_name, feature_matrix, class_matrix


def getTuples(X, idxList):
    ret = []
    for idx in idxList:
        ret.append(X[idx])
    return ret


def getUniqueClass(class_matrix, valid_tuple):
    class_list = []
    for row in valid_tuple:
        if class_matrix[row] not in class_list:
            class_list.append(class_matrix[row])
    return class_list


attidx = 0


def comparator(tuple):
    return tuple[attidx]


class Naive_Bayes():

    def g(self, x, u, std):
        if std == 0:
            return 0
        num = math.exp((-(x - u) ** 2) / (2 * (std ** 2)))
        denom = math.sqrt(2 * math.acos(-1)) * std
        ret = num / denom
        return ret

    def predict(self, row):
        argmax, max = None, float("-inf")
        for cls in self.class_list:
            prob = 1
            for i in range(len(self.isNumeric)):
                if self.isNumeric[i] == 1:
                    u, std = self.conditional_probability[cls][self.attribute_names[i]]
                    prob *= self.g(row[i], u, std)
                elif self.isNumeric[i] == 0:
                    prob *= self.conditional_probability[cls][self.attribute_names[i]][row[i]]
            prob *= self.probability[cls]
            if prob > max:
                max = prob
                argmax = cls
        return argmax

    def learn(self, attribute_names, isNumeric, feature_matrix,
              class_matrix, class_list, value_list):

        if len(set(class_matrix)) != len(class_list):
            print("Class absent")
            exit(0)

        self.conditional_probability = dict()
        self.attribute_names = attribute_names
        self.isNumeric = isNumeric
        self.class_list = class_list
        self.probability = dict()
        for cls in class_list:
            self.probability[cls] = 0
            if cls not in self.conditional_probability:
                self.conditional_probability[cls] = dict()
            for key in value_list:
                if key not in self.conditional_probability[cls]:
                    self.conditional_probability[cls][key] = dict()
                for value in value_list[key]:
                    self.conditional_probability[cls][key][value] = 0

        for cls in class_matrix:
            self.probability[cls] += 1

        for key in self.probability:
            self.probability[key] /= len(class_matrix)

        temp = dict()
        for i in range(len(isNumeric)):
            if isNumeric[i] == 1:
                for cls in class_list:
                    if cls not in temp:
                        temp[cls] = dict()
                    temp[cls][attribute_names[i]] = []

        for i in range(len(class_matrix)):
            for j in range(len(attribute_names)):
                if isNumeric[j] == 0:
                    self.conditional_probability[class_matrix[i]][attribute_names[j]][feature_matrix[i][j]] += 1
                elif isNumeric[j] == 1:
                    temp[class_matrix[i]][attribute_names[j]].append(feature_matrix[i][j])

        for cls in self.conditional_probability:
            for attribute in self.conditional_probability[cls]:
                laplace = False
                for value in self.conditional_probability[cls][attribute]:
                    if self.conditional_probability[cls][attribute][value] == 0:
                        laplace = True
                if laplace:
                    for value in self.conditional_probability[cls][attribute]:
                        self.conditional_probability[cls][attribute][value] += 1

        for cls in self.conditional_probability:
            for attribute in self.conditional_probability[cls]:
                total = 0
                for value in self.conditional_probability[cls][attribute]:
                    total += self.conditional_probability[cls][attribute][value]

                for value in self.conditional_probability[cls][attribute]:
                    self.conditional_probability[cls][attribute][value] /= total

        for cls in temp:
            for attribute in temp[cls]:
                self.conditional_probability[cls][attribute] = (
                np.mean(temp[cls][attribute]), np.std(temp[cls][attribute]))


def getAccuracy(y_test, y_predict):
    tot = len(y_test)
    cnt = 0
    for idx in range(0, len(y_test)):
        if y_test[idx] == y_predict[idx]:
            cnt += 1
    return (cnt / tot)


def getPrecision(y_test, y_predict, important_class):
    TP = 0
    P = 0
    for idx in range(0, len(y_test)):
        if y_test[idx] == important_class:
            P += 1
            if (y_test[idx] == y_predict[idx]):
                TP += 1
    if P == 0:
        return 1
    return (TP / P)


def getRecall(y_test, y_predict, important_class):
    TP = 0
    FP = 0
    P = 0
    for idx in range(0, len(y_test)):
        if y_test[idx] == important_class:
            P += 1
            if (y_test[idx] == y_predict[idx]):
                TP += 1
        else:
            if y_predict[idx] == important_class:
                FP += 1
    if (TP + FP) == 0:
        return 1
    return (TP / (TP + FP))


def getfScore(y_test, y_predict, important_class):
    precision = getPrecision(y_test, y_predict, important_class)
    recall = getRecall(y_test, y_predict, important_class)
    if (precision + recall) > 0:
        fScore = (2 * precision * recall) / (precision + recall)
    else:
        fScore = 0
    # print(precision,recall,fScore)
    return fScore


if __name__ == '__main__':
    while True:

        attributes, feature_matrix, class_matrix = readFile()

        attribute_name = []
        attriute_types = []

        value_list = dict()

        for x in attributes:
            attribute_name.append(x[0])
            attriute_types.append(x[1])
            if x[1] == 0:
                value_list[x[0]] = []

        dt2 = Naive_Bayes()
        X = np.array(deepcopy(feature_matrix))
        y = deepcopy(class_matrix)
        important_class = getImpClass(class_matrix)

        for i in range(len(attriute_types)):
            if attriute_types[i] == 0:
                value_list[attribute_name[i]] = set(X[:, i])
        X = deepcopy(feature_matrix)

        class_list = getUniqueClass(class_matrix, list(range(0, len(X))))

        print("\n\n\t\tEnter Number of folds: ", end="")
        numFold = int(input())
        kf = StratifiedKFold(n_splits=numFold, random_state=None, shuffle=True)  # KFold(n_splits=numFold, shuffle=True)
        kf.get_n_splits(X, y)

        accuracy = 0
        precision = 0
        recall = 0
        fScore = 0

        curFold = 1
        print("\n\n\t\t\t\t\t\tNaive Bayes Classification Results")
        print("\t\t\t\t\t==========================================\n\n")

        st = time.time()
        for train_index, test_index in kf.split(X, y):
            X_train = getTuples(X, train_index)
            y_train = getTuples(y, train_index)
            X_test = getTuples(X, test_index)
            y_test = getTuples(y, test_index)

            valid_tuple = list(range(0, len(X_train)))

            print("\n\t\tFold\t#%d\n\t\tLearning Naive Bayes..." % curFold)

            dt = Naive_Bayes()
            dt.learn(deepcopy(attribute_name), deepcopy(attriute_types), X_train, y_train, class_list, value_list)

            y_predict = []

            for i in range(0, len(X_test)):
                data = X_test[i]
                actual_class = y_test[i]

                predicted_class = dt.predict(data)
                y_predict.append(predicted_class)

            foldAccuraccy = getAccuracy(y_test, y_predict) * 100
            foldPrecision = getPrecision(y_test, y_predict, important_class) * 100
            foldRecall = getRecall(y_test, y_predict, important_class) * 100
            foldfScore = getfScore(y_test, y_predict, important_class) * 100

            # draw_auc(y_test,y_predict)

            accuracy += foldAccuraccy
            precision += foldPrecision
            recall += foldRecall
            # print(foldPrecision,foldRecall,foldfScore)
            fScore += foldfScore

            print("\t\tAccuracy(%%):\t%0.2lf\tTraining:\t%d\tTest:\t%d\t" % (foldAccuraccy, len(X_train), len(X_test)))
            curFold += 1

        en = time.time()
        accuracy = accuracy / numFold
        precision = precision / numFold
        recall = recall / numFold
        fScore = fScore / numFold

        print("\n\t\tTotal Folds: ", numFold)
        print("\t\tAvg Accuracy(%%): %0.6lf" % accuracy)
        print("\t\tAvg Precision(%%): %0.6lf" % precision)
        print("\t\tAvg Recall(%%): %0.6lf" % recall)
        print("\t\tAvg F-Score(%%): %0.6lf" % fScore)
        print("\n\t\tTime Required: %0.6lfseconds" % (en - st))
