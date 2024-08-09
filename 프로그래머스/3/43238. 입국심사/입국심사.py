def is_possible(n, total, times):
    return n <= sum(map(lambda x: total // x, times))

def solution(n, times):
    answer = 0
    low = 1
    high = max(times) * n
    while low + 1 < high:
        mid = (low + high) // 2
        if is_possible(n, mid, times):
            high = mid
        else:
            low = mid
            
    answer = low if is_possible(n, low, times) else high
    return answer 