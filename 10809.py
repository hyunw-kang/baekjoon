s = input()
eng =  'abcdefghijklmnopqrstuvwxyz'
for i in eng:
    if i in eng:
        print(s.index(), end = '')
    else:
        print(-1, end = '')