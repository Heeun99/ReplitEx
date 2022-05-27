left, right = 13, 17
cnt = 0
count = []
arr = []
for i in range(left,right+1):
  arr.append(i)
  for j in range(1,i+1):
    if i%j==0:
      cnt += 1
  count.append(cnt)
  cnt = 0
print(arr)
print(count)
#//
answer = 0

print(answer)