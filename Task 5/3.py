import re

expression = input()
res = re.findall(r"([A-Za-z0-9])\1+", expression)
if res:
    print(res[0])
else:
    print(-1)
