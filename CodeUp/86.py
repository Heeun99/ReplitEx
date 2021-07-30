n = int(input())
#합 반복 수
s=0
i=0
while True:
  i += 1
  s += i
  
  if s>=n:
    break

print(s)