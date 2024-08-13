def solution(N, number):
    answer = -1
    digit = str(N)
    dp = [ set([int(digit * (x + 1))]) for x in range(8) ]
    
    for i in range(8):
        for j in range(i):
            for a in dp[j]:
                  for b in dp[i - j - 1]:
                        dp[i].add(a + b)
                        dp[i].add(a * b)
                        dp[i].add(a - b)
                        if b != 0:
                            dp[i].add(a // b)
            
        if number in dp[i]:
                  answer = i + 1
                  return answer
                    
    
    return answer