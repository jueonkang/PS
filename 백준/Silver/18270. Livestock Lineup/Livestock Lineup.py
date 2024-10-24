cows = ['Beatrice', 'Bella', 'Belinda', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue']

n = int(input())
constraints = []


for _ in range(n):
    line = input().split()
    x = line[0]
    y = line[-1]
    constraints.append((x, y))

result = []
current_order = []
used = [False] * len(cows)

stack = [([], used[:], 0)]

while stack:
    current_order, used, index = stack.pop()

    if len(current_order) == len(cows):
        valid = True
        for x, y in constraints:
            xi = current_order.index(x)
            yi = current_order.index(y)
            if abs(xi - yi) != 1:  
                valid = False
                break
        if valid:
            result.append(current_order[:])  
        continue

    for i in range(len(cows) - 1, -1, -1):  
        if not used[i]:
          
            newo = current_order + [cows[i]]
            newu = used[:]
            newu[i] = True
            stack.append((newo, newu, i))

result.sort()
for cow in result[0]:
    print(cow)
  
