n = int(input())
L = []

for i in range(n):
  x = list(map(int,input().split()))
  L.append(x)

L.sort(key = lambda x : (x[1], x[0]))

for i in range(n):
  print(L[i][0], L[i][1])
  
  
  




