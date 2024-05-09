
N,K,P = map(int,input().split()) 
bread = [0] + list(map(int, input().split()))
ans = 0 

for i in range(N):
  b = 0 
  for j in range(1,K+1):
    b += bread[i*K + j]

  if b > K-P: 
    ans += 1 

print(ans) 
  
