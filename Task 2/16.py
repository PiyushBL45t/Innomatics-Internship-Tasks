n = int(input())
s = set()
for i in range(0, n):
    b = input()
    s.add(b)

operations = int(input())  
for x in range(operations):
  oper = input("Enter any operation: ").split()
  if oper[0] == "remove":
    s.remove(int(oper[1]))
  elif oper[0] == "discard":
    s.discard(int(oper[1]))
  else:
    s.pop()
    
print(sum(s))