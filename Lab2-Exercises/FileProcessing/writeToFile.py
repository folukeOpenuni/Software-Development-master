def write_to_file(file_name, text):
    # File is automatically closed when the "with" block is exited.
    with open(file_name, "w") as file:
        file.write(text)

# Open a file for writing (creates a new file or overwrites existing content)
file = open("example.txt", "w")

# Write content to the file
file.write("Hello, World!\n")
file.write("This is a new line.\n")

# Close the file when done
file.close()



