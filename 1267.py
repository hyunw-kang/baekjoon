a = int(input())
time = list(map(int,input().split()))

y_t = 0
m_t = 0
for i in (time):
    y_t += ((i // 30)*10) + 10
    m_t += ((i // 60) * 15) + 15
if(y_t > m_t):
    print("M",m_t)
elif(y_t <m_t):
    print("Y",y_t)
else:
    print("Y M", y_t)
print(m_t)