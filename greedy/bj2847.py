n = int(input())
a = [int(input()) for i in range(n)]
a.reverse()

ind = 0
end = a[0]

for i in range(1,n):
  if end<=a[i]:
    ind += a[i]-end+1
    end = a[i]-(a[i]-end+1)
  else:
    end = a[i]

print(ind)