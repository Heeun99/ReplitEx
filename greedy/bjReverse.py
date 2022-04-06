a = list(map(int, input()))

count0 = 0
count1 = 0

if a[0] == 0:
  count1 += 1
else:
  count0 += 1

for i in range(len(a)-1):
  if a[i] != a[i+1]:
    if a[i+1] == 1:
      count0 += 1
    else:
      count1 += 1

print(min(count0,count1))