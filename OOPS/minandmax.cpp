#include<iostream>

using namespace std;

int main(){

    #ifndef ONLINE_JUDGE
  	freopen("input.txt", "r", stdin);
  	freopen("output.txt", "w", stdout);
  	#endif
  	int n;
  	cin>>n;

	int Arr[n];	
	for(int i=0;i<n;i++)
		cin>>Arr[i];

    int max=0,min=Arr[0];
	for(int i : Arr){
		if(i>max)
			max = i;
		if(i<min)
			min = i;
	}

	cout<<"max:"<<max<<endl<<"min:"<<min<<endl;

}