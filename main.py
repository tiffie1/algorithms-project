from BFS import *
from DFS import *
from MST import *
from Node import *
from CSVReader import *
from Dijkstra import *
import os, os.path

def print_graph(graph: list['Node']) -> None:
    for node in graph:
        print(node)

if __name__ == "__main__":
    print("\n\n\nLET'S TALK GRAPHS\n-----------------")

    repeat: bool = True
    while repeat:
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
            while repeat2:
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
            print(graph_string)


        elif user_input == "2":
            pass
        elif user_input == "3":
            print("\nClosing program...")
            quit()
        else:
            print("\nError: Invalid input, please try again.")
            repeat = True