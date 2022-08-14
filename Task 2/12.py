n = int(input())
l = list(input().split())
m = int(input())
k = list(input().split())

s1 = set(l)
s2 = set(k)

s3 = s1.union(s2)
print(len(s3))