N = int(input())
lifeguards = [0]*1000
work = [] 
for j in range(N):
    start, end = map(int, input().split())
    work.append((start, end))
    for i in range(start, end):
        lifeguards[i] += 1

ans = 0
for i in work:
    start, end = i[0], i[1]
    for j in range(start, end): 
        lifeguards[j] -= 1
    time = 0    
    for lifeguard in lifeguards:
        if lifeguard > 0:        
            time += 1
    ans = max(time, ans)
    for k in range(start, end): 
        lifeguards[k] += 1  

print(ans)