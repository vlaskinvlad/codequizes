import heapq
import sys
from cormen.graph import V, G


class VW(V):
    def __init__(self, val, w=None):
        super().__init__(val)
        self.w = w

    def __lt__(self, other):
        return self.val < other.val

    def __repr__(self):
        return super().__repr__() + " w: %s" % self.w


def mst_prim(g, r):
    q = []
    for v in g.v:
        v.w = sys.maxsize if v != r else 0
        q.append(v)

    heapq.heapify(q)

    while q:
        u = heapq.heappop(q)
        print("got %s with weight: %s" % (u, u.w))
        for v in g.adj[u]:
            w_v = g.weight(v, u)
            if w_v < v.w:
                v.w = w_v
                v.p = u
            heapq.heapify(q)







if __name__ == '__main__':

    g = G()
    r = VW('a')
    g.add(r, VW('b'), w=4)
    g.add(VW('a'), VW('h'), w=8)
    g.add(VW('b'), VW('h'), w=11)

    mst_prim(g, r)




