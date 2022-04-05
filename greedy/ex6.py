data = list(map(int, input()))

result = 1
data.sort(reverse = True)

for i in data:
  if i == 0 or i == 1:
    result += i
  else:
    result *= i

print(result)    