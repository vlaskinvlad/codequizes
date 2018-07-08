def rod_cut_recursive(p, n):
    if n <= 0:
        return 0
    q = -1
    for j in range(1, n + 1):
        z = p[j - 1] + rod_cut_recursive(p, n - j)
        if q < z:
            q = z
    return q


def rod_cut_memorised(p, n):
    r = [-1]*n
    return rod_cut_memorised_aux(p, n ,r)


def rod_cut_memorised_aux(p, n, r):
    if r[n-1] >= 0:
        return r[n-1]
    if n <= 0:
        return 0
    q = -1
    for j in range(1, n+1):
        q = max(q, p[j-1] + rod_cut_memorised_aux(p, n-j, r))
    r[n-1] = q
    return q


def rod_cut_bottom_up(p, n):
    r = [None]*(n+1)
    r[0] = 0
    s = [0]*(n)
    for j in range(1, n+1):
        q = -1
        for i in range(1, j+1):
            z = p[i-1] + r[j-i]
            if z > q:
                q = z
                s[j-1] = i
        r[j] = q
    return r[-1], s


if __name__ == '__main__':

    n = 5
    p = [1, 2, 5, 3, 5]
    print("recursive: %s" % rod_cut_recursive(p, n))
    print("memorised top-down: %s" % rod_cut_memorised(p, n))
    a, s = rod_cut_bottom_up(p, n)
    print("memorised bottom-up: %s" % a)
    print("solution array: %s" % s)
