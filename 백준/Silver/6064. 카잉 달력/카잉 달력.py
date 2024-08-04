import sys

input = sys.stdin.readline

num_case = int(input())

def gcd(a, b):
  while b > 0:
    r = a % b
    a = b
    b = r
  return a


for i in range(num_case):
  M, N, x, y = map(int, input().split())

  lcm = M * N // gcd(M, N)
  rem_m = 0 if M == x else x
  rem_n = 0 if N == y else y
  ans = x

  while True:
    if ans > lcm:
      print(-1)
      break
    if ans % N == rem_n:
      print(ans)
      break
    ans += M
