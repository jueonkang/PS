N, K = map(int,input().split())
L = []

for i in range(N):
  A = int(input())
  L.append(A)

L.sort(reverse = True)
count = 0

for i in range(N):
  count += K//L[i]
  K %= L[i]

print(count)
  