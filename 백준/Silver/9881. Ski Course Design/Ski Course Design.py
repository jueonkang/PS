
N = int(input())
h = [int(input()) for i in range(N)]

min_cost = float("inf")

for low in range(0,84): #i --> min_h
  high = low+17
  cost = 0

  for j in h:
    if j < low:
      cost += (low-j) ** 2
    elif j > high:
      cost += (j - high) ** 2

  if cost < min_cost:
    min_cost = cost

print(min_cost)
    
      
      
  
  
  
  
  