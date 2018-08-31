from graph import V, G

def G1():
    g = G()
    s = V('s') #1
    t = V('t') #2
    y = V('y') #3
    x = V('x') #4
    z = V('z') #5
    g.li(s, t, w=6).li(s, t, w=7).li(s,y,w=7).li(t, y, w=8)\
    .li(t, x, w=5).li(x, t, w=-2).li(t, z, w=-4)
    g.li(z, s, w=2).li(z, x, w=7).li(y, x, w=-3)\
    .li(y, z, w=9)
    return g