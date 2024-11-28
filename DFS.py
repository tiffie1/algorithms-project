from Node import Node
from ResolveNodeReference import ResolveNodeReference

TIME = 0
def DFS(graph: list['Node']) -> list['Node']:
    global TIME

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
    mod_graph = DFS(graph)

    """
    This works because, if two nodes are connected,
    and u is not a parent of v and vice versa,
    then there is some path that you can take that
    connects both u and v to the root.
    There is also a connection between u and v,
    meaning there is some cycle between u, v, and the root.
    """
    if graph[0][0] == True: return None

    for u_node in mod_graph:
        u_node_ptr = ResolveNodeReference(u_node)

        if u_node_ptr is not None:
            for v_node in u_node.adjacent:
                v_node_ptr = ResolveNodeReference(v_node)

                if v_node_ptr is not None:
                    if (v_node_ptr.behind == None) or (u_node_ptr.behind == None):
                        if ((v_node_ptr.behind == None) and (u_node_ptr.behind.name != v_node_ptr.name)) \
                            or ((u_node_ptr.behind == None) and (v_node_ptr.behind.name != u_node_ptr.name)):
                            return True
                    elif (v_node_ptr.behind.name != u_node_ptr.name) and (u_node_ptr.behind.name != v_node_ptr.name):
                        return True
            
    return False

def TopologicalSort(graph: list['Node']) -> list[str]:
    global TIME

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