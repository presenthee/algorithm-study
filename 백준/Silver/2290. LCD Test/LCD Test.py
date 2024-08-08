import sys

input = sys.stdin.readline

s, n = input().split()
s = int(s)
h, v = '-', '|'


def save_ans(num):
  ans = [[' '] * (s + 2) for _ in range(2*s + 3)]

  if num in '23567890':
    ans[0][1:-1] = [h] * s
  if num in '12347890':
    for i in range(1, s+1):
      ans[i][-1] = v
  if num in '134567890':
    for i in range(s+2, 2*s + 2):
      ans[i][-1] = v
  if num in '2356890':
    ans[2*s + 2][1:-1] = [h] * s
  if num in '2680':
    for i in range(s+2, 2*s + 2):
      ans[i][0] = v
  if num in '456890':
    for i in range(1, s + 1):
      ans[i][0] = v
  if num in '2345689':
    ans[s + 1][1:-1] = [h] * s

  return ans

ans = [ save_ans(n[i]) for i in range(len(n)) ]

for l in zip(*ans):
  for w in l:
    print(''.join(w), end=' ')
  print()
