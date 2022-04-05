n,m,k = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort(reverse=True)

sum = 0

a = m//k
b = m%k

sum = lst[0]*a*k+lst[1]*b

print(sum)