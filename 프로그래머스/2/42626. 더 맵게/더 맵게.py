import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        m = heapq.heappop(scoville)
        if (m >= K):
            break
        if not scoville:
            return -1
        n = heapq.heappop(scoville)
        if (m == 0 and n == 0):
            return -1
        answer += 1
        heapq.heappush(scoville, m + n * 2)
    
    return answer