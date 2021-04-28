from pg_struct import PGStruct
from power_gate import PowerGate
import networkx as nx
from matplotlib import pyplot as plt

class StructAnalyzer(object):
    def __init__(self, pg_struct):
        self.pg_struct = pg_struct
    
    def analyze(self, vec_file_path):
        try:
            vec_file = open(vec_file_path, 'r')
        except:
            raise Exception("Could not open vec file")
        resistance_list = []
        biggest_size = 0
        for line in vec_file:
            new_G = nx.DiGraph()
            new_G.add_nodes_from(list(self.pg_struct.G.nodes()))
            new_G.add_edges_from(list(self.pg_struct.G.edges()))
            new_G.remove_nodes_from(['VDD', 'Logic'])
            config = line.strip()
            for index, bit in enumerate(config):
                if bit == '0':
                    new_G.remove_node(str(index))
            new_pg_struct = PGStruct()
            for node in list(new_G.nodes()):
                new_pg_struct.add_node(PowerGate.get_pg_by_id(node))
            for edge in list(new_G.edges()):
                new_pg_struct.add_edge(edge)
            new_pg_struct.connect_vdd_and_gnd()
            # new_pg_struct.draw()
            total = new_pg_struct.calc_res()
            if total.size > biggest_size:
                biggest_size = total.size
            resistance_list.append(total.res)
        resistance_list.sort()
        plt.hist(resistance_list)
        plt.show()
        result_dict = {'struct_size': biggest_size, 'res_list': resistance_list}
        return result_dict
