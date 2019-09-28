from copy import deepcopy
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
import math


def readFile(filename):
    f = open(filename,"r")
    lines = f.readlines()

    attribute_name = lines[0]
    attribute_name = attribute_name.replace("\n","")
    attribute_name = attribute_name.split(",")
    attribute_name = attribute_name[0:len(attribute_name)-1]
    feature_matrix = []
    class_matrix = []

    for i in range(1,len(lines)):
        x = str(lines[i])
        x = x.replace("\n","")
        x = x.split(",")
        # print(x[0: len(x)-1])
        feature_matrix.append(x[0:len(x)-1])
        class_matrix.append(x[len(x)-1])

    return  attribute_name,feature_matrix,class_matrix

def getTuples(X,idxList):
    ret = []
    for idx in idxList:
        ret.append(X[idx])
    return ret


class decision_tree():

    def __init__(self):
        self.node_class = ""        #leaf node
        self.splitting_attribute = ""    #splitting_attribute
        self.child_list = {}        #one child for each value of attribute
        self.parent = ""   #parent node

    def predict(self,row):
        if self.node_class != "":
            return self.node_class
        else:
            attribute_value = row[self.splitting_attribute]
            if attribute_value in self.child_list:
                next_node = self.child_list[attribute_value]
                return next_node.predict(row)
            else:
                # print("ERROR!! -> Attribute value is not in test data!!!")
                return "Prediction is not possible!!!"

    def learn(self,attribute_names,attribute_list,feature_matrix,class_matrix,valid_tuple):
        class_list = self.getUniqueClass(class_matrix,valid_tuple)

        # print(class_list)

        if len(valid_tuple) == 0:               #no tuples left -> perform max voting in parent
            self.node_class = self.maxVoting(self.parent.class_matrix,self.parent.valid_tuple)
            return

        elif len(attribute_list) == 0:          # no attribute left -> perform max voting in valid tuples
            self.node_class = self.maxVoting(class_matrix, valid_tuple)
            return

        elif len(class_list) == 1:
            self.node_class = class_list[0]     #all tuples have same class
            return


        else:
            splitting_attribute,idx,branches = self.attribute_selection_method(attribute_names,attribute_list,feature_matrix,class_matrix,class_list,valid_tuple)
            # print(splitting_attribute,branches)
            # attribute_names.remove(splitting_attribute)
            attribute_list.remove(idx)

            self.splitting_attribute = splitting_attribute

            # print(attribute_list)

            for attribute_type in branches:
                new_valid_tuple = branches[attribute_type]


                # print(splitting_attribute,attribute_type)

                self.child_list[attribute_type] = decision_tree()
                self.child_list[attribute_type].parent = self
                self.child_list[attribute_type].learn(attribute_names,attribute_list,feature_matrix,class_matrix,new_valid_tuple)



            return

    def getUniqueClass(self,class_matrix,valid_tuple):
        class_list = []
        for row in valid_tuple:
            if class_matrix[row] not in class_list:
                class_list.append(class_matrix[row])
        return class_list

    def attribute_selection_method(self,attribute_names,attribute_list,feature_matrix,class_matrix,class_list,valid_tuple):

        attribute_cnt = {}
        attribute_type = {}
        class_cnt = {}

        #map initialization
        for i in range(0,len(attribute_list)):
            colNum = attribute_list[i]
            attribute = attribute_names[colNum]
            attribute_cnt[attribute] = {}
            attribute_type[attribute] = {}
            for j in range(0,len(valid_tuple)):
                rowNum = valid_tuple[j]
                feature = feature_matrix[rowNum][colNum]
                attribute_cnt[attribute][feature] = {}
                attribute_type[attribute][feature] = 0

                for class_type in class_list:
                    attribute_cnt[attribute][feature][class_type] = 0

        for class_type in class_matrix:
            class_cnt[class_type] = 0


        #attribute_cnt_update
        for i in range(0, len(attribute_list)):
            colNum = attribute_list[i]
            attribute = attribute_names[colNum]
            for j in range(0, len(valid_tuple)):
                rowNum = valid_tuple[j]
                attribute_feature = feature_matrix[rowNum][colNum]
                class_type = class_matrix[rowNum]

                attribute_cnt[attribute][attribute_feature][class_type] += 1
                attribute_type[attribute][attribute_feature] += 1

        #class_cnt update
        for class_type in class_matrix:
            class_cnt[class_type] += 1

        # database info calculation
        infoD = 0
        total_tuple = len(valid_tuple)

        for class_type in class_list:
            prob = class_cnt[class_type] / total_tuple
            if prob > 0:
                prob = - prob * math.log(prob,2.0)
                infoD += prob

        # print(infoD)

        infoA = {}

        for x in attribute_list:
            attribute = attribute_names[x]
            tot = 0
            for feature in attribute_type[attribute]:
                temp = 0
                for class_type in class_list:


                    prob = attribute_cnt[attribute][feature][class_type] / attribute_type[attribute][feature]
                    # print(attribute,feature,class_type,attribute_cnt[attribute][feature][class_type],attribute_type[attribute][feature],prob)
                    if prob >0:
                        prob = - prob * math.log(prob, 2)
                        temp += prob

                # print(attribute, feature, attribute_type[attribute][feature], temp)
                temp *= (attribute_type[attribute][feature]/total_tuple)
                # print(attribute,feature,attribute_type[attribute][feature],temp)
                tot += temp
            gain = infoD - tot
            # print(attribute,infoD,tot,gain)
            infoA[attribute] = gain

        # print(infoA)
        bestAttributeIdx = attribute_list[0]
        bestAttribute = attribute_names[bestAttributeIdx]
        mx = infoA[bestAttribute]



        for idx in attribute_list:
            attribute = attribute_names[idx]
            gain = infoA[attribute]
            # print(attribute,"mx: ",mx,"gain: ",gain)
            if gain >= mx:
                mx = gain
                bestAttributeIdx = idx
                bestAttribute = attribute

        # print(bestAttribute)

        bestAttributeBranches = {}
        for type in attribute_type[bestAttribute]:
            bestAttributeBranches[type] = []

        for row in valid_tuple:
            type = feature_matrix[row][bestAttributeIdx]
            bestAttributeBranches[type].append(row)


        return bestAttribute,bestAttributeIdx,bestAttributeBranches

    def maxVoting(self,class_matrix,valid_tuple):
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

    def printDecisionTree(self,root,st):
        if root.node_class != "":
            print(st+"\tPredicted Class : " + root.node_class)
            return

        print(st+"Splitting Attribute: -> " + root.splitting_attribute)
        for attribute in root.child_list.keys():
            print(st+attribute)
            self.printDecisionTree(root.child_list[attribute],st+"\t")


