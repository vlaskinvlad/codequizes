import collections
import graphviz as grv

class V(object):

    def __init__(self, value):
        self.color = None
        self.d = None  # distance from the source in dfs
        self.f = None
        self.p = None
        self.val = value

    def __eq__(self, other):
        try:
            return self.val == other.val
        except AttributeError:
            return False

    def __lt__(self, other):
        return self.val < other.val

    def __hash__(self):
        return self.val.__hash__()

    def __repr__(self):
        return "(v:%s, p:%s, d:%s, c:%s)" % \
               (self.val, self.p.val if self.p is not None else 'none', self.d, self.color)


class G(object):

    def __init__(self):
        self.adj = collections.defaultdict(lambda: [])
        self.w = dict()
        self.v = []
        
    def edges(self):
        for u in self.v:
            for v in self.adj[u]:
                yield (u, v, self.weight(u, v))

    def key(self, v1, v2):
        k = hash(v1) + hash(v2) % (10**9 + 7)
        return k

    def weight(self, v1, v2):
        return self.w.get(self.key(v1, v2))
    
    def adj_matrix(self):
        """
            Return Adjacency matric multiplication of a graph
            The vertices are enumerated according the `self.v` list ordering
        """
        return [[self.weight(vi, vj)  for j,vj in enumerate(self.v)] for i, vi in enumerate(self.v)]
    
    def index_of(self, v):
        return self.v.index(v)
    
    def get_v_by_key(self, key):
        res = list(filter(lambda x: x.val == key, self.v))        
        if res:
            return res[0]
        else:
            return None

    def add(self, v1, v2=None, w=1, bi=True):
        a1 = self.adj[v1]
        if v2 is not None:
            a2 = self.adj[v2]
            if v2 not in a1:
                a1.append(v2)
                k = self.key(v1, v2)
                self.w[k] = w

            if v1 not in a2 and bi:
                a2.append(v1)
                k = self.key(v1, v2)
                self.w[k] = w

            if v2 not in self.v:
                self.v.append(v2)
        if v1 not in self.v:
            self.v.append(v1)
        return self

    def li(self, v1, v2=None, w=1):
        return self.add(v1, v2, w=w, bi=False)

    def T(self):
        gt = G()
        gt.v = self.v[:]
        for k in self.adj.keys():
            for z in self.adj[k]:
                gt.li(z, k)
        return gt
    
    def as_graphiz(self, layout='circo'):
        dg = grv.Graph()
        dg.attr(layout=layout)
        for (u, v, w) in self.edges():
            dg.edge(str(u.val), str(v.val), label=str(w))
        return dg

    def __repr__(self):
        g = "Graph vertices: %s\n" % [v.val for v in self.v]
        a = "Adjuscency lists: \n"
        for v in self.v:
            a += "key: %s, edges: %s\n" % (v.val, [k.val for k in self.adj[v]])
        return g + a
