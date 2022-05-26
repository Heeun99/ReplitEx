def solution(citations):
    n = len(citations)
    
    citations.sort(reverse=True)
    answer = 0
#내림차순 반복문을 쓴다 최대값 나오면 바로 Break 하기 위해
#리스트 컴프리헨션 활용한다
#len함수를 이용해 특정 논문 인용수 보다 많은 논문의 개수 카운트
#if문을 이용해서 i보다 크거나 같으면 답으로 하고 break로 for문을 나온다
    for i in range(len(citations),-1,-1):
        if(len([j for j in citations if j>=i])>=i):
            answer = i
            break
    
    return answer
####완전 신기한 다른사람풀이 진짜 고인물 풀이####
# 내림차순 정렬을 함
# citations.sort(reverse=True)
#
# enumerate를 이용해서 내림차순 정렬된 리스트에 인덱스 부여
# min(인덱스,값)에서 최소값을 구해서 그 부분을 min값들만 리스트부여
# 그 중 최댓값을 답으로 선정함
# answer = max(map(min,enumerate(citations,start=1))