import array

def p(i, m):
    """
    Assuming is is the true index of the array
    """
    z = i + 1
    if z == m:
        z = 2*m - 1
    elif z < m:
        z = 2*(z % m) - 1
    else:
        z = 2*(z % m)
    return z - 1


def rearrange(a):
    n = len(a)
    perm = lambda x: p(x, n >> 1)
    m = (n >> 1)
    def mutate(c0):
        c = perm(c0)
        while c != c0:
            a[c0], a[c] = a[c], a[c0]
            c = perm(c)

    def check():
        i = 0
        while i < n:
            if i % 2 == 0:
                if type(a[i]) is str:
                    break
            else:
                if type(a[i]) is int:
                    break
            i += 1
        return i
    mutate(m)
    k = check()
    while k < n:
        mutate(k)
        k = check()
    return a


if __name__ == '__main__':
    """
     Given a Data Structure having first n integers and next n chars.
     A = i1 i2 i3 … iN c1 c2 c3 … cN.
     Write an in-place algorithm to rearrange
     the elements of the array ass A = i1 c1 i2 c2 … in cn
    """
    n = 1000
    a = [i for i in range(n)] + ["i%d" % i for i in range(n)]
    print("Rearranged: %s" % rearrange(a))
