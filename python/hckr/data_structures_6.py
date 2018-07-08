n = int(raw_input())

r = []
m1 = -1000000000000.0
min2 = 1000000000000.0
for i in xrange(0, n):
    name = raw_input()
    avg_mark = float(raw_input())
    if m1 < 0:
        m1 = avg_mark

    if avg_mark < m1:
        m1 = avg_mark

    elif avg_mark > m1 and avg_mark < min2:
        min2 = avg_mark

    r.append([name, avg_mark])

for i in filter(lambda x: abs(x[1] - min2) < 0.0000000000001, r):
    print(i[0])
