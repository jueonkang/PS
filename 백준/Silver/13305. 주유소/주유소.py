
n = int(input())
dist = list(map(int,input().split()))
price = list(map(int,input().split()))

ans = 0
cost = price[0]
for i in range(n-1):
  if cost > price[i]:
    cost = price[i]
  ans += cost * dist[i]

print(ans)