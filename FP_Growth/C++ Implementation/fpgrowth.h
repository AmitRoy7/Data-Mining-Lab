#include<bits/stdc++.h>
using namespace std;

struct node
{
    int item;
    int cnt;
    node* par;
    map<int,node*> childs;

    node* prev;///for htable;

    node()
    {
        item = 0;
        cnt = 0;
        par = prev = NULL;
        childs.clear();
    }

    void mydelete()
    {
        item = 0;
        cnt = 0;
        par = prev = NULL;
        childs.clear();
    }
};

node* createChild(node* &parent, int &item,map<int,node*> &hTable)
{
    ///update node attribute
    node* newChild = new node();
    newChild->item = item;
    newChild->cnt = 0;
    newChild->par = parent;
    newChild->childs.clear();

    ///update header table chain
    newChild->prev = hTable[item];
    hTable[item] = newChild;

    return newChild;
}


void insertTransaction(node* &cur,vector<int> &transaction,int &sup,map<int,node*> &hTable,map<int,int> &hTableSupCnt)
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

void del(node* &cur)
{
    for(auto it = cur->childs.begin();it!=cur->childs.end();it++)
        del(it->second);

    cur->mydelete();
    delete(cur);
    return;
}

//void visitTrie(node* &curr, string st)
//{
//    for(auto it:curr->childs)
//        visitTrie(it.second,st+" "+(string)it.first);
//    if(curr->childs.empty())
//        cout<<st<<endl;
//    return;
//}

void visitHTable(node* &curr)
{
    while(true)
    {
        cout<<curr->item<<" "<<curr->cnt<<endl;
        curr = curr->prev;

        if(curr==NULL)
            break;
    }
}
