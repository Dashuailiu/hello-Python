

count = 0


def fact(n, k):
    if k == 0:
        return 1
    return n * fact(n - 1, k - 1)


def bi_coeff(n, k):
    return fact(n, k) // fact(k, k)


def find_pos(res):
    pos = -1
    for i in reversed(range(1, len(res))):
        if res[i] > res[i-1]+1:
            pos = i-1
    return pos


def colex_subset(n, k):
    res = [i for i in range(1, k+1)]
    while True:
        global count
        print(res, count)
        count += 1
        pos = find_pos(res)
        if pos != -1:
            if pos == 0:
                res[0] += 1
            else:
                res = [i for i in range(1, pos+1)] + [res[pos]+1] + res[pos+1:]
        else:
            if res[k-1] == n:
                break
            else:
                res = [i for i in range(1, k)] + [res[k-1]+1]


def colex_subsets_rank(arr, n):
    res = 0
    k = len(arr)
    for j in reversed(range(len(arr))):
        res += bi_coeff(arr[j]-1, k)
        k -= 1
    return res


def main():
    # binomial coefficients test
    #print(bi_coeff(8, 3))

    print(colex_subsets_rank([2, 5, 6, 8], 9))

    # colex subsets test
    colex_subset(6, 3)


if __name__ == "__main__":
    main()
