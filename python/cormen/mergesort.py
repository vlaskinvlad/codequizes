
def merge(a, l, m, r):
    """
    Assiming a[l..m] and a[m..r] is sorted, merge them in one
    Do it in place if possible
    """
    res = [0] * (r - l + 1)
    i = l
    j = m + 1
    k = 0
    while i <= m and j <= r:
        if a[j] < a[i]:
            res[k] = a[j]
            j += 1
        else:
            res[k] = a[i]
            i += 1
        k += 1
    for z in range(i, m+1):
        res[k] = a[z]
        k += 1
    for z in range(j, r+1):
        res[k] = a[z]
        k += 1
    for z in range(l, r+1):
        a[z] = res[z-l]


def mergesort(a, l, r):
    if l < r:
        mid = (l + r) >> 1
        mergesort(a, l, mid)
        mergesort(a, mid+1, r)
        merge(a, l, mid, r)


if __name__ == '__main__':
    a = [3, 9, 6, 19, 29, 12]
    r = merge(a, 0, 1, 3)
    print("after merge: %s" % r)
    mergesort(a, 0, len(a) - 1)
    print("after mergesort: %s" % a)
