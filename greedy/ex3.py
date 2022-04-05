n,m = map(int, input().split())
card = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
  card[i].sort()

min_value = [card[i][0] for i in range(n)]

print(max(min_value))
