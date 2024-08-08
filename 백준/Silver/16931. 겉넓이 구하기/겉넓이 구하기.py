import sys

input = sys.stdin.readline

N, M = map(int, input().split())

sq = [ list(map(int, input().split())) for _ in range(N) ]
diff = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = N * M * 2

for i in range(N):
  for j in range(M):
    x = sq[i][j]
    for d in diff:
      a, b = d
      ni = i + a
      nj = j + b
      if ni < 0 or nj < 0 or ni >= N or nj >= M:
        ans += x
        continue
      nx = sq[ni][nj]
      if nx > x:
        continue
      ans += (x - nx) if nx < x else 0

print(ans)
