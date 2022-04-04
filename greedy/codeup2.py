a,b = map(int, input().split())
count = 0
btn_type = [10,5,1]

d = abs(a-b)

for btn in btn_type:
    count += d//btn
    d %= btn
    if (d == 9):
      count += 2
      d=0
      break
    elif (d == 8):
      count += 3
      d=0
      break

    elif d == 4 :
      count += 2
      d=0
      break
  
print(count)