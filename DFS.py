from Node import Node

TIME = 0
def DFS(graph: list['Node']) -> list['Node']:
    global TIME

    def DFS_Visit(graph: list['Node'], u_node: 'Node') -> None:
        global TIME

        u_node.color = "gray"
        TIME += 1
        u_node.start = TIME

        for v_node in u_node.adjacent:
            for w_node in graph:
                if w_node.name == v_node:
                    v_node = w_node
                    break

            if v_node.color == "white":
                v_node.behind = u_node.name
                DFS_Visit(graph, v_node)
        u_node.color = "black"
        TIME += 1
        u_node.finalize = TIME  


    for u_node in graph:
        u_node.color = "white"
        u_node.behind = None

    for u_node in graph:
        if u_node.color == "white":
            DFS_Visit(graph, u_node)

    return graph

def CycleDetection(graph: list['Node']) -> bool:
    mod_graph = DFS(graph.copy())

    """
    This works because, if two nodes are connected,
    and u is not a parent of v and vice versa,
    then there is some path that you can take that
    connects both u and v to the root.
    There is also a connection between u and v,
    meaning there is some cycle between u, v, and the root.
    """
    for u_node in mod_graph:
        for v_node in u_node.adjacent:
            for w_node in mod_graph:
                if v_node == w_node.name:
                    v_node = w_node

            if (v_node.behind != u_node.name) and (u_node.behind != v_node.name):
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
            for w_node in graph:
                if w_node.name == v_node:
                    v_node = w_node
                    break

            if v_node.color == "white":
                v_node.behind = u_node.name
                result_list = DFS_Visit(graph, v_node, result_list)
        u_node.color = "black"
        result_list.append(u_node.name)
        TIME += 1
        u_node.finalize = TIME  

        return result_list

    for u_node in graph:
        u_node.color = "white"
        u_node.behind = None

    result_list = list()
    for u_node in graph:
        if u_node.color == "white":
            result_list = DFS_Visit(graph, u_node, result_list)

    result_list.reverse()
    return result_list