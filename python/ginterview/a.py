#Given a function which produces a random integer in
# the range 1 to 5,
# write a function which produces a random integer in the range 1 to 7.
import random


def rand5():
    return random.randint(1,5)


def rand7():
    r1 = rand5()
    r2 = rand5()
    return 7 - (r1 + r2) % 7

if __name__ == '__main__':
    import collections
    d = collections.defaultdict(lambda: 0)
    n = 100000
    for _ in range(n):
        d[rand7()] += 1
    for k in d.keys():
        d[k] = d[k]/n
        print("%s: %.2f" % (k, d[k]))
