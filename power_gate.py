class PowerGate(object):
    pg_id = 0
    all_pgs = {}
    def __init__(self, res, size=None, bias=False, name=None):
        if name == None:
            self.id = str(PowerGate.pg_id)
            PowerGate.pg_id += 1
            PowerGate.all_pgs[self.id] = self
        else:
            self.id = name
        self.size = 0
        self.res = res
        if bias:
            self.color = 'orange'
        else:
            self.color = 'blue'
        
    # Connect PGs in series
    def __and__(self, x):
        return PowerGate(self.res + x.res, self.size + x.size)
    
    # Connect PGs in parallel
    def __or__(self, x):
        try:
            new_res = ((self.res)**-1 + (x.res)**-1)**-1
        except:
            if self.res != 0:
                new_res = self.res
            else:
                new_res = x.res
        return PowerGate(new_res, self.size + x.size)
    def __str__(self):
        return f"Size: {self.size}, Resistance: {self.res}"

    def get_pg_by_id(id):
        return PowerGate.all_pgs.get(id, None)
    
    def update_pg(id, new_pg):
        pg = PowerGate.all_pgs.get(id, None)
        if pg == None:
            raise Exception("Can not update PG")
        else:
            pg.res = new_pg.res
            pg.size = new_pg.size

    def get_pg_area(size):
        area_dict = {'0.5': 16, '1': 8, '2': 4, '4': 2, '8': 1, '16': 2, '32': 4, '64': 8, '128': 16}
        if area_dict.get(size, None) == None:
            print("Size not in dict")
            return 0
        else:
            return area_dict.get(size)