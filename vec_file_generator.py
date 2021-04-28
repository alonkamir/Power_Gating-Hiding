class VecFileGenerator(object):
    def __init__(self, output_file_name):
        self.output_file_name = output_file_name
    
    def one_bias(self, bias_location, number_of_non_bias_pgs):
        number_of_pgs = 5
        base = 1 << (number_of_non_bias_pgs - bias_location)
        highest_value = 2**(number_of_non_bias_pgs + 1) - 1
        config_set = {base}  
        for i in range(highest_value):
            config_set.add(base | i)
        self._write_to_file(config_set, number_of_non_bias_pgs + 1)
        

    def _write_to_file(self, config_set, total_number_of_pgs):
        try:
            vec_file = open(self.output_file_name, 'w')
        except Exception as e:
            raise Exception(f'Could not open file: {e}')
        for config in config_set:
            vec_file.write(f'{config:0{total_number_of_pgs}b}\n')

def main():
    VecFileGenerator('5_pg.txt').one_bias(bias_location=0, number_of_non_bias_pgs=4)


if __name__ == "__main__":
    main()