#입력받는것을 16진수로 받을 때
a = int(input(),16)

#16진수 곱셈
for i in range(1,16):
  print("%X*%X=%X"%(a,i,a*i))