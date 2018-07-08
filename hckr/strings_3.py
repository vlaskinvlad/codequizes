origin = raw_input()
n, k = raw_input().split(" ")
l = list(origin)
l[int(n)] = k
print(''.join(l))
