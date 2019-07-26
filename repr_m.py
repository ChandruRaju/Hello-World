s=int(input())
end=int(input())
for i in range(s,end+1):
   if i>1: 
       for n in range(2,i): 
           if (i%n)==0: 
               break
       else: 
           print(i) 
