import re
from copy import deepcopy
import time

# from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import KFold
import math
import os
import termtables as tt

# from sklearn.tree import DecisionTreeClassifier




def getMostCommonAttVal(class_matrix,idx):
    cntMp={}
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




# function for reading dataset
# returns attribute,feature_matrix and class_matrix
def readFile():
    path = os.getcwd()
    path += "/"

    datasets = ["Sample Input", "Book Example","Iris", "Car", "Mushroom",
                "Breast Cancer", "Breast Cancer Wisconsin (Diagnostic)",
                "Breast Cancer Wisconsin (Original)", "Breast Cancer Wisconsin (Prognostic)",
                "Abalone", "Play Tennis","Poker Hand Testing"]

    print("\n\t\t\t\t\tDecision Tree - Classification Algorithm")
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

    # print("Has Missing Attributes: " , missing_attribute)
    # print("Class Label Idx: ", class_idx)
    # for x in attribute_name:
    #     print(x)

    # for idx in range(len(dataset)):
    #     print(dataset[idx])
    #     if idx > 100:
    #         break


    for idx in range(len(dataset)):
        tuple = dataset[idx]
        tuple = tuple.replace("\n", "")
        tuple = tuple.split(",")
        dataset[idx] = tuple


    for idx in range(len(dataset)):

        tuple = dataset[idx]

        for x in range(len(tuple)):
            if x in continuous_attribute:
                if tuple[x] == '?':
                    tuple[x] = getMostCommonAttVal(deepcopy(dataset),x)
                tuple[x] = float(tuple[x])


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



    print("\n\n\t\tDataset Name: ",datasets[choice])
    print("\t\tTotal Tuples: ",len(feature_matrix))
    print("\t\tTotal Attributes: ",len(attribute_name),"\n\n")
    print("\t\t\t\t\t\tClass Distribution")
    print("\t\t==============================================")


    class_distribution = []

    for _class in classCnt:

        class_distribution.append([_class,classCnt[_class],round(classCnt[_class]/totClass,4)])

    class_distribution = sorted(class_distribution)

    string = tt.to_string(
        class_distribution,
        header=["Class", "Cnt","Proportion"],
        style=tt.styles.ascii_thin_double,
        # alignment="ll",
        # padding=(1, 10),
    )
    string = string.split("\n")
    for x in string:
        print("\t\t\t",x)

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


