N, K = map(int,input().split())

total = K*(K+1) // 2

if N < total : 
  print(-1)
elif (N - total) % K == 0:
  print(K-1)
else:
  print(K)
