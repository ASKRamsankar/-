n,W=map(int,input().split())
wt=list(map(int,input().split()))
val=list(map(int,input().split()))
ratio=[]
for i in range(n):
  ratio.append(val[i]/wt[i])
cost=0
while W>=0 and len(val)>0:
  if W>=wt[ratio.index(max(ratio))]:
    cost+=val[ratio.index(max(ratio))]
    W-=wt[ratio.index(max(ratio))]
  val.pop(ratio.index(max(ratio)))
  wt.pop(ratio.index(max(ratio)))
print(cost)
