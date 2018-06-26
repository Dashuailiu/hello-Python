

def product_spaces(*args):
    if len(args) == 1:
        for i in args[0]:
            yield i
        return

    p_list = args[-1]
    p_list_rev = [i for i in reversed(p_list)]
    n_list = []

    for l in args[-2]:
        if l % 2 == 0:
            for i in p_list:
                if isinstance(i, list):
                    n_list.append([l] + [ii for ii in i])
                else:
                    n_list.append([l] + [i])

        else:
            for i in p_list_rev:
                if isinstance(i, list):
                    n_list.append([l] + [ii for ii in i])
                else:
                    n_list.append([l] + [i])
    for i in product_spaces(*args[:-2], n_list):
        yield i


def main():
    letters = [range(26)] * 3
    for (i, j) in enumerate(product_spaces(range(26), range(26), range(26))):
        print(i, j)
        # if j == [2,1,8]:
        #     break


if __name__ == "__main__":
    main()
