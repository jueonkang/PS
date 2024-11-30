n,m = map(int,input().split())
bessie = []
elsie = []

for i in range(n) : 
  speed,time = map(int,input().split())
  for t in range(time) : 
    bessie.append(speed)

for i in range(m) : 
  speed,time = map(int,input().split())
  for t in range(time) : 
    elsie.append(speed)

bessies = 0
elsies = 0
leader = -1
ans = 0 

for i in range(len(bessie)):
  bessies += bessie[i]
  elsies += elsie[i]
  if bessies > elsies :
    tmp = True 
  else : 
    tmp = False 

  if leader == - 1 : 
    leader = tmp 

  elif tmp != leader : 
    ans += 1
    leader = tmp 
    
print(ans)