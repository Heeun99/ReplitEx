n = int(input())
k = int(input())
s = list(map(int, input().split()))

s.sort()
a= []

if k >= n:
  print(0)
  
else:
  for i in range(n-1):
    a.append(abs(s[i]-s[i+1]))
  
  a.sort()
  
  for j in range(k-1):
    a.pop()

  print(sum(a))