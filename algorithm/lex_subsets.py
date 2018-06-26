"""
k-element subsets of the set [n]
3-element subsets of the set [6]

123
"""

result = []


def get_subset(A, k, n):
    a_list = [i for i in A]
    if len(a_list) == k:
        result.append(a_list)
        return
    s_num = max(a_list)+1 if a_list else 1
    for i in range(s_num, n+1):
        a_list.append(i)
        get_subset(a_list, k, n)
        a_list.remove(i)


def subset_algor(n, k):
    V = []
    get_subset(V, k, n)


def main():
    # subset_algor(int(input()), int(input()))
    subset_algor(7, 3)

    for i in range(len(result)):
        print(result[i], " Rank: ", i)
    print(len(result))


if __name__ == "__main__":
    main()
