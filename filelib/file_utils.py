import os


def get_files(directory=None, extensions=None):
    if directory is None:
        directory = os.path.expanduser("~")
    if extensions is None:
        extensions = [".jpg", ".txt"]
    matching_files = []
    for root, dirs, files in os.walk(directory, topdown=True):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                matching_files.append(os.path.join(root, file))

    return matching_files
