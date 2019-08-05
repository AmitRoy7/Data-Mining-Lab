#include<bits/stdc++.h>
#include "globals.h"
#include "accessories.h"
#include "Trie.h"
using namespace std;

#define scI(a)   scanf("%d",&a)
#define scD(a)   scanf("%lf",&a)

#define prI(a)   printf("%d",a);
#define prD(a)   printf("%0.2lf",a);
#define prS(a)   printf("%s",a);

#define sp       printf(" ");
#define nl       printf("\n");
#define MAX      1000007

void input(string &filename)
{
    ifstream fin;
    string temp;
    vector<string>itemset;



    fin.open(filename.c_str());
    char ch[MAX];
    while(fin.getline(ch,MAX) && strlen(ch)>0)
    {
        temp = (string)ch;

        if(temp=="")    continue;

        itemset = strToVec(temp);
        itemset = vSort(itemset);

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
    candidates = vSort(candidates);

    fin.close();
}

vector<string> apriori_generation(vector<string> &st,int sz)
{

    vector<string> v1,v2;
    bool flag;
    vector<string> st2;

    int cntJoinStep = 0;

    for(int i =0; i<st.size(); i++)
    {

        for(int j= i+1 ; j<st.size(); j++)
        {
            v1 = strToVec(st[i]);
            v2 = strToVec(st[j]);

            flag = true;

            for(int i=0; i<sz-1; i++)
            {
                if(v1[i]!=v2[i])
                {
                    flag = false;
                    break;
                }
            }

            if(!flag)   continue;


            v1.push_back(v2[sz-1]);

            cntJoinStep++;


            ///prune_step;


            for(int i=0; i<v1.size() && flag; i++)
            {
                string temp = "";
                bool first = true;

                for(int j=0; j<v1.size(); j++)
                {
                    if(j==i)
                        continue;

                    if(first)
                        first = false;
                    else
                        temp += " ";
                    temp += v1[j];

                }


                ///checking whether it has an infrequent subset
                ///if yes then it is not a candidate
                ///apriori property

                if(!contains(st,temp))
                {
                    flag = false;
                    break;
                }
            }


            if(flag)
            {
                string tmp = "";
                for(int i=0; i<v1.size(); i++)
                {
                    if(i)  tmp+= " ";
                    tmp += v1[i];
                }

                st2.push_back(tmp);
            }
        }
    }



    afterJoin.push_back(cntJoinStep);
    afterPrune.push_back(st2.size());


    return st2;
}


int main()
{


    prS("\n\t\t\tAPRIORI - frequenty itemset finding algorithm\n")
    prS("\t\t=============================================================\n")

    vector<string> datasets;

    // datasets.push_back("input.txt");
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

    input(datasets[choice]);


//    for(auto it:transactions)
//        vectorPrintSp(it);



    string datasetName = datasets[choice];
    int numOfTransation = transactions.size();
    int distinctItems = candidates.size();
    double avgLength = totalLength/transactions.size();
    double densityPercentage = (avgLength/distinctItems) * 100;
    string datasetType = densityPercentage>=10 ? "Dense Dataset":"Sparse Dataset";


    prS("\n\n\t\tDataset Name: ");prS(datasetName.c_str());nl;
    prS("\t\tNo. of Transactions: ");prI(numOfTransation);nl;
    prS("\t\tDistinct Items: ");prI(distinctItems);nl;
    prS("\t\tAvg. Length: ");prD(avgLength);nl;
    prS("\t\tDensity Percentage: ");prD(densityPercentage);prS("%");nl;
    prS("\t\tDataset Type: ");prS(datasetType.c_str());nl;nl;




    prS("\n\t\tEnter Minimum Frequency Percentage%: ");


    cin>>min_sup;
    minFreq = ceil((double)transactions.size()*min_sup/100.0);
    prS("\n\t\tMinimum Support Threshold: ");prI((int)minFreq);nl





    vector<string> prev_candidates,cur_candidates;


    clock_t tStart = clock();



    prS("\n\n\t\t=========================================================\n");
    prS("\t\t|LEVEL-i| After Joining | After Pruning |Actual Frequent|\n");
    prS("\t\t=========================================================");

    int i = 1;
    while(i)
    {
        if(i==1)
        {
            cur_candidates = candidates;
            afterJoin.push_back(candidates.size());
            afterPrune.push_back(candidates.size());

            candidates.clear();
        }
        else
        {
            cur_candidates = apriori_generation(prev_candidates,i-1);

            candidates.clear();
            freq.clear();

            root = new node();

            for(auto it: cur_candidates)
            {
                vector<string> newCandidate = strToVec(it);
                insertTrie(newCandidate);
            }


            ///counting frequency


            node* cur;

            for(int i =0; i<transactions.size(); i++)
            {
                cur = root;
                updateFrequency(i,cur);
            }

//            cout<<"frequency update complete"<<endl;

            cur = root;
            mapUpdate(cur,"");


            del(root);

//            cout<<"trie vanished"<<endl;

        }




        for(auto it:cur_candidates)
        {

            if(freq[it]>=minFreq)
            {
                candidates.push_back(it);
            }

        }



        actualFrequent.push_back(candidates.size());





        prS("\n\t\t|  L-");prI(i);
        prS("\t|\t");prI(afterJoin[i-1]);
        totJoin += afterJoin[i-1];
        prS("\t|\t");prI(afterPrune[i-1]);
        totCandidate += afterPrune[i-1];
        prS("\t|\t");prI(actualFrequent[i-1]);
        totFreqPattern += actualFrequent[i-1];
        prS("\t|\n");
        prS("\t\t=========================================================");

        if(candidates.size()<1)     break;

        ///Printing frequent i-itemsets with frequency
        if(candidates.size()>0)
        {

        if(PRINT_FLAG)
        {

//        cout<<endl<<endl<<"\t\tFrequent "<<i<<" itemsets: "<<endl;
        printf("\n\n\t\t Frequent %d itemsets: \n",i);
        for(auto it: candidates)
        {
            string itemset = it;
            cout<<"\t\t"<<itemset <<" Frequency: "<<freq[itemset]<<endl;
        }

        }

            prev_candidates = (candidates);
            i++;


        }
    }


    double execution_time = (double)(clock() - tStart)/CLOCKS_PER_SEC;


    prS("\n\t\t| Total ");
        prS("|\t");prI(totJoin);
        prS("\t|\t");prI(totCandidate);
        prS("\t|\t");prI(totFreqPattern);
        prS("\t|\n");
        prS("\t\t=========================================================");


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
