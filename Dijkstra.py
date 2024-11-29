from Node import *
from ResolveNodeReference import *

# shortest path from one node to another node
def Dijkstra(graph: list['Node'], source: str, target: str) -> list[str]:
    if graph[0][1] == False or graph[0][0] == True: return None

    for node in graph:
        node_ptr = ResolveNodeReference(node)

        if node_ptr is not None:
            if node.name == source: source_node = node
            elif node.name == target: target_node = node

    # node.start is treated as 'distance from source'
    unvisited = set()
    source_node.start = 0
    for node in graph:
        node_ptr = ResolveNodeReference(node)

        if node_ptr is not None and node_ptr is not source_node:
            node_ptr.start = float("inf")
            unvisited.add(node_ptr)

    return graph

    