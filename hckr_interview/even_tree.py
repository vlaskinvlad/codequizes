if __name__ == '__main__':
    s = """2 1
    3 1
    4 3
    5 2
    6 1
    7 2
    8 6
    9 8
    10 8"""
    import collections
    fr = list()
    to = list()
    adj = collections.defaultdict(lambda: [])
    nodes = set()
    root = 1
    i = 0
    for l in s.split("\n"):
        b, a = list(map(int, l.strip().split(" ")))
        adj[a].append(b)
        nodes.add(a)
        nodes.add(b)

    rank = collections.defaultdict(lambda: 0)
    color = collections.defaultdict(lambda: 0) # 0 - white, 1 - gray, 2 - black

    def dfs(v):
        if not adj[v]:
            rank[v] = 1
            return 1
        else:
            if color[v] == 0:
                rank[v] += 1
                color[v] == 1

            for c in adj[v]:
                if color[c] == 0:
                    rank[v] += dfs(c)
            return rank[v]

    dfs(1)
    print(rank)

    def maxcuts(v, r, stopset):
        print("Call: %s, rank: %s, stopset: %s" % (v,r, stopset))
        if not adj[v]:
            return 0

        if r % 2 != 0:
            return 0

        mc = 0
        for c in adj[v]:
            if c not in stopset:
                k = r - rank[c]
                if k % 2 == 0:
                    print("Node: %s, cut at: %s, rank: %s, stopset: %s" % (v, c, k, stopset))
                    sc = set(stopset)
                    sc.add(c)
                    print("calling a: %s, %s" % (c, rank[c]))
                    print("calling b: %s, %s" % (v, k))
                    mc += 1 + maxcuts(c, rank[c], sc) + maxcuts(v, k, sc)
        print("returning: %s" % mc)
        return mc

    print(maxcuts(1, rank[1], set()))






