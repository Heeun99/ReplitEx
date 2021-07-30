r,g,b = map(int,input().split())

for i in range(r):
  for j in range(g):
    for e in range(b):
      print(i,j,e)
      
print(r*g*b)