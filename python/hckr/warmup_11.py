from __future__ import division
n = int(raw_input())
d = {}
for i in range(0, n):
    l = raw_input().split(" ")
    name = l[0]
    marks = map(lambda x: float(x), l[1:])
    d[name] = marks

student = raw_input()
print "%0.2f" % (sum(d[student]) / len(d[student]))
