from BFS import *
from DFS import *
from MST import *
from Node import Node
from CSVReader import CSVReader
from Dijkstra import *

def print_graph(graph: list['Node']) -> None:
    for node in graph:
        print(node)

c_reader = CSVReader()
graph: list['Node'] = c_reader.create_graph('uw_4.csv')
print_graph(graph)
#print_graph(Kruskal(graph))
#print(Dijkstra(graph, 'a', 'b'))
print_graph(Dijkstra(graph, 'f', 'b'))