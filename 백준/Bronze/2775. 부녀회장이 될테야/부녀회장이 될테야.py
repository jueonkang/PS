t = int(input())

p_nums = [] 

for i in range(15): 
  p_nums.append( [0] * 15 )

for i in range(15):
  p_nums[0][i] = i

for i in range(1,15):
  for j in range(1,15): 
    for k in range(1,j+1) :
      p_nums[i][j] += p_nums[i-1][k]

for i in range(t): 
  k = int(input())
  n = int(input())
  print(p_nums[k][n])