import math
import sys

input = sys.stdin.readline

cases = []
m = 999997
primes = [True] * (m + 1)
end = int(math.sqrt(m))

for i in range(2, end + 1):
  if primes[i]:
    j = i ** 2
    while j <= m:
      primes[j] = False
      j += i

n_primes = list(filter(lambda x: primes[x], range(m + 1)))


while True:
  n = int(input())
  if (n == 0):
    break

  a = 0
  b = 0
  for i in range(3, len(n_primes)):
    a = n_primes[i]
    b = n - a
    if b < 3 or primes[b]:
      break

  if primes[b]:
    print(f"{n} = {a} + {b}")
  else:
    print("Goldbach's conjecture is wrong.")
