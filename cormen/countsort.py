def csort(a):
    min_a = min(a)
    max_a = max(a)
    count = [0]*(max_a - min_a + 1)

    for x in a:
        count[x - min_a] += 1

    for j in range(1, len(count)):
        count[j] += count[j-1]

    out = a[:]
    for x in a:
        j = count[x - min_a]
        out[j - 1] = x
        count[x-min_a] -= 1

    return out
if __name__ == '__main__':

    a = [3, 13, 8 ,5, 9, 12, 8,8,8,8,13,5]
    print(csort(a))
