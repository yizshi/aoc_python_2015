def _get_input(file_name):
    f = open(file_name, "r")
    return f

def get_input_as_string(file_name):
    file = _get_input(file_name)
    return file.read()

def get_input_as_list(file_name):
    file = _get_input(file_name)
    return file.read().split("\n")
