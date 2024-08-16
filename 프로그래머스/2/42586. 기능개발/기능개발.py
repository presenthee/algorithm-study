from collections import deque

def solution(progresses, speeds):
    answer = []
    que = deque()
    for i in range(len(progresses)):
        p = progresses[i]
        s = speeds[i]
        r_days = (100 - p) if s == 1 else (100 - p + s) // s 
        
        if que and que[0] < r_days:
            num = 0
            while que:
                que.pop()
                num += 1
            if num > 0:
                answer.append(num)
                
        que.append(r_days)
        
    if que:
        print(que)
        answer.append(len(que))
    
    return answer