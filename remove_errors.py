def correct_ini_file(config_file):
    with open(config_file, mode='r') as raw_open:
        raw_open.seek(0)
        temp_api_details = raw_open.readlines(0)
        # print(temp_api_details[0])

    with open(config_file, mode='w') as rewrite_config:
        rewrite_config.write('[TELEGRAM]\n\n')
        rewrite_config.write(temp_api_details[0])
        rewrite_config.write(temp_api_details[1] + '\n')
        rewrite_config.write(temp_api_details[2])
        rewrite_config.write(temp_api_details[3])
