def left(i):
    return ((i + 1) << 1) - 1


def right(i):
    return (i+1) << 1


def parent(i):
    return ((i+1) >> 1) - 1


def swap(a, i, j):
    b = a[i]
    a[i] = a[j]
    a[j] = b


def max_heapify(a, i, max_n=None):
    """
    Given array a and  where a[i] violates the property
    maintain the heap structure by letting the element go down
    because left right are working on the
    Running time O(lg(n))
    """
    l = left(i)
    r = right(i)
    n = len(a) if max_n is None else min(len(a), max_n)
    largest = l if l < n and a[l] > a[i] else i
    if r < n and a[r] > a[largest]:
        largest = r
    if largest != i:
        swap(a, largest, i)
        max_heapify(a, largest, n)


def max_heapify_for(a, i):
    """
       Same as max heapify but with for cycle
       TODO: implement it with for/while loop
    """
    pass


def build_max_heap(a):
    """
    Because half of the elemets is in the leaves of the heap
    We can start building the heap from the first part of the array
    it works in O(n)!!!
    rather than in o(nlog(n))
    """
    imax = len(a) << 2
    for i in range(imax, -1, -1):
        max_heapify(a, i)


def heapsort(a):
    """
    Works in O(nlog(n))
    """
    build_max_heap(a)
    n = len(a)
    for i in range(n-1, 0, -1):
        swap(a, 0, i)
        max_heapify(a, 0, max_n=i)


def is_maxheap(a):
    res = True
    for i in range(0, len(a)):
        k = parent(i)
        if 0 <= k < len(a):
            if a[i] > a[k]:
                res = False
                break
    return res


if __name__ == "__main__":
    a = [16, 21, 10, 35, 17, 9, 3, 2, 8, 110]
    print("before heapify: %s (is max heap: %s)" % (a, is_maxheap(a)))
    build_max_heap(a)
    print("after heapify: %s" % a)
    print("is max heap: %s" % is_maxheap(a))
    heapsort(a)
    print("after heapsort: %s" % a)
