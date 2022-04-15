a,b = map(int, input().split())
s = list(map(int, input().split()))

s.sort()
strt = 0
count = 0

for i in s:
  if strt<i:
    strt = i+b-1
    count += 1

print(count)