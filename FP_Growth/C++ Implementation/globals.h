#include<bits/stdc++.h>
using namespace std;

#define PRINT_FLAG 0

double min_sup,minFreq;
vector<vector<string> > transactions;
map<string,int> freq;
vector<string> candidates;
double totalLength = 0;


map<string,int> order;///fp-tree item order
map<int,int> frequentPatternsCnt;///for frequent patern count
map<int,vector<vector<string>>> frequentPatterns;

void init()
{
    transactions.clear();
    freq.clear();
    candidates.clear();
    totalLength = 0;

    order.clear();
    frequentPatternsCnt.clear();
    frequentPatterns.clear();
}
