airport = {}
ts = []
used = []
answer = []

def dfs(curr, route, target):
    global answer
    global used
    global ts
    global airport
    if len(route) == target:
        answer.append(route)
        return
    
    start, end = curr
    
    if end not in airport:
        return
    
    for idx in airport[end]:
        if used[idx]:
            continue
        start, end = ts[idx]
        used[idx] = True
        n_route = route[:]
        n_route.append(end)
        dfs(ts[idx], n_route, target)
        used[idx] = False
    

def solution(tickets):
    global airport
    global used
    global ts
    global answer 
    ts = tickets
    num = len(tickets)
    for i in range(num):
        start, end = tickets[i]
        if start in airport:
            l = airport.get(start)
            l.append(i)
        else:
            airport[start] = [i]
            
    used = [ False ] * num
    
    for i in range(num):
        start = tickets[i][0]
        if start != "ICN":
            continue
        used[i] = True
        dfs(tickets[i], tickets[i], num + 1)
        used[i] = False
    
    answer.sort()
        
    return answer[0]