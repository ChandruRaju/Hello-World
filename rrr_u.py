k=int(input(" "))
r=0
while(k>0):
    d=k%10
    r=r*10+d
    k=k//10
print(" ",r)
