import os

FILEPATH = './files/todos.txt'

if not os.path.exists(FILEPATH):
    with open(FILEPATH, 'w') as file:
        pass


def get_todos(filename=FILEPATH):
    """ Read a text file and return the list of
     to-do items.
    """
    with open(filename, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_args, filename=FILEPATH):
    """ Write the to-do item list in the file. """
    with open(filename, 'w') as file:
        file.writelines(todos_args)
    return None
