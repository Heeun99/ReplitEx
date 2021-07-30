#출석부 번호당 부른 횟수 세기
n = int(input())
number = list(map(int, input().split()))

#부른 횟수 처음 초기화
r = 24
d = [0]*r

for i in range(n):
  d[number[i]] += 1

for i in range(1,24):
  print(d[i],end=' ')