h,b,c,s = map(float,input().split())

#저장공간
mb = (h*b*c*s)/8/1024/1024

print('%.1f'%mb,'MB')