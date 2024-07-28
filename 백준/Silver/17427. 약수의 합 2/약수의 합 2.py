n = int(input())
ans = n
threshold = n // 2

for i in range(2, n + 1):
  if i > threshold:
    ans += i
  else:
    ans += (n // i) * i

print(ans)
