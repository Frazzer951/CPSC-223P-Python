def print_file(filename):
    """Print the contents of a file"""
    try:
        with open(filename, encoding="utf-8") as f:
            file = f.read()
    except FileNotFoundError:
        pass
        # print(f"Sorry, the file {filename} does not exist.")
    else:
        print(f"{filename}:")
        print(file)


filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    print_file(filename)