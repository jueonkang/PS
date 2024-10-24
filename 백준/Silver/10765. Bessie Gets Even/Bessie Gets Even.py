N = int(input())
variable = {"B": [0,0], "E": [0,0], "S": [0,0], "I":[0,0], "G":[0,0], "O":[0,0], "M":[0,0]}

for i in range(N):
  v, value = input().split()
  value = int(value)
  variable[v][value%2] += 1
  
count = 0
for B in range(2) : # B --> 0 짝수 , 1 --> 홀수 
  for E in range(2):
    for S in range(2):
      for I in range(2):
        for G in range(2):
          for O in range(2):
            for M in range(2):

              if ((B+E+S+S+I+E)*(G+O+E+S)*(M+O+O)) % 2 == 0:
                count += variable["B"][B] * variable["E"][E] * variable["S"][S]*variable["I"][I]*variable["G"][G]*variable["O"][O]*variable["M"][M]


print(count)
      
  