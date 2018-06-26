"""

 a. find the largest mobile integer
 b. swap, then go to a.
 c. end when no mobile num
 <1 <2 <3     "3 mobile
 <1 <3 <2
 <3 <1 <2
 3> <2 <1     "2 mobile num any larger than 2 change its direction
 <2 3> <1
 <2 <1 3>
"""
import itertools

count = 0


def jt_algor(n, target=None):
    p_list, A = [i for i in range(1, n+1)], [n]
    i_list = [i for i in range(-1, n)]
    d_list = [-1] * (n+1)

    while A:
        mob_num = max(A)
        j = i_list[mob_num]
        if j+d_list[mob_num] < 0 \
                or j + d_list[mob_num] > n-1 \
                or mob_num < p_list[j+d_list[mob_num]]:
            A.remove(mob_num)
            continue

        global count
        if p_list == target:
            print(p_list, " Rank: ", count)
            return
        print(p_list, " Rank: ", count)
        count += 1

        p_list[j], p_list[j+d_list[mob_num]] = p_list[j+d_list[mob_num]], mob_num
        i_list[mob_num] += d_list[mob_num]
        i_list[p_list[j]] = j

        if i_list[mob_num] + d_list[mob_num] == -1 or i_list[mob_num] + d_list[mob_num] == n:
            A = [i for i in range(1, n+1)]
            A.remove(mob_num)

        if mob_num != max(p_list):
            d_list[mob_num+1:] = [d*(-1) for d in d_list[mob_num+1:]]
            A = list(range(mob_num, n+1))

    print(p_list, " Rank: ", count)


def main():
    # print("element num of the set:")
    # jt_algor(int(input()))
    # jt_algor(6, list(map(int, "243516")))
    jt_algor(14, [1, 2, 11, 3, 13, 4, 5, 6, 10, 9, 14, 7, 12, 8])


if __name__ == "__main__":
    main()