class decision_tree():

    def __init__(self):
        self.node_class = ""  # leaf node
        self.splitting_attribute = ""  # splitting_attribute
        self.isNumeric = False  # if splitting attribute numeric or not
        self.splitpoint = 0  # required if splitting attribute is numeric
        self.child_list = {}  # one child for each value of attribute
        self.parent = ""  # parent node

    def predict(self, row):
        if self.node_class != "":
            return self.node_class
        else:
            attribute_value = row[self.splitting_attribute]

            if self.isNumeric:
                if attribute_value <= self.splitpoint:
                    next_node = self.child_list[0]
                else:
                    next_node = self.child_list[1]
                return next_node.predict(row)

            if attribute_value in self.child_list:
                next_node = self.child_list[attribute_value]
                return next_node.predict(row)
            else:
                # print("ERROR!! -> Attribute value is not in test data!!!")
                return "Prediction is not possible!!!"

    def learn(self, attribute_names, isNumeric, attribute_list,
              feature_matrix, class_matrix, valid_tuple
              , attribute_type, attribute_cnt, class_cnt,min_sup):

        class_list = getUniqueClass(class_matrix, valid_tuple)

        #pruning condition
        if len(valid_tuple) < min_sup:
            self.node_class = self.maxVoting(class_matrix,valid_tuple)
            return

        # # no tuples left -> perform max voting in parent
        # if len(valid_tuple) == 0:
        #     self.node_class = self.maxVoting(self.parent.class_matrix,self.parent.valid_tuple)
        #     return

        # no attribute left -> perform max voting in valid tuples
        # if only attribute is serial no/id -> max voting is performed
        if len(attribute_list) == 0 or (len(attribute_list) == 1 and isNumeric[attribute_list[0]] == 2):
            self.node_class = self.maxVoting(class_matrix, valid_tuple)
            return

        # all tuples have same class
        elif len(class_list) == 1:
            self.node_class = class_list[0]
            return


        else:

            splitting_attribute, idx, branches = self.attribute_selection_method(
                attribute_names, isNumeric, attribute_list,
                feature_matrix, class_matrix, class_list, valid_tuple,
                deepcopy(attribute_type), deepcopy(attribute_cnt), deepcopy(class_cnt))

            attribute_list.remove(idx)
            self.splitting_attribute = splitting_attribute

            # special case when the best splitting attribute is continuous

            if isNumeric[idx] == 1:

                self.isNumeric = True
                for x in branches:

                    new_valid_tuple0 = branches[x][0]
                    new_valid_tuple1 = branches[x][1]

                    self.splitpoint = x  # useful for prediction

                    branch_label = splitting_attribute + "<=" + str(x)
                    # 0 less or equal

                    self.child_list[0] = decision_tree()
                    self.child_list[0].parent = self

                    if len(new_valid_tuple0) == 0:
                        self.child_list[0].node_class = self.maxVoting(class_matrix, valid_tuple)

                    else:
                        self.child_list[0].learn(attribute_names, isNumeric, deepcopy(attribute_list),
                                                 feature_matrix, class_matrix, new_valid_tuple0,
                                                 deepcopy(attribute_type), deepcopy(attribute_cnt), deepcopy(class_cnt),min_sup)

                    branch_label = splitting_attribute + ">" + str(x)

                    # 1 greater than
                    self.child_list[1] = decision_tree()
                    self.child_list[1].parent = self

                    if len(new_valid_tuple1) == 0:
                        self.child_list[1].node_class = self.maxVoting(class_matrix, valid_tuple)

                    else:
                        self.child_list[1].learn(attribute_names, isNumeric, deepcopy(attribute_list),
                                                 feature_matrix, class_matrix, new_valid_tuple1,
                                                 deepcopy(attribute_type), deepcopy(attribute_cnt), deepcopy(class_cnt),min_sup)

                    return

            # normal case when attribute is categorical/nominal

            for branch_type in branches:
                new_valid_tuple = branches[branch_type]
                self.isNumeric = False

                self.child_list[branch_type] = decision_tree()
                self.child_list[branch_type].parent = self

                if len(new_valid_tuple) == 0:
                    self.child_list[branch_type].node_class = self.maxVoting(class_matrix, valid_tuple)
                    continue

                self.child_list[branch_type].learn(
                    attribute_names, isNumeric, deepcopy(attribute_list),
                    feature_matrix, class_matrix, new_valid_tuple,
                    deepcopy(attribute_type), deepcopy(attribute_cnt), deepcopy(class_cnt),min_sup)
            return

    # finds the best attribute for splitting
    # gain is used as the measure
    # id/serial no type attribute is avoided
    # continuous attribute are splitted in midpoints after sorting
    def attribute_selection_method(self, attribute_names, attribute_types, attribute_list
                                   , feature_matrix, class_matrix, class_list, valid_tuple
                                   , attribute_type, attribute_cnt, class_cnt):

        # attribute_cnt_update
        for i in range(0, len(attribute_list)):
            colNum = attribute_list[i]
            attribute = attribute_names[colNum]

            if attribute_types[colNum] > 0:  # 1-> numerical 2->serial number
                continue

            for j in range(0, len(valid_tuple)):
                rowNum = valid_tuple[j]
                attribute_feature = feature_matrix[rowNum][colNum]
                class_type = class_matrix[rowNum]

                attribute_cnt[attribute][attribute_feature][class_type] += 1
                attribute_type[attribute][attribute_feature] += 1

        # class_cnt update
        for row in valid_tuple:
            class_cnt[class_matrix[row]] += 1

        # database info calculation
        infoD = 0
        total_tuple = len(valid_tuple)

        for class_type in class_list:
            prob = class_cnt[class_type] / total_tuple
            if prob > 0:
                prob = - prob * math.log(prob, 2.0)
                infoD += prob

        # gain calculation
        gain = {}

        # for categorical attribute
        for x in attribute_list:

            type = attribute_types[x]
            if type == 1 or type == 2:
                continue

            attribute = attribute_names[x]
            tot = 0
            for feature in attribute_type[attribute]:
                if attribute_type[attribute][feature] == 0:
                    continue
                temp = 0
                for class_type in class_list:

                    prob = attribute_cnt[attribute][feature][class_type] / attribute_type[attribute][feature]
                    # print(attribute,feature,class_type,attribute_cnt[attribute][feature][class_type],attribute_type[attribute][feature],prob)
                    if prob > 0:
                        prob = - prob * math.log(prob, 2)
                        temp += prob

                # print(attribute, feature, attribute_type[attribute][feature], temp)
                temp *= (attribute_type[attribute][feature] / total_tuple)
                # print(attribute,feature,attribute_type[attribute][feature],temp)
                tot += temp
            attgain = infoD - tot
            # print(attribute,infoD,tot,attgain)
            gain[attribute] = attgain

        # appending class column for sorting
        temp_new_feature_matrix = deepcopy(feature_matrix)
        new_feature_matrix = []

        for row in valid_tuple:
            new_row = temp_new_feature_matrix[row]
            new_row.append(class_matrix[row])
            new_feature_matrix.append(new_row)



        # for numerical/continuous attribute:
        attribute_split_point = {}
        for attribute_id in attribute_list:
            attribute = attribute_names[attribute_id]

            # checking numerical/continuous or not
            if attribute_types[attribute_id] == 1:

                gain[attribute] = 0
                attribute_split_point[attribute] = 0


                # sorting based on that attribute id
                global attidx
                attidx = attribute_id
                new_feature_matrix = sorted(new_feature_matrix, key=comparator)

                # for n tuples try to split n-1 times and then
                # calculate infogain for each split
                for split_point in range(1, len(new_feature_matrix)):
                    first_half = new_feature_matrix[0:split_point]
                    second_half = new_feature_matrix[split_point:len(new_feature_matrix)]

                    mul1 = len(first_half) / len(new_feature_matrix)
                    mul2 = len(second_half) / len(new_feature_matrix)

                    cnt_mp1 = {}
                    cnt_mp2 = {}
                    class_idx = len(feature_matrix[0])



                    for x in first_half:
                        if x[class_idx] not in cnt_mp1:
                            cnt_mp1[x[class_idx]] = 0
                        cnt_mp1[x[class_idx]] += 1

                    for x in second_half:
                        if x[class_idx] not in cnt_mp2:
                            cnt_mp2[x[class_idx]] = 0
                        cnt_mp2[x[class_idx]] += 1

                    tot1 = 0

                    for x in cnt_mp1:
                        prob = cnt_mp1[x] / len(first_half)
                        prob = - prob * math.log(prob, 2.0)
                        tot1 += prob

                    tot2 = 0
                    for x in cnt_mp2:
                        prob = cnt_mp2[x] / len(second_half)
                        prob = - prob * math.log(prob, 2.0)
                        tot2 += prob

                    info = tot1 * mul1 + tot2 * mul2
                    attgain = infoD - info
                    if attgain > gain[attribute]:
                        gain[attribute] = attgain
                        attribute_split_point[attribute] = split_point



        bestAttributeIdx = attribute_list[0]
        for x in attribute_list:
            if attriute_types[x] != 2:
                bestAttributeIdx = x
                break


        bestAttribute = attribute_names[bestAttributeIdx]
        mx = 0

        for idx in attribute_list:

            type = attribute_types[idx]

            if type == 2:
                continue


            attribute = attribute_names[idx]
            attgain = gain[attribute]

            if attgain > mx:
                mx = attgain
                bestAttributeIdx = idx
                bestAttribute = attribute

        bestAttributeBranches = {}




        if attribute_types[bestAttributeIdx] == 0:

            for type in attribute_type[bestAttribute]:
                bestAttributeBranches[type] = []

            for row in valid_tuple:
                type = feature_matrix[row][bestAttributeIdx]
                bestAttributeBranches[type].append(row)

        else :

            split_point = attribute_split_point[bestAttribute]
            # appending class column for sorting
            temp_new_feature_matrix = deepcopy(feature_matrix)
            new_feature_matrix = []

            for row in valid_tuple:
                new_feature_matrix.append(temp_new_feature_matrix[row])

            for i in range(len(new_feature_matrix)):
                new_feature_matrix[i].append(class_matrix[i])

            attidx = bestAttributeIdx
            new_feature_matrix = sorted(new_feature_matrix, key=comparator)

            ai0 = new_feature_matrix[split_point - 1][bestAttributeIdx]
            ai1 = new_feature_matrix[split_point][bestAttributeIdx]


            try:
                mid = (ai0 + ai1)/ 2.0
                # print(mid)
            except:
                print("Number format exception: ",ai0,ai1,ai0+ai1)
                exit(0)

            first_half = []
            second_half = []

            for idx in valid_tuple:
                tuple = feature_matrix[idx]
                if tuple[bestAttributeIdx] <= mid:
                    first_half.append(idx)
                else:
                    second_half.append(idx)

            bestAttributeBranches[mid] = {}

            bestAttributeBranches[mid][0] = first_half  # less or equal
            bestAttributeBranches[mid][1] = second_half  # greater or equal

        # print("best attribute",bestAttributeIdx,bestAttribute,gain[bestAttribute])

        return bestAttribute, bestAttributeIdx, bestAttributeBranches

    def maxVoting(self, class_matrix, valid_tuple):
        class_cnt = {}
        for row in valid_tuple:
            class_type = class_matrix[row]
            if class_type not in class_cnt:
                class_cnt[class_type] = 0
            class_cnt[class_type] += 1

        maxClass = class_matrix[valid_tuple[0]]
        maxClassCnt = class_cnt[maxClass]

        for class_type in class_cnt:
            if class_cnt[class_type] > maxClassCnt:
                maxClass = class_type
                maxClassCnt = class_cnt[class_type]

        return maxClass

    def printDecisionTree(self, root, st):
        if root.node_class != "":
            print(st + "\tPredicted Class : " + root.node_class)
            return

        print(st + "Splitting Attribute: -> " + root.splitting_attribute)
        for attribute in root.child_list.keys():
            if root.isNumeric:
                if attribute == 0:
                    print(st + " <= " + str(root.splitpoint))
                elif attribute == 1:
                    print(st + " > " + str(root.splitpoint))
            else:
                print(st + str(attribute))
            self.printDecisionTree(root.child_list[attribute], st + "\t")


