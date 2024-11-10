class Node:
    def __init__(self, name: any, adjacent: list['Node'] = None, behind: str = "",
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
        behind_str = f", b={self.behind}" if self.behind != "" else ""
        color_str = f", c=\"{self.color}\"" if self.color != "" else ""
        adjacent_lst = ', '.join(str(node) for node in self.adjacent)
        return f"Node: (name=\"{self.name}\", adj=[{adjacent_lst}]{behind_str}, s={self.start}{final_str}{color_str})"