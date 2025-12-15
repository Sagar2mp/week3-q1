#include<iostream>
#include<map>
using namespace std;
int main(){
   map<string ,int>studentmarks;
   studentmarks["saif"]=90;
   studentmarks["sharif"]=99;
   studentmarks["gareeb"]=95;
   map<string,int>::iterator it;
   for(it=studentmarks.begin();it!=studentmarks.end();++it){
       cout<<it->first<<" : "<<it->second<<endl;
   }
   it=studentmarks.find("sharif");
   if(it!=studentmarks.end()){
       it->second=88;
   }
   cout<<"after updating sharif marks"<<endl;
   for(it=studentmarks.begin();it!=studentmarks.end();++it){
       cout<<it->first<<" : "<<it->second<<endl;
   }
}