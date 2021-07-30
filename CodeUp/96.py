#바둑판 깔기_리스트 컴프리헨션
#2차원 리스트 초기화 방법!
#바둑판에 흰 백을 깔아주자
board = [list(map(int,input().split())) for i in range(19)]

#뒤집기 횟수 받아오기
n = int(input())

#좌표받아서 그 줄 다 반대로 하기
for i in range(n):
  x,y = map(int,input().split())
  for j in range(19):
    if(board[j][y-1])==0:
      board[j][y-1]=1
    else:
      board[j][y-1]=0
    
    if(board[x-1][j])==0:
      board[x-1][j]=1
    else:
      board[x-1][j]=0

for i in range(19):
  for j in range(19):
    print(board[i][j],end=' ')
  print()