def f(a):
  if a < 2:
    return a
  return f(a-1) + f(a-2)

b = int(input())
print(f(b))
