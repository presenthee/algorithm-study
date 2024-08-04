import sys

input = sys.stdin.readline

N, M = map(int, input().split())

def find(ans, n):
  if n == M:
    print(*ans)
  else:
    s = 1 if not ans else ans[-1]
    for i in range(s, N + 1):
      find(ans + [i], n + 1)

find([], 0)
