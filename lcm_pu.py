import math
k,l=map(int,input().split())
m=math.gcd(k,l)
print((k*l)//m)
