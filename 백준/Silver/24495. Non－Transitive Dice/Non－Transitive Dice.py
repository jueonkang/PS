def beat(d1,d2):
  count1 = 0
  count2 = 0
  for i in d1:
    for j in d2:
      if i>j:
        count1 += 1
      elif i<j:
        count2 += 1
  return count1 > count2 


def check(A,B) : 
  for i in range(1,11):
    for j in range(1,11):
      for k in range(1,11):
        for l in range(1,11):
          C = [i,j,k,l]
          if beat(B,C) and beat(C,A):
            return True 
  return False 

t = int(input())
for i in range(t):
  num = list(map(int,input().split()))
  A = num[:4]
  B = num[4:]
  if beat(A,B) : 
    res = check(A,B) 
  else : 
    res = check(B,A)

  if res  : 
    print("yes")
  else : 
    print("no")