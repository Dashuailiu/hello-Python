#!/usr/bin/python3
#
# Solution of 720 Assignment 3 (linear-time vertex cover algorithm)
# <mjd@cs.auckland.ac.nz>  May 2006 [Python3 version May 2015]

import sys
import re
import array


class tOp:
    # "A t-parse Operator"
    def __init__(self, tok): self.tok = int(tok)

    def __str__(self): return str(self.tok)

    def isEdgeOp(self): return self.tok > 9

    def isVertexOp(self): return self.tok <= 9

    def v1(self): return self.tok % 10  # vertex 1

    def v2(self): return self.tok // 10  # vertex 2 if EdgeOp


def pwVC(pwTokens, state):
    # "dynamic program for Pathwidth Vertex Cover"
    for op in pwTokens:
        o = tOp(op)   # print o,'\n'
        if o.isEdgeOp():
            v1 = o.v1()
            v2 = o.v2()
            for i in range(2 ** (t + 1)):  # update all state boundary combinations
                if not (1 << v1 & i or 1 << v2 & i):
                    state[i] = 1 << 30  # not covered
        else:  # isVertOp()
            v1 = o.v1()
            for i in range(2 ** (t + 1)):
                if (1 << v1) & i:  # if v1 in boundary set?
                    state[i] = min(state[i], state[i - (1 << v1)]) + 1
                else:
                    state[i] = min(state[i], state[i + (1 << v1)])
    return state


def bits(n):
    # "how many 1 bits of int n?"
    cnt = 0
    for i in range(t + 1):
        if n & 1 << i:
            cnt += 1
    return cnt


def twVC(G):
    # "dynamic program for Treewidth Vertex Cover"
    G = G.strip()  # print "G=",G,'\n'
    state = array.array('i', map((lambda n: bits(n)), range(2 ** (t + 1))))
    if len(G) == 0:
        return state  # state of empty t-parse
    if G[0] != '(':
        return pwVC(re.findall('\d+', G), state)
    level = 1
    for i in range(1, len(G)):  # doing a circle plus operator
        if G[i] == ')':
            level -= 1
        elif G[i] == '(':
            level += 1
        if level == 0:
            state1 = twVC(G[1:i - 1])  # strip a level of ()'s
            while 1:
                k = G[i + 1:].find('(')  # level will imeadiately be set to 1 below
                if k == -1:
                    return pwVC(re.findall('\d+', G[i + 1:]), state1)
                for j in range(i + 1 + k, len(G)):  # get 2nd (next) argument to circle plus
                    if G[j] == ')':
                        level -= 1
                    elif G[j] == '(':
                        level += 1
                    if level == 0:
                        state2 = twVC(G[i + 2 + k:j - 1])   # print "circle plus\n"
                        for i in range(2 ** (t + 1)):  # now update state for circle plus
                            if state1[i] < 1 << 30 and state2[i] < 1 << 30:
                                state[i] = state1[i] + state2[i] - bits(i)
                            else:
                                state[i] = 1 << 30
                        if j + 1 < len(G):
                            state1 = state
                            i = j + 1
                            break  # to next while iteration to look for another circle plus
                        else:
                            return state

t = 2
# main program
def main():
    s = "2 ( 10 21 1 10 21 0 10 20 2 20 21 )"  # read input graph
    i = s.find('(')
    s = s[i:]  # set global treewidth t
    print(min(twVC(s)))


if __name__ == "__main__":
    main()

