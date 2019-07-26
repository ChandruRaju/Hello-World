a=int(input())
Factorial=1
if(a<0):
  print("Invalid")
elif(a==0):
  print(1)
else:
  for i in range(1,a+1):
    Factorial=Factorial*i
  print(Factorial)
