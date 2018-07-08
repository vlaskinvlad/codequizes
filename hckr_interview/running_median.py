import heapq

def get_median(lower, upper, median, item):
    n1 = len(lower)
    n2 = len(upper)
    if n1 == n2:
        if item < median:
            heapq.heappush(lower, -item)
            return - lower[0]
        else:
            heapq.heappush(upper, item)
            return upper[0]
    elif n1 > n2:
        if item < median:
            heapq.heappush(upper, -heapq.heappop(lower))
            heapq.heappush(lower, -item)
        else:
            heapq.heappush(upper, item)
        return (upper[0] - lower[0])/2

    else:  # n2 is larger
        if item < median:
            heapq.heappush(lower, -item)
        else:
            heapq.heappush(lower, -heapq.heappop(upper))
            heapq.heappush(upper, item)
        return (upper[0] - lower[0])/2

if __name__ == '__main__':

    a = [3, 2, 8, 13, 21, 5]
    r = []
    lh = []
    uh = []
    i = 0
    median = None
    for item in a:
        r.append(item)
        if median is None:
            median = item
        median = get_median(lh, uh, median, item)

        print("%.1f" % median)
        print("lower: %s" % lh)
        print("upper: %s" % uh)
