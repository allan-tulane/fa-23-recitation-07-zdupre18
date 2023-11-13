from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
       urrent_node = frontier.pop()
        neighbors = graph[current_node]
        for neighbor in neighbors:
            if neighbor not in result:
                result.add(neighbor)
                frontier.add(neighbor)
    return result




def connected(graph): #      a list of sets, where each set contains the nodes in a connected component
   remaining_nodes = set(graph.keys())
    connected_components = []

    while remaining_nodes:
        start_node = remaining_nodes.pop()
        component = reachable(graph, start_node)
        connected_components.append(component)
        remaining_nodes -= component

    return connected_components



def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
   connected_components = connected(graph)
    return len(connected_components)

