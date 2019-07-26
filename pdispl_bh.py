k,l=input().split()
k=int(k)
l=int(l)
L=[]
for c in range(k+1,l):
    if(c>1):
      for i in range(2,c):
        if(c%i==0):
          break
      else:
        L.append(c)
print(*L)
