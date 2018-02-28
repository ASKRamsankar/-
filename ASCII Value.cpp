#include<iostream>
#include<conio.h>
#include<string>
using namespace std;
int main()
{
  char m,q;
  do
  {
  cout<<"enter a character: ";
  cin>>m;
  int i=m;
  cout<<"ASCII value of the charater is : "<<i<<endl;
  cout<<"if u want to continue(y/n) :";
  cin>>q;
}while(q=='y');
getch();
return 0;
}
