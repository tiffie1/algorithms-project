from BFS import *
from DFS import *
from Node import Node
from CSVReader import CSVReader

def print_graph(graph: list['Node']) -> None:
    for node in graph:
        print(node)

c_reader = CSVReader()
graph: list['Node'] = c_reader.create_graph('uw_2.csv')
print_graph(graph)
print_graph(DFS(graph))