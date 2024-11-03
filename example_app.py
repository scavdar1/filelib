from filelib import get_files


def main():
    directory = None
    txt_files = get_files(directory=directory, extensions=[".txt"])
    print("text files found in the directory")
    for file in txt_files:
        print(file)


if __name__ == "__main__":
    main()
