k,l=input().split()
k=int(k)
l=int(l)
L=[]
for c in range(k+1,l):
  sum=0
  temp=c 
  while(temp!=0):
    l=temp%10
    sum+=l**3
    temp//=10
  if(c==sum):
    L.append(c)
print(*L)
