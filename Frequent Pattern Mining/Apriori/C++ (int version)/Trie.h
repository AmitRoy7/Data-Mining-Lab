#include<unordered_map>
using namespace std;


struct node {

    bool endmark;
    map<int, node*> mp;
    int cnt;


    node()
    {
        endmark = false;
        cnt = 0;
        mp.clear();
    }

    void mydelete()
    {
        mp.clear();
    }

} *root;

void insertTrie(vector<int> &st)
{
    node* curr = root;

    for(auto id: st)
    {
        if(curr->mp.find(id)==curr->mp.end())
            curr->mp[id] = new node();

        curr = curr->mp[id];
    }

    curr->endmark = true;
}
//

void updateFrequency(int i,node* &curr)
{

    if(curr->endmark)   return;


    for(auto it = curr->mp.begin();it!=curr->mp.end();it++)
    {
        int item = it->first;

        if(!containsINT(transactions[i],item))   continue;

        it->second->cnt += 1;

        updateFrequency(i,it->second);
    }
}


void mapUpdate(node* &curr,vector<int> &st)
{
    if(curr->endmark)
        {
            freq[st] = curr->cnt;
            return;
        }

    for(auto it = curr->mp.begin();it!=curr->mp.end();it++)
    {
        st.push_back(it->first);
        mapUpdate(it->second,st);
        st.pop_back();
    }

}

void del(node* &cur)
{
    for(auto it = cur->mp.begin();it!=cur->mp.end();it++)
        del(it->second);

    cur->mydelete();
    delete(cur);
    return;
}
