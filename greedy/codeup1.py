pasta=[]
juice=[]
for i in range(3):
  pasta.append(float(input()))

for i in range(2):
  juice.append(float(input()))
  
print(format((min(pasta)+min(juice))*1.1,".1f"))

