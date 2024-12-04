from BFS import *
from DFS import *
from MST import *
from Node import *
from CSVReader import *
from Dijkstra import *
import os, os.path

def print_graph(graph: list['Node']) -> None:
    for node in graph:
        # Print the metadata of a graph in a readable format.
        if type(node) is tuple:
            s1 = "Directed" if node[0] == True else "Undirected"
            s2 = "Weighted" if node[1] == True else "Unweighted"
            print(f"({s1}, {s2})")
        else: print(node)

def valid_csv_line(input: str, expected_columns: int) -> tuple[bool, str]:
    """
    Given a string, returns whether or not string is a valid CSV line.
    A valid CSV line is defined as a number of elements seperated by a comma.
    Ex: `value1,value2,value3`

    :param str input: Input string.
    :param int expected_columns: Amount of elements per line. Ex: `expected_columns = 2` means an input can only be of form `value1,value2`. Must be either 2 or 3.
    :returns: Validity of input given.
    :rtype: bool 
    """
    values = input.split(",")

    if len(values) != expected_columns: return False, ""
    if any(value == "" for value in values): return False, "" # If exist empty values.
    if expected_columns < 2 or expected_columns > 3: return False, ""
    if expected_columns == 3: # If expected_columns = 3, CSV is weighted and weight must be int.
        try: int(values[2])
        except ValueError: return False, ""

    new_input = ",".join(value.replace(" ", "") for value in values)
    return True, new_input

