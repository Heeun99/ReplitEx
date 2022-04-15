from itertools import combinations

n,m = map(int,input().split())
crd = list(map(int, input().split()))

result = list(combinations(crd,3))
a = []
for i in range(len(result)):
  a.append(sum(result[i]))

a.sort(reverse = True)

for i in a:
  if i == m:
    print(i)
    break
  elif i < m:
    print(i)
    break