import sys 



N,Q = map(int,sys.stdin.readline().split())
FJclose = list(map(int,sys.stdin.readline().split()))
bessie = list(map(int,sys.stdin.readline().split()))

diff = ([FJclose[i] - bessie[i] for i in range(N)])
diff.sort(reverse= True)

for _ in range(Q):
  V,S = map(int,sys.stdin.readline().split())
  print("YES" if diff[V-1] > S else "NO")
  
  