n1 = int(input())
set_1 = set(input().split())

n2 = int(input())
set_2 = set(input().split())

result = set_1.union(set_2) - set_1.intersection(set_2)
print(len(result))