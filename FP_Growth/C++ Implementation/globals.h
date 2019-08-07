#include<bits/stdc++.h>
using namespace std;

#define PRINT_FLAG 0

double min_sup,minFreq;
vector<vector<int> > transactions;
int freq[MAX];
vector<int> candidates;
double totalLength = 0;


map<int,int> frequentPatternsCnt;///for frequent patern count
map<int,vector<vector<int>>> frequentPatterns;///for frequent patterns

void init()
{
    transactions.clear();
    memset(freq,0,sizeof(freq));
    candidates.clear();
    totalLength = 0;

    frequentPatternsCnt.clear();
    frequentPatterns.clear();
}
