def f1(n, f2):
    x = 3
    y = 4
    f2 = lambda x: x + y

    def f3(y):
        return x + y + n

    return (lambda h, h1: h(y) + h1(h(x)))(f2, f3)


print(f1(7, lambda a: a + 1))\

