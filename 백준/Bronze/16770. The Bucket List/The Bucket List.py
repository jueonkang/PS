N = int(input())
total_bucket = [0] * 1001 


for i in range(N):
  s, t, b = map(int,input().split())
  for j in range(s,t+1):
    total_bucket[j] += b

print(max(total_bucket))