from collections import deque

def solution(prices):
    l = len(prices)
    answer = [ l - i - 1 for i in range(l) ]
    s = deque([0])
    for i in range(1, len(prices)):
        p = prices[i]    
        while s and prices[s[-1]] > p:
            j = s.pop()
            answer[j] = i - j
        s.append(i)        
    
    return answer