import collections


class V(object):

    def __init__(self, value):
        self.color = None
        self.d = None # distance from the source in dfs
        self.f = None
        self.p = None
        self.val = value

    def __eq__(self, other):
        try:
            return self.val == other.val
        except AttributeError:
            return False

    def __hash__(self):
        return self.val.__hash__()

    def __repr__(self):
        return "(v:%s, p:%s, d:%s, c:%s)" %\
            (self.val, self.p.val if self.p is not None else 'none', self.d, self.color)


class G(object):

    def __init__(self):
        self.adj = collections.defaultdict(lambda: [])
        self.v = []

    def add(self, v1, v2=None, bi=True):
        a1 = self.adj[v1]

        if v2 is not None:
            a2 = self.adj[v2]
            if v2 not in a1:
                a1.append(v2)
            if v1 not in a2 and bi:
                a2.append(v1)
            if v2 not in self.v:
                self.v.append(v2)
        if v1 not in self.v:
            self.v.append(v1)
        return self

    def li(self, v1, v2=None):
        return self.add(v1, v2, bi=False)


    def __repr__(self):
        g = "Graph vertices: %s\n" % [v.val for v in self.v]
        a = "Adjuscency lists: \n"
        for v in self.v:
            a += "key: %s, edges: %s\n" % (v.val, [k.val for k in self.adj[v]])
        return g + a
