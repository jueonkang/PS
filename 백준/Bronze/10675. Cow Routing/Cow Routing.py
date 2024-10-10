A, B, N = map(int,input().split())
ans = 1001
for i in range(N):
  c, r = map(int,input().split())
  route = list(map(int,input().split()))
  start = False  # A가 나왔다.
  end = False # B가 나왔다. False --> 안 나왔다.
  for j in range(r) : 
    if route[j] == A : 
      start = True
    if start == True and route[j] == B:
      end = True
      
  if start == True and end == True:
    if c < ans :
      ans = c 

if ans == 1001:
  print(-1)
else:
  print(ans)
