N, K = map(int,input().split())
days = list(map(int,input().split()))

total = K+1


for i in range(1,N):
  a = days[i]-days[i-1]
  if a <= K:
    total += a
  else:
    total += K+1
print(total)
  