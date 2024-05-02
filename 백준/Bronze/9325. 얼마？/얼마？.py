a = int(input())

for i in range(a):
    b = int(input())
    c = int(input())
    price = b

    for p in range(c):
        d, e = map(int, input().split())
        price += d * e

    print(price)