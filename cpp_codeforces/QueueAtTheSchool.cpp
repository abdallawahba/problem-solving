#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,t;
    cin>>n>>t;
    char s[n];
    for(int i=0;i<n;i++){
        cin>>s[i];
    }
    for(int i=0;i<n-1 && t;i++){
        if(s[i]=='B' && s[i+1]=='G'){
            swap(s[i],s[i+1]);
            i++;
        }
        if(i>=n-2){t--;i=-1;}
    }
    for(int i=0;i<n;i++){cout<<s[i];}
    cout<<endl;
    return 0;
}