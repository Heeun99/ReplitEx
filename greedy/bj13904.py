n = int(input())
arr = []
answer = [0]*1000
          
for i in range(n):
  a,b = map(int, input().split())
  arr.append([a,b])

#점수를 기준으로 내림차순 정렬
arr.sort(reverse=True,key = lambda x : x[1])

for i in range(n):
  for j in range(arr[i][0]-1,-1,-1):
    if answer[j]==0:
      answer[j] = arr[i][1]
      break

print(sum(answer))