arr = input().split('-')
a = 0
for i in arr[0].split('+'):
    a += int(i)
for i in arr[1:]:
    tmp = i.split("+") 
    for j in tmp:
        a -= int(j)
print(a)
