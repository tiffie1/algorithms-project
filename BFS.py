from Node import Node
from collections import deque
from ResolveNodeReference import ResolveNodeReference

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
        node_ptr = ResolveNodeReference(node)

        if node_ptr is not None:
            node_ptr.color = "white"
            node_ptr.start = float("inf")
            if node_ptr.name == starting_node:
                start = node_ptr
                continue
        
    start.color = "gray"
    start.start = 0
    start.behind = None
    queue: deque['Node'] = deque() # Queue.
    queue.append(start)

    while queue:
        u_node = queue.pop()
        u_node_ptr = ResolveNodeReference(u_node)

        if u_node_ptr is not None:
            for v_node in u_node_ptr.adjacent:
                v_node_ptr = ResolveNodeReference(v_node)

                if v_node_ptr is not None:
                    if v_node_ptr.color == "white":
                        v_node_ptr.color = "gray"
                        v_node_ptr.start = u_node_ptr.start + 1
                        v_node_ptr.behind = u_node_ptr
                        queue.append(v_node_ptr)
                    u_node_ptr.color = "black"
    
    return graph

def ConnectedComponents(graph: list['Node']) -> list[set]:
    """
    Given a graph, collects and prints out every individual connected component.
    Only works for undirected graphs.

    :param list[Node] graph: List of nodes that forms the graph
    :returns: List of connected components.
    :rtype: list[set]
    """
    if graph[0][0] == True: return None
    
    connected_components: list[set] = []
    for node in graph:
        node_ptr = ResolveNodeReference(node)
        
        if node_ptr is not None:
            mod_graph = BFS(graph, node_ptr.name)
            
            seen = set()
            for u_node in mod_graph:
                u_node_ptr = ResolveNodeReference(u_node)

                if u_node_ptr is not None:
                    if u_node_ptr.name not in seen and (u_node_ptr.color == "black" or u_node_ptr.color == "gray"):
                        seen.add(u_node_ptr.name)

            if seen not in connected_components:
                connected_components.append(seen)

    return connected_components