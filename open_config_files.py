import configparser

from remove_errors import correct_ini_file

def open_config():
    config_file = 'config.ini'
    config = configparser.ConfigParser()

    try:
        config.read(config_file)

    except configparser.MissingSectionHeaderError:
        print('Found error in config file...')
        print('Overcoming that error')

        correct_ini_file(config_file)

        print('Error Corrected!')
        print('Continuing')

    finally:
        config.read(config_file)

    # Storing the API ID and HASH
    api_id = config['TELEGRAM']['api_id']
    api_hash = config['TELEGRAM']['api_hash']

    username = config['TELEGRAM']['username']
    phone = config['TELEGRAM']['phone']

    # Converting to string.
    api_hash = str(api_hash)    

    return api_id, api_hash, username, phone