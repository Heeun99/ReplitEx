n = int(input())
count = 0
type = [50000,10000,5000,1000,500,100,50,10]

for t in type:
  count += n//t
  n %= t

print(count)
