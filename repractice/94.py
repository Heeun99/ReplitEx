n = int(input())

date = list(map(int, input().split()))

min = date[0] 

for i in range(n):
  if date[i]<min:
    min = date[i]

print(min)