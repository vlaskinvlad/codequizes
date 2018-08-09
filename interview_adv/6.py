def mem_o_n(a):
    n = len(a)
    x = [1]*n
    x[0] = 1
    i = 1
    while i < n:
        x[i] = x[i-1]*a[i-1]
        i += 1
    y = [1]*n
    y[n-1] = 1
    j = n-2
    y[j] = a[j]
    while j >= 0:
        y[j] = y[j+1]*a[j+1]
        j -= 1
    return [x[i]*y[i] for i in range(n)]


def mem_o_1(a):
    n = len(a)
    res = [1]*len(a)
    for i in range(1, n):
        res[i] = res[i-1]*a[i-1]
    p = 1
    # 1 a1 a1a2 ...a1a2...an-2, a1a2 ...an-1
    #                    an   1
    #                    yn-1 yn
    p = 1
    for j in range(n-1, -1, -1):
        res[j] = res[j]*p
        p = p * a[j]
    return res

if __name__ == '__main__':
    """
    You are given an array [a1 To an] and we have to construct
    another array [b1 To bn] where bi = a1*a2*…*an/ai.
    you are allowed to use only constant space and the
    time complexity is O(n). No divisions are allowed.
    """
    a = [1,2,3,4]
    # exp output
    # [2x3x4, 1x3x4, 1x2x4, 1x2x3]
    # [24, 12, 8, 6]
    print(mem_o_n(a))
    print(mem_o_1(a))


