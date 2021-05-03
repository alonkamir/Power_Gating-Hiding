from power_gate import PowerGate
from pg_struct import PGStruct
from struct_analyzer import StructAnalyzer
from vec_file_generator import VecFileGenerator


def main():
    generate_vec_file = False
    analyze_struct = False
    if generate_vec_file:
        # VecFileGenerator('5_pg.txt').one_bias(bias_location=0, number_of_non_bias_pgs=4)
        VecFileGenerator('4_biases.txt').multiple_biases_one_level(bias_location_list=[0,1,2,3], number_of_non_bias_pgs=4)

    if analyze_struct:
        vec_file_path = 'aaa.txt'
        pgs = PGStruct()
        bias = PowerGate(res=0.125, bias=True)
        bias2 = PowerGate(res=0.125, bias=False)
        bias3 = PowerGate(res=0.25, bias=False)
        a = PowerGate(res=1)
        b = PowerGate(res=0.25)
        c = PowerGate(res=0.125)
        d = PowerGate(res=0.5)
        pgs.add_node(bias)
        pgs.add_node(bias2)
        pgs.add_node(bias3)
        pgs.add_node(a)
        pgs.add_node(b)
        pgs.add_node(c)
        pgs.add_node(d)
        pgs.add_edge(d, bias2)
        pgs.add_edge(d, bias3)
        pgs.connect_vdd_and_gnd()
        pgs.draw()
        # analyzed = StructAnalyzer(pgs).analyze(vec_file_path, save_dist_as_csv=True, show_iteration=False)
        # print(analyzed)


    # # Weights with tree biases
    # vec_file_path = 'aaa.txt'
    # pgs = PGStruct()
    # bias = PowerGate(res=0.25, bias=True)
    # bias2 = PowerGate(res=0.25, bias=True)
    # bias3 = PowerGate(res=0.083333, bias=True)
    # a = PowerGate(res=0.125)
    # b = PowerGate(res=0.25)
    # c = PowerGate(res=0.5)
    # d = PowerGate(res=1)
    # pgs.add_node(bias)
    # pgs.add_node(bias2)
    # pgs.add_node(bias3)
    # pgs.add_node(a)
    # pgs.add_node(b)
    # pgs.add_node(c)
    # pgs.add_node(d)
    # pgs.add_edge(bias, bias2)
    # pgs.add_edge(bias, bias3)
    # analyzed = StructAnalyzer(pgs).analyze(vec_file_path)
    # print(analyzed)

if __name__ == "__main__":
    main()