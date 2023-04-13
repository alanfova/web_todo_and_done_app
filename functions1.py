FILEPATH = "todos.txt"
FILEPATH_D = "done.txt"
def get_todos(file_path = FILEPATH):
    with open(file_path, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(data2write, file_path=FILEPATH):
    with open(file_path, "w") as file:
        file.writelines(data2write)

def write_done(data2write, file_path=FILEPATH_D):
    with open(file_path, "w") as file:
        file.writelines(data2write)

def read_done(file_path=FILEPATH_D):
    with open(file_path, "r") as file_local:
        done_local = file_local.readlines()
        return done_local


if __name__ == "__main__":
    print("You are using Functions1 version")
