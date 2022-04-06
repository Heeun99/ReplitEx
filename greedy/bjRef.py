t = int(input())
btn = [5*60, 1*60, 10]

count = 0
result = []

for i in range(3):
  if t //btn[i] != 0:
    count += t//btn[i]
    result.append(t//btn[i])
    t %= btn[i]
  
  else:
    result.append(0)

if t !=0:
  result = [-1]

for i in result:
  print(i,end=' ')