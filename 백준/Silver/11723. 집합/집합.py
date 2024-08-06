import sys

input = sys.stdin.readline

n = int(input())
s = 0

for i in range(n):
  comp = input().split()
  op = comp[0]
  if op == "add":
    x = int(comp[1])
    s |= (1 << x)
  elif op == "remove":
    x = int(comp[1])
    s &= ~(1 << x)
  elif op == "check":
    x = int(comp[1])
    if s & (1 << x):
      print(1)
    else:
      print(0)
  elif op == "toggle":
    x = int(comp[1])
    mask = 1 << x
    s ^= mask
  elif op == "all":
    s = ~0
  elif op == "empty":
    s = 0
  else:
    print("error")

