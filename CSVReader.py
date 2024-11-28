from Node import Node
import csv

# File name:
#   d = directed
#   u = undirected
#   w = weighted
#   l = unweighted
#   graph_num = number of the graph
# Example:
#   [d/u][w/l]_[number].csv
class CSVReader:
    def __init__(self):
        pass

    # Makes adjacency list.
    def create_graph(self, file_name):
        full_dir = '/Users/tiffie/Documents/Uni/Code/algorithms-project/csv' 
        with open(f"{full_dir}/{file_name}", 'r') as f:
            csv_file: list[list[any]] = csv.reader(f)
            reading_params = self._read_file_name(file_name)
            next(csv_file) # Skip header.

            result_list: list['Node'] = list()
            seen = set()
            
            # Two elements per line.
            for line in csv_file:
                if line[0] not in seen:
                    v_node = Node(line[0])
                    result_list.append(v_node)
                    seen.add(line[0])
                else:
                    for node in result_list:
                        if node.name == line[0]:
                            v_node = node

                if len(line) > 1:
                    if line[1] not in seen:
                        u_node = Node(line[1])
                        result_list.append(u_node)
                        if reading_params[1]: # if weighted
                            v_node.adjacent.append((u_node, line[2]))
                        else:
                            v_node.adjacent.append(u_node)
                        #v_node.adjacent.sort()

                        if not reading_params[0]: # if undirected
                            if reading_params[1]: # if weighted
                                u_node.adjacent.append((v_node, line[2]))
                            else:
                                u_node.adjacent.append(v_node)
                            #u_node.adjacent.sort()
                        seen.add(line[1])
                    else:
                        for node in result_list:
                            if node.name == line[1]:
                                if node not in v_node.adjacent:
                                    if reading_params[1]: # if weighted
                                        v_node.adjacent.append((node, line[2]))
                                    else:
                                        v_node.adjacent.append(node)
                                    #v_node.adjacent.sort()

                                if not reading_params[0] and v_node not in node.adjacent: # if undirected
                                    if reading_params[1]: # if weighted
                                        node.adjacent.append((v_node, line[2]))
                                    else:
                                        node.adjacent.append(v_node)
                                    #node.adjacent.sort()
                                break
            f.close()

        return [reading_params] + result_list

    # directed = True, undirected = False  ;  weighted = True, unweighted = False
    def _read_file_name(self, read_string: str) -> tuple[bool, bool]:
        val1 = True if read_string[0] == 'd' else False
        val2 = True if read_string[1] == 'w' else False

        return (val1, val2)