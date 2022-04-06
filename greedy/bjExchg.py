n = int(input())

coin = [500,100,50,10,5,1]

exc = 1000-n
count = 0

for i in coin:
  count += exc//i
  exc %= i

print(count)