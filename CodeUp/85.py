w,h,b = map(int,input().split())

#저장용량
mb = (w*h*b)/8/1024/1024

print("%.2f"%mb,'MB')