"""
permutations of n objects of length k in lexicographic order

"""


count = 0
res_tab = []


def lex_permutation(arr, k, res=[]):
    if k == len(res):
        global count
        print(res, count)
        count += 1
        return
    arr_temp = [i for i in arr]
    for i in arr:
        res.append(i)
        arr_temp.remove(i)
        lex_permutation(arr_temp, k, res)
        arr_temp = [i for i in arr]
        res.remove(i)


def fact(n, k):
    if k == 0:
        return 1
    return n * fact(n - 1, k - 1)


def lex_permutation_rank(arr, n, k):
    n_list = [i for i in range(1, n + 1)]
    res = 0
    temp_arr = []
    for i in range(1, k + 1):
        temp_arr.append(arr[i - 1])
        lt_count = len(list(filter(lambda item: item < temp_arr[len(temp_arr) - 1], set(n_list) - set(temp_arr))))
        res += lt_count * fact(n - i, k - i)
    return res


def main():
    # lex order permutation test
    # array = list(range(1, n+1))
    # lex_permutation([1, 2, 3, 4], 3)

    # rank testing
    # [4] = {1,2,3,4}
    arr_list = [2, 4, 3]
    lex_permutation([1, 2, 3, 4], 3)
    print(arr_list, lex_permutation_rank(arr_list, 4, len(arr_list)))


if __name__ == "__main__":
    main()
