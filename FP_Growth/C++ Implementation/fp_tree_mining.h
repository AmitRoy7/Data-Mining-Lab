#include<bits/stdc++.h>
using namespace std;

bool containsSinglePath(node* &curr){
    while(true)
    {
        int child_count  = curr->childs.size();
        if(child_count>1)   return false;
        else if(child_count==0) return true;
        curr = curr->childs.begin()->second;
    }
}


vector<string> get_items_upto_root(node* &curr)
{
    vector<string> projected_transaction;
    while(curr->par!=NULL)
        {
            projected_transaction.push_back(curr->item);
            curr = curr->par;
        }
    sort(projected_transaction.begin(),projected_transaction.end(),transactionOrder);
    return projected_transaction;
}


void recursive_FPTree(
vector<vector<string>> &transactions,
vector<int> &transactionSupCnt,
vector<string> &patternSoFar,
int &supSoFar){


    node* root = new node();
    node* curr = root;

    map<string,node*> hTable;
    map<string,int> hTableSupCnt;

    for(int i=0;i<transactions.size();i++)
        {
            curr = root;
            insertTransaction(curr,transactions[i],transactionSupCnt[i],hTable,hTableSupCnt);
        }


    curr = root;
    if(containsSinglePath(curr))
    {

        vector<string> singlePath;
        vector<int> singlePathSupCnt;

        ///single path item collection
        curr = root;
        while(true)
        {

            if(curr->childs.size()==0)
                break;
            curr = curr->childs.begin()->second;

            if(curr->cnt>=minFreq)
            {
                singlePath.push_back(curr->item);
                singlePathSupCnt.push_back(curr->cnt);
            }


        }
        ///combination

        int bits = singlePath.size();
        int tot = 1ll<< bits;
        vector<string> maskVector;


        for(int i=1;i<tot;i++)
        {
            maskVector = patternSoFar;
            int mask = i;
            int sup = 100000000;


            for(int j=0;j<bits;j++)
            {
                if(checkBit(mask,j))
                {
                    maskVector.push_back(singlePath[j]);
                    sup = min(sup,singlePathSupCnt[j]);
                }
            }

//            if(maskVector.size()==1)    continue;
//            if(sup==100000000)  continue;

            sort(maskVector.begin(),maskVector.end(),transactionOrder);
            if(PRINT_FLAG)
            {
                cout<<"P a T t E r N: ";
                vectorPrintSp(maskVector);
                printf(": %d\n",sup);
            }

            frequentPatternsCnt[maskVector.size()]+=1;
            sort(maskVector.begin(),maskVector.end());
            frequentPatterns[maskVector.size()].push_back(maskVector);

        }

        return;
    }

//    visitTrie(curr,"");
//    return;

//    for(auto it:candidates){
//        if(hTable.find(it)!=hTable.end())
//        {
//            cout<<it<<endl;
//            visitHTable(hTable[it]);
//        }
//    }




    for(int i=candidates.size()-1;i>=0;i--)
    {


        string item = candidates[i];
        int supCount = hTableSupCnt[item];

        if(hTable.find(item)==hTable.end() || supCount<minFreq)    continue;


        node* nextNode = hTable[item];


        vector<vector<string>> new_transactions;
        vector<int> new_transactionSupCnt;
        node* curNode = nextNode;

        while(true)
        {
            node* par = curNode->par;
            vector<string> projectedTransaction = get_items_upto_root(par);
            if(projectedTransaction.size()>0)
            {
                new_transactions.push_back(projectedTransaction);
                new_transactionSupCnt.push_back(curNode->cnt);
            }

            if(curNode->next==NULL)break;
            curNode = curNode->next;
        }

        patternSoFar.push_back(item);


        if(PRINT_FLAG)
        {
            printf("\n\nFP-tree For: ");
            vectorPrintSp(patternSoFar);
            puts("");
            for(int i=0;i<new_transactions.size();i++)
            {
                vectorPrintSp(new_transactions[i]);
                cout<<" : "<<new_transactionSupCnt[i]<<endl;
            }
        }


        frequentPatternsCnt[patternSoFar.size()]+=1;
        frequentPatterns[patternSoFar.size()].push_back(patternSoFar);
        if(PRINT_FLAG)
            {
                cout<<"P a T t E r N: ";
                vectorPrintSp(patternSoFar);
                printf(": %d\n",supCount);
            }


        recursive_FPTree(new_transactions,new_transactionSupCnt,patternSoFar,supCount);
        patternSoFar.pop_back();
    }
}


