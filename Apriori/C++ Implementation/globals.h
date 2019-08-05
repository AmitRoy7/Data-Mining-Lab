#include<bits/stdc++.h>
using namespace std;

#define PRINT_FLAG 0

double min_sup,minFreq;
vector<vector<string> > transactions;
map<string,int> freq;
map<string,int> order;
vector<string> candidates;
double totalLength = 0;

int totJoin = 0;
int totCandidate = 0;
int totFreqPattern = 0;

vector<int> afterJoin, afterPrune, actualFrequent;


void init()
{
    transactions.clear();
    freq.clear();
    candidates.clear();
    totalLength = 0;
    afterJoin.clear();
    afterPrune.clear();
    actualFrequent.clear();

    totJoin = 0;
    totCandidate = 0;
    totFreqPattern  = 0;
}
