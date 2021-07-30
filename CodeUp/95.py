#반복문에 대한 범위 개념 확실히 하기
#바둑판에 흰 돌 넣기
n = int(input())

#x y 좌표 판으로 본다
#더 짧은 코드
#board = [[0]*19 for _ in range(19)]
board = [[0]*19 for i in range(19)]

for i in range(n):
  x,y = map(int, input().split())
  board[x-1][y-1]=1

#d[x][y] = 1 놓기

for i in range(19):
  for j in range(19):
    print(board[i][j],end=' ')
  print()