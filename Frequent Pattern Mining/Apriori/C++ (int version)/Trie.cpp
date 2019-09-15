#include<bits/stdc++.h>
using namespace std;

#include"accessories.h"

map<string,int> freq;

struct node {
    bool endmark;
    map<string, int> mp;
    vector<node*> v;
    int idx,freq;

    node()
    {
        endmark = false;
        idx=0;
        freq = 0;
        mp.clear();
        v.clear();

    }

    init()
    {
        endmark = false;
        idx=0;
        freq = 0;
        mp.clear();
        v.clear();
    }
} * root;

void insertTrie(vector<string> st)
{
    node *curr = root;

    for(auto it: st)
    {

        string id = it;
        int exists = curr->mp[id];

        if(!exists)
            {

                curr->idx++;
                curr->mp[id] = curr->idx;
                curr->v.push_back(new node());
            }

        curr = curr->v[curr->mp[id]-1];
    }

    curr->endmark = true;
}
//

bool exists(vector<string> v, string it)
{
    int lo = 0;
    int hi = v.size()-1;
    int mid;

    while(hi>=lo)
    {
        mid = (hi+lo)>>1;
        if(v[mid]==it)
            return true;
        else if(v[mid]<it)
            lo = mid+1;
        else
            hi = mid - 1;
    }
    return false;

}

void updateFrequency(set<string> transaction,node* curr,string st)
{

    if(curr->endmark)
        {
            freq[st] = curr->freq;
            return;
        }

    for(map<string,int>::iterator it = curr->mp.begin();it!=curr->mp.end();it++)
    {
        string item = it->first;
        node* new_node = curr->v[it->second -1];

        if(!exists(transaction,item))   continue;
//        if(transaction.find(item)==transaction.end())   continue;


        new_node->freq += 1;


        if(st!="")
            updateFrequency(transaction,new_node,st + " "+ item);
        else
            updateFrequency(transaction,new_node,st + item);
    }


    return;
}
void del(node* cur)
{
    for(map<string,int>::iterator it = cur->mp.begin();it!=cur->mp.end();it++)
        del(cur->v[it->second -1]);

    delete (cur);
}

int main()
{

    string filename = "input2.txt";

    vector< set<string> >candidate;

    ifstream fin;
    string temp;
    vector<string>v;

    fin.open(filename);
    while(!fin.eof())
    {
        getline(fin,temp);

        if(temp=="")    continue;
        v = strToVec(temp);

        //cout<<temp<<" ";
        //vectorPrint(v);

        set<string> itemSet;                                    ///saving transactions
        for(int i=0; i<v.size(); i++) itemSet.insert(v[i]);
        candidate.push_back(itemSet);
    }
    fin.close();

    root = new node();
    for(int i=0;i<candidate.size();i++)
        insertTrie(candidate[i]);

    set<string> transactions;
    transactions.insert("a");
    transactions.insert("b");
    transactions.insert("c");
    transactions.insert("d");
    transactions.insert("e");
    transactions.insert("f");
    transactions.insert("g");
    transactions.insert("h");

    node* cur = root;
    updateFrequency(transactions,cur,"");

//    for(map<string,int>::iterator it = freq.begin(); it!=freq.end();it++)
//        cout<<it->first<<" "<<it->second<<endl;

    del(root);

    return 0;
}
