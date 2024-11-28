from Node import Node
from collections import deque

def BFS(graph: list['Node'], starting_node: str = "") -> list['Node']:
    """
    Performs Breadth-First Search and returns the resulting graph.

    :param list[Node] graph: Graph on which to perform the search on.
    :param str starting_node: The node in which to begin the search from.
    :returns: Modified graph with BFS applied to it.
    :rtype: list[Node]
    """
    if not graph: return []
    if starting_node == "": starting_node = graph[1].name

    # TODO: ACCOUNT FOR WEIGHTED GRAPHS.
    for node in graph:
        if type(node) is not tuple:
            node.color = "white"
            node.start = float("inf")
            if node.name == starting_node:
                start = node
                continue

    start.color = "gray"
    start.start = 0
    start.behind = None
    queue: deque['Node'] = deque() # Queue.
    queue.append(start)

    while queue:
        u_node = queue.pop()
        for v_node in u_node.adjacent:
            if type(v_node) is not tuple: 
                if v_node.color == "white":
                    v_node.color = "gray"
                    v_node.start = u_node.start + 1
                    v_node.behind = u_node
                    queue.append(v_node)
                u_node.color = "black"
    
    return graph

def ConnectedComponents(graph: list['Node']) -> list[set]:
    """
    Given a graph, collects and prints out every individual connected component.

    :param list[Node] graph: List of nodes that forms the graph
    :returns: List of connected components.
    :rtype: list[set]
    """
    connected_components: list[set] = []
    for node in graph:
        temp_graph = BFS(graph, node.name)
        
        seen = set()
        for u_node in temp_graph:
            if u_node.name not in seen and (u_node.color == "black" or u_node.color == "gray"):
                seen.add(u_node.name)

        if seen not in connected_components:
            connected_components.append(seen)

    return connected_components