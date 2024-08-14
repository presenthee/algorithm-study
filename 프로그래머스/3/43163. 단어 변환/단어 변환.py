from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [ False ] * len(words)
    q = deque()
    q.append((begin, 0))
    
    while q:
        curr, d = q.popleft()
        if curr == target:
            answer = d
            break
        
        for j in range(len(words)):
            count = 0
            word = words[j]
            for i in range(len(begin)):
                count += 0 if word[i] == curr[i] else 1
                if count > 1:
                    break
            if count != 1 or visited[j]:
                continue
            visited[j] = True
            q.append((word, d + 1))
            
    
    return answer