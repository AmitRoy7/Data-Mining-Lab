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
void setPrint(set<string> &st)
{
    for(set<string>::iterator it=st.begin();it!=st.end();it++)
    {
        if(it!=st.begin())  cout<<" ";
        cout<<*it;
    }
    cout<<endl;
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

bool contains(vector<string> &v, string &it)
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

//void sortAll()
//{
//    for (auto it: transactions)
//        it = sort(it.begin(),it.end());
//    candidates = sort(candidates.begin(),candidates.end());
//}


vector<string> clean_vector(vector<string> &vec)
{
    sort( vec.begin(), vec.end() );
    vec.erase( unique( vec.begin(), vec.end() ), vec.end() );
    return vec;
}

