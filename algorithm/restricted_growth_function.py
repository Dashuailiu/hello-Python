

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


def d(m, t):
    if m == 0:
        return 1
    if m == 1:
        return t+1
    return t*d(m-1, t) + d(m-1, t+1)


def main():

    for (i, j) in enumerate(res_growth_func(8)):
        print(i, j)
        if i == 588:
            break
        # if j == [1, 1, 1, 1, 2, 2, 2]:  # 9
        #     break
        # if j == [1, 2, 3, 4, 4, 5, 5]:  # 838
        #     break
        # if j == [1, 2, 2, 3, 3, 4, 4]:  # 477
        #     break


    print(d(6, 1))
    print(d(5, 1))
    print(d(4, 2))
    print(d(3, 3))
    print(d(2,3))
    print(d(2,2))

if __name__ == "__main__":
    main()
