for a in range(1,101):
  for b in range(2,101):
    for c in range(b+1,101):
      for d in range(c+1,101):
        if b**3 + c**3 + d **3 == a**3:
          print(f"Cube = {a}, Triple = ({b},{c},{d}) ") 