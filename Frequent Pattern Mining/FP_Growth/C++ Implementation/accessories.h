#include<bits/stdc++.h>
using namespace std;

bool transactionOrder(int &a,int &b)
{
    int aa = freq[a];
    int bb = freq[b];
    if(aa==bb)
        return a<=b;
    return aa>bb;
}

inline bool checkBit(int mask,int pos){ return  (bool)(mask & (1<<pos));}


vector<int> vSort(vector<int> &v)
{
    sort(v.begin(),v.end(),transactionOrder);
    return v;
}

void vectorPrintLn(vector<int> &v)
{

    for(auto it: v)
        cout<<it<<" "<<endl;
    return;
}


void vectorPrintSp(vector<int> &v)
{

    for(int i=0;i<v.size();i++)
    {
        if(i)   cout<<" ";
        cout<<v[i];
    }

}


vector<int> strToVec(string &s)
{
    vector<int> v;
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
                v.push_back(atoi(tmp.c_str()));
            tmp = "";
        }
        i++;
    }
    if(tmp.size()>0)
        v.push_back(atoi(tmp.c_str()));

    return v;
}

