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


# def write_subgraphs_to_file2(subgraphs):
#     with open(f"subgraphs2_{len(subgraphs)}.txt", "w") as file:
#         file.write(f"count={len(subgraphs)}\n")
#         for sub, count in subgraphs.items():
#             file.write(f"#{count}\n")
#             for edge in sub.edges:
#                 file.write(f"{edge[0]} {edge[1]}\n")
def write_subgraphs_to_file_two(subgraphs):
    with open(f"subgraphs2_{len(subgraphs)}.txt", "w") as file:
        file.write(f"count={len(subgraphs)}\n")
        for sub, count in subgraphs.items():
            file.write(f"#{count}\n")
            for edge in sub.edges:
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
        for gg in [new_graph.subgraph(component) for component in nx.weakly_connected_components(new_graph)]:
            if len(gg.edges) == 0:
                continue
            iso = [nx.is_isomorphic(gg, g2) for g2 in subgraphs.keys()]
            if iso.count(True) > 1:
                print(f"iso_sum={iso}")
            if not iso.count(True):
                subgraphs[gg] = 1
            else:
                subgraphs[list(subgraphs.keys())[iso.index(True)]] = subgraphs[list(subgraphs.keys())[
                    iso.index(True)]] + iso.count(True)
            get_all_subgraph_count_dict(gg, subgraphs)
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
    g = create_graph_from_file()
    subs = get_all_subgraph_count_dict(g, {g: 1})
    all_subs = []
    for i in range(2, len(g.nodes) + 1):
        full_graph = get_multidigraph_with_connected_n_nodes(i)
        all_subs += get_all_unique_subgraph(full_graph, [full_graph])
    total_res_dict = {}
    for sub in all_subs:
        for sub_b in subs:
            if nx.is_isomorphic(sub, sub_b):
                total_res_dict[sub] = subs[sub_b]
        if sub not in total_res_dict:
            total_res_dict[sub] = 0
    write_subgraphs_to_file_two(total_res_dict)
    pass


def write_subgraphs_to_file2(subgraphs_dict, n):
    with open(f"subgraphs2_{n}.txt", "w") as file:
        file.write(f"n={n}\n count={len(subgraphs_dict)}\n")
        for i, subgraph in enumerate(subgraphs_dict, 1):
            file.write(f"#{i}\n")
            for edge in subgraph.edges:
                file.write(f"{edge[0]} {edge[1]}\n")


if __name__ == '__main__':
    EX1()
    EX2()
