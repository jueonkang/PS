
n = int(input())
time = []
for i in range(n) : 
  start,end = map(int,input().split())
  time.append((start,end))


time.sort(key=lambda x:(x[1], x[0]))

ans = 1
end = time[0][1]

for a, b in time[1:]:
    if a >= end:
        ans += 1
        end = b
      
print(ans)