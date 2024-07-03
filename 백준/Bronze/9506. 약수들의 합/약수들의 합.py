lst = []

while True: 
  a = int(input())
  if a != -1 :
    lst.append(a)
  else:
    break



for i in range(len(lst)):
  factor = []
  for j in range(1,lst[i]): 
    if lst[i] % j == 0:
      factor.append(j)
  if sum(factor) == lst[i] :
    print(lst[i] ,"= ", end= "")
    for k in range(len(factor)-1):
      print(factor[k], "+ ",end = "")
    print(factor[-1])
  else:
    print(lst[i], "is NOT perfect.")