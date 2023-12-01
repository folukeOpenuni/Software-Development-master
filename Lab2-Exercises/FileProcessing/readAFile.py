def read_a_file(file_name):
    # File is automatically closed when the "with" block is exited.
    with open(file_name, "r") as file:
        content = file.read()
        print(content)

read_a_file("example.txt")