#!/usr/bin/python


from bisect import insort
from collections import OrderedDict


def t_parse(t_graph):
    node_num = int(t_graph[0]) + 1
    t_graph = pre_data(t_graph)
    sub_graph_list = []

    while True:
        item = t_graph.pop()

        if item == ')':
            i = rfind_list(sub_graph_list, '(')
            exe_elm = sub_graph_list[i + 1:]
            sub_graph_list = sub_graph_list[:i]

            if exe_elm and isinstance(exe_elm[0], dict):
                if len(exe_elm) == 1:
                    adj = exe_elm[0]
                elif isinstance(exe_elm[1], str):
                    adj = add_adj(exe_elm[0], exe_elm[1:])
            else:
                adj = get_adj(node_num, exe_elm)

            if sub_graph_list and isinstance(sub_graph_list[-1], dict):
                sub_graph_list[-1] = cplus_adj(sub_graph_list[-1], adj)
            else:
                sub_graph_list.append(adj)

        elif item.isdigit() and t_graph[-1] == '(':
            sub_graph_list.append(item)
            i = rfind_list(sub_graph_list, '(')
            exe_elm = sub_graph_list[i + 1:]
            sub_graph_list = sub_graph_list[:i]
            adj = add_adj(exe_elm[0], exe_elm[1:])
            sub_graph_list.append(adj)
        else:
            sub_graph_list.append(item)

        if len(sub_graph_list) == 1 and isinstance(sub_graph_list[0], dict):
            break

    print_graph(sub_graph_list[0])
    # for graph in sub_graph_list:
    #     print_graph(graph)


def pre_data(t_graph):
    if t_graph[-1] != ')':
        t_graph = [t_graph[0]] + ['('] + t_graph[1:] + [')']
    return list(reversed(t_graph[1:]))


def print_graph(graph):
    print(graph['node_num'])
    for i in list(graph['adj'].values()):
        print(' '.join(map(lambda x: str(x), i)))


def rfind_list(o_list, obj):
    r_list = list(reversed(o_list))
    return len(o_list) - r_list.index(obj) - 1


def get_adj(node_num, sub_graph):
    adj_dict = {
        'node_label': {i: i for i in range(node_num)},
        'adj': OrderedDict({i: [] for i in range(node_num)}),
        'node_num': node_num,
        't': node_num - 1
    }
    for item in sub_graph:
        if len(item) == 1:
            adj_dict['node_label'][int(item)] = adj_dict['node_num']
            adj_dict['adj'][adj_dict['node_num']] = []
            adj_dict['node_num'] += 1
        else:
            i, j = map(int, item)
            if adj_dict['node_label'][j] not in adj_dict['adj'][adj_dict['node_label'][i]]:
                insort(adj_dict['adj'][adj_dict['node_label'][i]], adj_dict['node_label'][j])
            if adj_dict['node_label'][i] not in adj_dict['adj'][adj_dict['node_label'][j]]:
                insort(adj_dict['adj'][adj_dict['node_label'][j]], adj_dict['node_label'][i])
    return adj_dict


def cplus_adj(l_adj, r_adj):
    node_count = l_adj['node_num']
    node_update = OrderedDict({i: i for i in range(r_adj['node_num'])})
    r_label_node = r_adj['node_label'].values()
    for i in range(r_adj['node_num']):
        if i not in r_label_node:
            node_update[i] = node_count
            node_count += 1

    for i in range(l_adj['t'] + 1):
        node_update[r_adj['node_label'][i]] = l_adj['node_label'][i]

    for n, adj in r_adj['adj'].items():
        if n not in r_label_node:
            l_adj['adj'][node_update[n]] = sorted([node_update[i] for i in adj])
        else:
            temp = set(l_adj['adj'][node_update[n]]) | set([node_update[i] for i in adj])
            l_adj['adj'][node_update[n]] = sorted(list(temp))

    l_adj['node_num'] = l_adj['node_num'] + r_adj['node_num'] - r_adj['t'] - 1
    return l_adj


def add_adj(l_adj, edge_list):
    for item in edge_list:
        if len(item) == 1:
            l_adj['node_label'][int(item)] = l_adj['node_num']
            l_adj['adj'][l_adj['node_num']] = []
            l_adj['node_num'] += 1
        else:
            i, j = map(int, item)
            if l_adj['node_label'][j] not in l_adj['adj'][l_adj['node_label'][i]]:
                insort(l_adj['adj'][l_adj['node_label'][i]], l_adj['node_label'][j])
            if l_adj['node_label'][i] not in l_adj['adj'][l_adj['node_label'][j]]:
                insort(l_adj['adj'][l_adj['node_label'][j]], l_adj['node_label'][i])
    return l_adj


def main():
    with open('t_parse_input.txt', 'r') as f:
        for line in f.readlines():
            t_parse(line.strip().split())
            if line[0] == '0':
                break


if __name__ == "__main__":
    main()
