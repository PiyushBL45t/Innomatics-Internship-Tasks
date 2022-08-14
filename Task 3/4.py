"""
   divmod function that returns the quotient and then remainder 
   of two input values
   
"""
def modulus(a:int, b:int)->None:
    result = divmod(a, b)
    print(result[0])
    print(result[1])
    print(result)

a = int(input())
b = int(input())

modulus(a, b)