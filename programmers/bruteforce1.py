from itertools import permutations

def solution(numbers):
    answer = 0
    arr = []
    for i in range(1,len(numbers)+1):
        arr += list(permutations(numbers, i))
      
    nums = set([int(''.join(i)) for i in arr])
  
    answer = len(nums)
  
    for k in nums:
        if k < 2:
            answer -= 1
          
        for l in range(2, k//2 + 1):
            if k%l == 0:
                answer -= 1
                break
              
    return answer