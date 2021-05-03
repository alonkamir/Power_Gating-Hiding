from pg_struct import PGStruct
from power_gate import PowerGate
import networkx as nx
from matplotlib import pyplot as plt
import copy
import pandas as pd

class StructAnalyzer(object):
    def __init__(self, pg_struct):
        self.pg_struct = pg_struct
    
    def analyze(self, vec_file_path, save_dist_as_csv=False, show_iteration=False):
        try:
            vec_file = open(vec_file_path, 'r')
        except:
            raise Exception("Could not open vec file")
        resistance_list = []
        res_config = []
        biggest_size = 0
        all_pgs_temp = copy.deepcopy(PowerGate.all_pgs)
        for line in vec_file:
            PowerGate.all_pgs = copy.deepcopy(all_pgs_temp)
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
                new_pg_struct.add_edge(PowerGate.get_pg_by_id(edge[0]), PowerGate.get_pg_by_id(edge[1]))
            new_pg_struct.connect_vdd_and_gnd()
            total = new_pg_struct.calc_res()
            if show_iteration:
                print(total)
                new_pg_struct.draw()
            # area = new_pg_struct.calc_total_area()
            # if area > biggest_size:
            #     biggest_size = area
            # print(total.res)
            resistance_list.append(total.res)
            res_config.append(config)
        resistance_list.sort()
        if save_dist_as_csv:
            try:
                df = pd.DataFrame(data={'Config': res_config, 'Resistance': resistance_list})
                df.to_csv('resistance.csv')
            except:
                print("Could not write to file")
        plt.hist(resistance_list)
        plt.show()
        result_dict = {'struct_size': biggest_size, 'res_list': resistance_list}
        return result_dict