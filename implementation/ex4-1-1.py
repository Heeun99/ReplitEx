n = int(input())
plan = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
rule = ['L','R','U','D']
x,y=1,1

for i in plan:
  for j in range(len(rule)):
    if i == rule[j]:
      nx = x + dx[j]
      ny = y + dx[j]
      print(nx,ny)
  #여기에 if continue문을 적은 이유는 x,y=1,1이 유지되고 있음/공간 벗어나는 경우 무시
  if nx<1 or ny<1 or nx>n or ny>n:
    continue
  
  x,y = nx,ny

print(x,y)