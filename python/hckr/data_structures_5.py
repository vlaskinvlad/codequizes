n = raw_input()
l = map(lambda x: int(x), raw_input().split())
m1 = max(l)
for i in xrange(0, l.count(m1)):
    l.remove(m1)
print max(l)
