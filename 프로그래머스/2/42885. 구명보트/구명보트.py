from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    
    while people:
        if len(people) == 1:
            answer += 1
            break
        mx = people[-1]
        mn = people[0]
        if (mx + mn <= limit):
            people.popleft()
            answer += 1
        else:
            answer += 1
        people.pop()
    
    return answer