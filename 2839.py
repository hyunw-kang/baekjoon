a = int(input())
count2 =0
while a >= 0:
    if(a % 5 == 0):
        count2 += (a // 5)
        print(count2)
        break
    a -= 3
    count2 += 1
else:
    print(-1)











