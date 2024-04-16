N,M = map(int,input().split())
basket = [0] * N
for a in range(M):
  i,j,k = map(int,input().split())
  for b in range(i-1,j):
    basket[b] = k

for i in basket:
  print(i,end=" ")
