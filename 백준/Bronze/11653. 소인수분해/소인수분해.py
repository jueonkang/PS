N = int(input())

for i in range(2,N+1):
  while N%i == 0:
    N = N/i
    print(i)
