brown = 24
yellow = 24
answer = []
nums = brown + yellow
arr = []

for i in range(2,nums):
  if nums%i == 0:
    arr += [[i, nums//i]]

if len(arr)== 1:
  print(arr[0])
else:
  print(arr[int(len(arr)/2)])

print(arr)

###위 코드의 경우 몇개의 테스트케이스에서 오류가 난다...####
#
#
#
#