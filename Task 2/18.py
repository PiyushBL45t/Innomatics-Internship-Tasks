for _ in range(int(input())):
    x, a, z, b = input(), set(input().split()), input(), set(input().split())
    condition = a.issubset(b)
    if condition is True:
        print(True)
        
    else:
        print(False)