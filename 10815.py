a = int(input())
b = set(list(map(int,input().split())))
c = int(input())
d = list(map(int, input().split()))

value = {}

for n in b:
    value[n]= True
for m in d:
    if m in b:
        print(1, end ="")
    else: 
        print(0 , end = "")
