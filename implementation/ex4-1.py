n = int(input())
s = list(map(str,input().split()))

x,y = 1,1

for i in s:
  if y==1 and i=='L':
    continue
  elif x==1 and i=='U':
    continue
  elif y==n and i=='R':
    continue
  elif x==n and i=='D':
    continue
  else:
    if i=='L':
      y -= 1
    elif i=='R':
      y += 1
    elif i=='U':
      x -= 1
    else:
      x += 1

print(x,y,end=' ')