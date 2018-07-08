n = int(raw_input())
b = "{0:b}".format(n)
indent = len(b) + 1


def pad(s): return "".join(" " for i in xrange(0, indent - len(s)))

for i in xrange(1, n + 1):
    b = "{0:b}".format(i)
    o = "{0:o}".format(i)
    x = "{0:x}".format(i)
    print("%s" % i + pad(o) + o + pad(x) + pad(x) + pad(b) + b)
