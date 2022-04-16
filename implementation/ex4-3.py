pos = input()
x = int(pos[-1])
ss=['a','b','c','d','e','f','g','h']
#수직x 수평x
for i in range(len(ss)):
  if pos[0]==ss[i]:
    y = i+1

nx1 = x+2
ny1 = y+1

nx2 = x-2
ny2 = y+1

nx3 = x+2
ny3 = y-1

nx4 = x-2
ny4 = y-1

ny5 = y+2
nx5 = x-1

ny6 = y+2
nx6 = x+1

ny7 = y-2
nx7 = x+1

ny8 = y-2
nx8 = x-1

data = [[nx1,ny1],[nx2,ny2],[nx3,ny3],[nx4,ny4],[nx5,ny5],[nx6,ny6],[nx7,ny7],[nx8,ny8]]
result = 0
for i in range(len(data)):
    if (data[i][0] < 1 or data[i][0]>8)or(data[i][1] < 1 or data[i][1]>8):
      continue
    else:
      result += 1

print(result)