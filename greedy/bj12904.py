s = list(input())
t = list(input())
res = 0

for i in range(len(t)-1,-1,-1):

  if t == s:
    res = 1
    break
    
  if t[i] == "A":
    t.pop()
    
  else:
    t.pop()
    t.reverse()

print(res)