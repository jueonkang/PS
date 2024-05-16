
n = int(input())
L = []

for i in range(n):
  x = list(map(int,input().split()))
  L.append(x)

L.sort()

for i in range(n):
  print(L[i][0], L[i][1])
  
  
  

