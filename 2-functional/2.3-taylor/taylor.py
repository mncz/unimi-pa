import functools

def sin(x, n):
    s = sign()
    f = tfact()
    return functools.reduce(lambda i, j: i + j, [next(s) * (x ** k / next(f)) for k in range(1, (n * 2), 2)])

def sign():
    i = 1
    yield i

    while True:
        i *= -1
        yield i

def tfact():
    n, f = 1, 1
    yield f

    while True:
        n += 1
        f *= n
        n += 1
        f *= n
        yield f
