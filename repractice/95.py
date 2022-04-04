n = 20
m = 20

data = [[0]*m for _ in range(n)]
a = int(input())

for i in range(a):
  x,y = map(int, input().split())
  data[x][y] = 1

for i in range(1,20):
  for j in range(1,20):
    print(data[i][j],end=' ')
  print()
