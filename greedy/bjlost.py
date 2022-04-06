a,b = input().split()

A = []
B = []

for i in a:
  A.append(int(i))

for i in b:
  B.append(int(i))

max_A = []
max_B = []
min_A = []
min_B = []

for i in range(len(A)):
  if A[i] == 5:
    max_A.append(6)
  else:
    max_A.append(A[i])
    
for i in range(len(A)):
  if A[i] == 6:
    min_A.append(5)
  else:
    min_A.append(A[i])

for i in range(len(B)):
  if B[i] == 6:
    min_B.append(5)
  else:
    min_B.append(B[i])
    
for i in range(len(B)):
  if B[i] == 5:
    max_B.append(6)
  else:
    max_B.append(B[i])
max_ad = ""
min_ad = ""
max_bd = ""
min_bd = ""

for i in range(len(A)):
  max_ad = max_ad + str(max_A[i])
  min_ad = min_ad + str(min_A[i])

for i in range(len(B)):
  max_bd = max_bd + str(max_B[i])
  min_bd = min_bd + str(min_B[i])

print(int(min_ad)+int(min_bd),int(max_ad)+int(max_bd), end=' ')