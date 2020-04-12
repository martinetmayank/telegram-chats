def correct_ini_file(config_file):
    with open(config_file, mode='r') as raw_open:
        raw_open.seek(0)
        temp_api_details = raw_open.readlines(0)
        # print(type(temp_api_details[0]))

    with open(config_file, mode='w') as rewrite_config:
        if temp_api_details[0] != '[TELEGRAM]\n':
            rewrite_config.write('[TELEGRAM]\n')

        for i in temp_api_details:
            rewrite_config.write(i)
            
