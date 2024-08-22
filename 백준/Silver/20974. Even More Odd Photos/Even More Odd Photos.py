N = int(input())
a = list(map(int,input().split()))

odd,even = 0,0 

for i in range(N):
  if a[i] % 2 == 0:
    even += 1
  else:
    odd += 1


while odd > even : 
  even += 1 
  odd -= 2 

if odd < even  :
  print( odd * 2 + 1 )

else : 
  print(even + odd)

