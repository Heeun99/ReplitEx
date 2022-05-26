from itertools import permutations

numbers = [6, 10, 2]
plist = list(permutations(numbers,len(numbers)))
nlist = []

for i in range(len(plist)):
  string = ''
  for j in range(len(numbers)):
    string += str(plist[i][j])
  nlist.append(int(string))

max1 = str(max(nlist))

print(max1)

####위의 방법을 하면 시간초과를 일으킨다...####
# lambda 함수를 이해하지 못한다
#근데 다른 사람의 모든 풀이에 lambda함수를 이용하는 걸 확인함
# lambda함수 공부하자
# 이유 : permutations은 모든 조합을 다 찾아낸 후 처리하니까...
#
#    num = list(map(str, numbers)) #
#    num.sort(key = lambda x : x*3, reverse = True)
#    
#    return str(int(''.join(num)))
#