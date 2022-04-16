n = int(input())
seat = input()

a = seat.replace('LL','D')

#join함수 문자열 사이사이에 원하는 문자 넣는 방법

new = 'c'+'c'.join(a)+'c'

print(min(n,new.count('c')))