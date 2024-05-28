
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
a = [[0,0,0,0,0,0],[0,0,0,0,0,0]]
room_total = 0

for i in range(N):
  S, Y = map(int,input().split())
  a[S][Y-1] += 1

for i in a:
  for j in i:
    if j%K == 0:
      room_total += j//K
    else:
      room_total += (j//K) + 1
print(room_total)
    
