import sys

input = sys.stdin.readline

n = int(input())
c = [list(input()) for _ in range(n)]
ans = 0

def update():
  global ans
  for i in range(n):
    cur = c[i][0]
    count = 0
    for j in range(n):
      if cur == c[i][j]:
        count += 1
      else:
        ans = max(ans, count)
        count = 1
        cur = c[i][j]
    ans = max(ans, count)

  for i in range(n):
    cur = c[0][i]
    count = 0
    for j in range(n):
      if cur == c[j][i]:
        count += 1
      else:
        ans = max(ans, count)
        count = 1
        cur = c[j][i]
    ans = max(ans, count)

# i = 행 j = 열
for i in range(n):
  for j in range(n):
    if i != (n-1) and c[i][j] != c[i+1][j]:
      c[i][j], c[i+1][j] = c[i+1][j], c[i][j]
      update()
      c[i][j], c[i+1][j] = c[i+1][j], c[i][j]

    if j != (n-1) and c[i][j] != c[i][j+1]:
      c[i][j], c[i][j+1] = c[i][j+1], c[i][j]
      update()
      c[i][j], c[i][j+1] = c[i][j+1], c[i][j]

print(ans)
