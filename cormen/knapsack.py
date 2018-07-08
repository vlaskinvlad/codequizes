def knapsack(w, v, W, n):
    if n == 0:
        if w[0] <= W:
            return v[0]
        else:
            return 0
    s1 = knapsack(w, v, W, n-1)
    if w[n] <= W:
        s2 = v[n] + knapsack(w, v, W - w[n], n-1)
    else:
        s2 = -1
    return max(s1, s2)

def knapsack_dynamic(w,v, W):
    n = len(w)
    K= [[None]*(W + 1)]*(n+1)

    for i in range(n+1):
        for z in range(W+1):
            if i == 0 or z == 0:
                K[i][z] = 0
            elif w[i-1] <= z:
                K[i][z] = max(v[i-1] + K[i-1][z-w[i-1]], K[i-1][z])
            else:
                K[i][z] = K[i-1][z]
    return K[n][W]

if __name__ == '__main__':
    w = [10, 20, 30]
    v = [60, 100, 120]
    P = 50
    print("Dynamic kz: %s" % knapsack_dynamic(w, v, P))
    print("Recursive kz: %s" % knapsack(w, v, P, len(w)-1))
