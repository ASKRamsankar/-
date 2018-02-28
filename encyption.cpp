#include<iostream>
#include<conio.h>
#include<string>
#include<fstream>
using namespace std;
int j,k;
int small(int);
int caps(int);
int num(int);
int main()
{
  int n,i=0;
  char m;
  cout<<"enter the length of the unencypted string:"<<ends;
  cin>>n;
  string msg;
  cout<<"enter the string:"<<ends;
  cin>>msg;
  cout<<"enter the key:"<<ends;
  cin>>k;
  while(i<n)
  {
  j=msg[i];
  if(j>=97&j<=122)
    small(j);
  else if(j>=65&j<=90)
     caps(j);
  else  if(j>=48&j<=57)
      num(j);
  else
    goto s;
 s: msg[i]=j;  
   i++;
  }
 cout<<"encypted msg: "<<msg;
 ofstream outfile;
 outfile.open("tech.txt");
 outfile<<msg;
 outfile.close();
 getch();
 return 0;   
}
int small(int)
{
	j=j+k;
	if(j>122)
	 {
	 	j=j-122;
	 	j=96+j;
	 }
	 return j;
}
int  caps(int)
{
	j=j+k;
	if(j>90)
	{
		j=j-90;
		j=64+j;
	}
	return j;
}
int num(int)
{
	j=j+k;
	if(j>57)
	{
	j=j-57;
	j=47+j;
    }
    return j;
}
