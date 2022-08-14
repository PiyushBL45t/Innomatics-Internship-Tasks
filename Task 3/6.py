def printPowers(a:int, b:int, c:int, d:int)->int:
    result = (a**b) + (c**d)
    return(result)


a = int(input())
b = int(input())
c = int(input())
d = int(input())
ret = printPowers(a, b, c, d)
print(ret)