if __name__ == "__main__":
    print("\n\n\nLET'S TALK GRAPHS\n-----------------")

    repeat: bool = True
    c_reader = CSVReader()
    while repeat: # Select initial choice.
        repeat = False
        print("\nChoose one of the following:\n" +
            "\t(1) Select existing graph data.\n" +
            "\t(2) Create your own graph data.\n" +
            "\t(3) Quit program.\n\n")

        user_input = input("Selction: ")

        if user_input == "1":
            repeat2 = True
            directory = os.listdir("./csv/")
            directory.sort()
            while repeat2: # Choose existing file.
                i = 0
                repeat2 = False
                print("\nAvailable files:")
                for file in directory:
                    if i % 5 == 0: print("\n\t", end="")
                    whitespace = (len(str(len(directory))) - len(str(i))) + 1
                    print(f"({i+1}){file.rjust(len(file) + whitespace)}  ", end="")
                    i += 1

                user_file_select = input("\n\nSelection: ")
                try: user_file_select = int(user_file_select)
                except ValueError:
                    print("Error: Invalid input, please try again.")
                    repeat2 = True
                else:
                    if user_file_select < 0 or user_file_select > len(directory):
                        print("Error: Invalid input, please try again.")
                        repeat2 = True
                    else: repeat2 = False

            graph_string = directory[user_file_select-1]
            print(f"\'{graph_string}\':")
            with open(f"./csv/{graph_string}", 'r') as f:
                for line in f:
                    print(f"\t{line}", end="")
            print("\n\n")

        elif user_input == "2":
            repeat2 = True
            print("\n--------------\n" +
                    "Graph Creating\n" +
                    "--------------")
            while repeat2: # Choose graph type.
                repeat2 = False
                print("Graph type:\n" +
                      "\t(1) Directed.\n" +
                      "\t(2) Undirected.")
                graph_type = input("\n\n Selection: ")

                if graph_type == "1" or graph_type == "2": repeat = False
                else:
                    print("\nError: Invalid input, please try again.")
                    repeat2 = True

            repeat2 = True
            while repeat2: # Choose graph weight.
                repeat2 = False
                print("Graph weight:\n" +
                      "\t(1) Weighted.\n" +
                      "\t(2) Unweighted.")
                graph_weight = input("\n\n Selection: ")

                if graph_weight == "1" or graph_weight == "2": repeat = False
                else:
                    print("\nError: Invalid input, please try again.")
                    repeat2 = True

            direct_bool = True if graph_type == "1" else False
            weight_bool = True if graph_weight == "1" else False
            graph_metadata = (direct_bool, weight_bool)

            user_quit = False
            csv_pending: list[str] = []
            while not user_quit: # Write CSV file.
                user_quit = True
                print("You are in CSV input mode. Type one of the following " +
                      "commands for extra operations:\n" +
                      "\t\'print\': Prints the CSV being typed.\n" +
                      "\t\'finish\': Exit out of CSV input mode and save CSV " +
                      "into local files.")
                user_csv_input = input("\nInput:  ")

                if user_csv_input == "finish":
                    user_quit = True
                elif user_csv_input == "print":
                    print("\n", end="")
                    for line in csv_pending: print(f"\n\t{line}", end="")
                    print("\n\n")
                    user_quit = False
                else:
                    if graph_metadata[1]:
                        valid_input, new_input = valid_csv_line(user_csv_input, 3)
                        if valid_input: csv_pending.append(new_input)
                        else: print("Error: Invalid CSV input.")
                    else:
                        valid_input, new_input = valid_csv_line(user_csv_input, 2)
                        if valid_input: csv_pending.append(new_input)
                        else: print("Error: Invalid CSV input.")

                    print("\n")
                    user_quit = False

            graph_string = c_reader.write(csv_pending, graph_metadata) 
            print(f"File \'{graph_string}\' saved in \'./csv/\'.")

        elif user_input == "3":
            print("\nClosing program...")
            quit()
        else:
            print("\nError: Invalid input, please try again.")
            repeat = True

    repeat = True
    # graph_string, graph_metadata
    graph = c_reader.read(graph_string)
    while repeat: # Operate on graph.
        repeat = False
        print(f"Graph \'{graph_string}\' selected. Choose what operation " +
              f"you'd like to do perform on \'{graph_string}\':\n" +
              "\t(1) BFS: Run BFS and print graph.\n" +
              "\t(2) DFS: Run DFS and print graph.\n" +
              "\t(3) ConnectedComponents: Print connected components (graph must be undirected).\n" +
              "\t(4) DetectCycle: Print whether the graph has a cycle (graph must be undirected).\n" +
              "\t(5) TopologicalSort: Print topologically sorted list based on graph (graph must be directed).\n" +
              "\t(6) Kruskal: Print MST of the graph (graph must be weighted and undirected).\n" +
              "\t(7) Dijkstra: Print shortest path between two vertices (graph must be weighted).\n" +
              "\t(8) Print graph.\n" +
              "\t(9) Quit program.")
        user_input = input("\nSelection: ")
        print("\n\n")

        if user_input == "1":
            print("--- BFS ---")
            repeat2 = True
            nodes = [node.name for node in graph if type(node) != tuple]
            while repeat2: # Choose starting node.
                repeat2 = False
                print_graph(graph)
                print("\n")
                user_input2 = input("Choose starting node: ")

                if user_input2 in nodes or user_input2 == "": repeat2 = False
                else: 
                    print(f"Error: \'{user_input2}\' not in graph. Please try again.\n")
                    repeat2 = True

            print("\n")
            print(f"Starting node: \"{user_input2}\"")
            print_graph(BFS(graph, user_input2))
            print("\n\n")
            repeat = True

        elif user_input == "2":
            print("--- DFS ---")
            print_graph(graph)
            print("\n")
            print_graph(DFS(graph))
            print("\n\n")
            repeat = True

        elif user_input == "3":
            if graph[0][0] == True:
                print("Cannot do. Graph is directed.")
            else:
                print("--- Connected Components ---")
                print_graph(graph)
                print("\n" + str(ConnectedComponents(graph)))
                print("\n\n")
            repeat = True

        elif user_input == "4":
            if graph[0][0] == True:
                print("Cannot do. Graph is directed.")
            else:
                print("--- Cycle Detection ---")
                print_graph(graph)
                if CycleDetection(graph): print("\nThis graph has a cycle.")
                else: print("\nThis graph does NOT have a cycle.")
                print("\n\n")
            repeat = True

        elif user_input == "5":
            if graph[0][0] == False:
                print("Cannot do. Graph is undirected.")
            else:
                print("--- Topological Sort ---")
                print_graph(graph)
                print("\n")
                print(TopologicalSort(graph))
                print("\n\n")
            repeat = True

        elif user_input == "6":
            if graph[0][1] == False or graph[0][0] == True:
                print("Cannot do. Graph is unweighted or directed.")
            else:
                print("--- Minimum Spanning Tree ---")
                print_graph(graph)
                print("\n")
                print_graph(Kruskal(graph))
                print("\n\n")
            repeat = True

        elif user_input == "7":
            if graph[0][1] == False:
                print("Cannot do. Graph is unweighted.")
            else:
                print("--- Shortest Path ---")
                nodes = [node.name for node in graph if type(node) != tuple]
                repeat2 = True
                while repeat2: # Get source node.
                    repeat2 = False
                    print_graph(graph)
                    print("\n")
                    user_input2 = input("Choose source node: ")

                    if user_input2 in nodes: repeat2 = False
                    else: 
                        print(f"Error: \'{user_input2}\' not in graph. Please try again.\n")
                        repeat2 = True
                source = user_input2
                print("\n")

                repeat2 = True
                while repeat2: # Get target node.
                    repeat2 = False
                    print_graph(graph)
                    print("\n")
                    user_input2 = input("Choose target node: ")

                    if user_input2 in nodes: repeat2 = False
                    else: 
                        print(f"Error: \'{user_input2}\' not in graph. Please try again.\n")
                        repeat2 = True
                target = user_input2

                print("\n---")
                print(Dijkstra(graph, source, target))
                print("\n\n")
            repeat = True

        elif user_input == "8":
            print_graph(graph)
            print("\n\n")
            repeat = True

        elif user_input == "9":
            print("Quiting program...\n\n\n")
            repeat = False

        else:
            print("Error: Input is invalid. Try again.\n")
            repeat = True