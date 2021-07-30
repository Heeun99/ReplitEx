a,d,n = map(int, input().split())
i = 1
while True:
  i += 1
  a += d
  if i == n:
    break

print(a)