import math 

def solution(brown, yellow):
    answer = []
    end = int(math.sqrt(yellow))
    for h in range(1, end + 1):
        if yellow % h != 0:
            continue
        w = yellow // h
        if (w + 2) * (h + 2) - yellow == brown:
            answer.append(w+2)
            answer.append(h+2)
            break
    return answer