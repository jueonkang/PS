n = int(input())
dictio = {"Bessie" : 0 , "Elsie" : 0, "Daisy" :0, "Gertie" :0, "Annabelle" : 0, "Maggie" :0, "Henrietta":0}

for i in range(n):
    a,b = input().split()
    dictio[a] += int(b)

min = float("inf")
for i in dictio : 
    if dictio[i] < min : 
        min = dictio[i]
    
ans = float("inf")
lst=[]
for i in dictio:
    if min < dictio[i] < ans:
        ans = dictio[i]
        lst = [i]
    elif dictio[i] == ans: 
        lst.append(i)

if len(lst) > 1 or len(lst) == 0 : 
    print("Tie")
else :  
    print(lst[0])