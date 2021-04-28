from power_gate import PowerGate
from pg_struct import PGStruct
from struct_analyzer import StructAnalyzer


def main():
    vec_file_path = '5_pg.txt'
    pgs = PGStruct()
    bias = PowerGate(size=8, bias=True)
    a = PowerGate(size=8)
    b = PowerGate(size=4)
    c = PowerGate(size=2)
    d = PowerGate(size=1)
    pgs.add_node(bias)
    pgs.add_node(a)
    pgs.add_node(b)
    pgs.add_node(c)
    pgs.add_node(d)
    analyzed_5_pg = StructAnalyzer(pgs).analyze(vec_file_path)
    print(analyzed_5_pg)


if __name__ == "__main__":
    main()