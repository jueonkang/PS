
correct = ""
guess = ""
green = 0
yellow = 0

for i in range(3):
    a = input()
    correct += a 

for i in range(3):
    b = input()
    guess += b

correct = list(correct)
guess = list(guess)

# guess[i]= "?"

for i in range(9):
    if correct[i] == guess[i]:
        green += 1
        guess[i] = "&"
        correct[i] = "&"

    
for i in range(9) : 
    for j in range(9) : 
        if guess[i] == correct[j]  and guess[i] != "&":
            yellow +=1
            guess[i] = "&"
            correct[j] = "&"

print(green)
print(yellow)

