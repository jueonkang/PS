n = int(input())
output = {'Bessie': 7, 'Elsie': 7, 'Mildred': 7}
measurements = []

for i in range(n):
    parts = input().split()
    day = int(parts[0])
    cow = parts[1]
    change = int(parts[2])
    measurements.append((day, cow, change))

measurements.sort()

display_changes = 0
current_display = {'Bessie', 'Elsie', 'Mildred'}  

for day, cow, change in measurements:
    output[cow] += change

    max_output = max(output.values())
    new_display = {cow for cow in output if output[cow] == max_output}

    if new_display != current_display:
        display_changes += 1
        current_display = new_display

print(display_changes)