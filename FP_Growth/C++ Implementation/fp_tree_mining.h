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


vector<int> get_items_upto_root(node* &curr)
{
    vector<int> projected_transaction;
    while(curr->par!=NULL)
        {
            projected_transaction.push_back(curr->item);
            curr = curr->par;
        }
    sort(projected_transaction.begin(),projected_transaction.end(),transactionOrder);
    return projected_transaction;
}


void recursive_FPTree(
vector<vector<int>> &transactions,
vector<int> &transactionSupCnt,
vector<int> &patternSoFar,
int &supSoFar){


    node* root = new node();
    node* curr = root;

    map<int,node*> hTable;
    map<int,int> hTableSupCnt;

    int one = 1;
    for(int i=0;i<transactions.size();i++)
        {
            curr = root;
            insertTransaction(curr,transactions[i],transactionSupCnt[i],hTable,hTableSupCnt);

        }


    curr = root;
    if(containsSinglePath(curr))
    {

        vector<int> singlePath;
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
        vector<int> maskVector;


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
//            frequentPatterns[maskVector.size()].push_back(maskVector);

        }
        return;
    }






    for(auto it: hTable)
    {
        int item = it.first;
        int supCount = hTableSupCnt[item];

        if(supCount<minFreq)    continue;


        node* nextNode = hTable[item];


        vector<vector<int>> new_transactions;
        vector<int> new_transactionSupCnt;
        node* curNode = nextNode;

        while(true)
        {
            node* par = curNode->par;
            vector<int> projectedTransaction = get_items_upto_root(par);
            if(projectedTransaction.size()>0)
            {
                new_transactions.push_back(projectedTransaction);
                new_transactionSupCnt.push_back(curNode->cnt);
            }

            if(curNode->prev==NULL)break;
            curNode = curNode->prev;
        }

        patternSoFar.push_back(item);
        frequentPatternsCnt[patternSoFar.size()]+=1;
//        frequentPatterns[patternSoFar.size()].push_back(patternSoFar);


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



        if(PRINT_FLAG)
            {
                cout<<"P a T t E r N: ";
                vectorPrintSp(patternSoFar);
                printf(": %d\n",supCount);
            }


        recursive_FPTree(new_transactions,new_transactionSupCnt,patternSoFar,supCount);
        patternSoFar.pop_back();
    }
    return;

}


