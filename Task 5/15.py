import re
number = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
    
inp = int(input().strip())
for i in range(inp):
    num = input().strip()
    if number.search(num):
        print("Valid")
        
    else:
        print("Invalid")
    
