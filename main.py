from BFS import *
from DFS import *
from Node import Node
from CSVReader import CSVReader

def print_graph(graph: list['Node']) -> None:
    for node in graph:
        print(node)

c_reader = CSVReader()
graph: list['Node'] = c_reader.create_graph('ul_3.csv')

print_graph(graph)
print("\n\n")

print_graph(BFS(graph, "D"))
print("\n\n")


print(ConnectedComponents(graph))

print("\n\n\n---\n\n\n")

graph2 = c_reader.create_graph('ul_4.csv')
print_graph(graph2)
print("\n")

#print_graph(DFS(graph2))
print(CycleDetection(graph2))