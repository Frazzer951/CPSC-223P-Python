def word_count(filename):
    """Print the contents of a file"""
    try:
        with open(filename, encoding="utf-8") as f:
            file = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        word_list = file.split()
        the_count = word_list.count("the")
        print(f"{filename} has the word 'the' {the_count} times")


filenames = ["alice.txt", "frankenstein.txt", "gatsby.txt", "sherlock.txt"]

for filename in filenames:
    word_count(filename)