N, M = map(int,input().split())
a = []
b=[]
d = [0] * 100

last = 0 
for i in range(N):
  road,speed = map(int,input().split())
  for j in range(road):
    d[last] = speed
    last += 1 


last = 0 
ans = 0 
for i in range(M):
  road,speed = map(int,input().split())
  for j in range(road):
    ans = max( ans , speed -  d[last] ) 
    last += 1 

print(ans)


