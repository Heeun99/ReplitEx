a,b = map(int, input().split())
s = list(map(int, input().split()))

s.sort()
strt = 0
count = 0

#테이프 개수 최소
#테이프의 첫 위치에서 테이프의 길이 -1만큼(0.5 + 0.5) 수리 가능함 
# 그 이전은 시작 위치에서 제외
# 다음 테이프 시작위치

for i in s:
  if strt<i:
    strt = i+b-1
    count += 1

print(count)