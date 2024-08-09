import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
h = max(trees) // 2

def is_possible(len):
  return M <= sum(map(lambda x: 0 if x <= len else x - len, trees))

low = 0
high = max(trees) - 1
while low + 1 < high:
  mid = (low + high) // 2
  if is_possible(mid):
    low = mid
  else:
    high = mid

if is_possible(high):
  print(high)
else:
  print(low)