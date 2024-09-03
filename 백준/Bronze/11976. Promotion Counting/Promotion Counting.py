lst = []

for i in range(4):
    a,b = map(int,input().split())
    lst.append([a,b])

gtop = lst[3][1] - lst[3][0]
stog = (lst[2][1]-lst[2][0]) + gtop
btos = (lst[1][1]-lst[1][0]) + stog

print(btos)
print(stog)
print(gtop)
