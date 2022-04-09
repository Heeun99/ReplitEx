n = input()

sp = n.split('-')

num = []

for i in sp:
  cnt = 0
  s = i.split('+')
  for j in s:
    cnt += int(j)
  num.append(cnt)

a = num[0]

for i in range(1,len(num)):
  a -= num[i]

print(a)