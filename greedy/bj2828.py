n,m = map(int, input().split())
j = int(input())
strt = 1
end = m
distance = 0
for i in range(j):
  p = int(input())

  if p < strt:
    distance += (strt-p)
    strt = p
    end = p + m -1

  elif p > end:
    distance += (p-end)
    end = p
    strt = end-m+1

print(distance)