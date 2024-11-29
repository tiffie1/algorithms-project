from Node import *
from ResolveNodeReference import *
from typing import Union

def Kruskal(graph: list['Node']) -> list['Node']:
    def inMST(node: 'Node', graph: list['Node']) -> bool:
        if not graph: return False

        for n in graph:
            if n.name == node.name:
                return True
        return False
    
    def isConnected(u_node: str, v_node: str, board: list[str, set]) -> bool:
        if not board: return False

        for element in board:
            if type(element) is set:
                if u_node in element and v_node in element:
                    return True
                
        return False
    
    def createBoard() -> list[Union[str, set[str]]]:
        board = []
        for node in graph:
            node_ptr = ResolveNodeReference(node)

            if node_ptr is not None: board.append(node_ptr.name)
        return board

    if graph[0][1] == False or graph[0][0] == True: return None

    board = createBoard() 
    edges: list[tuple['Node', 'Node', int]] = []
    seen = set()
    for u_node in graph:
        if type(u_node) is not tuple:
            for v_node, weight in u_node.adjacent:
                if type(v_node) is not bool:
                    edge_str = f'{u_node.name}{v_node.name}'
                    if edge_str not in seen:
                        edges.append((u_node, v_node, int(weight)))
                        seen.add(edge_str)
                        seen.add(edge_str[::-1]) # Save both directions of edge.

    edges.sort(key=lambda x: x[2])
    answer_graph: list['Node'] = []
    seen.clear()
    for u_node, v_node, weight in edges:
        u_boolean, v_boolean = inMST(u_node, answer_graph), inMST(v_node, answer_graph)

        if u_boolean and v_boolean:
            if not isConnected(u_node.name, v_node.name, board):
                for node in answer_graph:
                    if node.name == u_node.name:
                        u_temp = node
                        continue
                    elif node.name == v_node.name:
                        v_temp = node
                        continue

                u_temp.adjacent.append((v_temp, weight))
                v_temp.adjacent.append((u_temp, weight))

                for i in range(len(board)):
                    if type(board[i]) == set:
                        if u_temp.name in board[i]:
                            board1 = board[i]
                            continue
                        elif v_temp.name in board[i]:
                            board2 = board[i]
                            continue

                new_set = board1 | board2 
                board.remove(board1)
                board.remove(board2)
                board.append(new_set)

        elif u_boolean ^ v_boolean:
            for node in answer_graph:
                if node.name == u_node.name:
                    u_temp = node
                    found = 1
                    break
                elif node.name == v_node.name:
                    u_temp = node
                    found = 2
                    break
            
            v_temp = Node(v_node.name) if found == 1 else Node(u_node.name)
            answer_graph.append(v_temp)

            u_temp.adjacent.append((v_temp, weight))
            v_temp.adjacent.append((u_temp, weight))

            for i in range(len(board)):
                if type(board[i]) == set:
                    if u_temp.name in board[i] or v_temp.name in board[i]:
                        set_index = i
                        continue
                else:
                    if board[i] == u_temp.name or board[i] == v_temp.name:
                        alone_node = u_temp.name if board[i] == u_temp.name else v_temp.name
                        alone_index = i
                        continue

            board[set_index].add(alone_node)
            board = board[0:alone_index] + board[alone_index+1:]

        else:
            u_temp, v_temp = Node(u_node.name), Node(v_node.name)
            answer_graph.append(u_temp)
            answer_graph.append(v_temp)

            u_temp.adjacent.append((v_temp, weight))
            v_temp.adjacent.append((u_temp, weight))

            board.remove(u_node.name)
            board.remove(v_node.name)
            temp_set = {u_node.name, v_node.name}
            board.append(temp_set)

    return [(True, True)] + answer_graph