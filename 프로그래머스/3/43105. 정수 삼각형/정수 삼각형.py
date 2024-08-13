def solution(triangle):
    answer = 0
    l = len(triangle)
    for i in range(1, l):
        arr = triangle[i]
        for j in range(len(arr)):
            a = triangle[i - 1][j - 1] if j > 0 else -1
            b = triangle[i - 1][j] if j < len(arr) - 1 else -1
            arr[j] = arr[j] + max(a, b)
    
    return max(triangle[-1])