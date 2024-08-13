N,K = map(int,input().split())
lst = []


for i in range(N):
  a = int(input())
  lst.append(a)

lst.sort()
max_ = 0

for i in range(N):
  current = 0
  for j in range(i,N):
    if lst[j] - lst[i] <= K:
      current += 1
  max_ = max(max_,current)

print(max_)
    