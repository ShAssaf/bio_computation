import itertools

import networkx as nx


def get_multidigraph_with_connected_n_nodes(n):
    """
    Generate connected directed multi-graph with n vertices.
    """
    # Start with the set of all possible edges, excluding self-loops
    all_edges = list(itertools.permutations(range(n), 2))
    # Generate all combinations of edges
    return nx.MultiDiGraph(all_edges)


def write_subgraphs_to_file(subgraphs, n):
    with open(f"subgraphs_{n}.txt", "w") as file:
        file.write(f"n={n}\n count={len(subgraphs)}\n")
        for i, subgraph in enumerate(subgraphs, 1):
            file.write(f"#{i}\n")
            for edge in subgraph.edges:
                file.write(f"{edge[0]} {edge[1]}\n")


def get_all_unique_subgraph(graph: nx.MultiDiGraph, subgraphs: list = []):
    for e in graph.edges:
        new_graph = graph.copy()
        new_graph.remove_edge(e[0], e[1])
        if nx.is_weakly_connected(new_graph) and not sum([nx.is_isomorphic(new_graph, g2) for g2 in subgraphs]):
            subgraphs.append(new_graph)
            get_all_unique_subgraph(new_graph, subgraphs)
    return subgraphs


def get_all_subgraph_count_dict(graph: nx.MultiDiGraph, subgraphs: dict = {}):
    for e in graph.edges:
        new_graph = graph.copy()
        new_graph.remove_edge(e[0], e[1])
        if nx.is_weakly_connected(new_graph):
            iso = [nx.is_isomorphic(new_graph, g2) for g2 in subgraphs.keys()]
            if iso.count(True) > 1:
                print(f"iso_sum={iso}")
            if not iso.count(True):
                subgraphs[new_graph] = 1
            else:
                subgraphs[list(subgraphs.keys())[iso.index(True)]] = subgraphs[list(subgraphs.keys())[
                    iso.index(True)]] + iso.count(True)
            get_all_subgraph_count_dict(new_graph, subgraphs)
    return subgraphs


def EX1():
    for n in range(2, 5):
        g = get_multidigraph_with_connected_n_nodes(n)
        subgraphs = get_all_unique_subgraph(g, [g])
        write_subgraphs_to_file(subgraphs, n)


def create_graph_from_file(file_path='./graph_example.txt'):
    with open(file_path, 'r') as file:
        lines = [line.replace('\n', '') for line in file.readlines()]
    g = nx.MultiDiGraph()
    for line in lines:
        g.add_edge(line.split('->')[0], line.split('->')[1])
    return g


def EX2():
    g = get_multidigraph_with_connected_n_nodes(4)
    full_graph = get_multidigraph_with_connected_n_nodes(g.nodes.__len__())

    subs = get_all_subgraph_count_dict(g, {g: 1})
    all_subs = get_all_unique_subgraph(full_graph, [full_graph])
    #
    #
    # res_dict = {}
    # while subs:
    #     sub_graph = subs.pop()
    #     iso_sub = [nx.is_isomorphic(sub_graph, g2) for g2 in subs]
    #     res_dict[sub_graph] = iso_sub.count(True)
    #     if True in iso_sub:
    #         indexes_to_remove = [index for index, item in enumerate(iso_sub) if item == True]
    #         subs = [elem for index, elem in enumerate(subs) if index not in indexes_to_remove]

    total_res_dict = {}
    for sub in all_subs:
        for s in subs.keys():
            if nx.is_isomorphic(sub, s):
                total_res_dict[sub] = subs[s]
                subs.pop(s)
                break
        total_res_dict[sub] = 0

    pass


def write_subgraphs_to_file2(subgraphs_dict, n):
    with open(f"subgraphs2_{n}.txt", "w") as file:
        file.write(f"n={n}\n count={len(subgraphs_dict)}\n")
        for i, subgraph in enumerate(subgraphs_dict, 1):
            file.write(f"#{i}\n")
            for edge in subgraph.edges:
                file.write(f"{edge[0]} {edge[1]}\n")


if __name__ == '__main__':
    # EX1()
    EX2()
