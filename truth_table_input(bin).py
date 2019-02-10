def sort(bi,temp):
  copy=list(temp)
  temp=copy
  nos=[]
  for i in bi:
    t=''
    for j in i:
      t+=str(j)
    nos.append(int(t,2))
  for i in range(len(bi)):
    c=0
    for j in bi[i]:
      if j==1:
        c+=1
    bi[i]=c

  for i in range(len(bi)-1):
    for j in range(0,len(bi)-i-1):
      if bi[j]>bi[j+1]:
        bi[j],bi[j+1]=bi[j+1],bi[j]
        nos[j],nos[j+1]=nos[j+1],nos[j]
        temp[j],temp[j+1]=temp[j+1],temp[j]

  for i in range(len(bi)-1):
    for j in range(0,len(bi)-i-1):
      if bi[j]==bi[j+1]:
        if nos[j]>nos[j+1]:
          nos[j],nos[j+1]=nos[j+1],nos[j]
          temp[j],temp[j+1]=temp[j+1],temp[j]
  out=[]
  for i in temp:
    o=''
    for j in i:
      o+=str(j)
    out.append(o)
  for i in out:
    print(i)
import sys
n=int(input())
if n==0:
  print(0)
  sys.exit(0)
t=2**n
b=[[0]*n for _ in range(t)]
c1,c2=len(b),len(b)
j=0
f=0

while j<len(b[0]):
  c1=int(c1/2)
  c2=int(c2/2)
  c11=c1
  c22=c2
  for i in range(len(b)):
    if f==0 and c11>0:
      b[i][j]=0
      c11-=1
    elif f==1 and c22>0:
      b[i][j]+=1
      c22-=1
    if c11==0:
      f=1
      c11=c1
    if c22==0:
      f=0
      c22=c2    
  j+=1
sort(b,b)
