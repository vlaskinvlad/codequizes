import sys

def min_loss_bf(a):
    """
    brute force
    """
    q = sys.maxsize
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            d = a[i] - a[j]
            if d > 0 and d < q:
                q = d
    return q

def min_loss(a):
    q = sys.maxsize
    n = len(a)



if __name__ == '__main__':
    a = [20, 7, 8, 2, 5]
    print("Min loss: %s" % min_loss(a))
