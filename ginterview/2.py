def Q():
    """
    You are given a list of numbers.
    When you reach the end of the list
    you will come back to the beginning of the list
    (a circular list). Write the most efficient algorithm
    to find the minimum # in this list.
    Find any given # in the list.
    The numbers in the list are always increasing but you don’
    t know where the circular list begins, ie:
        38, 40, 55, 89, 6, 13, 20, 23, 36.
    """

def find_dip(a, p, q):
    if p == q:
        return a[p]

    m  = q + p >> 1
    if m >p and m < q and a[m-1] > a[m] < a[m+1]:
        return a[m]

    if a[m] < a[m + 1]:
        return find_dip(a, p, m-1)
    else:
        return find_dip(a, m+1, q)

def find_min(a):
    return find_dip(a, 0, len(a) - 1)


def ci(a, i):
    k = len(a)
    return a[i % k]

def find_peak(a, p, q):
    mid = (p + q + 1) >> 1
    print("peak: (%s, %s, %s, val: %s)" % (p, mid, q, ci(a, mid)))
    #if p == q:
        #return ci(a, p)
    mid = (p + q + 1) >> 1
    if ci(a, mid-1) < ci(a, mid):
        return find_peak(a, p-1, mid-1)
    elif ci(a, mid+1) < ci(a, mid):
        return find_peak(a, mid+1, q+1)
    else:
        return ci(a, mid)



if __name__ == '__main__':
    a = [38, 40, 55, 89, 100, 200, 6, 13, 20, 23, 36]
    #a = [38, 40, 55, 89, 100 ,200, 300, 20, 23, 36]
    print("Peak: %s" % find_peak(a, 0, len(a)-1))
