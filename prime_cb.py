k=int(input())
count=0
for m in range(1,k+1):
    if(k%m==0):
        count+=1
if(count==2):
    print("yes")
else:
    print("no")
