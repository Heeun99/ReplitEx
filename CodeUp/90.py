a,m,d,n = map(int, input().split())

#시간초과 : 무한루프때문에
#while True:
#  i += 1
#  a = a*m+d
#  if i == n:
#    break

for i in range(1,n):
  a = a*m+d

print(a)