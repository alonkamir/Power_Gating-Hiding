from pg_struct import PGStruct
from power_gate import PowerGate
def main():
    pgs = PGStruct()
    bias = PowerGate(res=8, size=1, bias=True)
    a = PowerGate(res=1, size=8)
    b = PowerGate(res=2, size=4)
    c = PowerGate(res=4, size=2)
    d = PowerGate(res=8, size=1)
    e = PowerGate(res=8, size=1)
    pgs.add_node(bias)
    pgs.add_node(a)
    pgs.add_node(b)
    pgs.add_node(c)
    pgs.add_node(d)
    pgs.add_node(e)
    pgs.add_edge(bias, a)
    pgs.add_edge(bias, b)
    pgs.add_edge(b, c) 
    pgs.add_edge(b, d) 
    pgs.connect_vdd_and_gnd()
    pgs.draw()
    print(pgs.calc_res())


if __name__ == "__main__":
    main()