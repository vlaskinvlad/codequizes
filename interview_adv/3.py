
def max_a7(a):
    n = len(a)
    q = 0
    mi = None
    mj = None
    for i in range(n):
        for j in range(i+1, n):
            m = sum(a[i:j]) %  7
            if m > q:
                q = m
                mi = i
                mj = j
    return q, mi, mj

def max_sum_n2(a):
    n = len(a)
    q = 0
    mi = None
    mj = None
    for i in range(n):
        for j in range(i+1, n):
            m = sum(a[i:j])
            if m > q:
                q = m
                mi = i
                mj = j
    return q, mi, mj-1

def max_sum_dynamic(a):
    if not a:
         return None

    n = len(a)
    if n == 1:
         return a[0]

    s = [0 for x in range(n)]
    s[0] = a[0]
    m = s[0]
    p = 0  # start of the range
    q = 0  # end of the range
    for i in range(1, n):
        right = s[i-1] + a[i]
        left = a[i]
        s[i] = left if left > right else right
        if s[i] > m:
            m = s[i]
            p, q = (i, i) if left > right else (p, i)

        print("s[%s]: %s, (%s, %s)" %(i, s[i], p, q ))

    return m, p, q

def max_submatrix_sum(M):
    n = len(M) # rows
    m = len(M[0]) # cols # n == m

if __name__ == '__main__':
    a =[3, 3, 9, 9, 5]
    a = [-1, -3, 3, -3, 2, -1, 2, 3, 4, -5]
    print(max_sum_n2(a))
    print(max_sum_dynamic(a))

    b = [
     [-1, -2, -4],
     [-8, -2, 5],
     [-3, 6, 7]
    ]

