def solution(name):
    l = len(name)
    answer = 0
    for c in name:
        diff = ord(c) - ord('A')
        answer += min(diff, 26 - diff)
    
    move = l - 1
    for i in range(l):
        next = i + 1
        while next < l and name[next] == 'A':
            next += 1
        dist = min(l - next, i)
        move = min(move, dist + i + l - next)
    
    return answer + move