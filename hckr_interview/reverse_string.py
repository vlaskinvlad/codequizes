def z(s):
    cs = [c for c in s]
    n = len(s)
    return "".join([cs[i] for i in range(n-1,-1, -1)])

def z2(s):
    cs = [c for c in s]
    n = len(s)
    i = 0
    while i < n - 1 - i:
        if cs[i] != cs[n -1 - i]:
            cs[i], cs[n - 1 - i] = cs[n - 1 - i], cs[i]
        i += 1
    return "".join(cs)

def z3(s, p, q):
    if p == q:
        return s[p]
    m = p + (q - p + 1 >> 1)
    a = s[p:m]
    b = s[m:q+1]


if __name__ == '__main__':

    s = 'abcdefz'
    print(s)
    print(z(s))
    print(z2(s))