def getAccuracy(y_test,y_predict):
    tot = len(y_test)
    cnt = 0
    for idx in range(0,len(y_test)):
        if y_test[idx] == y_predict[idx]:
           cnt += 1
    return (cnt/tot)

def getPrecision(y_test, y_predict,important_class):
    TP = 0
    P = 0
    for idx in range(0,len(y_test)):
        if y_test[idx] == important_class:
            P+=1
            if(y_test[idx]==y_predict[idx]):
                TP+=1
    return (TP/P)

def getRecall(y_test, y_predict,important_class):
    TP = 0
    FP = 0
    P = 0
    for idx in range(0,len(y_test)):
        if y_test[idx] == important_class:
            P+=1
            if(y_test[idx]==y_predict[idx]):
                TP+=1
        else:
            if y_predict[idx] == important_class:
                FP += 1
    return (TP/(TP+FP))

def getfScore(y_test,y_predict,important_class):
    precision = getPrecision(y_test,y_predict,important_class)
    recall = getRecall(y_test,y_predict,important_class)
    fScore = (2*precision*recall)/(precision+recall)
    # print(precision,recall,fScore)
    return fScore



if __name__ == '__main__':

    while True:

        attributes, feature_matrix, class_matrix = readFile()

        attribute_name = []
        attriute_types = []

        # print(feature_matrix)

        for x in attributes:
            attribute_name.append(x[0])
            attriute_types.append(x[1])

        attribute_list = list(range(0, len(attributes)))

        dt2 = decision_tree()
        X = deepcopy(feature_matrix)
        y = deepcopy(class_matrix)
        important_class = getImpClass(class_matrix)


        valid_tuple = list(range(0, len(X)))

        attribute_cnt = {}
        attribute_type = {}
        class_cnt = {}

        class_list = getUniqueClass(class_matrix, valid_tuple)

        for i in range(0, len(attribute_list)):
            colNum = attribute_list[i]

            if attriute_types[colNum] > 1:
                continue

            attribute = attribute_name[colNum]
            attribute_cnt[attribute] = {}
            attribute_type[attribute] = {}
            for j in range(0, len(valid_tuple)):
                rowNum = valid_tuple[j]
                feature = feature_matrix[rowNum][colNum]
                # print(attribute,colNum,feature_matrix[rowNum])
                attribute_cnt[attribute][feature] = {}
                attribute_type[attribute][feature] = 0

                for class_type in class_list:
                    attribute_cnt[attribute][feature][class_type] = 0

        for class_type in class_matrix:
            class_cnt[class_type] = 0



        # testTuple = {"age": 35, "income": "medium", "married": "yes", "credit_rating": "fair"}
        #
        # print("\n\n\t\tTest Tuple: ", testTuple)
        #
        # print("\n\n\t\tPredicted Class: ", dt.predict(testTuple))

        # perform cross validation and accuracy,recall,precision,f1-score

        print("\n\n\t\tEnter Number of folds: ",end="")
        numFold = int(input())
        print("\n\n\t\tEnter Pruning Threshold(%): ",end="")
        pruneThresh = float(input())
        pruneThresh /= 100
        min_sup = pruneThresh * len(X)

        # dt2.learn(deepcopy(attribute_name), deepcopy(attriute_types), deepcopy(attribute_list), X, y,
        #          valid_tuple, deepcopy(attribute_type), deepcopy(attribute_cnt), deepcopy(class_cnt), min_sup)
        # dt2.printDecisionTree(dt2, "")

        kf = KFold(n_splits=numFold,shuffle=True)
        kf.get_n_splits(X)


        accuracy = 0
        precision = 0
        recall = 0
        fScore = 0

        curFold = 1
        print("\n\n\t\t\t\t\t\tDecision Tree Classification Results")
        print("\t\t\t\t\t==========================================\n\n")


        # skLearnDecisionTree = DecisionTreeClassifier(criterion='entropy')


        st = time.time()
        for train_index, test_index in kf.split(X):


            # print("TRAIN:", train_index, "TEST:", test_index)
            X_train = getTuples(X, train_index)
            y_train = getTuples(y, train_index)
            X_test = getTuples(X, test_index)
            y_test = getTuples(y, test_index)

            valid_tuple = list(range(0, len(X_train)))

            print("\n\t\tFold\t#%d\n\t\tLearning Decision Tree..."%curFold)

            min_sup = pruneThresh * len(X_train)

            dt = decision_tree()
            dt.learn(deepcopy(attribute_name), deepcopy(attriute_types), deepcopy(attribute_list), X_train, y_train, valid_tuple
                     , deepcopy(attribute_type), deepcopy(attribute_cnt), deepcopy(class_cnt),min_sup)





            # skLearnDecisionTree.fit(X_train,y_train)
            # sky_predict = skLearnDecisionTree.predict(X_test)
            #
            # sk_accuracy = accuracy_score(y_test,sky_predict)*100


            y_predict = []

            for i in range(0, len(X_test)):
                data = X_test[i]
                actual_class = y_test[i]

                curTuple = {}
                for i in range(0, len(attribute_name)):
                    if attriute_types[i] == 2:              #serial number type attribute
                        continue
                    curTuple[attribute_name[i]] = data[i]
                predicted_class = dt.predict(curTuple)
                y_predict.append(predicted_class)

            foldAccuraccy = getAccuracy(y_test, y_predict)*100
            foldPrecision = getPrecision(y_test,y_predict,important_class)*100
            foldRecall = getRecall(y_test,y_predict,important_class)*100
            foldfScore = getfScore(y_test,y_predict,important_class)*100

            accuracy += foldAccuraccy
            precision += foldPrecision
            recall += foldRecall
            # print(foldPrecision,foldRecall,foldfScore)
            fScore += foldPrecision


            print("\t\tAccuracy(%%):\t%0.2lf\tPrecision(%%):\t%0.2lf\tRecall(%%):\t%0.2lf\tfScore(%%):\t%0.2lf\tTraining:\t%d\tTest:\t%d\t"%(foldAccuraccy,foldPrecision,foldRecall,foldfScore,len(X_train),len(X_test)))
            # print("\t\tSKlearn Accuracy: %0.2lf"%sk_accuracy)
            # print("\t\tFold #%d\t"%curFold," Accuracy(%%): %0.2lf\t"%(foldAccuraccy)," Training Set: %d\t"%len(X_train),"Test Set: %d\t",len(X_test))
            curFold += 1

        en = time.time()
        accuracy = accuracy/numFold
        precision = precision/numFold
        recall = recall/numFold
        fScore = fScore/numFold

        print("\n\t\tTotal Folds: ",numFold)
        print("\t\tAvg Accuracy(%%): %0.6lf"%accuracy)
        print("\t\tAvg Precision(%%): %0.6lf" % precision)
        print("\t\tAvg Recall(%%): %0.6lf" % recall)
        print("\t\tAvg F-Score(%%): %0.6lf" % fScore)
        print("\n\t\tTime Required: %0.6lfseconds"%(en-st))