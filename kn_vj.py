M,L=input().split()
M=int(M)
L=int(L)
x=list(map(int,input().strip().split()))
sum=0
for b in range(1,L+1):
    sum=sum+b
print(sum)
