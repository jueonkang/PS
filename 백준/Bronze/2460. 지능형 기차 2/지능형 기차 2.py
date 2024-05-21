bus_total = 0
bus_max = 0
for i in range(10):
  a,b = map(int,input().split())
  bus_total += b - a 
  if bus_total > bus_max:
    bus_max = bus_total

print(bus_max)


