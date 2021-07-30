#격자판 크기 설정 및 초기화
w,h = map(int, input().split())

#보드판 초기화
board =[[0]*h for i in range(w)]

n = int(input())

#입력값 받기
for i in range(n):
  l,d,x,y = map(int, input().split())
  for j in range(l): #막대기 길이 만큼 반복
    if d == 0: #막대기가 가로
      board[x-1][y-1+j]=1 #막대기 길이 만큼 반복해서 1로 채워두기
    else:
      board[x-1+j][y-1]=1

for i in range(w):
  for j in range(h):
    print(board[i][j],end=" ")
  print()