a,r,n = map(int, input().split())
i = 1
while True:
  i += 1
  a *= r
  if i == n:
    break

print(a)