t = int(input())

for _ in range(t) :
    n = int(input())
    score1, score2 = 0, 0	

    for _ in range(n) :
        p1, p2 = input().split()
        if p1 == p2 :	
            continue
        else :	
            if p1 == 'R' and p2 == 'S' :
                score1 += 1
            elif p1 == 'R' and p2 == 'P' :
                score2 += 1
            elif p1 == 'P' and p2 == 'R' :
                score1 += 1
            elif p1 == 'P' and p2 == 'S' :
                score2 += 1
            elif p1 == 'S'and p2 == 'P' : 
                score1 += 1
            elif p1 == 'S' and p2 == "R" :
                score2 += 1
              
    if score1 > score2 :
        print('Player 1')
    elif score1 < score2 :
        print('Player 2')
    else :
        print('TIE')
