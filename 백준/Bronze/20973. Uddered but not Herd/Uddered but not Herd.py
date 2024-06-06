a = input()
b = input()
count = 1
pre_idx = -1
curr_idx = -1

for i in range(1,len(b)):
  pre = b[i-1]  # m  / o / o  
  curr = b[i] # o / o / d 
  for j in range(26):
    if pre == a[j]:
      pre_idx = j 

    if curr == a[j] : 
      curr_idx = j 
      
  if pre_idx >= curr_idx :   
    count += 1
  
print(count) 
