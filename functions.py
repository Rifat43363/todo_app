FILEPATH= "todos_gui.txt"
def get_todoms(filepath=FILEPATH):
    with open(filepath,'r') as file_local:
        todoms_local = file_local.readlines()
    return todoms_local
def write_todoms(todos_local,filepath=FILEPATH):
    with open(filepath,'w') as file_local:
        file_local.writelines(todos_local)