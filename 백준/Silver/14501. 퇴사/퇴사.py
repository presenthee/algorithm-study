import sys

input = sys.stdin.readline
N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]
ans = 0

def search(cost, curr):
  global schedule, ans
  if curr >= N:
    ans = max(cost, ans)
    return

  T, P = schedule[curr]

  if curr + T <= N:
    search(cost + P, curr + T)
  search(cost, curr + 1)

search(0, 0)
print(ans)
