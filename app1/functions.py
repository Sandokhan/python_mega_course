def get_todos(filename):
    """ Read a text file and return the list of
     to-do items.
    """
    with open(f'./files/{filename}', 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(filename, todos_args):
    """ Write the to-do item list in the file. """
    with open(f'./files/{filename}', 'w') as file:
        file.writelines(todos_args)
    return None
