n = int(input())

number = list(map(int, input().split()))

number.reverse()

for i in range(n):
  print(number[i],end=' ')