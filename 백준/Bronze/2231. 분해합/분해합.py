def sum(i) : 
  ans = 0 
  while True:
    b = i%10
    i = i//10
    ans += b
    if i == 0:
      break
  return(ans)



def get(a) : 

  for i in range(1,a+1):
    if i + sum(i) == a : 
      return i 

  return 0
  
a = int(input())
print(get(a))