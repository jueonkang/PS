
from itertools import combinations

N, M = map(int,input().split())
cows = []
for _ in range(N):
  s, t, c = map(int,input().split())
  cows.append((s,t,c))

aircon = []
for _ in range(M):
  ai, bi, pi, mi = map(int,input().split())
  aircon.append((ai,bi,pi,mi))

mincost = float("inf")


for i in range(2**M):
  cooling = [0]*101
  cost = 0
  
  for j in range(M):
    if (i//(2**j)) %2 == 1:
      a, b, p, m = aircon[j]
      cost+=m
      for k in range(a,b+1):
        cooling[k] += p

  T= True
  for s,t,c in cows:
    require = True
    for l in range(s,t+1):
      if cooling[l] < c:
        require = False
        break

    if not require:
      T = False
      break

  if T == True:
    mincost = min(mincost, cost)

print(mincost)