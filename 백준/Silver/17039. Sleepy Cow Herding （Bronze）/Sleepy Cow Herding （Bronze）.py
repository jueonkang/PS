lst = list(map(int,input().split()))
lst.sort()


min = 0 

diff_bc = lst[2]-lst[1]
diff_ab = lst[1]-lst[0]


if lst[1] -2 == lst[0] or lst[2] - 2 == lst[1]:
  min = 1
elif diff_ab > 2 or diff_bc > 2 : 
  min = 2

if diff_bc >= diff_ab:
  max = diff_bc
else:
  max = diff_ab

print(min)
print(max-1)