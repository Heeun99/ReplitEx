#주사위의 숫자 1~n이고 주사위 2개일때
#나올 수 있는 경우의 수

n, m = map(int,input().split())

for i in range(1,n+1):
  for j in range(1,m+1):
    print(i,j)