FILEPATH = r"F:/ani personal/python apps/todos.txt"

# Rest of the code remains the same


def get_todos(filepath=FILEPATH):
    """reads the text file and returns the list of
    todos."""
    with open(FILEPATH, 'r') as file_local:
        todos_local=file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath=FILEPATH):
    """writes a todo list in the text file"""
    with open(filepath,"w") as file:
        file.writelines(todos_arg)


print("Hello from functions")



