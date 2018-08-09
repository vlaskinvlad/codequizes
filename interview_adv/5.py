def heaps_permut(a, n):
    if n == 1:
        print("".join(a))

    for i in range(n):
        heaps_permut(a, n-1)
        if n % 2 == 1:
            a[n-1], a[0] = a[0], a[n-1]
        else:
            a[n-1], a[i] = a[i], a[n-1]

if __name__ == '__main__':
    """
    write some code to find all permutations
    of the letteris in particular string
    """
    s = "abc"
    heaps_permut([c for c in s], len(s))

