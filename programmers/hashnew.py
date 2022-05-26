def solution(participant, completion):
    answer = ''
    participant.sort() #문자열도 abc순으로 정렬이 가능함
    completion.sort() 
  
    answer = participant[-1] # 동명이인인 경우 마지막으로 남는 사람
  
  #참가자 목록과 완주자 목록을 하나씩 비교하는 for구문
  #다르면 참가자 목록에서 완주하지 못한 사람 = answer
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
        
    return answer