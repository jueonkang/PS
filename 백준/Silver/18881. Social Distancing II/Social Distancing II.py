def maxR():
  r = float("inf")
  for i in healthy : 
    for j in sick : 
      if abs(i-j) < r : 
        r = abs(i-j)

  return r-1
  
N = int(input())
healthy = []
sick = [] 

for i in range(N):
  x,s = map(int,input().split())
  if s == 0:
    healthy.append(x)
  else:
    sick.append(x)


r = maxR() 
ans = 1 
sick.sort() 
for i in range(len(sick)-1) : 
  if sick[i+1] - sick[i] > r:
    ans += 1

print(ans)
    