from power_gate import PowerGate
from pg_struct import PGStruct
from struct_analyzer import StructAnalyzer


def main():
    vec_file_path = 'aaa.txt'
    pgs = PGStruct()
    bias = PowerGate(res=8, size=1, bias=True)
    bias2 = PowerGate(res=4, size=1, bias=True)
    # bias3 = PowerGate(res=2, size=1, bias=True)
    a = PowerGate(res=1, size=8)
    b = PowerGate(res=2, size=4)
    c = PowerGate(res=4, size=2)
    d = PowerGate(res=8, size=1)
    pgs.add_node(bias)
    pgs.add_node(bias2)
    # pgs.add_node(bias3)
    pgs.add_node(a)
    pgs.add_node(b)
    pgs.add_node(c)
    pgs.add_node(d)
    StructAnalyzer(pgs).analyze(vec_file_path)
    # bias = PowerGate(res=8, size=1, bias=True)
    # bias2 = PowerGate(res=4, size=1, bias=True)
    # a = PowerGate(res=1, size=8)
    # b = PowerGate(res=2, size=4)
    # c = PowerGate(res=4, size=2)
    # d = PowerGate(res=8, size=1)
    # e = PowerGate(res=8, size=1)
    # f = PowerGate(res=1, size=1)
    # g = PowerGate(res=2, size=1)
    # pgs.add_node(bias)
    # pgs.add_node(f)
    # pgs.add_node(g)
    # pgs.add_node(bias2)
    # pgs.add_node(a)
    # pgs.add_node(b)
    # pgs.add_node(c)
    # pgs.add_node(d)
    # pgs.add_node(e)
    # pgs.add_edge(bias, e)
    # pgs.add_edge(bias, bias2)
    # pgs.add_edge(d, f)
    # pgs.add_edge(d, g)
    # pgs.add_edge(b, c) 
    # pgs.add_edge(b, d)
    # pgs.connect_vdd_and_gnd()
    # pgs.draw()
    # print(pgs.calc_res())


if __name__ == "__main__":
    main()