n = int(input())
a,b = map(int, input().split())
c = int(input())
kcal=[]

for i in range(n):
  kcal.append(int(input()))

kcal.sort(reverse = True)

total = c
cost = 0

res = total//a

for j in range(n):
  total += kcal[j]
  cost += 1
  now_res = total//(a+b*cost)  
  if res<=now_res:
    res = now_res
  else:
    print(res)
    break
