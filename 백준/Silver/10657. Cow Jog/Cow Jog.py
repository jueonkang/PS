N = int(input())
lst = []
for i in range(N):
  p, s = map(int,input().split())
  lst.append((p, s))

group = 0
mins = float("inf")

for i in range(N-1, -1, -1):
  p, s = lst[i]
  if s <= mins:
    group += 1
    mins = s

print(group)
