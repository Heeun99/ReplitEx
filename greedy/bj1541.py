n = input()

sp = n.split('-')
m = 0

if sp[0].isdigit() == True:
  m += int(sp[0])
else:
  m += eval(sp[0]) 

for i in range(1,len(sp)):
  if sp[i].isdigit()==True:
    m -= int(sp[i])
  else:
    m -= eval(sp[i])

print(m)