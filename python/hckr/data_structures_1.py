n = int(raw_input())
l = map(lambda x: int(x), raw_input().split())
print hash(tuple(l))
