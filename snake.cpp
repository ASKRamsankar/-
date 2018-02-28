#include<iostream>
#include<conio.h>
#include<windows.h>
#include<stdlib.h>
#include<unistd.h>
#include<time.h>
using namespace std;
int i,j,p,q,f=1,e=1,z=0,r=0,o=0,scor,count=0;
int t=5;int a[1000],b[1000];
char m,n;char l[10000];
clock_t t0,t1;
void check();
void copy();
void wallcheck();
void food();
void foodcheck();
void score();
void fake();
void end();
void growth();
void startclk();
void duration();
void delfood();
void wait();
int main();
void delback();
void getkey(char);
bool running=true;
void gotoxy(int x,int y)
{
	COORD P={x,y};
	SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE),P);
}
void wall()
{
   int n=0,m=0;
   for(int w=0;w<61;w++)
    {
    	gotoxy(m,n);cout<<"_";m++;
	}--m;
	for(int w=0;w<27;w++)
	{
		gotoxy(m,++n);cout<<"|";
	}
	for(int w=0;w<60;w++)
	{
		gotoxy(--m,n);cout<<"-";
	}
	for(int w=0;w<27;w++)
	{
	gotoxy(m,n);cout<<"|";--n;
	}	
}
void score()
{
	gotoxy(73,3);
	cout<<"SCORE BOARD"<<endl;
	gotoxy(73,4);
	cout<<"SCORE:"<<scor;
}
void create()
{   
 	for(int c=0;c<5;c++)
	{
	 gotoxy(i,j);
	 cout<<"0";
	 i=i-1;
	}
	p=i;q=j;i=i+5;
	for(int i0=1;i0<6;i0++)
	{
	  a[i0]=i;
	  i=i-1;
	}i=i+5;
	for(int j0=1;j0<6;j0++)
	{
	   b[j0]=j;	
	}
	m='d';food();score();
}
void move()
{	
	while(1)
	{
	if(m=='d')
	    {
		++i;check();gotoxy(i,j);wallcheck();cout<<"0";foodcheck();l[r]=m;r++;
	    }
	 else if(m=='w')
	    {
	     --j;check();gotoxy(i,j);wallcheck();cout<<"0";foodcheck();l[r]=m;r++;
		} 
	else  if(m=='a')
	    {  
	    --i;check();gotoxy(i,j);wallcheck(); cout<<"0";foodcheck();l[r]=m;r++;
		}	 
	 else if(m=='s')
	    {  
	       ++j;check();gotoxy(i,j);wallcheck();cout<<"0";foodcheck();l[r]=m;r++;
		}duration();delback();
    }
}
void delback()
{	_sleep(20);		
    if(z<5)
	{
		gotoxy(++p,q);
	   cout<<" ";z=z+1;copy(); score();getkey(m);
       }
	   else if(l[o]=='d')
	   {
	   gotoxy(++p,q);
	   cout<<" "; o++;copy(); score();getkey(m);
	   	   }
    else if(l[o]=='w')
	   {
	   	gotoxy(p,--q);
	    cout<<" ";o++;copy(); score();getkey(m);  
	   }
	else if(l[o]=='a')
	{
		 gotoxy(--p,q);
	   cout<<" ";o++;copy(); score();getkey(m);
	   }   
	else if(l[o]=='s')
	{
		 gotoxy(p,++q);
	   cout<<" ";o++;copy(); score();getkey(m);
	   }
}
void check()
{   
    for(int i0=2,j0=2;i0<=t&j0<=t;i0++,j0++)
    {
     if(i==a[i0]&j==b[j0])
	 {
	 	if(i0==2&j0==2)
	 	{
		  fake();
	      if(l[r-1]=='d')
	        m='d';
          else if(l[r-1]=='w')
            m='w';
	      else if(l[r-1]=='a')
		    m='a'; 
	      else if(l[r-1]=='s')
	        m='s';
		  move();    
	 	}
		 else
		  end();
	}
	if(a[i0]==e&b[j0]==f)
	{  
	  gotoxy(e,f);
	  cout<<"*";
    }
   }return;
}
void copy()
{ 	
  for(int i0=t,j0=t;i0>1&j0>1;i0--,j0--)
  {
    a[i0]=a[i0-1];
	b[j0]=b[j0-1];
  }a[1]=i;b[1]=j;	
}
void fake()
{
	if(m=='d')
	  --i;
	else if(m=='w')
	   ++j;
	else if(m=='a') 
	   ++i;
	else if(m=='s')
	   --j; 
	   return;      
}
void wallcheck()
{
	if(i==60||i==0||j==0||j==27)
	{
	end();
    }
}
void end()
{
	gotoxy(23,14); cout<<"*== GAME OVER ==*";getch();
	 exit(0);
}
void food()
{ z: e=rand();f=rand(); 
	if(e<50&f<25>0&f>0)
	{
		gotoxy(e,f);
		cout<<"*";startclk();
		count++;
		if(count==5)
		{
			gotoxy(e,f);
			cout<<"Q";startclk();
			count=0;
		}
    }
    else
     goto z;
}
void foodcheck()
{
	if(i==e&&j==f)
	{   if(count==0)
	      {scor=scor+10;growth();++t;startclk();}
	    else  
		  {scor=scor+2;growth();++t;startclk();}
		food();
		score();
	}
}
void startclk()
{
	t0=clock();
	return;
}
void duration()
{
  t1=(clock()-t0)/(double)CLOCKS_PER_SEC;
  if(t1>5)
  {  if(count==0)
     {
      delfood();food();
     }
	t1=0;
  } 
  return;
}
void delfood()
{
    gotoxy(e,f);
   cout<<" ";
}
void growth()
{
	    if(l[o]=='d')
	   {gotoxy(p,q);cout<<"0";--p;o=o-1;l[o]='d';}
	else if(l[o]=='w')
	   {gotoxy(p,q);cout<<"0";++q;o=o-1;l[o]='w';}
	else if(l[o]=='a') 
	   {gotoxy(p,q);cout<<"0";++p;o=o-1;l[o]='a';}
	else if(l[o]=='s')
	    {gotoxy(p,q);cout<<"0";--q;o=o-1;l[o]='s';}
return;
}
void getkey(char)
{
	while(running)
	{
		if(kbhit())
		{
			m=getch();
		}running=false;
	}_sleep(45);running=true;move();
}
int main()
{   wall();
   i=20;j=15;gotoxy(17,14);
   cout<<"==Press Any Key to Start==";
   getch();system("cls");
   wall();
   create();
   move();
}
