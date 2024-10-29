import os


def get_files(directory=None):
    if directory is None:
        directory = os.path.expanduser("~")
    if not os.path.exists(directory):
        raise ValueError(f"directory {directory} does not exists.")
    for root, dirs, files in os.walk(directory, topdown=True):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".txt"):
                full_path = os.path.join(root, file)
                print(full_path)

