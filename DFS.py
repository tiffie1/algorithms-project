from Node import Node
from ResolveNodeReference import ResolveNodeReference

TIME = 0
def DFS(graph: list['Node']) -> list['Node']:
    """
    Given a graph, calculates the start and finalize times for each node
    using Depth-First Search.

    :param list[Node] graph: Graph to be processed.
    """
    global TIME
    TIME = 0

    def DFS_Visit(graph: list['Node'], u_node: 'Node') -> None:
        global TIME

        u_node.color = "gray"
        TIME += 1
        u_node.start = TIME

        for v_node in u_node.adjacent:
            v_node_ptr = ResolveNodeReference(v_node)

            if v_node_ptr is not None:
                if v_node_ptr.color == "white":
                    v_node_ptr.behind = u_node
                    DFS_Visit(graph, v_node_ptr)

        u_node.color = "black"
        TIME += 1
        u_node.finalize = TIME  


    for u_node in graph:
        u_node_ptr = ResolveNodeReference(u_node)

        if u_node_ptr is not None:
            u_node_ptr.color = "white"
            u_node_ptr.behind = None

    for u_node in graph:
        u_node_ptr = ResolveNodeReference(u_node)
        
        if u_node_ptr is not None:
            if u_node.color == "white":
                DFS_Visit(graph, u_node)

    return graph

def CycleDetection(graph: list['Node']) -> bool:
    """
    Uses DFS to determine whether a graph has a cycle.
    """
    global TIME
    TIME = 0

    def DFS_Visit(graph: list['Node'], u_node: 'Node') -> None:
        global TIME

        u_node.color = "gray"
        TIME += 1
        u_node.start = TIME

        for v_node in u_node.adjacent:
            v_node = ResolveNodeReference(v_node)
            if v_node:
                if v_node.color == "white":
                    v_node.behind = u_node
                    if DFS_Visit(graph, v_node): return True
                    else: continue
                elif v_node.color == "gray": return True # We found the cycle.

        u_node.color = "black"
        TIME += 1
        u_node.finalize = TIME  

        return False


    for u_node in graph:
        u_node = ResolveNodeReference(u_node)
        if u_node:
            u_node.color = "white"
            u_node.behind = None

    for u_node in graph:
        u_node = ResolveNodeReference(u_node)
        if u_node:
            if u_node.color == "white":
                if DFS_Visit(graph, u_node): return True
                else: continue

    return False

def TopologicalSort(graph: list['Node']) -> list[str]:
    """
    Given a directed acyclic graph, determines the topological order of the nodes within the graph.

    :returns: The topological order of the graph as a list of the strings of the names of the nodes.
    :rtype: list[str]
    """
    if CycleDetection(graph): return []
    global TIME
    TIME = 0

    def DFS_Visit(graph: list['Node'], u_node: 'Node', result_list: list[str]) -> None:
        global TIME

        u_node.color = "gray"
        TIME += 1
        u_node.start = TIME

        for v_node in u_node.adjacent:
            v_node_ptr = ResolveNodeReference(v_node)

            if v_node_ptr is not None:
                if v_node_ptr.color == "white":
                    v_node_ptr.behind = u_node.name
                    result_list = DFS_Visit(graph, v_node_ptr, result_list)

        u_node.color = "black"
        result_list.append(u_node.name)
        TIME += 1
        u_node.finalize = TIME  

        return result_list

    if graph[0][0] == False: return None

    for u_node in graph:
        u_node_ptr = ResolveNodeReference(u_node)

        if u_node_ptr is not None:
            u_node_ptr.color = "white"
            u_node_ptr.behind = None

    result_list = list()
    for u_node in graph:
        u_node_ptr = ResolveNodeReference(u_node)

        if u_node_ptr is not None:
            if u_node_ptr.color == "white":
                result_list = DFS_Visit(graph, u_node_ptr, result_list)

    result_list.reverse()
    return result_list