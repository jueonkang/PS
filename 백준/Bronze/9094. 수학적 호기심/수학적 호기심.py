T = int(input())
for i in range(T):
  N, M = map(int,input().split())
  answer = 0
  for a in range(1, N):
    for b in range(1, N):
      if a<b and (a**2+b**2+M)%(a*b) == 0:
        answer += 1
  print(answer)