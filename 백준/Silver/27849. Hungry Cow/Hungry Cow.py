N, T = map(int,input().split())
days = []

for _ in range(N):
  day, amount = map(int,input().split())
  days.append((day,amount))

ans = 0
hay = 0

for i in range(N):
  currentday, totalhay= days[i]
  if i+1 < N:
    nextday = days[i+1][0]
  else:
    nextday = T+1
    
  hay+= totalhay

  eat = min(nextday-currentday, hay)

  ans += eat
  hay -= eat

print(ans)
  