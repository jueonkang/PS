N = int(input())
total = 0
cows = [-1]*11

for i in range(N):
  A, B = map(int,input().split())
  if cows[A] == -1 : 
    cows[A] =B
  else : 
    if cows[A] != B:
      cows[A] = B
      total += 1

print(total)
