import re
inp = int(input())
for _ in range(0, inp):
    x, y = input().split(' ')
    res = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if res:
        print(x,y)