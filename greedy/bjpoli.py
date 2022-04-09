b = input()

c=''
r1 = ''

c = b.replace('XXXX','AAAA')
r1 = c.replace('XX','BB')

if r1.count('X') > 0:
  print(-1)
else:
  print(r1)