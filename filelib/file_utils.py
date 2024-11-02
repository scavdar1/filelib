import os


def get_files(directory=None, extensions=None):
    if directory is None:
        directory = os.path.expanduser("~")
    if extensions is None:
        extensions = [".jpg", ".txt"]

    for root, dirs, files in os.walk(directory, topdown=True):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                print(os.path.join(root, file))
