from Node import *
from ResolveNodeReference import *
from typing import Union

def Kruskal(graph: list['Node']) -> list['Node']:
    """
    Finds the minimum spanning tree of a given graph.

    :param list[Node] graph: The graph to be processed.
    :returns: A new graph that is the MST of the graph parameter.
    :rtype: list[Node]
    """

    # Checks if a Node is already inside the MST.
    def inMST(node: 'Node', graph: list['Node']) -> bool:
        if not graph: return False

        for n in graph:
            if n.name == node.name:
                return True
        return False

    # Checks if two nodes have a path within the MST by using the board.    
    def isConnected(u_node: str, v_node: str, board: list[str, set]) -> bool:
        if not board: return False

        for element in board:
            if type(element) is set:
                if u_node in element and v_node in element:
                    return True
                
        return False

    # Creates a board that contains the data structure for keeping track of
    # which nodes have been added to the MST.    
    def createBoard() -> list[Union[str, set[str]]]:
        board = []
        for node in graph:
            node_ptr = ResolveNodeReference(node)

            if node_ptr is not None: board.append(node_ptr.name)
        return board

    if graph[0][1] == False or graph[0][0] == True: return None # Check metadata.

    board = createBoard() 
    edges: list[tuple['Node', 'Node', int]] = []
    seen = set()
    for u_node in graph: # Create list of edges.
        if type(u_node) is not tuple: # Avoid processing metadata.
            for v_node, weight in u_node.adjacent:
                if type(v_node) is not bool:
                    edge_str = f'{u_node.name}{v_node.name}'
                    if edge_str not in seen:
                        edges.append((u_node, v_node, int(weight)))
                        seen.add(edge_str)
                        seen.add(edge_str[::-1]) # Save both directions of edge.

    edges.sort(key=lambda x: x[2]) # Sort edges by weight descending.
    answer_graph: list['Node'] = []
    seen.clear()
    """
    Possibilities for adding nodes to the MST.

        1. Neither node is inside of the MST.
            * Make two new nodes and add to the graph list.
            * Update the adjacency data type to have the other node.
        2. One of the nodes is inside the MST.
            * Find the node already inside of the graph.
            * Create a new node and append to the graph.
            * Append the new node to the adjacency list of the node already in the graph.
            * Append the node already in the graph in the adjacency list of the new node.
        3. Both nodes are inside of the MST.
            * Find both nodes inside of the graph.
            * Append on both nodes the connection between each other.
    """
    for u_node, v_node, weight in edges:
        u_boolean, v_boolean = inMST(u_node, answer_graph), inMST(v_node, answer_graph)

        if u_boolean and v_boolean: # Both nodes already in MST.
            if not isConnected(u_node.name, v_node.name, board):
                for node in answer_graph: # Look for nodes.
                    if node.name == u_node.name:
                        u_temp = node
                        continue
                    elif node.name == v_node.name:
                        v_temp = node
                        continue

                # Add to MST.
                u_temp.adjacent.append((v_temp, weight))
                v_temp.adjacent.append((u_temp, weight))

                for i in range(len(board)): # Update board.
                    if type(board[i]) == set:
                        if u_temp.name in board[i]:
                            board1 = board[i]
                            continue
                        elif v_temp.name in board[i]:
                            board2 = board[i]
                            continue

                new_set = board1 | board2 # Unionize both sets.
                board.remove(board1)
                board.remove(board2)
                board.append(new_set)

        elif u_boolean ^ v_boolean: # Only one node is in MST.
            for node in answer_graph: # Find the node.
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

            # Add to MST.
            u_temp.adjacent.append((v_temp, weight))
            v_temp.adjacent.append((u_temp, weight))

            for i in range(len(board)): # Update board. Find set and lonely element.
                if type(board[i]) == set:
                    if u_temp.name in board[i] or v_temp.name in board[i]:
                        set_index = i
                        continue
                else:
                    if board[i] == u_temp.name or board[i] == v_temp.name:
                        alone_node = u_temp.name if board[i] == u_temp.name else v_temp.name
                        alone_index = i
                        continue

            board[set_index].add(alone_node) # Add lonely to set.
            board = board[0:alone_index] + board[alone_index+1:] # Remove lonely.

        else: # Neither node is in the MST. Add both to the MST and remove them from board.
            u_temp, v_temp = Node(u_node.name), Node(v_node.name)
            answer_graph.append(u_temp)
            answer_graph.append(v_temp)

            u_temp.adjacent.append((v_temp, weight))
            v_temp.adjacent.append((u_temp, weight))

            board.remove(u_node.name)
            board.remove(v_node.name)
            temp_set = {u_node.name, v_node.name}
            board.append(temp_set)

    return [(False, True)] + answer_graph