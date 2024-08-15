def solution(n, lost, reserve):
    answer = 0
    for p in reserve.copy():
        if p in lost.copy():
            lost.remove(p)
            reserve.remove(p)
            
    answer = n - len(lost)
    lost.sort()
    print(lost)
    print(reserve)
    for i in lost:
        if (i > 1 and i - 1 in reserve):
            reserve.remove(i - 1)
            answer += 1
            continue
        if (i < n and i + 1 in reserve):
            reserve.remove(i + 1)
            answer += 1
            continue
            
    return answer