

def ibsearch(a, v, p, q):  # returns index of the bin search or None if not found
    if p == q:
        return a[p] if a[p] == v else None
    m = p + (q-p+1) >> 1
    if v < a[m]:
        return ibsearch(a, v, p, m - 1)
    elif v > a[m]:
        return ibsearch(a, v, m+1, q)
    else:
        return m


class N(object):
    def __init__(self, val, parent=None):
        self.left = None
        self.right = None
        self.val = val
        self.parent = parent
    def __repr__(self):
        return "n: %s, left: %s, %s, parent: %s " % (self.val, self.left, self.right, self.parent.val if self.parent is not None else 'nan')

def tree_build(io, po, io_range, po_range, parent, is_left=False):
    if not io or not po:
        return

    print("Tree build: io:(%s, %s)" % io_range + " po:(%s, %s)" % po_range)

    i, j = io_range
    if i>j:
        return
    if j > len(io):
        return
    if i < 0:
        return
    if i == j:
        leaf = N(io[i], parent)
        print("Got to the leaf: %s" %  leaf)
        if parent is not None:
            if is_left:
                parent.left = leaf
            else:
                parent.right = leaf
        return

    p, q = po_range
    root = N(po[p], parent = parent)
    print(root)
    if parent is not None:
        if is_left:
            parent.left = root
        else:
            parent.right = root

    #i_root = ibsearch(io, root.val, i, j)
    i_root = io.index(root.val)

    if i_root is None:
        print("I root is not found")
        return
    print("i root: %s" % i_root)

    i_left, j_left = i, i_root - 1
    size_left = j_left - i_left + 1

    i_right, j_right = i_root +1, j
    size_right = j_right - i_right + 1

    p_left, q_left = p+ 1, p + 1 + size_left
    p_right, q_right = q_left + 1, q_left + 1 + size_right


    print("Size left, right(%s, %s)" % (size_left, size_right))

    if size_left >= 1:
        tree_build(io, po, (i_left, j_left), (p_left, q_left), root, is_left=True)

    if size_right >= 1:
        tree_build(io, po, (i_right, j_right), (p_right, q_right), root, is_left=False)




if __name__ == '__main__':
    inorder = [10, 30, 40, 50, 60, 70, 90]
    postorder = [50, 30, 10, 40, 70, 60, 90]
    n = len(inorder)
    tree_build(inorder, postorder, (0, n-1), (0, n-1), None, False)
