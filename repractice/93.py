n = int(input())
date = list(map(int, input().split()))

for i in range(1, n+1):
  print(date[-i],end=' ')