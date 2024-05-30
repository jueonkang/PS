def check(i,j,board) : # i,j 는 체스판 맨 위, 맨 왼쪽의 시작 인덱스, board는 input
  # 다시 칠해야 하는 블록의 개수를 리턴 
  w,b = 0, 0  # w : white로 보드를 시작했을 때, 다시 칠해야 하는 개수
  # 8 * 8 크기의 보드를 가지고 온다. 
  # 0,0 / 0,1 . ..  / 0, 7 
  # 1,0 //  
  # 7,0 --- 7,7 
  for k in range(8): 
    for l in range(8):
      if (k+l) % 2 == 0 : 
        if board[i+k][j+l] != "B" : b += 1 
        elif  board[i+k][j+l] != "W" : w += 1 
      else : 
        if board[i+k][j+l] == "B" : b += 1 
        elif  board[i+k][j+l] == "W" : w += 1 

  return min(w,b)


N,M = map(int,input().split())
board = [] 

ans = 65

for i in range(N) : # board를 채우는 코드 
  board.append(input())
  
for i in range(N-7) : # N-7, M-7까지만 루프를 도는 이유는 체스판의 크기가 8 * 8 이기 때문에, 
  for j in range(M-7) :  #ex ) N = 10, M= 10이면,  N = 6, M= 5는 시작 지점이 될 수 없다.
    b = check(i,j,board) # b에는  B로 시작했을 떄, W로 시작했을 때 다시 칠한 개수 중 작은 값이 저장
    if  ans > b : # 특정 지점에서 다시 칠한 값을 구한 게 현재 가지고 있는 ans보다 작으면 바꾸기 
      ans = b 

print(ans)