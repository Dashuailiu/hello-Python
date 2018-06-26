#!/usr/bin/python2

import sys, re, array


class tOp:

    def __init__(self, tok): self.tok = int(tok)

    def __str__(self): return str(self.tok)

    def isEdgeOp(self): return self.tok > 9

    def isVertexOp(self): return self.tok <= 9

    def v1(self): return int(self.tok % 10)  # vertex 1

    def v2(self): return int(self.tok / 10)  # vertex 2 if EdgeOp


def rankColoring(C, t):
    # "extract boundary vertex coloring from state index"
    num = 0
    for i in range(t + 1):
        num = num * 3 + C[t - i]
    return num


def unrankColoring(num, t):
    # "extract boundary vertex coloring from state index"
    C = []
    for i in range(t + 1):
        C.append(int(num % 3))
        num /= 3
    return C


def pw3Col(pwTokens, state, state_sum, t):
    # "dynamic program for Pathwidth 3-Colorable"
    for op in pwTokens:
        o = tOp(op)
        if o.isEdgeOp():
            v1 = o.v1()
            v2 = o.v2()
            if v1 == v2:
                continue
            for i in range(3 ** (t + 1)):  # update all state boundary combinations
                C = unrankColoring(i, t)
                if C[v1] == C[v2]:
                    state[i] = 0  # edge makes invalid coloring
        else:  # isVertOp()
            v1 = o.v1()
            for i in range(3 ** (t + 1)):
                C = unrankColoring(i, t)
                if C[v1] == 0:  # process all coloring states only when v1 is colored 0
                    temp_sum = state_sum[i] if state[i] else float('inf')
                    C[v1] = 1
                    i1 = rankColoring(C, t)  # extract other slices
                    temp_sum1 = state_sum[i1] if state[i1] else float('inf')
                    C[v1] = 2
                    i2 = rankColoring(C, t)
                    temp_sum2 = state_sum[i2] if state[i2] else float('inf')

                    if max(state[i], state[i1], state[i2]) == 1:
                        state[i] = state[i1] = state[i2] = 1
                        temp_sum = min(temp_sum, temp_sum1, temp_sum2)
                        state_sum[i] = temp_sum + 1
                        state_sum[i1] = temp_sum + 2
                        state_sum[i2] = temp_sum + 3

    return state, state_sum


def tw3Col(G, t):
    G = G.strip()
    state = array.array('i', map((lambda n: 1), range(3 ** (t + 1))))
    state_sum = array.array('i', map((lambda n: sum(unrankColoring(n, t))), range(3 ** (t + 1))))
    if len(G) == 0:
        return state, state_sum
    if G[0] != '(':
        return pw3Col(re.findall('\d+', G), state, state_sum, t)
    level = 1
    for i in range(1, len(G)):
        if G[i] == ')':
            level -= 1
        elif G[i] == '(':
            level += 1
        if level == 0:
            state1, state_sum1 = tw3Col(G[1:i - 1], t)  # strip a level of ()'s
            if i + 1 >= len(G):
                return state1, state_sum1
            if G[i + 1:len(G)].find('(') < 0:  # append pathwidth operators?
                return pw3Col(re.findall('\d+', G[i + 1:len(G)]), state1, state_sum1, t)

            state2, state_sum2 = tw3Col(G[i + 1:len(G)], t)  # recurse remaining half
            state = array.array('i')
            state_sum = array.array('i')
            for i in range(3 ** (t + 1)):  # now update state for circle plus
                state_el = min(state1[i], state2[i])
                state.append(state_el)
                state_sum.append(state_sum1[i]+state_sum2[i]-sum(unrankColoring(i, t)))
            return state, state_sum


def main():
    with open('t_parse_input.txt', 'r') as f:
        for line in f.readlines():
            i = line.find('(')
            t = int(line[0])
            line = line[i:]
            state, state_num = tw3Col(line.strip(), t)
            # print(state, state_num)
            min_sum = -1
            for i in range(3 ** (t+1)):
                if state[i] != 0:
                    # print(state_num[i])
                    if min_sum == -1 or min_sum > state_num[i]:
                        min_sum = state_num[i]
            if min_sum == -1:
                print(None)
            else:
                print(min_sum+t+1)
            if t == 0:
                break


if __name__ == "__main__":
    main()
# # main program
# for line in sys.stdin:
#     i = line.find('(');
#     t = int(line[0:i - 1]);
#     line = line[i:]
#     print(tw3Col(line))
#     if line[0] == '0':
#         exit()
