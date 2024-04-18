N = int(input())
Score = list(map(int,input().split()))
M= 0

for i in range(N):
  if M < Score[i]:
    M = Score[i]

for i in range(N):
  Score[i] = Score[i] / M*100

total = 0
for i in range(N):
  total += Score[i]

b = total/N
print(b)