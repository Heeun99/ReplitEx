w,h,b = map(int, input().split())
s = w*h*b/8/1024/1024
print('%.2f'%s,"MB")