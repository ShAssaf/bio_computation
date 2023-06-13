import itertools
import networkx as nx


def get_multigrain_with_connected_n_nodes(n):
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


def get_all_subgraph(graph: nx.MultiDiGraph, subgraphs: list = []):
    for e in graph.edges:
        new_graph = graph.copy()
        new_graph.remove_edge(e[0], e[1])
        if nx.is_weakly_connected(new_graph) and not sum([nx.is_isomorphic(new_graph, g2) for g2 in subgraphs]):
            subgraphs.append(new_graph)
            get_all_subgraph(new_graph, subgraphs)
    return subgraphs


def EX1():
    for n in range(2, 5):
        g = get_multigrain_with_connected_n_nodes(n)
        subgraphs = get_all_subgraph(g, [g])
        write_subgraphs_to_file(subgraphs, n)

def EX2():
    pass

if __name__ == '__main__':
    EX1()
    EX2()
