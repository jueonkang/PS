T = int(input())

for i in range(T):
    a,b=input().split()
    Alist = list(a)
    Blist = list(b)
    if sorted(Alist) == sorted(Blist):
        print(a,"&",b,"are anagrams.")
    else:
        print(a,"&",b,"are NOT anagrams.")