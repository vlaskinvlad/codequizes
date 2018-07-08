def lcs_recursive(x, y):
    return lcs_recursive_aux(x, y, len(x)-1, len(y)-1)


def lcs_recursive_aux(x, y, i, j):
    if i < 0 or j < 0:
        return 0, []
    if x[i] == y[j]:
        sl, sr = lcs_recursive_aux(x, y, i-1, j-1)
        sr.append(x[i])
        return sl+1, sr
    else:
        z1 = lcs_recursive_aux(x, y, i-1, j)
        z2 = lcs_recursive_aux(x, y, i, j-1)
        return max(z1, z2, key=lambda x: x[0])


def lcs_dynamic(x, y):
    nx = len(x)
    ny = len(y)
    c = [[None]*(ny+1)]*(nx+1)
    c[0] = [0]*(ny+1)
    for i in range(nx + 1):
        c[i][0] = 0
    s = 0
    imax, jmax = -1, -1
    for i in range(1, nx + 1):
        for j in range(1, ny + 1):
            if x[i-1] == y[j-1]:
                c[i][j] = 1 + c[i-1][j-1]
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])

            if c[i][j] > s:
                s = c[i][j]
                imax = i
                jmax = j

    r = []
    while imax > 0 and jmax > 0:
        if x[imax-1] == y[jmax-1]:
            r.append(x[imax-1])
            imax -=1
            jmax -=1
        elif c[imax][jmax] == c[imax-1][jmax]:
            imax -=1
        else:
            jmax -=1
    r = [r[i] for i in range(len(r) - 1, -1, -1)]
    return s, r


if __name__ == '__main__':

    x = "abcbdab"
    y = "bdcaba"

    z = lcs_recursive(x, y)
    lcs ="".join(z[1])
    print("Recursive: #lcs: %s, %s" % (z[0], lcs))


    z = lcs_dynamic(x, y)
    print("Dynamic: #lcs: %s, %s" % (z[0], z[1]))
