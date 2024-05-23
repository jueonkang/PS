

t = []
max = 0
idx = 0 
for i in range(5):
    score = list(map(int, input().split()))
    total = 0 
    for j in range(4):
      total += score[j]
    
    if total > max:
      max = total
      idx = i+1
      
print(idx,max)

