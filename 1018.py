n , m = map(int, input(). split())
chess = []
change = []
for i in range(n):
    chess.append(input())
for a in range(n-7):
    for b in range(m-7):
        white = 0 #White 개수 
        black = 0 #black 개수
        for i in range(a,a+8):
            for j in range(b , b+8):
                if (i+j)%2 == 0:
                    if chess[i][j] != 'B': #white 일때
                        black +=1
                    else:
                        white += 1
                else:
                    if chess[i][j] != 'B': 
                        white +=1
                    else:
                        black +=1              
        change.append(white)
        change.append(black)

print(min(change))




