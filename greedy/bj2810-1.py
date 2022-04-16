n = int(input())
seat = input()

x = seat.count('LL')
y = seat.count('S')

if x < 1:
  print(y)
else:
  print(x+y+1)