from graph import G, V
from collections import deque


def bfs(Z, s):
    for v in Z.v:
        v.color = 'w'
    s.color = 'g'
    s.d = 0
    s.p = None
    q = deque([])
    q.append(s)
    while q:
        u = q.popleft()
        for v in Z.adj[u]:
            if v.color == 'w':
                v.color = 'g'
                v.d = u.d + 1
                v.p = u
                q.append(v)
        u.color = 'b'
        print("%s processed" % u)

time = 0


def dfs(Z, start_with=None):
    for v in Z.v:
        v.color = 'w'
        v.p = None
    if start_with is not None:
        i_st = Z.v.index(start_with)
        dfs_visit(Z, Z.v[i_st])
    print("Enter the secod cycle")
    for v in Z.v:
        if v.color == 'w':
            dfs_visit(Z, v)


def dfs_visit(Z, s):
    global time
    time += 1
    s.d = time
    print("V: %s enter at: %s" % (s.val, time))
    s.color = 'g'
    for v in Z.adj[s]:
        if v.color == 'w':
            v.p = s
            dfs_visit(Z, v)
    time += 1
    s.f = time
    s.color = 'b'
    print("V: %s exit at: %s" % (s.val, time))


def dfs_visit_stack(Z, s):
    """
    TODO: todo to be done
    """
    global time
    ztack = []
    ztack.append(s)

    while ztack:
        u = ztack.pop()
        time += 1
        u.d = time
        u.color = 'g'
        for v in Z.adj[u]:
            if v.color == 'w':
                v.color = 'g'
                ztack.append(v)


def make_graph():
    r = V('r')
    v = V('v')
    s = V('s')
    w = V('w')
    t = V('t')
    x = V('x')
    u = V('u')
    y = V('y')
    g = G()
    g.add(s, r).add(r, v).add(s, w).add(w, t).add(w, x).add(t, x)\
        .add(t, u).add(u, y).add(x, y).add(x, u)
    print(g)
    return g


def make_graph2():
    u = V('u')
    v = V('v')
    w = V('w')
    z = V('z')
    y = V('y')
    x = V('x')
    g = G().li(u, v).li(u, x).li(x, v).li(v, y).li(y, x).li(w, y).li(w, z)\
        .li(z, z)
    print(g)
    return g

if __name__ == '__main__':
    #g = make_graph()
    #i_s = g.v.index(V('s'))

    # bfs makes up bfs tree forests
    # bfs oftentimes used to find the shortest paths
    # print("bfs traversal")
    # bfs(g, g.v[i_s])
    g = make_graph2()
    dfs(g, start_with=V('u'))
    for v in g.v:
        print("%s: %s/%s" % (v.val, v.d, v.f))
