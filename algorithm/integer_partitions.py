

def partitions_tuple(n):
    # tuple version
    if n == 0:
        yield ()
        return

    for p in partitions_tuple(n-1):
        yield (1, ) + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield (p[0] + 1, ) + p[1:]


def partitions_rev(n):
    # tuple version
    if n == 0:
        yield []
        return

    for p in partitions_rev(n - 1):
        yield p + [1]
        if p and (len(p) < 2 or p[-2] > p[-1]):
            yield p[:-1] + [p[-1] + 1]


def main():
    res = []
    # rank testing
    for i in partitions_rev(6):
        res.append(i)

    for i, j in enumerate(reversed(res)):
        print(i, j)


if __name__ == "__main__":
    main()
