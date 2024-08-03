import sys

input = sys.stdin.readline

num_case = int(input())
inputs = []
m = 0

for i in range(num_case):
  n = int(input())
  inputs.append(n)
  m = max(m, n)

ans = [1, 1, 2, 4] + [0] * m

for i in range(4, m + 1):
  ans[i] = ans[i - 1] + ans[i - 2] + ans[i - 3]

for i in range(num_case):
  print(ans[inputs[i]])
