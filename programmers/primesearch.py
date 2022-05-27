n = 10
prime = [False]+[False]+[True]*(n-1)

print(prime)

for i in range(2, int(n**0.5)+1):
  if prime[i]:
    for j in range(i*i, n+1, i):
      prime[j] = False

answer = prime[1:n+1].count(True)
print(prime)
print(answer)