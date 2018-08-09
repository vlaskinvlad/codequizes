import sys
from graph import V, G


def relax(g, u, v):
    w = g.weight(u, v)
    if v.d > u.d + w:
        v.d = u.d + w
        v.p = u

def init(g, source) 


if __name__ == '__main__':

    g = G()
    g.li(V('s'), V('t'), w=6)
    g.li(V('s'), V('y'), w=7)
    g.li(V('t'), V('y'), w=8)
    g.li(V('t'), V('x'), w=5)
    g.li(V('x'), V('t'), w=-2)
    g.li(V('t'), V('z'), w=-4)
    g.li(V('z'), V('s'), w=2)
    g.li(V('z'), V('x'), w=7)
    g.li(V('y'), V('x'), w=-3)
    g.li(V('y'), V('z'), w=9)

    print("Graph: %s" % g)
