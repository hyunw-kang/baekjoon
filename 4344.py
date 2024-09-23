a = int(input())

for i in a:
    num = list(map(int, input().split()))
    avg = sum(num[1:])/ num[0]
    #print(avg)
    count = 0
    for i in range (1, len(num)):
        if num[i] > avg:
            count +=1
    rate = count / num[0]*100
    print("%.3f.format(rate)")