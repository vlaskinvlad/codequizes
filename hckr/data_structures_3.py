n = raw_input()
a = set(map(lambda x: int(x), raw_input().split()))
m = raw_input()
b = set(map(lambda x: int(x), raw_input().split()))

u = list(a.symmetric_difference(b))
u.sort()
for x in u:
    print x
