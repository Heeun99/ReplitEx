n = int(input())
a = list(map(int, input().split()))

count = 0
re = 0

for i in range(n):
  if a[i] == re:
    count += 1
    re += 1
    if re == 3:
      re = 0

print(count)