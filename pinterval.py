s,t=map(int,input().split())
for n in range(s+1,t):
  if n>1:
    for i in range(2,n):
      if(n%i)==0:
        break
    else:
     print(n,end=" ")  
