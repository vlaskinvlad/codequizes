class node(object):
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.p = None
        self.lvl = 0

    def __str__(self):
        return "node: %s" % self.key


class tree(object):
    def __init__(self):
        self.root = None
        self.height = 0

    def insert(self, node):
        if self.root is None:
            self.root = node
            self.root.lvl = 0
            self.height = 0
            return
        y = None
        x = self.root
        i = 0
        while x is not None:
            y = x
            i += 1
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        # y is the parent of node
        node.p = y
        node.lvl = i
        if i > self.height:
            self.height = i

        if node.key < y.key:
            y.left = node
        else:
            y.right = node

    def is_search(self):
        def node_in_range(node, lower, upper):
            if node is None:
                return True
            is_local = lower <= node.key <= upper
            if not is_local:
                print("Not search node is: %s, with pred: %s" % (node, node.p))
            is_left = node_in_range(node.left, lower, node.key)
            is_right = node_in_range(node.right, node.key, upper)
            return is_local and is_left and is_right
        return node_in_range(self.root, -1, int(10**8))


def traverse(v):
    print(v.key)


def inorder_stack(t):
    ztack = []

    def put_node(v):
        current = v
        while current is not None:
            ztack.append(current)
            current = current.left
    put_node(t)
    while ztack:
        v = ztack.pop()
        traverse(v)
        put_node(v.right)


def inorder_recursive(t):
    if t is not None:
        inorder_recursive(t.left)
        traverse(t)
        inorder_recursive(t.right)


def search(root, val):
    if root is None:
        return None
    elif root.key == val:
        return root
    elif val < root.key:
        return search(root.left, val)
    elif val > root.key:
        return search(root.right, val)
    else:
        return None


def tmin(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def tmax(node):
    current = node
    while current.right is not None:
        current = current.right
    return current


def second_biggest(node):
    m, parent = tmax(node)
    if m.left is not None:
        m_second, _ = tmax(m.left)

        return m_second
    else:
        return parent


def kth_biggest(node, k):
    def postorder_with_iteration(node, i):
        if i >= k:
            return node, i
        if node is None:
            return None, i
        r, ir = postorder_with_iteration(node.right, i)
        if r is not None:
            return r, ir
        i = ir + 1
        if i == k:
            return node, i
        return postorder_with_iteration(node.left, i)
    return postorder_with_iteration(node, 0)[0]


def succ(node):
    if node.right is not None:
        return tmin(node.right)
    x = node
    y = node.p
    while y is not None and x == y.right:
        x = y
        y = y.p
    return y


def pred(node):
    if node.left is not None:
        return tmax(node.left)
    x = node
    y = node.p
    while y is not None and x == y.left:
        x = y
        y = y.p
    return y


if __name__ == '__main__':
    import random
    root = node(10)
    n4 = node(4)
    n17 = node(17)
    root.left = n4
    n4.p = root
    root.right = n17
    n17.p = root
    n4.left = node(1)
    n4.right = node(5)
    n17.left = node(16)
    n17.right = node(21)

    nodes = [node(random.randint(0, 200)) for i in range(0, 100)]
    t = tree()
    for v in nodes:
        t.insert(v)

    print("Generated tree" +
          " of height: %d, is search: %s" % (t.height, t.is_search()))

    node_min = tmax(t.root)
    z = node_min
    while z is not None:
        print(z)
        z = pred(z)
    # inorder traversal
