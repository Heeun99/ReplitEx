n = int(input())
a = [int(input()) for i in range(n)]
a.reverse()

end = a[0]
count = 0
for i in range(1,n):
  if a[i] >= end:
    count += a[i]-end+1
    end = a[i]-(a[i]-end+1)
  else:
    end = a[i]

print(count)