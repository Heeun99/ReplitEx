def solution(s, n):
    answer = ''
    
    for i in s:
        if i == ' ':
            answer += ' '
        elif ord('a') <= ord(i) <= ord('z'):
            answer += chr((ord(i)+n-ord('a'))%26 + ord('a'))
        elif ord('A') <= ord(i) <= ord('Z'):
            answer += chr((ord(i)+n-ord('A'))%26 + ord('A'))
    
    return answer