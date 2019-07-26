k=int(input())
Factorial=1
if(k<0):
  print("Invalid")
elif(k==0):
  print(1)
else:
  for o in range(1,k+1):
    Factorial=Factorial*o
  print(Factorial)
