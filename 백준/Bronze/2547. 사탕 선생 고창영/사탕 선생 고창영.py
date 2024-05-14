a = int(input())
for i in range(a):
    m, n = input(), int(input())
    candy = [int(input()) for j in range(n)]
    print('YES' if sum(candy) % n == 0 else 'NO')