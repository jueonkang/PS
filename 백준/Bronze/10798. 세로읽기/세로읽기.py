words = [] 

for i in range(5):
  words.append([""] * 15)

for i in range(5):
  a = input() 
  for j in range(len(a)) : 
    words[i][j] += a[j]


for i in range(15) : 
  for j in range(5): 
    print(words[j][i], end= "")