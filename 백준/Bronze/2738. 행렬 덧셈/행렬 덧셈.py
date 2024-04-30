N, M = map(int,input().split())
A, B = [], []

for i in range(N):
  a = list(map(int,input().split()))
  A.append(a)

for i in range(N):
  b = list(map(int,input().split()))
  B.append(b)


for i in range(N) : 
  for j in range(M) : 
    A[i][j] += B[i][j]


for i in range(N):
  print(*A[i])
  