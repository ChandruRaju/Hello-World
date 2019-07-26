k,l=list(map(int,input().split()))
k=k^l
l=k^l
k=k^l
print(k,end=" ")
print(l)
