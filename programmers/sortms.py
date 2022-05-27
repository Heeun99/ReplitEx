def solution(s):
    ll = ''.join(j for j in s if j.islower())
    uu = ''.join(i for i in s if i.isupper())
    
    l = sorted(ll,reverse=True)
    u = sorted(uu,reverse=True)
    
    answer = ''.join(l)+''.join(u)
    
    return answer

##문자열을 정렬할때는 sorted를 이용한다
##리스트의 값을 문자열로 만들 때는 join을 사용