N, S = map(int,input().split())
lst = []

for i in range(N):
  q,v = map(int,input().split())
  lst.append((q,v))

currentp = S-1
power = 1
direction = 1
brokent = set()

for i in range(1000000):
  if currentp < 0 or currentp > N : break 
  q,v = lst[currentp]
  if q == 1:
    if power >= v:
      brokent.add(currentp)
  elif q == 0:
    power +=v
    direction *= -1
    
  currentp += power*direction

print(len(brokent))

  
  
  
  