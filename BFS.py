from Node import Node
from collections import deque

def BFS(graph: list['Node'], starting_node: str) -> list['Node']:
    """
    Performs Breadth-First Search and returns the resulting graph.

    :param list[Node] graph: Graph on which to perform the search on.
    :param str starting_node: The node in which to begin the search from.
    :returns: Modified graph with BFS applied to it.
    :rtype: list[Node]
    """

    for node in graph:
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
            for w_node in graph:
                if w_node.name == v_node:
                    v_node = w_node
                    break
            
            if v_node.color == "white":
                v_node.color = "gray"
                v_node.start = u_node.start + 1
                v_node.behind = u_node.name
                queue.append(v_node)
            u_node.color = "black"
    
    return graph