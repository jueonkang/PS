N,M = map(int,input().split())
grid = [ input() for _ in range(N) ]
dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,-1,-1,-1,0,1,1,1]

count = {}

for i in range(N): 
  for j in range(M) : 
    for k in range(8) : 
      if (0 <= i + dy[k] * 2 < N) and ( 0<= j +dx[k]*2 < M) :
        if grid[i][j] != "M" and grid[i][j] != grid[i+dy[k]][j+dx[k]] == grid[i+dy[k]*2][j+dx[k]*2] != "O" : 
          target = grid[i][j] + grid[i+dy[k]][j+dx[k]] + grid[i+dy[k]*2][j+dx[k]*2]
          count[target] = count.get(target,0) + 1 

if len(count) > 0 : print( max(count.values()) )  
else: print(0)