n = int(input())
seat = input()

a = seat.replace('LL','D')

new = 'c'+'c'.join(a)+'c'

print(min(len(seat),new.count('c')))