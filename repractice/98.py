data = [list(map(int,input().split())) for i in range(10)]
x,y = 1,1

while data[x][y]==0:

  data[x][y]=9

  if data[x][y+1]==0 or data[x][y+1]==2:
    y += 1
  elif data[x][y+1]==1:
    x += 1
  if data[x][y]==2:
    data[x][y]=9

for i in range(10):
  for j in range(10):
    print(data[i][j], end=' ')
  print()