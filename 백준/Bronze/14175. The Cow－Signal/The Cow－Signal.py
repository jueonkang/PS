M, N, K = map(int,input().split())
for i in range(M):
  a = input()
  for j in range(K): 
    for k in range(N):
      print(a[k]*K, end = "" )   
    print()

  