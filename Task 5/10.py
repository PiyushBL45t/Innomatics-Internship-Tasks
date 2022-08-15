import re
inp = int(input())

for i in range(0,inp):
    string = input()
    splitted_Str = string.split()

    # if length greater than 1 and curly brackets not in string
    if len(splitted_Str)>1  and  '{' not in splitted_Str:      
        result = re.findall(r'#[a-fA-F0-9]{3,6}',string)
        [print(i) for  i in result]