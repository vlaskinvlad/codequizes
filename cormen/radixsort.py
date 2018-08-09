
def csort(a, ex):
    res = [0]*len(a)
    count = [0]*10
    for x in a:
        e = (x // ex) % 10
        count[e] += 1
    for i in range(1, len(count)):
        count[i] += count[i-1]

    # to make it stable we have to get from bottom to the down
    for i in range(len(a)-1, -1, -1):
        x = a[i]
        e = (x // ex) % 10
        res[count[e] - 1] = x
        count[e] -= 1

    for i in range(len(a)):
        a[i] = res[i]


def rsort(a):
    import math
    d = math.floor(math.log10(max(a)))

    for k in range(0, d + 1):
        ex = int(10**k)
        csort(a, ex)
        print("EX: %s" % ex)
        print(a)

    return a


if __name__ == '__main__':
    a = [170, 45, 75, 90, 802, 24, 2, 66]
    print(rsort(a))
