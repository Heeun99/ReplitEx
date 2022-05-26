def solution(answers):
    supo1 = [1,2,3,4,5]
    supo2 = [2,1,2,3,2,4,2,5]
    supo3 = [3,3,1,1,2,2,4,4,5,5]
    count = [0,0,0]
    answer = []
    for i in range(len(answers)):
        if answers[i] == supo1[i%len(supo1)]:
            count[0] += 1
            
        if answers[i] == supo2[i%len(supo2)]:
            count[1] += 1
        
        if answers[i] == supo3[i%len(supo3)]:
            count[2] += 1
    
    mxcnt = max(count)
    
    for j in range(len(count)):
        if count[j] == mxcnt:
            answer.append(j+1)
            
    return answer

###외워서 해보는 lambda###
#  result = list(filter(lambda x: count[x] == max(count),range(len(count))))
# ##lambda와 filter 함수 이해가 필요한,,,
#