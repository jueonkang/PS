def isPrime(n) :  # prime --> true / false 
  if n == 1 : 
    return False
  for i in range(2,n):
    if n%i == 0:
      return False 
  return True 


N = int(input())
a = list(map(int,input().split()))
Prime = 0

for i in range(N) : 
   if (isPrime(a[i]))  : 
     Prime += 1 

print(Prime)
      