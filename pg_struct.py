from matplotlib import pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
from power_gate import PowerGate

class PGStruct(object):
    def __init__(self):
        self.G = nx.DiGraph()
        self.vdd = PowerGate(0, 0, name='VDD')
        self.logic = PowerGate(0, 0, name='Logic')
        self.G.add_node(self.vdd.id)
        self.G.add_node(self.logic.id)
        self.label_dict = {'VDD':'VDD', 'Logic':'Logic'}
        self.color_map = ['green', 'green'] 
        # Father is key, children are values in a list
        self.family_tree = {}
        # Child is key, father is value
        self.reverse_family_tree = {}

    def add_node(self, pg):
        self.label_dict[pg.id] = pg.res
        self.color_map.append(pg.color)
        self.G.add_node(pg.id)

    def add_edge(self, pg1, pg2):
        self.G.add_edge(pg1.id, pg2.id)
        if self.family_tree.get(pg1.id, None) == None:
            self.family_tree[pg1.id] = [pg2.id]
        else:
            self.family_tree[pg1.id].append(pg2.id)
        self.reverse_family_tree[pg2.id] = pg1.id

    def merge_children_to_father(self, node):
        father_id = self.reverse_family_tree.get(node, None)
        if father_id == None:
            return None
        siblings = self.family_tree.get(father_id, node)
        res = 0
        for sib in siblings:
            if res == 0:
                res = PowerGate.get_pg_by_id(sib)
            else:
                res |= PowerGate.get_pg_by_id(sib)
        new_father = PowerGate.get_pg_by_id(father_id) & res
        PowerGate.update_pg(father_id, new_father)
        return siblings

    def calc_res(self):
        all_paths = dict(nx.all_pairs_shortest_path_length(self.G))
        longest_path = 0
        for i in all_paths:
            for j in all_paths[i]:
                if all_paths[i][j] > longest_path:
                    longest_path = all_paths[i][j]
        for i in range(longest_path):
            distance_i = []
            for j in all_paths['VDD']:
                if all_paths['VDD'][j] == longest_path - i:
                    distance_i.append(j)
            ignore_list = []
            for node in distance_i:
                if node in ignore_list:
                    continue
                else:
                    siblings = self.merge_children_to_father(node)
                    if siblings != None:
                        for sib in siblings:
                            ignore_list.append(sib)
        final_result = 0
        for i in all_paths['VDD']:
            if all_paths['VDD'][i] == 1:
                if final_result == 0:
                    final_result = PowerGate.get_pg_by_id(i)
                else:
                    final_result |= PowerGate.get_pg_by_id(i)
        return final_result

    def connect_vdd_and_gnd(self):
        for node in (list(self.G.nodes)):
            if node == 'VDD' or node == 'Logic':
                continue
            if len(list(self.G.predecessors(node))) == 0:
                self.G.add_edge(self.vdd.id, node)
            if len(nx.descendants(self.G, node)) == 0:
                self.G.add_edge(node, self.logic.id)

    def draw(self):
        pos=graphviz_layout(self.G, prog='dot')
        nx.draw(self.G, pos, node_color=self.color_map, labels=self.label_dict, with_labels=True, node_size=1500)
        plt.show()