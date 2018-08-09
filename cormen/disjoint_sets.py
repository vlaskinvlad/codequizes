class V(object):
    def __init__(self, key, parent=None):
        self.key = key
        self.p = self if parent is None else parent
        self.rank = 0

    def __repr__(self):
        return "node: %s" % self.key

    def __eq__(self, other):
        try:
            return self.key == other.key
        except Exception as e:
            return False
    def __hash__(self):
        return self.key


def make_set(x):
    return V(x)


def find_set(v):
    if v.p != v:
        v.p = find_set(v.p)
    return v.p


def union(x, y):
    link(find_set(x), find_set(y))


def link(x, y):
    if y.rank > x.rank:
        x.p = y
        return y
    else:
        y.p = x
        if x.rank == y.rank:
            x.rank += 1
        return x

if __name__ == '__main__':

    edges = [(1,2), (2,3), (3,4), (4,1), (5, 6)]
    nodes = set()
    for a, b in edges:
        if a not in nodes:
            nodes.add(a)
        if b not in nodes:
            nodes.add(b)

    s = dict([(x, make_set(x)) for x in nodes])

    for a,b in edges:
        if find_set(s[a]) != find_set(s[b]):
            union(s[a], s[b])
    from collections import Counter
    c = Counter( (find_set(s[v]) for v in nodes))
    print(c)
    print(max(c.values()))
    print(min(c.values()))
