from BFS import BFS
from DFS import DFS
from Node import Node
from CSVReader import CSVReader

def print_graph(graph: list['Node']) -> None:
    for node in graph:
        print(node)

c_reader = CSVReader()
graph: list['Node'] = c_reader.create_graph('ul_2.csv')

print_graph(graph)
print("\n\n")
mod_graph = BFS(graph, 's')
print_graph(mod_graph)

print("\n\n")

graph_2 = c_reader.create_graph('dl_2.csv')
print_graph(graph_2)
print("\n\n")
mod_graph_2 = DFS(graph_2)
print_graph(mod_graph_2)