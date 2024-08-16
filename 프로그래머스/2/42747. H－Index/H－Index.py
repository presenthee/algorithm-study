def solution(citations):
    answer = 0
    l = len(citations)
    while l > 0:
        if (sum([ x >= l for x in citations]) >= l):
            return  l
        l -= 1
    
    return l