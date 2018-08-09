def Q():
    """
    Write a function f(a, b) which takes two character string arguments and
    returns a string containing only the characters found in both strings
    in the order of a. Write a version which is order
    N-squared and one which is order N.
    """
    pass

def fn2(a,b):
    return "".join([c for c in a if c in b])


def fn(a,b):
    s = {c for c in b}
    return "".join([c for c in a if c in s])


if __name__ == '__main__':
    a = 'abcdeff'
    b = 'czfdefqz'


    print(fn2(a,b))
    print(fn(a,b))
