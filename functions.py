# custom function

FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_name:
        return file_name.readlines()


def write_todos(todo_items, filepath="todos.txt"):
    """ Write the to-do items in the text file."""
    with open(filepath, 'w') as files_to_write:
        files_to_write.writelines(todo_items)

# "__name__"
# "__main__"
