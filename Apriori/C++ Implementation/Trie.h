#include<unordered_map>
using namespace std;


struct node {

    bool endmark;
    map<string, node*> mp;
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

void insertTrie(vector<string> &st)
{
    node* curr = root;

    for(auto id: st)
    {
        if(curr->mp.find(id)==curr->mp.end())
            {

                curr->mp[id] = new node();
            }

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
        string item = it->first;

        if(!contains(transactions[i],item))   continue;

        it->second->cnt += 1;

        updateFrequency(i,it->second);
    }
}


void mapUpdate(node* &curr,string st)
{
    if(curr->endmark)
        {
            freq[st] = curr->cnt;
            return;
        }

    if(st!="")
        st += " ";
    for(auto it = curr->mp.begin();it!=curr->mp.end();it++)
        mapUpdate(it->second,st+it->first);

}

void del(node* &cur)
{
    for(auto it = cur->mp.begin();it!=cur->mp.end();it++)
        del(it->second);

    cur->mydelete();
    delete(cur);
    return;
}
