import math
cans = set()

def dfs(curr, numbers):
    global cans
    for n in numbers:
        n1 = curr[:]+n
        c1 = int(n1)
        n2 = n+curr[:]
        c2 = int(n2)
        if not c1 in cans:
            numbers1 = numbers[:]
            numbers1.remove(n)
            cans.add(c1)
            dfs(n1, numbers1)
        if not c2 in cans or n == '0':
            numbers2 = numbers[:]
            numbers2.remove(n)
            cans.add(c2)
            dfs(n2, numbers2)    

def solution(numbers):
    global visited
    global cans
    answer = 0
    numbers = list(numbers)
        
    dfs("", numbers)
    
    n = max(cans)
    end = int(math.sqrt(n))
    is_prime = [ True ] * (n + 1)
    
    for i in range(2, end + 1):
        if is_prime[i]:
            j = i ** 2
            while j <= n:
                is_prime[j] = False
                j += i
    
    answer = sum([ x > 1 and is_prime[x] for x in cans ])
    return answer