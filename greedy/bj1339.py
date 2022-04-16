n = int(input())
wrd = [input() for _ in range(n)]

dict = {}
#사전 자료형 초기화 
for w in wrd:
  #rst는 제곱근 할 수 = 자릿수
  #ex 'ABC' A는 100의 자리수임 10의 2(전체 문자열-1)제곱 
  rst = len(w)-1
  for c in w: #문자열을 하나씩 확인하는 과정 (w 문자열 c는 문자)
    if c in dict: #dict에 해당하는 문자가 있으면!
      dict[c] += pow(10,rst) # 각 자리수 만큼 제곱근
    else:
      dict[c] = pow(10,rst)
    rst -= 1
#value값으로 정렬 가장 많은 값 순으로 순차적으로 9~1로 곱해준다음 더하기
dict = sorted(dict.values(), reverse=True)

result, k = 0,9
#가장 큰 거 부터 9곱해서 result에 하나씩 더하기
for value in dict:
  result += value * k
  k -= 1

print(result)