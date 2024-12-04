N = input()
behind = 0
front = 0

for i in range(len(N)-1):
  if N[i] == "(" and N[i+1] == "(":
    behind += 1
  if N[i] == ")" and N[i+1] == ")":
    front += behind

print(front)
  
    
