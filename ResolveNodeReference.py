from typing import Union
from Node import *

def ResolveNodeReference(node_object: Union['Node', tuple]) -> 'Node':
    """
    Meant to check the nodes inside of the adjacency list of another node.
    It ignores the metadata tuple, but returns the pointer to the node if
    the graph is weighted. This is done because weighted graphs have 
    adjacency lists composed of tuples, one of which has the pointer to the
    node in question.
    If the graph is unweighted, returns the pointer to the node.
    Returns None if the node to be checked is metadata tuple.

    :param Node | tuple node_object: The object to be checked. Can be either a Node or a tuple.
    :returns: Pointer to the required node object.
    :rtype: Node
    """
    if type(node_object) is tuple:
        if type(node_object[0]) is not bool:
            return node_object[0]
        else:
            return None
    else:
        return node_object