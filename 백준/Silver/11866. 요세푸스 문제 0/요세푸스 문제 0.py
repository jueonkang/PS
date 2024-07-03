from collections import deque


N, K = map(int,input().split())

q = deque()
lst = []

for i in range(1,N+1):
  q.append(i)

while True:
  for i in range(K-1):
    a = q.popleft()
    q.append(a)
  b = q.popleft()
  lst.append(b)
  if len(q) == 0:
    break
    
print("<",end = "")
print(*lst, sep = ", ",end = "")
print(">", end = "")