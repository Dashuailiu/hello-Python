

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


def res_growth_func(n):
    n_list = [1] * n

    while True:
        pos = -1
        yield n_list
        for i in range(n)[:0:-1]:
            if n_list[i] < max(n_list[:i])+1:
                pos = i
                break
        if pos == -1:
            break
        n_list = n_list[:pos] + [n_list[pos]+1]+[1] * (n-pos-1)


def main():
    from itertools import product
    for (i, j) in enumerate(product(range(5), range(5), range(5))):
        print(i, j)
        # if j == (2, 3, 2):
        #     break

    # for (i, j) in enumerate(res_growth_func(7)):
    #     print(i, j)
    #     if j == [1, 1, 1, 1, 2, 2, 2]:  # 9
    #         break
        # if j == [1, 2, 3, 4, 4, 5, 5]:  # 838
        #     break
        # if j == [1, 2, 2, 3, 3, 4, 4]:  # 477
        #     break


if __name__ == "__main__":
    main()
