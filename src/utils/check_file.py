from os import path

def check_file():
    file_exists = path.isfile('temp/input.txt')
    if file_exists:
        return True
    return False

def read_file():
    with open('temp/input.txt', 'r') as file:
        data = [int(data) for data in file]
        file.close()
    return data