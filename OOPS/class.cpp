#include<iostream>

using namespace std;

class Book{

    int noOfPages;
    int pageNo = 0;

    public:

    Book(int pgNo){
        noOfPages = pgNo;
    }

    void incrementPage() { pageNo+=1; }

    void display(){
        cout<<"The no. of pages in this book:"<<noOfPages<<endl;
        cout<<"The no. of pages read till now:"<<pageNo<<endl;
    }
};

int main(){
    Book B1(320);

    for(int i=0;i<25;i++){
        B1.incrementPage();
    }

    B1.display();

}