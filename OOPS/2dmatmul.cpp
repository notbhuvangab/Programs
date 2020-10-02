#include<iostream>

using namespace std;

int main(){

    #ifndef ONLINE_JUDGE
  	freopen("input.txt", "r", stdin);
  	freopen("output.txt", "w", stdout);
  	#endif

    int mat1[3][3] , mat2[3][3];

    for(int i=0;i<3;i++){
        for(int j=0;i<3;j++){
            cin>>mat1[i][j];
        }
    }

    for(int i=0;i<3;i++){
        for(int j=0;i<3;j++){
            cin>>mat2[i][j];
        }
    }

    cout<<"After Multiplication:"<<endl;

    
    
}