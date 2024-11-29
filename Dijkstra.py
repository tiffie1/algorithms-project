from Node import *
from ResolveNodeReference import *
import heapq

# shortest path from one node to another node
def Dijkstra(graph: list['Node'], source: str, target: str) -> list[str]:
    if graph[0][1] == False or graph[0][0] == True: return None
    if source == target: return [source]

    for neighbor in graph:
        node_ptr = ResolveNodeReference(neighbor)

        if node_ptr is not None:
            if neighbor.name == source: source_node = neighbor
            elif neighbor.name == target: target_node = neighbor

    # node.start is treated as 'distance from source'
    source_node.start = 0
    for neighbor in graph:
        if ResolveNodeReference(neighbor) and neighbor is not source_node:
            neighbor.start = float("inf")
            neighbor.behind = None

    unseen = [node for node in graph if ResolveNodeReference(node)]
    heapq.heapify(unseen)

    while unseen:
        current_node = heapq.heappop(unseen)
        if current_node is target_node: break
        for neighbor, weight in current_node.adjacent:
            if neighbor in unseen:
                if current_node.start + int(weight) < neighbor.start:
                    neighbor.start = current_node.start + int(weight)
                    neighbor.behind = current_node
                    heapq.heapify(unseen)

    result_path: list[str] = []
    if target_node.behind:
        current_node = target_node
        while current_node.behind is not None:
            result_path.append(f"{current_node.behind.name} -> {current_node.name}")
            current_node = current_node.behind

    result_path.reverse()
    return result_path