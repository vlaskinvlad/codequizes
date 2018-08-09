import sys

def d1(a, v):
    mmin = abs(a[0] - v)
    mmax = abs(a[-1] - v)
    if mmin > mmax:
        return mmin, 0
    else:
        return mmax, len(a) - 1

def merge(a, b):
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    r  = [0]*(m+n)
    k  = 0
    while i < n and j < m:
        if a[i] < b[j]:
            r[k] = a[i]
            i += 1
        else:
            r[k] = b[j]
            j += 1
        k += 1

    if i < n:
        while i < n:
            r[k] = a[i]
            k += 1
            i += 1
    if j < m:
        while j < m:
            r[k] = b[j]
            k += 1
            j += 1
    return r

def smart_force(a, b, c):
    n = len(c)
    q = - sys.maxsize
    j = 0
    k = n-1
    ia = ib = ic = 0
    while j < n and k >= 0:
        vb, vc = b[j], c[k]
        vbc = abs(vb - vc)
        vab, i_vab = d1(a, vb)
        vac, i_vac = d1(a, vc)
        z = max(vbc, vab, vac)
        if z > q:
            q = z
            ib = j
            ic = k
            ia = i_vab if vab > vac else i_vac
        j += 1
        k -= 1
    return q, ia, ib, ic


def brute_force(a, b, c):
    q = - sys.maxsize
    ia = ib = ic = 0
    for k in range(len(c)):
        for j in range(len(b)):
            for i in range(len(a)):
                z = max( abs(a[i] - b[j]), abs(a[i] - c[k]), abs(c[k] - b[j]))
                if z > q:
                    q = z
                    ia = i
                    ib = j
                    ic = k
    return q, ia, ib, ic



if __name__ == '__main__':
    a = [3, 2, 13, 21, 21]
    b = [4, 2, 5, 3, 423]
    c = [ 1, 3, 5, 7, 1]
    import random
    for e in range(100):
        n = 10
        a = [random.randint(0, 100) for i in range(n)]
        b = [random.randint(0, 100) for i in range(n)]
        c = [random.randint(0, 100) for i in range(n)]
        a = sorted(a)
        b = sorted(b)
        c = sorted(c)

        res, i, j, k = brute_force(a, b, c)
        res_2, i, j, k = smart_force(a, b, c)
        print("bf: %s, sf: %s, assert: %s" % (res, res_2, res == res_2))

        #res, i, j, k = smart_force(a, b, c)
        #print("Smart force: %s, tuple(%s, %s, %s) ind: (%s, %s, %s)" % (res, a[i], b[j], c[k], i, j, k))

