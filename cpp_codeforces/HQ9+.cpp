#include<bits/stdc++.h>
using namespace std;

int main(){
    string s;
    cin>>s;
    bool f=0;
    for(int i=0;i<s.size();i++){
        if(s[i]=='H' || s[i]=='Q' || s[i]=='9'){f=1;break;}
    }
    if(f==1){cout<<"YES"<<endl;}
    else{cout<<"NO"<<endl;}
    return 0;
}