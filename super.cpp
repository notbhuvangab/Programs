#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;
int main()
  {
    system("cls");
    //First create 2 files
    ofstream fileout;        //output stream
    fileout.open("Stunames",ios::out);
    fileout<<"Devyani\n"<<"Mounika Patrick\n"<<"Neil Banerjee \n";
    fileout.close();
    fileout.open("stumarks",ios::out);
    fileout<<"78.92 \n"<<"72.17 \n"<<"69.33 \n";
    fileout.close();

    char line[80];
    ifstream filein;
    filein.open("stunames",ios::in);
    cout<<" The contents of stunames file are given below \n";
    filein.getline(line,80);
    cout<<line<<endl;
    filein.getline(line,80);
    cout<<line<<endl;
    filein.getline(line,80);
    cout<<line<<endl;
    filein.close();
    filein.open("stumarks",ios::in);
    cout<<"\n The contents of stumarks file are given below \n";
    filein.getline(line,80);
    cout<<line<<endl;
    filein.getline(line,80);
    cout<<line<<endl;
    filein.getline(line,80);
    cout<<line<<endl;
    filein.close();
    return 0;
}
