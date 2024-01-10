a, b, c = map(int,input().split())
count = 1
E = 1
S = 1
M = 1
while True:
    if(E == a and S == b and M == c):
        break
    E+=1
    S+=1
    M+=1
    count+=1
    if(E >= 16):
        E -= 15
    if(S >= 29):
        S -= 28
    if(M >= 20):
        M -= 19
print(count)
