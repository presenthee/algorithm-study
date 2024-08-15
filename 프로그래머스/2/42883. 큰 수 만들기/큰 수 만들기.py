from collections import deque

def solution(number, k):
    number = list(number)
    stack = deque([number[0]])
    for i in range(1, len(number)):
        while stack and k > 0 and stack[-1] < number[i]:
            stack.pop()
            k -= 1
        stack.append(number[i])
    
    while k > 0:
        stack.pop()
        k -= 1
        
    return ''.join(list(stack))