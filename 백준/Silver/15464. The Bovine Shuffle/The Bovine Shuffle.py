N = int(input())
a = [0] + list(map(int,input().split()))
cowid = [0] + list(map(int,input().split()))
reverse = [0] * (N+1)

for i in range(1,N+1): 
  reverse[ a[i] ] = i 

b = cowid.copy()

for i in range(3):
  for j in range(1,N+1) : 
    cowid[reverse[j]] = b[j]
  b = cowid.copy()
    
print(*cowid[1:],sep="\n")  
      