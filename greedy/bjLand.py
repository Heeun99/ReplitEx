T = int(input())
m = [int(input()) for _ in range(T)]
coin = [25,10,5,1]

for i in range(T):
  count = ""
  for j in coin:
    count += str(m[i]//j)+ " "
    m[i] %= j
  print(count)