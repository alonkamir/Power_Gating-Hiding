class PowerGate(object):
    pg_id = 0
    all_pgs = {}
    def __init__(self, size, res=None, bias=False, name=None):
        if name == None:
            self.id = str(PowerGate.pg_id)
            PowerGate.pg_id += 1
            PowerGate.all_pgs[self.id] = self
        else:
            self.id = name
        self.size = size
        if res == None:
            if size == 0:
                self.res = 0
            else:
                self.res = 1/size
        else:
            self.res = res
        if bias:
            self.color = 'orange'
        else:
            self.color = 'blue'
        
    # Connect PGs in series
    def __and__(self, x):
        return PowerGate(self.size + x.size, self.res + x.res)
    
    # Connect PGs in parallel
    def __or__(self, x):
        try:
            new_res = ((self.res)**-1 + (x.res)**-1)**-1
        except:
            if self.res != 0:
                new_res = self.res
            else:
                new_res = x.res
        return PowerGate(self.size + x.size, new_res)
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