n = int(input())
date = list(map(int, input().split()))

d = [0]*24

for i in range(n):
  d[date[i]] += 1

for i in range(1,24):
  print(d[i],end=' ')
