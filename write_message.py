def write_file(index, line, filename=None):

    if filename is None:
        filename = 'message.txt'

    with open(filename, mode='a+', encoding='utf-8') as file:
        file.write(index + " " + line + '\n')


def check_previous_message(filename):
    pass
