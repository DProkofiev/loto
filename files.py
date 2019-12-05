import os

def load_txt(file_name, mode):
    if os.path.exists(file_name):
        with open(file_name, mode, encoding='utf-8') as f:
            data = f.read()
    else:
        data = 0
    return (data)