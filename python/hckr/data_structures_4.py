x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
n = int(raw_input())

res = []
for i in xrange(0, x + 1):
    for j in xrange(0, y + 1):
        for k in xrange(0, z + 1):
            if i + j + k != n:
                res.append([i, j, k])
print res
