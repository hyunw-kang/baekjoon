A, B = map(int,input().split())
C = int(input())
h = (B + C) // 60
m = (B + C) % 60
A += h
B = m
if A > 23:
    A -= 24
print(A,B) 