if __name__ == '__main__':

    while True:

        print("\n\t\t\tDecision Tree - Classification Algorithm")
        print("\t\t=============================================================")

        datasets = ["input.txt","car.data"]

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


        attribute_names,feature_matrix,class_matrix = readFile(datasets[choice])
        attribute_list = list(range(0,len(attribute_names)))

        dt = decision_tree()


        X = deepcopy(feature_matrix)
        y = deepcopy(class_matrix)

        numFold = 10

        kf = KFold(n_splits=numFold,random_state=true)
        kf.get_n_splits(X)

        accuracy = 0


        for train_index, test_index in kf.split(X):
            # print("TRAIN:", train_index, "TEST:", test_index)
            X_train = getTuples(X,train_index)
            y_train = getTuples(y,train_index)
            X_test = getTuples(X,test_index)
            y_test = getTuples(y, test_index)

            valid_tuple = list(range(0,len(X_train)))
            dt.learn(deepcopy(attribute_names),deepcopy(attribute_list),X_train,y_train,valid_tuple)

            y_predict = []

            for i in range(0,len(X_test)):
                data = X_test[i]
                actual_class = y_test[i]

                curTuple = {}
                for i in range(0,len(attribute_names)):
                    curTuple[attribute_names[i]] = data[i]
                predicted_class = dt.predict(curTuple)
                y_predict.append(predicted_class)

            accuracy += accuracy_score(y_test,y_predict)

        print("\n\t\tAccuracy: ", accuracy/numFold)