
def k_element(s, i, k):
    if i < k - 1:
        return []
    if k == 0:
        return []
    if k == 1:
        return [ [s[x]] for x in range(0, i+1)]
    res = []
    for e in k_element(s, i-1, k-1):
        e.append(s[i])
        res.append(e)
    for z in k_element(s, i-1, k):
        res.append(z)
    return res

def k_element_sum(s, i, k):
    if i < k - 1:
        return 0
    if k == 0:
        return 0
    if k == 1:
        return sum([s[x] for x in range(i+1)])
    q = 0
    q += s[i] + k_element_sum(s, i-1, k-1)
    q += k_element_sum(s, i-1, k)
    print("i: %s, q:%s" % (i, q))
    return q


if __name__ == '__main__':
    # find k unique subsets of a set
    B = {1,3,6, 8, 10, 11}
    k = 3
    res = k_element(list(B), len(B) -1, k)
    s = k_element_sum(list(B), len(B) -1, k)
    r = set([sum(z) for z in res])
    print("Size: %s" % len(res))
    print("Sum: %s" % s)
    print("Sum: %s" % r)
    print("Sets: %s" % res)
