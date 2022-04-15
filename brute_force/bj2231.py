n = int(input())

for i in range(1, n+1):
  num = sum(map(int,str(i))) #각 자리수 합하기
  num_sum = i + num #생성자 i + 생성자 자릿 수 합 num
  if num_sum == n:
    print(i)
    break
  if i == n: #생성자가 없으면
    print(0)