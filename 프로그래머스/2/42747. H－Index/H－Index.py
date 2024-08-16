def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    l = len(citations)
    for i in range(l):
        if (i + 1 >= citations[i]):
            answer = max(i, citations[i])
            break
    
    return l if answer == 0 and citations[0] != 0 else answer