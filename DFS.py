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