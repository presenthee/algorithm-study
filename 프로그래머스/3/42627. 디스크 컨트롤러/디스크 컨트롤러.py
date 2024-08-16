import heapq

def solution(jobs):
    num = len(jobs)
    answer = 0
    reqs = [] # heap
    jobs.sort()
    time = 0
    
    while jobs or reqs:
        idx = -1
        for i in range(len(jobs)):
            j = jobs[i]
            t, spend = j
            if t <= time:
                heapq.heappush(reqs, (spend, t))
                idx = i
            else:
                break
        if idx >= 0:
            jobs = jobs[idx+1:]
        if reqs:
            spend, t = heapq.heappop(reqs)
            answer += time - t + spend
            time += spend
        else:
            time += 1
    
    return answer // num