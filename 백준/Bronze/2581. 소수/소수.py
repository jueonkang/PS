def isPrime(n) :
  for i in range(2,n):
    if n % i == 0:
      return False 
  return n > 1 
 
  
M = int(input())
N = int(input())

total = 0
minimum = 0 
for i in range(M,N+1):
  if isPrime(i) :
    total += i
    if minimum == 0 : 
      minimum = i 
if total == 0:
  print(-1)
else:
  print(total)
  print(minimum)
