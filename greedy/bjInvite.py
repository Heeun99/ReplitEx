n = int(input())
tr = list(map(int, input().split()))

tr.sort(reverse = True)
result = []
j = 0
for i in tr:
  j += 1
  result.append(i+1+j)

print(max(result))