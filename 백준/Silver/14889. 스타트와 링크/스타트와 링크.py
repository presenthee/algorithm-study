import sys

input = sys.stdin.readline

N = int(input())
num = N // 2
mat = [list(map(int, input().split())) for _ in range(N)]

ans = sys.maxsize


def find_ans(start, link, rem):
  global ans
  if len(start) > num or len(link) > num:
    return

  if rem == 0:
    cal = 0
    for i in start:
      for j in start:
        if i != j:
          cal += mat[i][j]

    for i in link:
      for j in link:
        if i != j:
          cal -= mat[i][j]

    ans = min(abs(cal), ans)
    return

  find_ans(start + [N - rem], link, rem - 1)
  find_ans(start, link + [N - rem], rem - 1)

find_ans([], [], N)
print(ans)
