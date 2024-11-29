from typing import Union

class Node:
    def __init__(self, name: any, adjacent: Union[list['Node'], tuple['Node', int]] = None, behind: 'Node' = None,
                 start: int = 0, finalize: int = 0, color: str = ""):
        if adjacent is None:
            adjacent = []

        self.adjacent = adjacent
        self.name = name
        self.behind = behind
        self.start = start
        self.finalize = finalize
        self.color = color

    def __str__(self):
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