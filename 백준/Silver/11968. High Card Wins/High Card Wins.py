
N = int(input())
ecard = [int(input()) for _ in range(N)]

totalcard = set(range(1,2*N+1))
bcard = sorted(totalcard-set(ecard))
ecard.sort()

bindex = 0
eindex = 0
ans = 0

while bindex < N and eindex < N : 
  if bcard[bindex] < ecard[eindex] : 
    bindex += 1
  else : 
    eindex += 1
    bindex += 1
    ans +=1 

print(ans)