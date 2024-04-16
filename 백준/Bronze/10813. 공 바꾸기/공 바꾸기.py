N,M = map(int,input().split())
basket = []
for i in range(N):
  basket.append(i+1)

for b in range(M):
  i,j = map(int,input().split())
  tmp = basket[i-1]
  basket[i-1] = basket[j-1]
  basket[j-1] = tmp

for i in basket:
  print(i,end=" ")