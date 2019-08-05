#include<bits/stdc++.h>
using namespace std;

struct node
{
    string item;
    int cnt;
    node* par;
    map<string,node*> childs;

    node* next;///for htable;

    node()
    {
        item = "";
        cnt = 0;
        par = next = NULL;
        childs.clear();
    }
};

node* createChild(node* &parent, string &item,map<string,node*> &hTable)
{
    ///update node attribute
    node* newChild = new node();
    newChild->item = item;
    newChild->cnt = 0;
    newChild->par = parent;
    newChild->childs.clear();

    ///update header table chain
    if(hTable.find(item)==hTable.end())
        hTable[item] = newChild;
    else
    {
        node* cur = hTable[item];
        while(cur->next!=NULL)
            cur = cur->next;
        cur->next = newChild;
    }
    newChild->next = NULL;

    return newChild;
}


void insertTransaction(node* &cur,vector<string> &transaction,int &sup,map<string,node*> &hTable,map<string,int> &hTableSupCnt)
{

    for(auto item: transaction)
    {
        if(cur->childs.find(item)==cur->childs.end())
            cur->childs[item] = createChild(cur,item,hTable);
        cur = cur->childs[item];
        cur->cnt += sup;
        hTableSupCnt[item]+=sup;
    }
}

void visitTrie(node* &curr, string st)
{
    for(auto it:curr->childs)
        visitTrie(it.second,st+" "+it.first);
    if(curr->childs.empty())
        cout<<st<<endl;
    return;
}

void visitHTable(node* &curr)
{
    while(true)
    {
        cout<<curr->item<<" "<<curr->cnt<<endl;
        curr = curr->next;

        if(curr==NULL)
            break;
    }
}
