n = int(input())
data = list(map(int, input().split()))

data.sort()
sum1 = []
result=0


for i in range(n):
  result += data[i]
  sum1.append(result)

print(sum(sum1))