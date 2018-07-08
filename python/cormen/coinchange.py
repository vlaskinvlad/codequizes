import sys


def coinchange_greedy(coins, N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    z = max((c for c in coins if c <= N))
    return 1 + coinchange_greedy(coins, N - z)


def coinchange_recursive(coins, n):
    if n == 0:
        return 0
    res = sys.maxsize
    for c in coins:
        if c <= n:
            sub_res = coinchange_recursive(coins, n-c)
            if sub_res != sys.maxsize and sub_res + 1 < res:
                res = sub_res + 1
    return res


def coinchange_dynamic(coins, n):
    s = [sys.maxsize]*(n+1)
    # make it in bottom up manner
    s[0] = 0
    s[1] = 1
    for i in range(1, n+1):
        for c in coins:
            if c <= i:
                s[i] = min(s[i], s[i - c] + 1)
    return s[n]


def coinchange_count_recursive(coins, m, n):
    if n == 0:
        return 1

    if n < 0:
        return 0

    if m <= 0 and n >= 1:
        return 0

    return coinchange_count_recursive(coins, m-1, n) +\
           coinchange_count_recursive(coins, m, n - coins[m-1])


def coinchange_count_dynamic(coins, n):
    s = [[0 for x in range(k)] for x in range(n+1)]
    for i in range(k):
      s[0][i] = 1

    for i in range(1, n+1):
        for j in range(k):
            x = s[i-coins[j]][j] if i - coins[j] >= 0 else 0
            y = s[i][j-1] if j > 0 else 0
            s[i][j] = x + y
    return s[n][k-1]

# Dynamic Programming Python implementation of Coin
# Change problem
def count(S, n):
    table = [[0 for x in range(m)] for x in range(n+1)]
    for i in range(m):
        table[0][i] = 1

    for i in range(1, n+1):
        for j in range(m):
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
            y = table[i][j-1] if j >= 1 else 0
            table[i][j] = x + y

    return table[n][m-1]


if __name__ == '__main__':
    nominals = [1, 8, 13]
    N = 20
    # greedy soltion yields: 13 x 1 + 1 x 7 = 8 coins
    # optimal solution yields: 8 x 2 + 1 x 4 = 6 coins
    print("Greedy answer: %d" % coinchange_greedy(nominals, N))
    print("Recursive answer: %d" % coinchange_recursive(nominals, N))
    print("Dynamic answer: %d" % coinchange_dynamic(nominals, N))

    print("# ---------- #")
    nominals = [2, 5, 3, 6]
    N = 10
    print("Coinchage count recursive: %d"
          % coinchange_count_recursive(nominals,len(nominals), N))
    print("Coinchage count dynamic: %d"
          % coinchange_count_dynamic(nominals, N))
    print("Coinchage count dynamic2: %d"
          % count(nominals, len(nominals), N))
