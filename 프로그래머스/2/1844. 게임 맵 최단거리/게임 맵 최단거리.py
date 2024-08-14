from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    next = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [ [ False ] * m for _ in range(n) ]
    q = deque()
    q.append((0, 0, 1))
    visited[0][0] = True
    while q:
        a, b, d = q.popleft()
        if (a == n-1 and b == m-1):
            answer = d
            break
        
        for da, db in next:
            n_a = a + da
            n_b = b + db
            if n_a < 0 or n_a > n - 1 or n_b < 0 or n_b > m - 1:
                continue
            if visited[n_a][n_b] or maps[n_a][n_b] == 0:
                continue
            visited[n_a][n_b] = True
            q.append((n_a, n_b, d + 1))
        
    return answer if answer > 0 else -1