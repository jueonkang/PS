X, Y, M = map(int,input().split())

max = 0
for i in range(1000):
  for j in range(1000):
    if (X*i + Y*j) <= M and X*i + Y*j > max:
      max = X*i + Y*j

print(max)