class VecFileGenerator(object):
    def __init__(self, output_file_name):
        self.output_file_name = output_file_name
    
    def one_bias(self, bias_location, number_of_non_bias_pgs):
        base = 1 << (number_of_non_bias_pgs - bias_location)
        highest_value = 2**(number_of_non_bias_pgs + 1) - 1
        config_set = {base}  
        for i in range(highest_value):
            config_set.add(base | i)
        self._write_to_file(config_set, number_of_non_bias_pgs + 1)

    def multiple_biases_one_level(self, bias_location_list, number_of_non_bias_pgs):
        total_number_of_pgs = len(bias_location_list) + number_of_non_bias_pgs
        highest_value = 2**(total_number_of_pgs) - 1
        config_set = set()
        for bias_location in bias_location_list:
            base = 1 << (total_number_of_pgs - 1 - bias_location)
            for i in range(highest_value):
                config_set.add(base | i)
        # for x in config_set:
        #     print(f'{x:06b}')
        self._write_to_file(config_set, number_of_non_bias_pgs + len(bias_location_list))



    def _write_to_file(self, config_set, total_number_of_pgs):
        try:
            vec_file = open(self.output_file_name, 'w')
        except Exception as e:
            raise Exception(f'Could not open file: {e}')
        for config in config_set:
            vec_file.write(f'{config:0{total_number_of_pgs}b}\n')