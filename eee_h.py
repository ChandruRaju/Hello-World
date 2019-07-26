v=list(input())  
for k in range(0, len(v), 2):
  v[k],v[k+1]=v[k+1],v[k] 
print(''.join(v))
