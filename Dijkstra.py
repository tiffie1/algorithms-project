from Node import *
from ResolveNodeReference import *
import heapq

def Dijkstra(graph: list['Node'], source: str, target: str) -> list[str]:
    if graph[0][1] == False: return None
    if source == target: return [source]

    for node in graph:
        node_ptr = ResolveNodeReference(node)

        if node_ptr is not None:
            if node_ptr.name == source: source_node = node
            elif node_ptr.name == target: target_node = node

    # node.start is treated as 'distance from source'
    source_node.start = 0
    for node in graph:
        if ResolveNodeReference(node) and node is not source_node:
            node.start = float("inf")
            node.behind = None

    unseen = [node for node in graph if ResolveNodeReference(node)]
    heapq.heapify(unseen) # Use node.start as comparisson value.

    while unseen: # Calculate distances.
        current_node = heapq.heappop(unseen)
        if current_node is target_node: break
        for node, weight in current_node.adjacent:
            if node in unseen:
                if current_node.start + int(weight) < node.start:
                    node.start = current_node.start + int(weight)
                    node.behind = current_node
                    heapq.heapify(unseen)
    
    result_path: list[str] = []
    total_weight = 0
    if target_node.behind:
        current_node = target_node
        while current_node.behind is not None:
            weight = [element[1] for element in current_node.behind.adjacent if element[0].name == current_node.name]
            total_weight += int(weight[0])
            result_path.append(f"{current_node.behind.name} -({weight[0]})-> {current_node.name}")
            current_node = current_node.behind
    else: result_path.append("No path available.")

    result_path.reverse()
    result_path.append(f"Total weight: {total_weight}")
    return result_path