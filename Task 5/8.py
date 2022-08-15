import re
inp = int(input())
for i in range(0, inp):
    if re.match(r'[789]\d{9}$',input()):   
        print('YES')  
    else:  
        print('NO')