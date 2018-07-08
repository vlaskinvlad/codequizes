import random


def partition(a, p, r):
    q = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] < q:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1


def rpartition(a, p, r):
    z = random.randint(p, r)
    a[z], a[r] = a[r], a[z]
    return partition(a, p, r)


def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q+1, r)


def rquicksort(a, p, r):
    if p < r:
        q = rpartition(a, p, r)
        rquicksort(a, p, q - 1)
        rquicksort(a, q + 1, r)


def tailrec_quicksort(a, p, r):
    while p < r:
        q = rpartition(a, p, r)
        tailrec_quicksort(a, p, q-1)
        p = q + 1


def iterative_quicksort(a, p, r):
    ztack = []
    ztack.append((p, r))
    while ztack:
        l, h = ztack.pop()
        if h > l:
            q = rpartition(a, l, h)

            if q - l > 1:
                ztack.append((l, q-1))

            if h - q > 1:
                ztack.append((q+1, h))


def randomised_select(a, p, r, i):
    """
       Given array find the the value x such that:
       i-1 elements are smaller
       randomised select complexity: O(n) on average
       in the worst case it goes as O(n**2)
    """
    if p == r:  # recursion termination
        return a[p]
    q = rpartition(a, p, r)
    k = q - p + 1
    if k == i:
        return a[q]
    elif i < k:
        return randomised_select(a, p, q-1, i)
    else:
        return randomised_select(a, q+1, r, i-k)


if __name__ == '__main__':
    a = [2, 8, 7, 1, 3, 5, 6, 4]
    print("before partition: %s" % a)
    n = len(a)
    partition(a, 0, n-1)
    print("after partition: %s" % a)
    iterative_quicksort(a, 0, n-1)
    print("after quicksort: %s" % a)

    a = [2, 8, 7, 1, 3, 5, 6, 4]
    print("Select 0: %s" % randomised_select(a, 0, n-1, 1))
    print("Select 4: %s" % randomised_select(a, 0, n-1, 4))
    print("Select n-1: %s" % randomised_select(a, 0, n-1, n))
