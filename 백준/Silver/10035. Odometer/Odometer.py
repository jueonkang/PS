X,Y= map(int,input().split())

def interesting(n):
  num = int("".join(n)) 
  if X <= num <= Y and n[0] != "0":
        return True
  return False

ans = 0 

for i in range(3,18) :
  for j in range(10) : 
    tmp = [str(j)] * i 
    for k in range(10) : 
      if j == k : continue
      for l in range(i) :
        tmp[l] = str(k)
        if interesting(tmp) : ans += 1 
        tmp[l] = str(j)

print(ans)