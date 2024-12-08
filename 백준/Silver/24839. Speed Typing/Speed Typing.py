def check_type(type, typed):
  result = 0
  key = 0
  for i in range(len(typed)):
    if key < len(type) and type[key] == typed[i]:
      key +=1
    else:
      result +=1
  return result if key == len(type) else "IMPOSSIBLE"

T =int(input())
for t in range(1,T+1):
  type_str = input()
  typed_str = input()
  result = check_type(type_str, typed_str)
  print(f'Case #{t}: {result}')
      