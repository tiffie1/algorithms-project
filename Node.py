from typing import Union

"""
Represents a node within a graph. By default, 
"""
class Node:
    """
    Represents a node within a graph. By default, every data member is set to None, except for the name, which
    is required.

    Attributes:
        name (str): Name of the node.
        adjacent (list[Node] | list[tuple(Node, int)]): List of neighbors that Node is pointing to.
        behind (Node): Pointer to the parent of Node.
        start (int): Number variable for processing.
        finalize (int): Other number variable for processing.
        color (str): String variable for processing.
    """
    def __init__(self, name: str, adjacent: Union[list['Node'], list[tuple['Node', int]]] = None, behind: 'Node' = None,
                 start: int = 0, finalize: int = 0, color: str = ""):
        """
        Defines a Node object.

        :param str name: Name of Node.
        :param list[Node] | list[tuple[Node, int]] adjacent: List of other nodes Node is pointing to.
        :param Node behing: Pointer to Node's parent.
        :param int start: Number value for processing.
        :param int finalize: Number value for processing.
        :param str color: String value for processing.
        """
        if adjacent is None:
            adjacent = []

        self.adjacent = adjacent
        self.name = name
        self.behind = behind
        self.start = start
        self.finalize = finalize
        self.color = color

    def __lt__(self, other: 'Node'):
        """Compares two node objects by their start value."""
        return self.start < other.start

    def __str__(self):
        """
        Prints the values of a Node object.  
        Output example: ``Node: (name="B", adj=[C, A], b=A, s=2, f=5, c="black")`` 
        """
        final_str = f", f={self.finalize}" if self.finalize != 0 else ""
        behind_str = f", b={self.behind.name}" if self.behind != None else ""
        color_str = f", c=\"{self.color}\"" if self.color != "" else ""
        adjacent_lst: list[str] = []
        for node in self.adjacent:
            if type(node) is not tuple:
                adjacent_lst.append(f'{node.name}')

            # If graph is weighted, every node in adj is a tuple.
            # (node, weight)
            elif type(node[0]) is not bool: 
                adjacent_lst.append(f'({node[0].name}, {node[1]})')

        adjacent_lst_str = ', '.join(element for element in adjacent_lst)
        return f"Node: (name=\"{self.name}\", adj=[{adjacent_lst_str}]{behind_str}, s={self.start}{final_str}{color_str})"