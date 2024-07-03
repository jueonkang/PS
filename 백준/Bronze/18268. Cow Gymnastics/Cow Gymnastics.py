K, N = map(int,input().split())
ranking = [ list(map(int,input().split())) for i in range(K) ]

answer = 0

for i in range(1,N+1): 
  for j in range(1,N+1):
    if i != j:
      i_better = True
      for k in range(K):
        c1,c2 = -1,-1 
        for l in range(N) :
          if ranking[k][l]  == i : 
            c1 = l
          elif ranking[k][l]  == j : 
            c2 = l
        if c1 < c2 : 
          i_better = False 
      if i_better :  answer += 1 

print(answer)