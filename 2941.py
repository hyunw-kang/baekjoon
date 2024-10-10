croatia = ['c=', 'c-', 'dz=', 'd-', 'lj','nj','s=','z=']
alpa = input()
for i in croatia:
    alpa = alpa.replace(i,'!')
print(len(alpa))