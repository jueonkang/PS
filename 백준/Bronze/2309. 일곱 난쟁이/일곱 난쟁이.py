
def solve() : 
  for i in range(len(a)):
      for j in range(i + 1, len(a)):
        if sum_ - a[i] - a[j] == 100:
          for k in range(len(a)):
            if k == i or k == j:
              pass
            else:
              print(a[k])
          return 

a = []
for i in range(9):
    a.append(int(input()))

a.sort()
sum_ = sum(a)
solve() 

      