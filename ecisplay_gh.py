k,m=input().split()
k=int(k)
m=int(m)
L=[]
for i in range(k+1,m):
    if(i%2==0):
        L.append(i)
print(*L)
