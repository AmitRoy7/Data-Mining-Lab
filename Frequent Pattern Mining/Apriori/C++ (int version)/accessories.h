#include<bits/stdc++.h>
using namespace std;

vector<int> vSort(vector<int> &v)
{
    sort(v.begin(),v.end());
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

set<string> makeClone(set<string> &st)
{
    set<string> st2;

//    int cnt = 0;
    for(set<string>::iterator it=st.begin();it!=st.end();it++)

        {
//            cnt++;
            st2.insert(*it);
        }
//        cout<<"DONE"<<" "<<cnt<<endl;
    return st2;
}

bool containsINT(vector<int> &v, int &it)
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


bool contains(vector<vector<int>> &v, vector<int> &it)
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
