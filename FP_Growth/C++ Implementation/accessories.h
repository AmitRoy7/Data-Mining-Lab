#include<bits/stdc++.h>
using namespace std;

vector<string> vSort(vector<string> &v)
{
    sort(v.begin(),v.end());
    return v;
}

void vectorPrintLn(vector<string> &v)
{

    for(auto it: v)
        cout<<it<<" "<<endl;
    return;
}


void vectorPrintSp(vector<string> &v)
{

    for(int i=0;i<v.size();i++)
    {
        if(i)   cout<<" ";
        cout<<v[i];
    }

}


vector<string> strToVec(string &s)
{
    vector<string> v;
    string tmp = "";
    int i=0;
    while(s[i])
    {
        if(isalnum(s[i]))
        {
            tmp += s[i];
        }
        else
        {
            if(tmp.size()>0)
                v.push_back(tmp);
            tmp = "";
        }
        i++;
    }
    if(tmp.size()>0)
        v.push_back(tmp);

    return v;
}

bool transactionOrder(string &a,string &b)
{
    int aa = order[a];
    int bb = order[b];
    return aa<bb;
}

inline bool checkBit(int mask,int pos){ return  (bool)(mask & (1<<pos));}
