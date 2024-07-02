
d = {"Poblano" : 1500,"Mirasol" : 6000, "Serrano" : 15500 , "Cayenne" : 40000, "Thai" : 75000, "Habanero" : 125000 } 




total = int(input())
answer = 0

for i in range(total):
  pepper = input()
  answer += d[pepper]
print(answer)
