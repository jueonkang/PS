a = int(input())
c = 0
b = 64
while a > 0:
	if b > a:
		b = b // 2
	else:
		c += 1
		a -= b
print(c)