#3개의 수를 비교하는 삼항연산자 작은 수 비교
a,b,c = map(int, input().split())

print((a if a<b else b) if((a if a<b else b)<c) else c)