#include<iostream>
#include<conio.h>
#include<string>
using namespace std;
int main()
{
	string s;
	int p,q,max,c=0,d=0,n,i=0,f;
	char m;
    cout<<"enter the string:";
    getline(cin, s);
	while(i<s.length())
	{   
		if(s[i]== '<')
		{
			if(c==0)
			{d=0;c=1;p=1;}
			else 
			 p++;
		}
		else if(s[i]=='>')
		{
			if(d==0)
			{c=0;d=1;q=1;}
			else
			 q++;
		}
		if(max<p)
		  max=p;
	    else if(max<q)
	      max=q;
	    i++;  
	}
	cout<<max+1;
		return 0;
}
