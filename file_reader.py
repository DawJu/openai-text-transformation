def file_reader(file_path):
    try:
        with open(file_path, 'r', encoding='UTF-8') as f:
            return f.read()
    except FileNotFoundError:
        print('No such file or directory')
