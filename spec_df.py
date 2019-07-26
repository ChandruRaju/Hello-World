k=input()
count=0
for m in k:
  if m.isdigit()!=True and m.isalpha()!=True :
    count=count+1
print(count)
