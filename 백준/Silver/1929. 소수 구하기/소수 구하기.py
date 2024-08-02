import math

m, n = map(int, input().split())
end = int(math.sqrt(n))
ans = [True] * (n + 1)

for i in range(2, end + 1):
  if ans[i]:
    j = i ** 2
    while j <= n:
      ans[j] = False
      j += i

for i in range(max(m, 2), n + 1):
  if ans[i]:
    print(i)