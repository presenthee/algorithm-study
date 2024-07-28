def find_ans(n):
    i = 1
    ans = 1
    while True:
        ans %= n
        if ans == 0:
          return i
        else:
          ans = 1 + (ans * 10)
          i += 1

while True:
    try:
      n = int(input())
      print(find_ans(n))
    except:
        break