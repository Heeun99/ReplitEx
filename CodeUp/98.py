#미로판 입력 받으면서 초기화
#시간 단축시키는 방법
# import sys import stdin
# board = [list(map(int, stdin.readline.split())) for _ in range(10)]
board = [list(map(int, input().split())) for _ in range(10)]

#리스트상 좌표로 인식! 수학좌표 ㄴㄴ
x,y = 1,1

while(board[x][y]==0):
  #현재 지점을 9로 설정(지나간 길은 9로 표시)
  board[x][y]=9

  #만약 오른쪽이 비었거나 먹이가 있으면 이동
  if(board[x][y+1]==0 or board[x][y+1]==2):
    y += 1
  elif(board[x][y+1]==1):
    x += 1
  if(board[x][y]==2):
    board[x][y]=9

for i in range(10):
  for j in range(10):
    print(board[i][j],end=' ')
  print()