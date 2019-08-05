#include<bits/stdc++.h>

#define scI(a)   scanf("%d",&a)
#define scD(a)   scanf("%lf",&a)

#define prI(a)   printf("%d",a);
#define prD(a)   printf("%0.2lf",a);
#define prS(a)   printf("%s",a);

#define sp       printf(" ");
#define nl       printf("\n");
#define MAX      1000007

#define debug   printf("\t\t\t!!!!!!!!!!!!!!Hi!!!!!!!!!!!!!!!!\n")


#include "globals.h"
#include "accessories.h"
#include "fpgrowth.h"
#include "fp_tree_mining.h"
using namespace std;



void input()
{
    prS("\n\t\t\tFP-Growth - Frequent Itemset Mining Algorithm\n")
    prS("\t\t=============================================================\n")

    vector<string> datasets;

//    datasets.push_back("input.txt");
    datasets.push_back("Data Mining Book Example.txt");
    datasets.push_back("FP-Growth Paper.dat");
    datasets.push_back("mushroom.dat");
    datasets.push_back("retail.dat");
    datasets.push_back("chess.dat");
    datasets.push_back("kosarak.dat");
    datasets.push_back("pumsb.dat");
    datasets.push_back("pumsb_star.dat");
    datasets.push_back("connect.dat");
    datasets.push_back("T10I4D100K.dat");
    datasets.push_back("T40I10D100K.dat");
    datasets.push_back("accidents.dat");




    prS("\n\n\t\t SELECT DATASET :\n\n");
    for(int i=0; i<datasets.size(); i++)
    {
        prS("\t\t");
        prI(i+1);
        prS(". ");
        prS(datasets[i].c_str());
        prS("\n");
    }
    prS("\t\t0. Exit");

    int choice;

    while(true)
    {
        prS("\n\n\t\tEnter Choice: ");
        scI(choice);


        if(!choice)
            exit(0);

        if(choice>=1 && choice<=datasets.size())
        {

            choice--;
            break;
        }

        prS("\n\t\tInvalid Choice: ");


    }

    prS("\n\t\tReading Dataset...");


//    for(auto it:transactions)
//        vectorPrintSp(it);

    string filename = datasets[choice];

    ifstream fin;
    string temp;
    vector<string>itemset;

    vector<pair<int,string>> sorted_list;


    fin.open(filename.c_str());
    char ch[MAX];
    int cn = 1;

    while(fin.getline(ch,MAX) && strlen(ch)>0)
    {
//        cout<<cn++<<endl;

        temp = (string)ch;

        if(temp=="")
            continue;

        itemset = strToVec(temp);
//        itemset = vSort(itemset);

        totalLength += itemset.size();

        transactions.push_back(itemset);

        for(auto it : itemset)
        {

            if(!freq[it])
            {

                candidates.push_back(it);     ///candidates
            }

            freq[it]++;                ///counting frequency
        }

    }

    prS("Scan Done");

    for( auto it:candidates)
        sorted_list.push_back({-freq[it],it});

    sort(sorted_list.begin(),sorted_list.end());


    int cnt = 1;
    for (auto it: sorted_list)
        order[it.second] = cnt++;

    for(int i =0; i<transactions.size(); i++)
    {

        vector<string> tr = transactions[i];
        sort(tr.begin(),tr.end(),transactionOrder);
        transactions[i] = tr;
    }
    sort(candidates.begin(),candidates.end(),transactionOrder);

    fin.close();

    prS("Sorting Done");

    string datasetName = datasets[choice];
    int numOfTransation = transactions.size();
    int distinctItems = candidates.size();
    double avgLength = totalLength/transactions.size();
    double densityPercentage = (avgLength/distinctItems) * 100;
    string datasetType = densityPercentage>=10 ? "Dense Dataset":"Sparse Dataset";


    prS("\n\n\t\tDataset Name: ");
    prS(datasetName.c_str());
    nl;
    prS("\t\tNo. of Transactions: ");
    prI(numOfTransation);
    nl;
    prS("\t\tDistinct Items: ");
    prI(distinctItems);
    nl;
    prS("\t\tAvg. Length: ");
    prD(avgLength);
    nl;
    prS("\t\tDensity Percentage: ");
    prD(densityPercentage);
    prS("%");
    nl;
    prS("\t\tDataset Type: ");
    prS(datasetType.c_str());
    nl;
    nl;




    prS("\n\t\tEnter Minimum Frequency Percentage%: ");


    cin>>min_sup;
    minFreq = ceil((double)transactions.size()*min_sup/100.0);
    prS("\n\t\tMinimum Support Threshold: ");
    prI((int)minFreq);
    nl

}

void build_FP_Tree()
{

    vector<int> transactionSupCnt;
    vector<string> patternsofar;
    for(int i=0; i<transactions.size(); i++)
        transactionSupCnt.push_back(1);


    int zero = 0;
    recursive_FPTree(transactions,transactionSupCnt,patternsofar,zero);


}

int main()
{

    input();

    clock_t tStart = clock();

    build_FP_Tree();

    clock_t tEnd = clock();


    printf("\t\t=================================================\n");
    printf("\t\t|     LEVEL-i   |\tFrequent Patterns\t|\n");
    printf("\t\t=================================================\n");

    int tot = 0;
    for(auto it: frequentPatternsCnt)
    {
        printf("\t\t|\tL-%d\t|\t\t%d\t\t|\n",it.first,it.second);
        printf("\t\t=================================================\n");


        tot += it.second;
    }
    printf("\t\t|\tTotal\t|\t\t%d\t\t|\n",tot);
    printf("\t\t=================================================\n");

    double execution_time = (double)(tEnd - tStart)/CLOCKS_PER_SEC;

    prS("\n\n\t\tExecution Time: ");

    if(execution_time >=60)
    {

        prI((int)(execution_time/60));prS(" minute ")
        execution_time -= (int)(execution_time/60) * 60;
    }

    printf("%0.2lf seconds\n\n",execution_time);

    init();
    main();

    return 0;
}
