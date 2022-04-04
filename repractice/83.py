r,g,b = map(int, input().split())
s = 0
for i in range(r):
  for j in range(g):
    for u in range(b):
      print(i,j,u, sep=' ')
      s += 1

print(s)