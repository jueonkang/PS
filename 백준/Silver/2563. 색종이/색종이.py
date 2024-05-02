white = []

for i in range(100):
  white.append( [0] * 100 )

a = int(input())
for i in range(a):
  b, c = map(int,input().split())
  for j in range(b,b+10):
    for k in range(c,c+10):
      white[j][k] = 1

ans = 0 

for i in range(100) : 
  for j in range(100): 
    ans += white[i][j]

print(ans)