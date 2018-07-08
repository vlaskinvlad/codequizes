def activity_selector_iterative(s, f):
    m = 0
    k = m
    n = len(s)
    res = [0] if n >=1 else []
    while k < n:
        if s[k] > f[m]:
            res.append(k)
            m = k
        k += 1
    return res

def activity_selector(s, f):
    if len(s) == 1:
        return [0]
    res = [0]
    res.extend(activity_selector_aux(s, f, 0, len(s)))
    return res


def activity_selector_aux(s, f, k, n):
    m = k + 1
    while m < n and s[m] < f[k]:
        m = m + 1
    if m < n:
        res = [m]
        res.extend(activity_selector_aux(s, f, m, n))
        return res
    else:
        return []

if __name__ == '__main__':
    s = [int(z) for z in "1 3 0 5 3 5 6 8 8 2 12".split()]
    f = [int(z) for z in "4 5 6 7 9 9 10 11 12 14 16".split()]
    # f is sorted in ascending order
    #
    print("Greedy recursive selector: %s" % activity_selector(s,f))
    print("Greedy iterative selector: %s" % activity_selector_iterative(s,f))
