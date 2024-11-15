def file_reader(file_path):
    try:
        with open(file_path, 'r', encoding='UTF-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f'FileNotFoundError: {file_path} does not exist.')
        return
