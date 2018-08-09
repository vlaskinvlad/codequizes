class N(object):
    def __init__(self, val, p=None, is_left=None):
        self.val = val
        self.p = p
        self.left = None
        self.right = None
        if p is not None:
            if is_left:
                self.p.left = self
            else:
                self.p.right = self

    def __repr__(self):
        return "n: %d" % self.val



class T(object):
    def __init__(self, root=None):
        self.root = root

    def inorder_print(self):
        def inorder(e):
            if e is None:
                return []
            r = []
            r.extend(inorder(e.left))
            r.extend([e.val])
            r.extend(inorder(e.right))
            return list(map(str, r))
        s = inorder(self.root)
        return ", ".join(s)


def tmin(e):
    y = e
    x = None
    while y is not None:
        x = y
        y = y.left
    return x


def tmax(e):
    y = e
    x = None
    while y is not None:
        x = y
        y = y.right
    return x


def make_tree(a):
    t = T()
    for x in a:
        e = N(x)
        if t.root is None:
            t.root = e
        else:
            y = t.root
            p = None
            while y is not None:
                p = y
                if x > y.val:
                    y = y.right
                else:
                    y = y.left
            e.p = p
            if x > p.val:
                p.right = e
            else:
                p.left = e
    return t


def search_t(t, val):
    y = t.root
    while y is not None and y.val != val:
        if val > y.val:
            y = y.right
        else:
            y = y.left
    return y


def successor(e):
    if e.right is not None:
        return tmin(e.right)
    x = e
    y = e.p
    while y is not None and y.right is not None and x.val == y.right.val:
        x = y
        y = y.p
    return y


def predessor(e):
    if e.left is not None:
        return tmax(e.left)
    x = e
    y = e.p
    while y is not None and y.left is not None and x.val == y.left.val:
        x = y
        y = y.p
    return y


def kth_minimum(t, k):
    e = tmin(t.root)
    for j in range(1, k):
        e = successor(e)
    return e


if __name__ == '__main__':

    a = [21, 13, 8, 2, 34, 45]
    t = make_tree(a)
    print(t.inorder_print())
    print("Successor root :%s is %s" % (t.root, successor(t.root)))
    e = search_t(t, 34)
    print("Successor %s is %s" % (e, successor(e)))
    print("Predessor %s is %s" % (e, predessor(e)))

    for k in range(1, len(a) + 1):
        print("%dth min: %s" % (k, kth_minimum(t, k)))

